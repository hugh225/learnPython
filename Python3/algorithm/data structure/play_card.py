# 发牌
class Queue(object):
	"""docstring for Queue"""
	def __init__(self):
		self.items=[]

	def isEmpety(self):
		return self.items==[]

	def size(self):
		return len(self.items)

	def enqueue(self, item):
		self.items.insert(0,item)

	def dequeue(self, item):
		self.items.pop()

# 发牌
while True:
	a=[int(n) for n in input().split(',')]
	b=[int(n) for n in input().split(',')]
	if len(a)==len(b):
		break
	print("cards not equal, please try again!")

# 打牌
def play_card(player):
	t=player[-1]


while True:
	

