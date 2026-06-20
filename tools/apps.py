import subprocess


APPS = {
    "vscode": ["code"],
    "notepad": ["notepad.exe"],
    "github": ["explorer.exe", "https://github.com"],
}


def open_app(app_name):

    app_name = app_name.lower()

    if app_name not in APPS:

        return f"I don't know how to open {app_name}."

    subprocess.Popen(APPS[app_name])

    return f"Opening {app_name}..."