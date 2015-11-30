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
<<<<<<< HEAD
S -> Cmd Sep S | Cmd
Sep -> "then"
Cmd -> "move" FileExp "to" Dir
FileExp -> FileList | Quantifier "in" Dir
Quantifier -> "all files" | "everything"
FileList -> File FileList | FilePair | File
=======
CmdList -> CmdList Sep Cmd | Cmd
Sep -> "and" | "then"
Cmd -> "move" FileExp "to" Dir
FileExp -> FileList | Quantifier "in" Dir
Quantifier -> "all files" | "everything"
FileList -> FileList "," FilePair | FilePair | File
>>>>>>> 0cdf21db7d239416676d61f72820b1c86ff1bdff
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
<<<<<<< HEAD
=======
Cmd -> "move" FileList "to" Dir
>>>>>>> 0cdf21db7d239416676d61f72820b1c86ff1bdff
Cmd -> "where am i"
Cmd -> "what directory am i in"
Cmd -> "new folder" String
Cmd -> "find" File
Cmd -> "clear history"
Cmd -> "go home"
Cmd -> "go back"
<<<<<<< HEAD
File -> "testfile" | "somefile" | "anotherfile"
Dir -> "somedir"
=======
File -> "test.file" | "another_one.txt"
Dir -> "/somedir" | "/"
>>>>>>> 0cdf21db7d239416676d61f72820b1c86ff1bdff
String -> "ladeeda" | "some string"
''');


<<<<<<< HEAD
# print(nltk.app.srparser())

=======
>>>>>>> 0cdf21db7d239416676d61f72820b1c86ff1bdff
# FIXME: this is broken: trying to figure out why. Probably the grammar is 
# still not right possibly something with FileList using left-recursion.

# UPDATE: made FileList right-recursive, still getting same errors

for sentence in generate(g, n=2):
  print(' '.join(sentence))


# TODO: should merge FileList and FileExp, since a list is technically a form of expression
# and we might want something like: "everything in /home and file.txt"