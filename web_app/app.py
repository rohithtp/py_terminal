#!/usr/bin/env python3
"""
Web application version of Py Terminal
Provides a web interface for the terminal functionality
"""

from flask import Flask, render_template, request, jsonify, Response
import subprocess
import threading
import queue
import time
import os
import signal
import json

app = Flask(__name__)

# Global storage for running processes
running_processes = {}

class ProcessManager:
    def __init__(self):
        self.processes = {}
        self.output_queues = {}
    
    def start_process(self, process_id, command, mode="capture"):
        """Start a new process"""
        if process_id in self.processes:
            return {"error": "Process already running"}
        
        output_queue = queue.Queue()
        self.output_queues[process_id] = output_queue
        
        if mode == "interactive":
            # For interactive mode, we'll stream output
            def run_interactive():
                try:
                    process = subprocess.Popen(
                        command, 
                        shell=True, 
                        stdout=subprocess.PIPE, 
                        stderr=subprocess.PIPE,
                        text=True,
                        bufsize=1,
                        universal_newlines=True
                    )
                    self.processes[process_id] = process
                    
                    # Stream output
                    while True:
                        output = process.stdout.readline()
                        if output == '' and process.poll() is not None:
                            break
                        if output:
                            output_queue.put({"type": "output", "data": output})
                    
                    # Get final status
                    return_code = process.poll()
                    output_queue.put({"type": "finished", "return_code": return_code})
                    
                except Exception as e:
                    output_queue.put({"type": "error", "data": str(e)})
            
            thread = threading.Thread(target=run_interactive)
            thread.daemon = True
            thread.start()
            
        else:
            # Capture mode
            try:
                result = subprocess.run(
                    command, 
                    shell=True, 
                    capture_output=True, 
                    text=True, 
                    timeout=30
                )
                
                output_data = {
                    "stdout": result.stdout,
                    "stderr": result.stderr,
                    "return_code": result.returncode
                }
                output_queue.put({"type": "finished", "data": output_data})
                
            except subprocess.TimeoutExpired:
                output_queue.put({"type": "error", "data": "Command timed out after 30 seconds"})
            except Exception as e:
                output_queue.put({"type": "error", "data": str(e)})
        
        return {"status": "started", "process_id": process_id}
    
    def stop_process(self, process_id):
        """Stop a running process"""
        if process_id in self.processes:
            process = self.processes[process_id]
            try:
                process.terminate()
                process.wait(timeout=5)
            except subprocess.TimeoutExpired:
                process.kill()
            
            del self.processes[process_id]
            return {"status": "stopped"}
        return {"error": "Process not found"}
    
    def get_output(self, process_id):
        """Get output from a process"""
        if process_id in self.output_queues:
            queue = self.output_queues[process_id]
            outputs = []
            while not queue.empty():
                outputs.append(queue.get_nowait())
            return outputs
        return []

process_manager = ProcessManager()

@app.route('/')
def index():
    """Main web interface"""
    return render_template('index.html')

@app.route('/api/execute', methods=['POST'])
def execute_command():
    """Execute a command via API"""
    data = request.get_json()
    command = data.get('command')
    mode = data.get('mode', 'capture')
    
    if not command:
        return jsonify({"error": "No command provided"}), 400
    
    process_id = f"process_{int(time.time() * 1000)}"
    result = process_manager.start_process(process_id, command, mode)
    
    return jsonify(result)

@app.route('/api/stop/<process_id>', methods=['POST'])
def stop_process(process_id):
    """Stop a running process"""
    result = process_manager.stop_process(process_id)
    return jsonify(result)

@app.route('/api/output/<process_id>')
def get_output(process_id):
    """Get output from a process"""
    outputs = process_manager.get_output(process_id)
    return jsonify(outputs)

@app.route('/api/processes')
def list_processes():
    """List all running processes"""
    processes = list(process_manager.processes.keys())
    return jsonify({"processes": processes})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000) 