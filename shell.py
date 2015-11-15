"""
Zachary Green, Cindy La, Jonathan Price, Aaron Gershman

Shell class to execute bash commands.
"""
import os
from subprocess import call, check_output, CalledProcessError

class Shell():
    """
    Id for refrencing previous commands. Call methods to execute the command.
    Executes the command using given inputs and prints out the bash command
    used.
    """
    def __init__(self):
        self.cmd = []

    # #Clear history.
    # def c_history(self):
    #     call("history", shell=True)

    #See what user is running the commands
    def whoami(self):
        print(check_output(["whoami"]))
        self.cmd.append("whoami")

    #Calls cat to print the given file
    def cat(self, file):
        try:
            print(check_output(["cat", file]))
            self.cmd.append("cat " + file)
        except CalledProcessError:
            print("Invalid File name.")

    #Writes string to end of given file if it exists.
    #If file doesn't exist it will create new file with given text.
    def echo(self, file, str):
        try:
            s = "echo " + str + " >> " + file
            check_output(s, shell=True)
            self.cmd.append(s)
        except TypeError:
            print("Must pass string type.")

    #Change directory to root
    def cd_root(self):
        os.chdir("/")
        call("ls")
        self.cmd.append("cd")

    # #Go to the given directory. Incorrect directory doesn't cause errors so
    # #check_output is used to check return code for success.
    # def cd(self, dir):
    #     s = "cd " + dir
    #     output = check_output(s, shell=True)
    #     if output == 0:
    #         print(self.output)
    #     else:
    #         print("Directory doesn't exist or can't be accessed.")

    #Open the given directory. Incorrect directory doesn't cause errors so
    #check_output is used to check return code for success.
    def cd(self, dir):
        self.cmd = "cd " + dir + "; ls"
        output = check_output(self.cmd, shell=True)
        if output == 0:
            print(self.cmd)
        else:
            print("Directory doesn't exist or can't be accessed.")

    #Copy 1 file to a given destination.
    def cp(self, file, dest):
        self.cmd = "cp " + file + dest
        output = check_output(self.cmd, shell=True)
        if output == 0:
            print(self.cmd)
        else:
            print("Source file doesn't exist or can't be accessed.")

    #Copies multiple files to a given destination.
    def cp_multi(self, files, dest):
        self.cmd = "cp "
        for file in len(files):
            self.cmd = self.cmd + " " + file
        self.cmd = " " + dest
        output = check_output(self.cmd, shell=True)
        if output == 0:
            print(self.cmd)
        else:
            print("1 or more source files don't exist or can't be accessed.")

s = Shell()

#done

#whoami
#s.whoami()

#Print unexisting file
#s.cat("t.txt")
#Print existing file
#s.cat("test.txt")

#Try to add integer to end of file
#s.echo("test.txt", 1)
#Add string to end of file
#s.echo("test.txt", "foo")
#Create new file from given string
#s.echo("t.txt", "foo")

#In progress
s.cd_root()

