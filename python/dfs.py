from binary_node import BinaryNode as Node

n1 = Node(value='A')
n2 = Node(value='B')
n3 = Node(value='C', left=n1, right=n2)
n4 = Node(value='D')
n5 = Node(value='E')
n6 = Node(value='F', left=n4, right=n5)
n7 = Node(value='G', left=n3, right=n6)

graph = n7

'''
Implement Depth First Search
1. First, check if the root node is the target. If it is, return the root node.
2. Otherwise, add the children of the current node to the **stack** of nodes.
3. Pop each from the stack and check if each are the target.
4. Return if target. Otherwise, go to step 2 and repeat.
'''
def dfs(graph, target_value):
    # if graph.value == target_value:
    #     return graph
    # elif graph.left.value == target_value:
    #     return graph.left
    # elif graph.right.value == target_value:
    #     return graph.right
    # elif graph.left.value > target_value:
    #     return dfs(graph.left, target_value)
    # elif graph.right.value > target_value:
    #     return dfs(graph.right, target_value)
    stack = [graph]
    while len(stack) > 0:
        node = stack.pop()
        if node.value == target_value: return node
        if node.left is not None:
            stack.append(node.left)
        if node.right is not None:
            stack.append(node.right)
    return None


# Pass these tests
assert dfs(graph, 'G').value == 'G'
assert dfs(graph, 'C').left.value == 'A'
assert dfs(graph, 'F').right.value == 'E'
assert dfs(graph, 'E').left == None
