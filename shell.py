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

    #Calls cat to print the given file
    def print(self, file):
        try:
            cmd = "cat " + file
            call(cmd)
            print(cmd)
        except NameError:
            print("Invalid File name.")

    #Writes str to end of given file. File must exist.
    def write(self, str, file):
        try:
            cmd = "echo " + str + " >> " + file
            call(cmd, shell=True)
        except FileNotFoundError:
            print("File doesn't exist.")

    #Go to the given directory. Incorrect directory doesn't cause errors so
    #check_output is used to check return code for success.
    def goto(self, dir):
        cmd = "cd " + dir
        output = check_output(cmd, shell=True)
        if output != 0:
            print(cmd)
        else:
            print("Directory doesn't exist or can't be accessed.")



