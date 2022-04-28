class Tower_Of_Hanoi:
	def __init__(self,max_disks=5) :
		
		self.max_disks = max_disks
		
		self.rod_data = {
			'A' : [i+1 for i in range(max_disks)],
			'B' : [0 for i in range(max_disks)],
			'C' : [0 for i in range(max_disks)],
		}

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

	def print_disk(N) :
		if N == 0 :
			ch = '|'
		else :
			ch = f"|{N}"

		half_disk = f"{' '*(self.max_disks-N)}{'@'*N}"

		return f"{half_disk}{ch}{half_disk}"

	def draw_tower(self) :
		'''Draw the tower on the console window'''
		pass





