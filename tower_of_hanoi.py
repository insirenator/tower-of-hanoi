class Tower_Of_Hanoi:
	'''Implementation of Tower Of Hanoi'''
	def __init__(self,max_disks=5) :
		
		# Max disks
		self.max_disks = max_disks
		
		# Disks in each rod
		self.rod_data = {
			'A' : [i+1 for i in range(max_disks)],
			'B' : [0 for i in range(max_disks)],
			'C' : [0 for i in range(max_disks)],
		}

		# Keep track of the top of each rod
		self.rod_state = {
			'A' : 0,
			'B' : max_disks-1,
			'C' : max_disks-1,
		}

	def move_disk(self,f,t) :
		'''Move disk from rod (f) to rod (t)'''
		disk = self.rod_data[f][self.rod_state[f]]
		self.rod_data[f][self.rod_state[f]] = 0
		self.rod_state[f] += 1

		self.rod_data[t][self.rod_state[t]] = disk
		self.rod_state[t] -= 1

	def print_disk(self,N) :
		'''Print Indiviual Disks based on their length'''
		if N == 0 :
			ch = '||'
		else :
			ch = f"|{N}"

		left_half = f"{' '*(self.max_disks-N)}{'@'*N}"
		right_half = f"{'@'*N}{' '*(self.max_disks-N)}" 

		return f"{left_half}{ch}{right_half}"

	def draw_tower(self) :
		'''Draw the tower on the console window'''
		print(f"{self.print_disk(0)} {self.print_disk(0)} {self.print_disk(0)} ")

		rodA = self.rod_data['A']
		rodB = self.rod_data['B']
		rodC = self.rod_data['C']

		for a,b,c in zip(rodA,rodB,rodC) :
			print(f"{self.print_disk(a)} {self.print_disk(b)} {self.print_disk(c)}")




