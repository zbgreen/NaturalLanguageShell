# uses Python3.5, NLTK version 3.1
import nltk
from nltk.tag import *
from nltk.parse import *
from nltk.corpus import *
from nltk.parse.generate import *

# based on Aaron's grammar

grammar = nltk.CFG.fromstring("""
S -> Cmd | Cmd Sep S
<<<<<<< HEAD
Sep -> "then" 
=======
String -> "SOME_STRING"
Sep -> "then" | "and"
Dir -> "SOME_DIRECTORY"
DirList -> "SOME_DIRECTORY_LIST"
File -> "FILE_NAME"
>>>>>>> 0cdf21db7d239416676d61f72820b1c86ff1bdff
FileExp -> FileList | Quantifier "in" Dir
Quantifier -> "EVERYTHING" | "all files"
FileList -> File "," FileList | File "and" File | File
FilePair -> File "and" File
Cmd -> "write" String "to" File
Cmd -> "print" File
Cmd -> "show" File
Cmd -> "open" File
Cmd -> "put" String "into" File
<<<<<<< HEAD
Cmd -> "rename" File "to" String
=======
Cmd -> "rename" File "to" Name
>>>>>>> 0cdf21db7d239416676d61f72820b1c86ff1bdff
Cmd -> "open" Dir
Cmd -> "what is in" Dir
Cmd -> "where am i"
Cmd -> "what directory am i in"
Cmd -> "new folder" String
Cmd -> "find" File
Cmd -> "clear history"
Cmd -> "go home"
Cmd -> "go back"
<<<<<<< HEAD
String -> "SOME_STRING"
Dir -> "SOME_DIRECTORY"
File -> "FILE_NAME"
""")



=======
Cmd -> "delete" DirList
Cmd -> "go to" DirList
Cmd -> "copy" FileList "to" Dir
Cmd -> "delete" FileList
Cmd -> "move" FileList "to" Dir
""")

>>>>>>> 0cdf21db7d239416676d61f72820b1c86ff1bdff
# right recursive filelist:
#FileList -> File "," FileList | FilePair | File

# not working:
#Cmd -> "move" FileExp "to" Dir

# maybe not worknig
# Cmd -> "copy" FileList "to" Dir
# Cmd -> "delete" FileList
# Cmd -> "move" FileList "to" Dir

# print all possible sentence permutations with a depth of '4'. Change
# the value of 'n' to get more sentences

<<<<<<< HEAD
#for sentence in generate(grammar, n=20):
#  print(' '.join(sentence))

sent = "rename FILE_NAME to SOME_STRING".split()
rd_parser = nltk.RecursiveDescentParser(grammar)
for tree in rd_parser.parse(sent):
    print(tree)
=======
for sentence in generate(grammar, n=20):
  print(' '.join(sentence))


>>>>>>> 0cdf21db7d239416676d61f72820b1c86ff1bdff

