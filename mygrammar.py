# uses Python3.5, NLTK version 3.1
import nltk
from nltk.tag import *
from nltk.parse import *
from nltk.corpus import *
from nltk.parse.generate import *

# It looks like the grammar that nltk expects in right
# recursive.

# fixed CmdList, need to do FileList
# FileList was: 
## FileList -> File "," FileList | FilePair | File

g = nltk.CFG.fromstring('''
CmdList -> CmdList Sep Cmd | Cmd
Sep -> "and" | "then"
Cmd -> "move" FileExp "to" Dir
FileExp -> FileList | Quantifier "in" Dir
Quantifier -> "all files" | "everything"
FileList -> FileList "," FilePair | FilePair | File
FilePair -> File "and" File
Cmd -> "print" File
Cmd -> "show" File
Cmd -> "open" File
Cmd -> "write" String "to" File
Cmd -> "put" String "into" File
Cmd -> "go to" DirList
Cmd -> "open" Dir
Cmd -> "what is in" Dir
Cmd -> "copy" FileList "to" Dir
Cmd -> "delete" FileList
Cmd -> "delete" DirList
Cmd -> "rename" File "to" Name
Cmd -> "move" FileList "to" Dir
Cmd -> "where am i"
Cmd -> "what directory am i in"
Cmd -> "new folder" String
Cmd -> "find" File
Cmd -> "clear history"
Cmd -> "go home"
Cmd -> "go back"
File -> "test.file" | "another_one.txt"
Dir -> "/somedir" | "/"
String -> "ladeeda" | "some string"
''');


# FIXME: this is broken: trying to figure out why. Probably the grammar is 
# still not right possibly something with FileList using left-recursion.

# UPDATE: made FileList right-recursive, still getting same errors

for sentence in generate(g, n=2):
  print(' '.join(sentence))


# TODO: should merge FileList and FileExp, since a list is technically a form of expression
# and we might want something like: "everything in /home and file.txt"