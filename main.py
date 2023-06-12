import os
from sys import argv, executable
from win32com.client import Dispatch

#Generating batch file
def bat_gen():
    with open("autologin.bat", "w") as file:
        file.write("@echo off\n")
        file.write("set \"RESOURCE_FILE=creds.txt\"\n")
        file.write(f"set \"PYTHON_PATH={python_path}\n")
        file.write(f"%PYTHON_PATH% autologin.py %RESOURCE_FILE%\n")
        file.write("exit")
        file.close()
# Getting the batch file path
script_path = os.path.abspath(argv[0])
script_dir = os.path.dirname(script_path)
script_path = os.path.join(script_dir, "autologin.bat")
python_path = executable

# Getting startup folder path
user_dir = os.path.expanduser("~")
startup_folder = os.path.join(user_dir, "AppData", "Roaming", "Microsoft", "Windows", "Start Menu", "Programs", "Startup")

# Creates a startup folder if it doesn't exist
if not os.path.exists(startup_folder):
    os.makedirs(startup_folder)


def is_logged():  # Checks if the user has entered the credentials
    with open("creds.txt", 'r') as file:
        USERNAME = file.readline().strip()
        if USERNAME == "f20xxxxxx":
            return False
        else:
            return True

# If the user has not logged in, then ask for the credentials
def creds():
    try:

        username = input("Enter your username: ")
        password = input("Enter your password: ")

        with open("creds.txt", 'w') as file:
            file.write(f"{username}\n")
            file.write(f"{password}")
        print("Credentials saved successfully!")
        set_startup_program()
    except FileNotFoundError:
        creds_path = os.path.join(script_dir, "creds.txt")
        os.mkdir(creds_path)


# Sets the program as a startup program
def set_startup_program():
    try:
        if is_logged():

            shortcut_path = os.path.join(startup_folder, "autologin.lnk")
            shell = Dispatch('WScript.Shell')
            shortcut = shell.CreateShortCut(shortcut_path)
            shortcut.Targetpath = script_path
            shortcut.WorkingDirectory = script_dir
            shortcut.save()
            print("Internet Auto Login set as startup program!")
        else:
            creds()
    except Exception as e:
        print(f"Error occurred while setting the startup program: {str(e)}")


if __name__ == "__main__":
    bat_gen()
    set_startup_program()
    
