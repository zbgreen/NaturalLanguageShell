# uses Python3.5, NLTK version 3.1
import nltk
from nltk.tag import *
from nltk.parse import *
from nltk.corpus import *
from nltk.parse.generate import *



'''
Accepts a string, returns a 'grammified' version
of that string-- it will be a parsed tree, but

'''
def grammify(sent):

    #EDITED GRAMMAR
    grammar = nltk.CFG.fromstring("""
    S -> Cmd | Cmd Sep S
    Sep -> "then"
    Cmd -> "write" String "to" String
    Cmd -> "print" String
    Cmd -> "put" String "into" String
    Cmd -> "rename" String "to" String
    Cmd -> "open" String
    Cmd -> "find" String
    Cmd -> "copy" String "to" String
    Cmd -> "delete" String
    Cmd -> "move" String "to" String
    Cmd -> "new" "folder" String
    Cmd -> "clear" "history"
    Cmd -> "go" "home"
    Cmd -> "go" "back"
    Cmd -> "go" "to" String
    Cmd -> "where" "am" "i"
    Cmd -> "what" "directory" "am" "i" "in"
    Cmd -> "what" "is" "in" String
    String -> "STRING"
    """)

    # Example sentence
    sent = sent.split()



    # REGEX identifiers to tag words with their respective
    # parts of speech as either commands, prepositions, locations, or strings
    pattern = [
        (r'(write|print|put|rename|open|find|copy|delete|move|clear|go)$', 'COMMAND'),
        (r'(into|to|in)$', 'PREP'),
        (r'(home|back)$', 'LOCATION'),
        (r'\'[^\]]*\'$', 'STRING')
    ]



    # Set up the tagger for regex
    tagger = nltk.RegexpTagger(pattern)

    # List of terminal classifiers and their actual string counterparts
    terminals = []
    opp_terminals = []

    # Separate out the parts of speech from the sentence
    # and add them to a list of terminals and
    # a list of actual proper nouns
    for (token, tag) in tagger.tag(sent):
        if tag in ['PREP', 'COMMAND', 'LOCATION']:
            terminals.append(token)
        elif tag == 'STRING':
            terminals.append(tag)
            opp_terminals.append(token)

        else: #if None
            terminals.append(token)

    # Parse out the grammar and pass in the terminals
    # from the tokenized words

    # TO DO????
    parser = nltk.ChartParser(grammar)
    for tree in parser.parse(terminals):
        # ????????
        True
            
    # Turn the tree object into a String
    tree_string = str(tree);


    # Zip the two lists together while replacing the
    # word "STRING" with the actual words back that
    # were previously used before we stripped them back out for
    # use in our grammar
    tmp = tree_string
    for i in range(len(opp_terminals)):

        # remove the apostrophies around the word
        tmp = re.sub(r'STRING', (opp_terminals[i].strip('\'')), tmp, 1);


    return(tmp)

t_sent = "  rename 'Jazzy_Jeff' to 'Disco_Dave' "

print(grammify(t_sent))



