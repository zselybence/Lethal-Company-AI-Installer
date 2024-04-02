import customtkinter as ctk
import os
import platform
import webbrowser

folder = ""
def installerfolder(folder_path,install_button):
    """
    Function to select a directory for installation.

    This function prompts the user to select a directory using a file dialog window.
    If a directory is selected, it updates the global variable 'folder' with the chosen path,
    sets the path to a tkinter variable 'folder_path', and packs the install button for further action.
    Additionally, it changes the current working directory to the selected folder.

    Note:
    - This function relies on the 'ctk' module for the file dialog window.
    - The global variable 'folder' is updated to reflect the selected directory.

    Returns:
    None
    """
    global folder
    folder = ctk.filedialog.askdirectory()
    if folder != "":
        folder_path.set(folder)
        install_button.pack(pady=5)
        os.chdir(folder)
    
def install(app):
    """
    Function to install and setup the Lethal Company AI project.

    This function clones the project repository from GitHub, sets up a virtual environment,
    activates it based on the operating system, installs necessary dependencies, and launches
    the Jupyter notebook.

    Note:
    - This function assumes that the required packages are listed in 'requirements.txt' file.
    - 'git' and 'python' should be installed and accessible from the command line.
    - It's recommended to run this function in a directory where the user has appropriate permissions.

    Returns:
    None

    Raises:
    OSError: If any operation related to file system, environment activation, or package installation fails.
    """
    os.system("git clone https://github.com/Synt-Axe/lethal-company-ai.git")
    os.chdir(f"{folder}/lethal-company-ai")
    os.system("python -m venv lcenv")
    if platform.system() == "Linux":
        os.system("source lcenv/bin/activate")
    elif platform.system() == "Windows":
        os.system(".\lcenv\Scripts\activate")
    os.system("python -m pip install --upgrade pip")
    os.system("pip install ipykernel")
    os.system("python -m ipykernel install --user --name=lcenv")
    os.system("pip install -r requirements.txt")
    os.system("python -m notebook")
    app.destroy()

def openurl(url):
    """
    Open a web URL in the default browser.

    Args:
    url (str): The URL of the webpage to open in the default web browser.

    Returns:
    None

    Raises:
    This function does not raise any exceptions.
    """
    webbrowser.open(url)

def main():
    #Set Customtkinter appearance and color theme
    ctk.set_appearance_mode("System")
    ctk.set_default_color_theme("blue")
    #Create ctk instance
    app = ctk.CTk()

    #Add title to the installer
    app.title("LethalCompanyAIInstaller")

    #Initialize all widgets used in the installer
    folder_path = ctk.StringVar(app)
    mlbl = ctk.CTkLabel(app, text="If you have already installed the repo, you can still run this file to update/play (with) the AI (in case it gets updated).").pack(pady=5)
    crlbl = ctk.CTkLabel(app, text="AI made by: syntaxeai").pack()
    btn1 = ctk.CTkButton(app, text="His Video", command=lambda: openurl("https://www.youtube.com/watch?v=poZt_KjCwV4&t")).pack(pady=5)
    btn1 = ctk.CTkButton(app, text="Channel", command=lambda: openurl("https://youtube.com/@synt_axe?sub_confirmation=1")).pack(pady=5)
    btn1 = ctk.CTkButton(app, text="Discord server", command=lambda: openurl("https://discord.com/invite/emgtCVS6Vs")).pack(pady=5)
    crfmlbl = ctk.CTkLabel(app,text="This installer was made by: magicnothief").pack(pady=5)
    folder_button = ctk.CTkButton(app,command=lambda:installerfolder(folder_path,install_button), text="Select parent folder for installation/already existing parent folder").pack(pady=5)
    lbl1 = ctk.CTkLabel(master=app,textvariable=folder_path).pack(pady=5)
    install_button = ctk.CTkButton(app,command=lambda:install(app),text="Install/Play")

    #Set installer default  size
    app.geometry("800x480")

    #Start application
    app.mainloop()

if __name__ == "__main__":
    main()