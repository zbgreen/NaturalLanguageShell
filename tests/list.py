from nltk.tree import Tree

# A grammar
'''
List -> Item List | Item
'''
# Sample:
# (List Item Item Item)

# (List (Item "one") 
#		(List (Item "two") 
#			  (List (Item "three"))))

## TODO: later: expand grammar
# S -> Cmd List "to" Item
# Cmd -> "delete"


############

t1 = Tree('List', [
	Tree('Item', [1]), 
	Tree('List', [
		Tree('Item', [2]),
		Tree('List', [Tree('Item', [3])])])])
		

print(t1)
print(t1.flatten())

###########

# A slightly larger grammar
'''
S -> "copy" List "to" Item
S -> "delete" List
S -> "rename" Item "to" Item
List -> Item List | Item
'''

#(copy (List ...) to (Item ...))
#(copy (List f1 (List f2 (List f3))) to (Item folder))

# Tree('S', ['copy', Tree('List', [...]), to, Tree('Item', [...])])
t2 = Tree('S', [
	'copy', 
	Tree('List', [
		Tree('Item', ['f1']), 
		Tree('List', [
			Tree('Item', ['f2']),
			Tree('List', [Tree('Item', ['f3'])])])]),
	'to', 
	Tree('Item', ['folder'])])

print(t2)
print(t2.flatten())
print(type(t2.flatten()))
print(t2.collapse_unary())

max_subtree = Tree('', [])
for subtree in t2.subtrees(filter = lambda x: x.label() == 'List'):
	if len(subtree.flatten().pos()) > len(max_subtree.pos()):
		max_subtree = subtree
print(max_subtree)


'''
tmp = t2
i = 
while tmp.label() != 'List':
	i += 1
	tmp = tmp.pos()
	print("the " + str(i) + " time:")
	print(tmp)
	print(type(tmp))
tmp = tmp.flatten()

print(t2)
'''