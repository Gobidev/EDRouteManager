import os


def copy_to_clipboard(text):
    command = 'echo ' + text.strip() + '| clip'
    os.system(command)
