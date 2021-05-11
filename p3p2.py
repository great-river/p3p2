#!/usr/bin/env python3
import subprocess
import os

class P3P2:
    def __init__(self, home_path=os.getcwd()):
        self.home_path = home_path

    def call(self, python2_file_name, arguments=()):
        if python2_file_name.find('.py') < 0:
            python2_file_name = python2_file_name + '.py'
        file_path = os.path.join(self.home_path, python2_file_name)
        command = ['python2'] + [file_path] + list(arguments)
        process = subprocess.Popen(command, stdout=subprocess.PIPE)
        output, error = process.communicate()
        if error is not None:
            print(error)
            raise ValueError("Facing an error when try to execute " + command.join())
        return output
