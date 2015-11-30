# uses Python3.5, NLTK version 3.1
import nltk
from nltk.tag import *
from nltk.parse import *
from nltk.corpus import *
from nltk.parse.generate import *

# based on Aaron's grammar
grammar = nltk.CFG.fromstring("""
S -> Cmd | Cmd Sep S
Sep -> "then"
FilePair -> File "and" File
Cmd -> "write" String "to" File
Cmd -> "print" File
Cmd -> "show" File
Cmd -> "open" File
Cmd -> "put" String "into" File
Cmd -> "rename" File "to" String
Cmd -> "open" Dir
Cmd -> "find" File
Cmd -> "delete" Dir
Cmd -> "copy" File "to" Dir
Cmd -> "delete" File
Cmd -> "move" File "to" Dir
Cmd -> "where" "am" "i"
Cmd -> "new" "folder" String
Cmd -> "clear" "history"
Cmd -> "go" "home"
Cmd -> "go" "back"
Cmd -> "go" "to" Dir
Cmd -> "what" "directory" "am" "i" "in"
Cmd -> "what" "is" "in" Dir
String -> "SOME_STRING"
Dir -> "SOME_DIRECTORY"
File -> "FILE_NAME"
""")

# The following didn't work:
# delete SOME_DIRECTORY
# where am i
# new folder SOME_STRING
# clear history
# go home
# go back

# CHANGED FileList TO File
# Cmd -> "copy" File "to" Dir
# Cmd -> "delete" File
# Cmd -> "move" File "to" Dir

# NOT WORKING:
# FileExp -> FileList | Quantifier "in" Dir
# Quantifier -> "EVERYTHING" | "all files"
# FileList -> File "," FileList | File "and" File | File

# right recursive filelist:
#FileList -> File "," FileList | FilePair | File

# not working:
#Cmd -> "move" FileExp "to" Dir

# print all possible sentence permutations with a depth of '4'. Change
# the value of 'n' to get more sentences

#for sentence in generate(grammar, n=20):
#  print(' '.join(sentence))

sent = "rename FILE_NAME to SOME_STRING".split()
rd_parser = nltk.RecursiveDescentParser(grammar)
for tree in rd_parser.parse(sent):
    print(tree)

