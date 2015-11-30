"""
Zachary Green, Cindy La, Jonathan Price, Aaron Gershman

Shell class to execute bash commands.
"""
import os
from subprocess import call, check_output, CalledProcessError

class Shell():
    """
    Call methods to execute the command.
    Executes the command using given inputs, stores command and directories, and
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
    """
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


    def c_history(self):
        """
        Clears current class's representation of history. Does not clear the bash
        history since Python runs sh.
        """
        self.cmd[:] = []
        print("History deleted.")


    def whoami(self):
        """
        See what user is running the commands.
        """
        print(call(["whoami"]))
        self.cmd.append("whoami")


    def ls(self):
        """
        Print current directory.
        """
        call("ls")
        self.cmd.append("ls")


    def cat(self, file):
        """
        Calls cat to print the given file.
        """
        try:
            print(call(["cat", file]))
            self.cmd.append("cat " + file)
        except CalledProcessError:
            print("Invalid File name.")

    def echo(self, file, str):
        """
        Writes string to end of given file if it exists.
        If file doesn't exist it will create new file with given text.
        """
        try:
            cmd = "echo " + str + " >> " + file
            call(cmd, shell=True)
            #Manually call cat to print file to avoid having cmd added to list.
            print(call(["cat", file]))
            self.cmd.append(cmd)
        except TypeError:
            print("Must pass string type.")


    def cd_root(self):
        """
        Change directory to root.
        """
        os.chdir("/")
        call("ls")
        self.cmd.append("cd")
        self.dir.append("/")


    def cd_h(self):
        """
        Change directory to home.
        """
        os.chdir("/home")
        call("ls")
        self.cmd.append("cd ~")
        self.dir.append("/home")


    def cd_b(self):
        """
        Go back a directory. Prints name of current directory.
        """
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


    def cd(self, dir):
        """
        Go to the given directory.
        """
        try:
            os.chdir(dir)
            call("ls")
            self.cmd.append("cd " + dir)
            self.dir.append(dir)
        except FileNotFoundError:
            print("The file or directory " + dir + " doesn't exist.")


    def cp(self, files, dest):
        """
        Copies 1 or more files from a list to a given destination. Prints contents
        of the directory without changing to it.
        """
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


    def pwd(self):
        """
        Print current directory name
        """
        print(call(["pwd"]))
        self.cmd.append("pwd")


    def rm(self, list):
        """
        Delete 1 or more directories or files. Prints names of directories that were
        successfully deleted.
        """
        try:
            cmd = "rm -r"
            for element in list:
                cmd += " " + element
            call(cmd, shell=True)
            self.cmd.append(cmd)
            print(str(list) + " has/have been deleted.")
        except FileNotFoundError:
            print("1 or more Directories don't exist or can't be accessed.")


    def mv_rename(self, file, name):
        """
        Rename file to given name. Must not be same name.
        """
        try:
            call(["mv", file, name])
            print(file + " has been renamed to " + name)
            self.cmd.append("mv " + file + " " + name)
        except FileNotFoundError:
            print("File not found.")


    def mv(self, files, dir):
        """
        Move file(s) to given directory. Directory must be checked to ensure that
        file doesn't get renamed to non-existing directory name. Prints updated
        directory.
        """
        try:
            #Test directory to make sure it exists.
            testDir = "-d " + dir
            call(testDir, shell=True)

            #Directory exists so continue.
            cmd = "mv"
            for file in files:
                cmd += " " + file
            cmd += " " + dir
            call(cmd, shell=True)

            #print updated directory
            upDir = "ls " + dir
            print(call(upDir, shell=True))
            self.cmd.append(cmd)
        except FileNotFoundError:
            print("File(s) or directory don't exist or can't be accessed.")


    def mkdir(self, name):
        """
        Make new directory. Print new directory name.
        """
        call(["mkdir", name])
        print("New directory " + name + " has been created.")
        self.cmd.append("mkdir " + name)


    def find(self, file):
        """
        Find given file. Print out given file.
        """
        try:
            check_output(["find", file])
            call(["cat", file])
            self.cmd.append("find " + file)
        except CalledProcessError:
            print("File not found!.")

    def get_dir(self):
        """
        Find given file. Print out given file.
        """
        return self.dir


    def get_cmd(self):
        """
        Get command list.
        """
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
#s.c_history()

#Go back a directory
#s.cd_b()