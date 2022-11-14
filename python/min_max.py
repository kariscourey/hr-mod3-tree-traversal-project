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
    # if graph.left:
    #     return min_of_tree(graph.left)
    # return graph.left.value
    stack = [graph]
    the_min = float('inf')
    while len(stack) > 0:
        node = stack.pop()
        if node.value < the_min:
            the_min = node.value
        for child in ['left', 'right']:
            n = getattr(node, child)
            if n is not None:
                stack.append(n)
    return the_min

'''
Traverse the tree to find the maximum value in the tree
'''
def max_of_tree(graph):
    # if graph.right:
    #     return min_of_tree(graph.right)
    # return graph.right.value

    stack = [graph]
    the_max = float('-inf')
    while len(stack) > 0:
        node = stack.pop()
        if node.value > the_max:
            the_max = node.value
        for child in ['left', 'right']:
            n = getattr(node, child)
            if n is not None:
                stack.append(n)
    return the_max

# Pass these tests
assert min_of_tree(graph) == 1
assert max_of_tree(graph) == 7
