#Natural Langauge Shell

import nltk
from shell import *

class main():

    def __init__(self):
        dictionary = {'print': 'cat',
                      'write': 'echo',
                      'go to': 'cd',
                      'copy': 'cp',
                      'delete': 'rm',
                      'rename': 'mv_rename',
                      'move': 'mv',
                      'where am i': 'pwd',
                      'new folder': 'mkdir',
                      'find': 'find',
                      'clear history': 'c_history',
                      'go home': 'cd_h',
                      'go back': 'cd -'}
        s = Shell()
        #self.main_loop()

    def main_loop(self):
        print("Welcome to the Natural Language shell.\n"
                  + "Enter your English commands in the terminal.\n"
                  + "Enter 'dictionary' to print list of supported commands.\n")
        input = ""
        #Input loop
        while input != "exit":
            print("")
            input = input("Enter Command: ")

    def command(self, string):
        #Remove beginning of string
        string = string[8:]
        #Find whitespace after command name and assign it to cmd
        index = string.index(" ")
        cmd = string[:index]
        #Remove command from string
        string = string[index + 1:]

        if cmd == "print":
            self.print(string)
        elif cmd == "open":
            self.open(string)
        elif cmd == "write":
            self.write(string)
        elif cmd == "rename":
            self.rename(string)
        elif cmd == "find":
            self.find(string)
        elif cmd == "where":
            self.where_am_i()
        elif cmd == "new":
            self.new_folder(string, index)
        elif cmd == "clear":
            self.clear_history()
        elif cmd == "go":
            self.go(string)

    def print(self, string):
        #Find whitespace before file name
        index = string.index(" ")
        string = string[index + 1:]
        #Find file name
        index = string.index(")")
        file = string[:index]
        #Execute Command
        s.cat(file)

    def open(self, string):
        #Find whitespace before dir name
        index = string.index(" ")
        string = string[index + 1:]
        #Find dir name
        index = string.index(")")
        dir = string[:index]
        #Execute Command
        s.cd(dir)

    def write(self, string):
        #Find whitespace before string
        index = string.index(" ")
        string = string[index + 1:]
        print(string)
        #Find Str name
        index = string.index(")")
        str = string[:index]
        print(str)
        #remove str from string
        string = string[index + 11:]
        print(string)
        #Find file name
        index = string.index(")")
        name = string[:index]
        #Execute Command
        s.echo(name, str)

    #TODO
    def copy(self, string):
        print(string)

    def rename(self, string):
        #Find whitespace before file
        index = string.index(" ")
        string = string[index + 1:]
        #Find file
        index = string.index(")")
        file = string[:index]
        #remove file from string
        string = string[index + 13:]
        #Find name
        index = string.index(")")
        name = string[:index]
        #Execute
        s.mv_rename(file, name)

    def find(self, string):
        print(string)
        #Find whitespace before file
        index = string.index(" ")
        string = string[index + 1:]
        print(string)
        #Find file
        index = string.index(")")
        file = string[:index]
        print(file)
        #Execute
        s.find(file)

    def where_am_i(self):
        s.pwd()

    def new_folder(self, string, index):
        print(string)
        #remove str from string
        string = string[index + 12:]
        print(string)
        #Find str
        index = string.index(")")
        str = string[:index]
        print(str)
        #Execute
        s.mkdir(str)

    def clear_history(self):
        s.c_history()

    def go(self, string):
        print(string)
        if "back" in string:
            s.cd_b()
        else:
            s.cd_h()


m = main()
#m.command("(S (Cmd print (File test.txt)))")
#m.command("(S (Cmd open (Dir /))")
#m.command("(S (Cmd write (String foo) to (File derp.txt)))")
#m.command("(S (Cmd rename (File derp.txt) to (String test.txt)))")
#m.command("(S (Cmd find (File derp.txt)))")
#m.command("(S (Cmd where am i))")
#m.command("(S (Cmd new folder (String truman)))")
#m.command("(S (Cmd clear history))")
#s.cd("/")
#m.command("(S (Cmd go back))")
#m.command("(S (Cmd go home))")

#TODO
#m.command("(S (Cmd copy (FileList (File FILE_NAME)) to (Dir SOME_DIRECTORY)))")