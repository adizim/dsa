class SLLNode:
	def __init__(self, data=0, next=None):
		self.data = data
		self.next = next
	
	def __repr__(self):
		return 'Node(data={})'.format(self.data)

class DLLNode:
	def __init__(self, prev=None, data=0, next=None):
		self.prev = prev
		self.data = data
		self.next = next
	
	def __repr__(self):
		return 'Node(data={})'.format(self.data)

class SinglyLL:
	def __init__(self):
		self._sentinel = SLLNode()
		self.length = 0

	def addFirst(self, data):
		self._sentinel.next = SLLNode(data, self._sentinel.next)
		self.length += 1

	def addLast(self, data):
		p = self._sentinel
		while p.next is not None:
			p = p.next
		p.next = SLLNode(data)
		self.length += 1

	def removeFirst(self):
		if self.length == 0:
			raise Exception("the list is empty")

		self._sentinel.next = self._sentinel.next.next
		self.length -= 1

	def removeLast(self):
		if self.length == 0:
			raise Exception("the list is empty")

		p = _sentinel
		while p.next.next is not None:
			p = p.next
		p.next = p.next.next
		self.length -= 1
	
	def head(self):
		if self.length == 0:
			raise Exception("there is no head node")
		return self._sentinel.next

	def get(self, index):
		if index >= self.length:
			raise Exception("there is no item at the index you are getting")

		p = self._sentinel.next
		for _ in range(index):
			p = p.next
		return p.data

	def get_node(self, index):
		if index >= self.length:
			raise Exception("there is no item at the index you are getting")

		p = self._sentinel.next
		for _ in range(index):
			p = p.next
		return p

	def search(self, data):
		if self.length == 0:
			return None

		p = self._sentinel.next
		while p is not None:
			if p.data == data:
				return p
			p = p.next
		return p

	def __iter__(self):
		p = self._sentinel.next
		while p is not None:
			yield p.data
			p = p.next

class DoublyLL:
	def __init__(self):
		self._sentinel = DLLNode(self._sentinel, 42, self._sentinel)
		self.length = 0

	def addFirst(self, data):
		self._sentinel.next = DLLNode(self._sentinel, data, self._sentinel.next)

	def addLast(self, data):
		return 
	def removeFirst(self, data):
		return
	def removeLast(self, data):
		return
	def get(self, index):
		return
	def search(self, data):
		return
	def __iter__(self):
		return
		




