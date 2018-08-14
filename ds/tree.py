class Tree:
	def __init__(self, data=0, children=[]):
		self.data = data
		self.children = children

	def leaf(self):
		return len(self.children) == 0

class BinaryTree:
	def __init__(self, left=None, data=0, right=None):
		self.data = data
		self.left = left
		self.right = right

	def leaf(self):
		return self.left is None and self.right is None

class Trie
class Graph
		