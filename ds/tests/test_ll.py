import pytest
import sys
sys.path.insert(0, '../src')
from src.ll import SinglyLL

def test_something():
	lst = SinglyLL(3)
	assert lst.val == 3