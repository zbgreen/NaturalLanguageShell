# uses Python3.5, NLTK version 3.1
import nltk
from nltk.tag import *
from nltk.parse import *
from nltk.corpus import *
from nltk.parse.generate import *


# Also check out this link: http://www.nltk.org/howto/generate.html

####################################
'''First example of a grammar'''
####################################

grammar2 = nltk.CFG.fromstring("""
  S -> NP VP
  PP -> P NP
  NP -> Det N | NP PP
  VP -> V NP | VP PP
  Det -> 'a' | 'the'
  N -> 'dog' | 'cat'
  V -> 'chased' | 'sat'
  P -> 'on' | 'in'
  """)

for sentence in generate(grammar2, n=4):
  print(' '.join(sentence))


####################################
'''Second example of our grammar'''
####################################


grammar = nltk.CFG.fromstring("""

  S -> Cmd | Cmd Sep S

  String -> "SOME_STRING"

  Sep -> "then"

  Prep -> "in" | "to"

  Dir -> "SOME_DIRECTORY"

  DirList -> "SOME_DIRECTORY_LIST"

  File -> "FILE_NAME"

  FileExp -> FileList | Quantifier Prep Dir

  Quantifier -> "EVERYTHING"

  FileList -> File "," FileList | FilePair | File

  FilePair -> File "and" File

  Cmd -> "write" String "to" File | "show" File

""")


# print all possible sentence permutations with a depth of '4'. Change
# the value of 'n' to get more sentences

for sentence in generate(grammar, n=4):
  print(' '.join(sentence))








# A potential grammar to be adapted. Currently doesn't port over to NLTK's grammar
# creation perfectly, but it's a work in progress...
'''

CmdList -> Cmd Sep CmdList | Cmd
Sep -> "and" | "then"
Cmd -> "move" FileExp "to" Dir
FileExp -> FileList | Quantifier Dir
Qauntifier -> "all files" | "everything"
FileList -> File "," FileList | FilePair | File
FilePair -> File "and" File
Cmd ->  "print" File
        | "show" File
        | "open" File
        | "write" String "to" File
        | "put" String "into" File
        | "go to" DirList
        | "open" Dir
        | "what is in" Dir
        | "copy" FileList "to" Dir
        | "delete" FileList
        | "delete" DirList
        | "rename" File "to" <name>
        | "move" FileList "to" Dir
        | "where am i"
        | "what directory am i in"
        | "new folder" String
        | "find" File
        | "clear history"
        | "go home"
        | "go back"


'''
