## List of Use-Case Commands: 
format:
Natural language command
Shell command

----------------------------------


```
(print|show|open) <file>
cat <file>
```

----------------------------------

```
(write|echo|output) <string> to <file>
echo <string> >> <file>
```

----------------------------------

```
put <string> into <file>
echo <string> >> <file>
```

----------------------------------

```
go to <directory>
cd <directory>
```

----------------------------------

```
(open|what is in) <directory>
cd <directory>; ls
```

----------------------------------

```
copy <file>[, <file2>, …[,] and <fileN>] to <directory>
cp [-r] <file> [<file2> ... <fileN>] <dir>
```

----------------------------------

```
delete <file>[, <file2>, …[,] and <fileN>]
rm <file> [<file2> ... <fileN>]
```

----------------------------------

```
delete <directory> [<directory2>, …[,] and <directoryN>]
rm -r <directory> [<directory2> ... <directoryN>]
```

----------------------------------

```
rename <file> to <name>
mv <file> <name>
```

----------------------------------

```
move <file>[, <file2>, …[,] and <fileN>] to <directory>
mv <file> [<file2> ... <fileN>] <directory>
```

----------------------------------

```
where am i, what directory am i in
pwd
```

----------------------------------

```
new folder <name>
mkdir <name>
```

----------------------------------

```
find <file>
find <file>
```

----------------------------------

```
clear history
history -c
```

----------------------------------

```
undo
echo "Too Bad"
```

----------------------------------

```
go home
cd ~
```

----------------------------------

```
go back
cd ..
```

----------------------------------

## Potential Grammars:
```
Sentence -> Action PrepPhrase
PrepPhrase -> DirObj Prep IndObj | DirObj
Prep -> to | ...
DirObj -> Obj | ObjList
IndObj -> Obj | ObjList
ObjList -> Obj, ObjList | Obj and Obj
Obj -> <string> | File
File -> <filename> | <directory>

Command-specific grammars:

Command -> rename <File> to <string>
  | move <FileList> to <directory>
  | delete <FileList>
  | ...

TODO: define FileList (see ObjList definition) 
TODO: define Path /dir/dir/.../file

```

----------------------------------


Merging the contents of “grammar.txt” and “simple_grammar.txt” into one file.
This potential grammar was updated & created by JP on Nov. 15th 2015 (?)

```

CmdList -> Cmd Sep CmdList | Cmd
Sep -> "and" | "then"
Cmd -> "move" FileExp "to" Dir
FileExp -> FileList | Quantifier Dir
Quantifier -> "all files" | "everything"
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

```
