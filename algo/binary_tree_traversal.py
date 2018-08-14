sys.path.insert(0, '../ds')
import tree

def ppreorder(root):
	if root:
		print(root.val)
		ppreorder(root.left)
		ppreorder(root.right)

def pinorder(root):
	if root:
		pinorder(root.left)
		print(root.val)
		pinorder(root.right)

def ppostorder(root):
	if root:
		ppostorder(root.left)
		ppostorder(root.right)
		print(root.val)

def lpreorder(root):
	if root:
		return [root.val] + lpreorder(root.left) + lpreorder(root.right)

def linorder(root):
	if root:
		return linorder(root.left) + [root.val] + linorder(root.right)

def lpostorder(root):
	if root:
		return lpostorder(root.left) + lpostorder(root.right) + [root.val]


