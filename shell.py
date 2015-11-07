"""
Zachary Green, Cindy La, Jonathan Price, Aaron Gershman

Shell class to execute bash commands.
"""
from subprocess import call, check_output


class Shell():
    """
    Id for refrencing previous commands. Call methods to execute the command.
    Executes the command using given inputs and prints out the bash command
    used.
    """
    def __init__(self, id):
        self.id = id
        self.cmd = ""

    #Calls cat to print the given file
    def print(self, file):
        try:
            self.cmd = "cat " + file
            call(self.cmd)
            print(self.cmd)
        except NameError:
            print("Invalid File name.")

    #Writes str to end of given file. File must exist.
    def write(self, str, file):
        try:
            self.cmd = "echo " + str + " >> " + file
            call(self.cmd, shell=True)
        except FileNotFoundError:
            print("File doesn't exist.")

    #Go to the given directory. Incorrect directory doesn't cause errors so
    #check_output is used to check return code for success.
    def goto(self, dir):
        self.cmd = "cd " + dir
        output = check_output(self.cmd, shell=True)
        if output == 0:
            print(self.cmd)
        else:
            print("Directory doesn't exist or can't be accessed.")

    #Open the given directory. Incorrect directory doesn't cause errors so
    #check_output is used to check return code for success.
    def open_dir(self, dir):
        self.cmd = "cd " + dir + "; ls"
        output = check_output(self.cmd, shell=True)
        if output == 0:
            print(self.cmd)
        else:
            print("Directory doesn't exist or can't be accessed.")

    #Copy 1 file to a given destination.
    def copy_1(self, file, dest):
        self.cmd = "cp " + file + dest
        output = check_output(self.cmd, shell=True)
        if output == 0:
            print(self.cmd)
        else:
            print("Source file doesn't exist or can't be accessed.")

    #Copies multiple files to a given destination.
    def copy_multiple(self, files, dest):
        self.cmd = "cp "
        for file in len(files):
            self.cmd = self.cmd + " " + file
        self.cmd = " " + dest
        output = check_output(self.cmd, shell=True)
        if output == 0:
            print(self.cmd)
        else:
            print("1 or more source files don't exist or can't be accessed.")

