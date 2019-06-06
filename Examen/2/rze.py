import Queue
import threading

class Bistate(threading.Thread):

	def __init__(self, a, b, c):
		threading.Thread.__init__(self)
		self.a = a
		self.b = b
		self.c = c
		self.impar = True

	def run(self):
		while True:
			number = self.a.get()
			if self.impar: 
				self.b.put(number)
			else :
				self.c.put(number)
			self.impar = not self.impar
			
class Split(threading.Thread):

	def __init__(self, i, o1, o2):
		threading.Thread.__init__(self)
		self.i = i
		self.o1 = o1
		self.o2 = o2

	def run(self):
		while True:
			tmp = self.i.get()
			self.o1.put(tmp)
			self.o2.put(tmp)			

class ZeroGen(threading.Thread):
	
	def __init__(self, i, o):
		threading.Thread.__init__(self)
		self.i = i
		self.o = o

	def run(self):
		while True:
			counter = self.i.get()
			for x in xrange(counter):
				self.o.put(0)


class Merge(threading.Thread):
	
	def __init__(self, a, b, c):
		threading.Thread.__init__(self)
		self.a = a
		self.b = b
		self.c = c
		self.o = Queue.Queue()

	def run(self):
		while True:
			counter = self.a.get()
			for x in xrange(counter):
				self.o.put(self.b.get())
			self.o.put(self.c.get())	
			print list(self.o.queue)

def main():
	print("RZE decoder")

	print("Creating queues...")
	ak = Queue.Queue()
	ak.put(3)
	ak.put(-1)
	ak.put(0)
	ak.put(255)	
	ak.put(0)
	ak.put(3)
	bk = Queue.Queue()
	ck = Queue.Queue()
	dk = Queue.Queue()
	ek = Queue.Queue()
	fk = Queue.Queue()

	print(" Input Queue:"),
	print(list(ak.queue))

	print("Creating threads...")
	
	bistate = Bistate(ak,bk,ck)
	bistate.setName('Bistate Thread')
	
	split = Split(bk, dk, ek)
	split.setName('Split Thread')

	zeroGen = ZeroGen(ek, fk)
	zeroGen.setName('ZeroGen Thread')

	merge = Merge(dk, fk, ck)
	merge.setName('Merge Thread')
		
	print("Starting threads...")
	bistate.start()
	split.start()
	zeroGen.start()
	merge.start()

if __name__ == '__main__':main()	