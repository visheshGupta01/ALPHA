import os
import subprocess as sp
from AppOpener import run

paths = {
    'notepad': "C:\\Windows\\System32\\notepad.exe",
    'calculator': "C:\\Windows\\System32\\calc.exe",
    'vscode': "C:\\Users\\vishe\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe",
    'twitter': "C:\\Users\\vishe\\AppData\\Local\\Microsoft\\Edge\\User Data\\Default\\Web Applications\\_crx__jgeocpdicgmkeemopbanhokmhcgcflmi\\Twitter.Ink"
}


def open_camera():
    sp.run('start microsoft.windows.camera:', shell=True)


def open_notepad():
    os.startfile(paths['notepad'])


def open_cmd():
    os.system('start cmd')


def open_calculator():
    sp.Popen(paths['calculator'])


def open_vscode():
    os.startfile(paths['vscode'])


def open_app(app):
    run(app)
