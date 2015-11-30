from nltk import RegexpParser

paser = RegexpParser('''
	List: {<Item> <Item>*}
''')