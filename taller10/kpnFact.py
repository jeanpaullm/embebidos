import time
import Queue
import threading

class Increment(threading.Thread):

	def __init__(self, a, b):
		threading.Thread.__init__(self)
		self.a = a
		self.b = b

	def run(self):
		while True:
			self.b.put(self.a.get() + 1)

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

class Multiply(threading.Thread):

	def __init__(self, a, b , c):
		threading.Thread.__init__(self)
		self.a = a
		self.b = b
		self.c = c

	def run(self):
		while True:
			self.c.put(self.a.get() * self.b.get())


class Printer(threading.Thread):
	
	def __init__(self, i):
		threading.Thread.__init__(self)
		self.i = i

	def run(self):
		while True:
			print(self.i.get())

def main():
	print("Factorial")

	print("Creating queues...")
	ak = Queue.Queue()
	bk = Queue.Queue()
	ck = Queue.Queue()
	dk = Queue.Queue()
	ek = Queue.Queue()
	fk = Queue.Queue()
	gk = Queue.Queue()
	hk = Queue.Queue()

	print("Creating threads...")
	increment = Increment(ak, bk)
	increment.setName('Increment Thread')
	split0 = Split(bk, ck, dk)
	split0.setName('Split0 Thread')
	delay0 = Delay0(dk, ak)
	delay0.setName('Delay0 Thread')
	multiply = Multiply(ck, gk, ek)
	multiply.setName('Multiply Thread')	
	delay1 = Delay1(ek, fk)
	delay1.setName('Delay1 Thread')
	split1 = Split(fk, gk, hk)
	split1.setName('Split1 Thread')
	printer = Printer(hk)
	printer.setName('Printer Thread')
		
	print("Starting threads...")
	increment.start()
	split0.start()
	delay0.start()
	multiply.start()
	delay1.start()
	split1.start()
	printer.start()

if __name__ == '__main__':main()	