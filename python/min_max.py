from binary_node import BinaryNode as Node

n1 = Node(value=2)
n2 = Node(value=5)
n3 = Node(value=1, left=n1, right=n2)
n4 = Node(value=7)
n5 = Node(value=3)
n6 = Node(value=6, left=n4, right=n5)
n7 = Node(value=4, left=n3, right=n6)

graph = n7

'''
Traverse the tree to find the minimum value in the tree
'''
def min_of_tree(graph):
    pass

'''
Traverse the tree to find the maximum value in the tree
'''
def max_of_tree(graph):
    pass

# Pass these tests
assert min_of_tree(graph) == 1
assert max_of_tree(graph) == 7
