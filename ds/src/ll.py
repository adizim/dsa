class SLLNode:
	def __init__(self, data=0, next=None):
		self.val = val
		self.next = next

class DLLNode:
	def __init__(self, prev=None, data=0, next=None):
		self.prev = prev
		self.val = val
		self.next = next

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

		self._sentinel.next = self_sentinel.next.next
		self.length -= 1

	def removeLast(self):
		if self.length == 0:
			raise Exception("the list is empty")

		p = _sentinel
		while p.next.next is not None:
			p = p.next
		p.next = p.next.next
		self.length -= 1

	def get(self, index):
		if index >= self.length:
			raise Exception("there is no item at the index you are getting")

		p = self._sentinel.next
		for _ in range(index):
			p = p.next
		return p.val

	def search(self, data):
		if self.length == 0:
			return None

		p = self._sentinel.next
		while p is not None:
			if p.val == data:
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
	def removeFirst(self, data):
	def removeLast(self, data):
	def get(self, index):
	def search(self, data):
	def __iter__(self):
		




