import PageTemplate.MainWindow_support as window
import glob
import os


def pprint():
    window.w.Label.configure(text='Waiting')
    a = window.w.InputField.get('0.0', 'end')
    print(a.strip())


def saveToTxtFile(*args):
    userProfileFolder = os.getenv('USERPROFILE')
    targetTextFile = userProfileFolder + "\\Desktop\\file.txt"
    inputFieldText = window.w.InputField.get('0.0', 'end')
    print('Saved')
    with open(targetTextFile, 'a') as file:
        file.write(inputFieldText.strip() + '\n')
    window.w.InputField.delete('0.0', 'end')
# event=None
