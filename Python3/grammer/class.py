class people:
	name = 'hugh'
	contry = 'China'
	__salary = 3000
	family = "chen"
	def getName(self):
		print(self.name)
	@classmethod
	def getContry(cls):
		return(cls.contry)
	@staticmethod
	def getFamily():
		return people.family

p = people()
print(p.name)
people.name = "jack"
print(p.name)
p.getName()
print(p.getContry())
#print(people.getName())
print(people.getContry())
print(people.getFamily())
print(p.getFamily())