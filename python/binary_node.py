from pydantic import BaseModel
import typing

'''
Binary Node that has left and right children

Args:
    value: Contents of this node
    left: Reference to left child
    right: Reference to right child
'''
class BinaryNode(BaseModel):
    value: typing.Any
    left: 'BinaryNode' = None
    right: 'BinaryNode' = None
