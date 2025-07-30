class PyTerminal < Formula
  desc "A powerful terminal-based UI web project using Python and Rich"
  homepage "https://github.com/yourusername/py_terminal"
  url "https://github.com/yourusername/py_terminal/archive/refs/tags/v1.0.0.tar.gz"
  sha256 "YOUR_SHA256_HERE"  # Replace with actual SHA256
  license "Unlicense"

  depends_on "python@3.11"

  def install
    system "python3", "-m", "pip", "install", *std_pip_args, "."
  end

  test do
    system "#{bin}/py-terminal", "--help"
  end
end 