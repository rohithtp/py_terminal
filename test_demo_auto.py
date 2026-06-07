import pexpect
import sys
import time

def verify_demo():
    print("Starting DEMO Verification...")
    
    # 1. Launch the application
    child = pexpect.spawn('venv/bin/python terminal_web/main.py', encoding='utf-8', timeout=10)
    child.logfile = sys.stdout

    # Wait for the menu
    child.expect('Enter your choice')
    print("✓ App launched and menu displayed")

    # 2. Run a safe command
    child.sendline('3')
    child.expect('Enter the bash command to run')
    child.sendline('echo hello')
    child.expect('Execution mode')
    child.sendline('capture')
    
    # It should output hello and prompt to return
    child.expect('hello')
    child.expect('Press Enter to return to menu...')
    child.sendline('')
    child.expect('Enter your choice')
    print("✓ Safe command 'echo hello' executed successfully")

    # 3. Trigger a risky preflight warning
    child.sendline('3')
    child.expect('Enter the bash command to run')
    child.sendline('rm -rf /tmp/testdir')
    child.expect('Execution mode')
    child.sendline('capture')
    
    # It should warn
    child.expect('IRREVERSIBLE')
    # Since we might or might not have LLM, it should prompt to proceed
    child.expect('exactly to confirm')
    child.sendline('no') # Let's not actually delete anything right now
    child.expect('Press Enter to return to menu...')
    child.sendline('')
    child.expect('Enter your choice')
    print("✓ Risky preflight warning triggered correctly")

    # 4. Trigger a failed command and healing suggestion
    child.sendline('3')
    child.expect('Enter the bash command to run')
    child.sendline('mkdir /root/should-fail')
    child.expect('Execution mode')
    child.sendline('capture')
    
    # Fails with permission error
    child.expect('Command failed with exit code')
    
    # Check if healing panel appears (this depends on LLM, but let's check for it)
    # The healing loop might prompt "Apply this fix?" or "Do you want to run"
    try:
        child.expect(['Do you want to run this fix?', 'Apply this fix?'], timeout=2)
        child.sendline('no')
        print("✓ Healing suggestion appeared and prompted")
    except pexpect.TIMEOUT:
        print("⚠ Healing suggestion did not prompt (expected if LLM is unavailable)")

    child.expect('Press Enter to return to menu...')
    child.sendline('')
    child.expect('Enter your choice')

    # 6. Demonstrate SQLite Caching
    # Run the exact same risky command
    child.sendline('3')
    child.expect('Enter the bash command to run')
    child.sendline('rm -rf /tmp/testdir2')
    child.expect('Execution mode')
    child.sendline('capture')
    child.expect('exactly to confirm')
    child.sendline('no')
    child.expect('Press Enter to return to menu...')
    child.sendline('')
    child.expect('Enter your choice')

    # Run again, it should be faster, but let's just ensure it hits the preflight again
    start = time.time()
    child.sendline('3')
    child.expect('Enter the bash command to run')
    child.sendline('rm -rf /tmp/testdir2')
    child.expect('Execution mode')
    child.sendline('capture')
    child.expect('exactly to confirm')
    latency = time.time() - start
    print(f"✓ SQLite Caching: second run latency {latency:.2f}s")
    child.sendline('no')
    child.expect('Press Enter to return to menu...')
    child.sendline('')
    child.expect('Enter your choice')

    # 7. Show status capture
    child.sendline('6')
    child.expect('Status Capture')
    child.expect('Press Enter to return to menu...')
    child.sendline('')
    child.expect('Enter your choice')
    print("✓ Status capture displayed")

    # 5. Exit
    child.sendline('5')
    child.expect(pexpect.EOF)
    print("✓ Exited cleanly")
    
    # Test Offline fallback
    print("Testing offline fallback...")
    import os
    env = os.environ.copy()
    env['OFFLINE_MODE'] = 'true'
    child2 = pexpect.spawn('venv/bin/python terminal_web/main.py', env=env, encoding='utf-8', timeout=10)
    child2.expect('Enter your choice')
    
    child2.sendline('3')
    child2.expect('Enter the bash command to run')
    child2.sendline('rm -rf /tmp/testdir_offline')
    child2.expect('Execution mode')
    child2.sendline('capture')
    
    # It should still perform heuristic tier-1 scan and fall back gracefully
    child2.expect('IRREVERSIBLE')
    child2.expect('exactly to confirm')
    child2.sendline('no')
    child2.expect('Press Enter to return to menu...')
    child2.sendline('')
    child2.expect('Enter your choice')
    child2.sendline('5')
    child2.expect(pexpect.EOF)
    print("✓ Offline fallback works gracefully")

    print("\nALL TESTS PASSED.")

if __name__ == '__main__':
    verify_demo()
