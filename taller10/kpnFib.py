import time
import Queue
import threading

class Add(threading.Thread):

	def __init__(self, a, b, c):
		threading.Thread.__init__(self)
		self.a = a
		self.b = b
		self.c = c

	def run(self):
		while True:
			self.c.put(self.a.get() + self.b.get())

class Delay0(threading.Thread):
	def __init__(self, i, o):
		threading.Thread.__init__(self)
		self.i = i
		self.o = o

	def run(self):
		self.o.put(0);
		while True:
			time.sleep(1)
			self.o.put(self.i.get())

class Delay1(threading.Thread):
	def __init__(self, i, o):
		threading.Thread.__init__(self)
		self.i = i
		self.o = o

	def run(self):
		self.o.put(1);
		while True:
			time.sleep(1)
			self.o.put(self.i.get())

class Split(threading.Thread):

	def __init__(self, i, o1, o2, o3):
		threading.Thread.__init__(self)
		self.i = i
		self.o1 = o1
		self.o2 = o2
		self.o3 = o3

	def run(self):
		while True:
			tmp = self.i.get()
			self.o1.put(tmp)
			self.o2.put(tmp)
			self.o3.put(tmp)

class Printer(threading.Thread):
	
	def __init__(self, i):
		threading.Thread.__init__(self)
		self.i = i

	def run(self):
		while True:
			print(self.i.get())

def main():
	print("Fibonacci")

	print("Creating queues...")
	ak = Queue.Queue()
	bk = Queue.Queue()
	ck = Queue.Queue()
	dk = Queue.Queue()
	ek = Queue.Queue()
	fk = Queue.Queue()

	print("Creating threads...")
	add = Add(ck, fk, ak)
	add.setName('Add Thread')
	delay1 = Delay1(ak, bk)
	delay1.setName('Delay1 Thread')
	split = Split(bk, ck, dk, ek)
	split.setName('Split Thread')
	printer = Printer(dk)
	printer.setName('Printer Thread')
	delay0 = Delay0(ek, fk)
	delay0.setName('Delay1 Thread')

	print("Starting threads...")
	add.start()
	delay1.start()
	split.start()
	delay0.start()
	printer.start()

if __name__ == '__main__':main()	