class erange:

	#Has a constructor which can take 1-3 paramters
	def __init__(self, pos1, pos2 = None, pos3 = None):

		self.start = 0
		self.step = 1

		#Assigns the correct paramters to the correct variables depending on how many parameters are passed
		if pos2 == None and pos3 == None:
			self.stop = pos1
		elif pos3 == None:
			self.start = pos1
			self.stop = pos2
		else:
			self.start = pos1
			self.stop = pos2
			self.step = pos3

		#Saves the initial start number for printing (__str___) because self.start changes with iterations
		self.initialStart = self.start


	#Used for when you try to: print(erange(<values>))
	def __str__(self):
		return "erange({}, {})".format(self.initialStart,self.stop) if self.step == 1 else "erange({}, {}, {})".format(self.initialStart,self.stop,self.step)

	def __iter__(self):
		return self

	#Cycles through the numbers at the step value until all numbers are covered
	def __next__(self):
		ret = self.start
		self.start += self.step
		pos_dir = True if self.step > 0 else False
		#Two conditions for exiting (increasing && start surpasses or equals stop) or (decreasing && start falls below of equals stop)
		if(pos_dir == True and ret >= self.stop) or (pos_dir == False and ret <= self.stop):
			raise StopIteration
		else:
			return ret


class numerate:

	pos = 0

	#Constructor can take a str/lst and an optional int
	def __init__(self,lst,start = 0):
		self.start = start
		self.lst = lst
		#If the constructor does not receive a list, converts the string to a list
		if not isinstance(lst,list):
			self.lst = list(lst)

	def __iter__(self):
		return self

	#Using self.pos to track position, iterates through the list returning tuples starting at self.start (default = 0)
	def __next__(self):
		#Stops iteration once it reaches end of list
		if self.pos >= len(self.lst):
			raise StopIteration
		else:
			self.pos += 1
			return (self.pos - 1 + self.start,self.lst[self.pos-1])