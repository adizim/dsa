sys.path.insert(0, '../ds')
import tree

from collections import deque

def ppreorder(root):
	if root:
		print(root.val)
		for child in root.children:
			ppreorder(child)

def ppostorder(root):
	if root:
		for child in root.children:
			ppostorder(child)
		print(root.val)

def lpreorder(root):
	if root:
		return [root.val] + [lpreorder(child) for child in root.children]

def lpostorder(root):
	if root:
		return [lpostorder(child) for child in root.children] + [root.val]

def dfs(root):
	return lpreorder(root)

def bfs(root):
	result = []
	q = deque()
	if root:
		q.append(root)
	while q:
		cur = q.popleft()
		result.append(cur)
		for child in cur.children:
			q.append(child)
	return result

