import os
import subprocess

PROGRAMS_DIR = "programs"  # Folder where scripts/executables are stored

def list_programs():
    """Scans the programs directory and returns a list of available programs."""
    programs = []
    if not os.path.exists(PROGRAMS_DIR):
        os.makedirs(PROGRAMS_DIR)  # Ensure the directory exists
    for file in os.listdir(PROGRAMS_DIR):
        path = os.path.join(PROGRAMS_DIR, file)
        if os.path.isfile(path) and os.access(path, os.X_OK):  # Only list executable files
            programs.append(file)
    return programs

def launch_program(program):
    """Launches the selected program in a new window."""
    path = os.path.join(PROGRAMS_DIR, program)
    if os.name == "nt":  # Windows
        subprocess.Popen(f'start "" "{path}"', shell=True)
    elif os.name == "posix":  # macOS/Linux
        subprocess.Popen(f'xdg-open "{path}"' if "linux" in os.sys.platform else f'open "{path}"', shell=True)
    else:
        print("Unsupported OS")

def main_menu():
    """Displays the dynamic launcher menu."""
    while True:
        print("\n=== OMEGA Launcher ===")
        programs = list_programs()
        
        if not programs:
            print("No programs found. Add files to the 'programs' folder.")
        
        for i, program in enumerate(programs, 1):
            print(f"{i}. {program}")

        print("0. Exit")

        choice = input("\nSelect a program by number or name: ").strip()

        if choice == "0":
            print("Exiting OMEGA...")
            break
        elif choice.isdigit() and 1 <= int(choice) <= len(programs):
            launch_program(programs[int(choice) - 1])
        elif choice in programs:
            launch_program(choice)
        else:
            print("Invalid selection. Try again.")

if __name__ == "__main__":
    main_menu()
