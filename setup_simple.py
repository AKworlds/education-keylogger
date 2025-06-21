"""
Simple setup script that handles Windows paths with spaces
"""

import os
import subprocess
import sys
from pathlib import Path

def main():
    print("Setting up Educational Keylogger...")
    
    # Get current directory
    current_dir = Path.cwd()
    print(f"Working in: {current_dir}")
    
    # Create virtual environment in current directory
    venv_path = current_dir / "venv"
    
    try:
        print("Creating virtual environment...")
        subprocess.run([sys.executable, "-m", "venv", str(venv_path)], check=True)
        print("✓ Virtual environment created")
        
        # Determine activation script path
        if os.name == 'nt':  # Windows
            activate_script = venv_path / "Scripts" / "activate.bat"
            pip_path = venv_path / "Scripts" / "pip.exe"
        else:  # Linux/Mac
            activate_script = venv_path / "bin" / "activate"
            pip_path = venv_path / "bin" / "pip"
        
        # Install packages
        print("Installing keyboard package...")
        subprocess.run([str(pip_path), "install", "keyboard"], check=True)
        print("✓ Keyboard package installed")
        
        print("\nSetup complete!")
        print(f"Virtual environment: {venv_path}")
        
        if os.name == 'nt':
            print(f"To activate: {activate_script}")
            print("Then run: python educational_keylogger.py")
        else:
            print(f"To activate: source {activate_script}")
            print("Then run: python educational_keylogger.py")
            
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
        print("Try running as administrator or check Python installation")
    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    main()