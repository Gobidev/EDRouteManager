import os


def add_to_clipboard(text):
    command = 'echo ' + text.strip() + '| clip'
    os.system(command)
