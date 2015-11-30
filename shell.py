"""
Zachary Green, Cindy La, Jonathan Price, Aaron Gershman

Shell class to execute bash commands.
"""
import os
from subprocess import call, check_output, CalledProcessError

class Shell():
    """
    Call methods to execute the command.
    Executes the command using given inputs, stores cmd and prints results.

    cmd: for refrencing previous commands.
    """
    def __init__(self):
        self.cmd = []
    '''Executes the command using given inputs, stores command and directories, and
    prints results.

    !!!WARNING!!!
    USE AT YOUR OWN DISCRETION. THIS CODE DIRECTLY EXECUTES OPERATING SYSTEM
    COMMANDS. WE DID NOT IMPLEMENT INPUT SANITATION SO USE THIS CODE CAREFULLY.
    POTENTIAL SIDE EFFECTS INCLUDE ALTERING YOUR FILES, DELETING EVERYTHING OFF
    YOUR COMPUTER AND MORE. CONSULT THE DOCUMENTATION TO SEE IF THIS PROGRAM IS
    RIGHT FOR YOU.
    !!!END WARNING!!!

    Fields:
    cmd: for referencing previous commands.
    dir: for referencing previous directories.
    '''
    def __init__(self):
        self.cmd = []
        self.dir = []

        #Add initial directory to list
        dir = check_output("pwd")
        #Decode from byte literals to string
        dir = dir.decode("utf-8")
        #remove "\n" from string
        dir = dir[:-1]

        self.dir.append(dir)

    """
    Clears current class's representation of history. Does not clear the bash
    history since Python runs sh.
    """
    def c_history(self):
        self.cmd[:] = []
        print("History deleted.")

    """
    See what user is running the commands.
    """
    def whoami(self):
        print(call(["whoami"]))
        self.cmd.append("whoami")

    """
    Print current directory.
    """
    def ls(self):
        call("ls")
        self.cmd.append("ls")

    """
    Calls cat to print the given file.
    """
    def cat(self, file):
        try:
            print(call(["cat", file]))
            self.cmd.append("cat " + file)
        except CalledProcessError:
            print("Invalid File name.")

    """
    Writes string to end of given file if it exists.
    If file doesn't exist it will create new file with given text.
    """
    def echo(self, file, str):
        try:
            cmd = "echo " + str + " >> " + file
            call(cmd, shell=True)
            #Manually call cat to print file to avoid having cmd added to list.
            print(call(["cat", file]))
            self.cmd.append(cmd)
        except TypeError:
            print("Must pass string type.")

    """
    Change directory to root.
    """
    def cd_root(self):
        os.chdir("/")
        call("ls")
        self.cmd.append("cd")
        self.dir.append("/")

    """
    Change directory to home.
    """
    def cd_h(self):
        os.chdir("/home")
        call("ls")
        self.cmd.append("cd ~")

    # """
    # Go back a directory. Currently not implemented due to not having directory
    # history.
    # """
    # def cd_b(self):
    #     print()
        self.dir.append("/home")

    """
    Go back a directory. Prints name of current directory.
    """
    def cd_b(self):

        try:
            #Pop current directory
            del self.dir[-1]
            #Get last directory from list
            dir = self.dir[-1]
            os.chdir(dir)
            call("pwd")
            self.cmd.append("cd -")
        except IndexError:
            print("No directory to go back to.")

    """
    Go to the given directory.
    """
    def cd(self, dir):
        try:
            os.chdir(dir)
            call("ls")
            self.cmd.append("cd " + dir)
            self.dir.append(dir)
        except FileNotFoundError:
            print("The file or directory " + dir + " doesn't exist.")

    """
    Copies 1 or more files from a list to a given destination. Prints contents
    of the directory without changing to it.
    """
    def cp(self, files, dest):
        try:
            #copy files to given destination
            cmd = "cp"
            for file in files:
                cmd += " " + file
            cmd += " " + dest
            call(cmd, shell=True)

            #print given directory without changing current directory
            newCmd = "ls " + dest
            call(newCmd, shell=True)

            self.cmd.append(cmd)
        except FileNotFoundError:
            print("File(s) or destination don't exist or can't be accessed.")

    """
    Print current directory name
    """
    def pwd(self):
        print(call(["pwd"]))
        self.cmd.append("pwd")

    """
    Delete 1 or more directories or files. Prints names of directories that were
    successfully deleted.
    """
    def rm(self, list):
        try:
            cmd = "rm -r"
            for element in list:
                cmd += " " + element
            call(cmd, shell=True)
            self.cmd.append(cmd)
            print(str(list) + " has/have been deleted.")
        except FileNotFoundError:
            print("1 or more Directories don't exist or can't be accessed.")

    """
    Rename file to given name. Must not be same name.
    """
    def mv_rename(self, file, name):
        try:
            call(["mv", file, name])
            print(file + " has been renamed to " + name)
            self.cmd.append("mv " + file + " " + name)
        except FileNotFoundError:
            print("File not found.")

    """
    Move file(s) to given directory. Directory must be checked to ensure that
    file doesn't get renamed to non-existing directory name. Prints updated
    directory.
    """
    def mv(self, files, dir):
        try:
            #Test directory to make sure it exists.
            testDir = "-d " + dir
            call(testDir, shell=True)

            #Directory exists so continue.
            cmd = "mv"
            for file in files:
                cmd += " " + file
            cmd += " " + dir
            print(cmd)
            call(cmd, shell=True)

            #print updated directory
            upDir = "ls " + dir
            print(call(upDir, shell=True))
            self.cmd.append(cmd)
        except FileNotFoundError:
            print("File(s) or directory don't exist or can't be accessed.")

    """
    Make new directory. Print new directory name.
    """
    def mkdir(self, name):
        call(["mkdir", name])
        print("New directory " + name + " has been created.")
        self.cmd.append("mkdir " + name)

    """
    Find given file. Print out given file.
    """
    def find(self, file):
        try:
            check_output(["find", file])
            call(["cat", file])
            self.cmd.append("find " + file)
        except CalledProcessError:
            print("File not found.")


    """
    Get directory list.
    """
    def get_dir(self):
        return self.dir

    """
    Get command list.
    """
    def get_cmd(self):
        return self.cmd

#Initialize object
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
# s.echo("t.txt", "foo")

#cd to root
#s.cd_root()
#cd to home
# s.cd_h()
#cd back a directory
s.cd("/home/zach/PycharmProjects")
s.cd_b()
#s.cd("/home/zach/PycharmProjects")
#s.cd_b()
#cd to given directory
#s.cd("/home")

#Copy file to existing file
#s.cp("test.txt", "t.txt")
#Copy file and create new copy
#s.cp("test.txt", "a.txt")

#Copy file to given destination
# file =["test.txt"]
# s.cp(file, "~/CS480")
#Copy multiple files to given destination
# files = ["test.txt", "t.txt"]
# s.cp(files, "~/CS480")

#Print current directory name
#s.pwd()

#Delete directories or files
#l = ["t.txt"]
#s.rm_d(l)
#Delete directories
# l = ["dirTest", "dirTest2"]
# s.rm_d(l)

#Rename file to given name
# s.mv_rename("~/CS480", "t.txt")

#Move file to directory
# file = ["t.txt"]
# s.mv(file, "~CS480")
#Move files to directory. -d is currently an illegal option but works.
# files = ["t.txt", "test.txt"]
# s.mv(files, "~/CS480")

#Print current directory
#s.ls()

#Create new directory
# s.mkdir("dir")

#Find file
# s.find("t.txt")

#Clear history
s.c_history()
#s.c_history()

#Go back a directory
#s.cd_b()
