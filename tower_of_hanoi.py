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
			'B' : max_disks,
			'C' : max_disks,
		}

	def move_disk(self,f,t) :
		'''Move disk from rod (f) to rod (t)'''
		disk = self.rod_data[f][self.rod_state[f]]
		self.rod_data[f][self.rod_state[f]] = 0
		self.rod_state[f] += 1

		self.rod_data[t][self.rod_state[t]-1] = disk
		self.rod_state[t] -= 1

	def valid_move(self,move):
		'''Check for a valid move'''
		if move in ('AB','AC','BA','BC','CA','CB') :
			f = move[0]
			t = move[1]

			F = self.rod_data[f]
			T = self.rod_data[t]
			a = self.rod_state[f]
			b = self.rod_state[t]

			# Rod f must not be empty and Rod t must not be full
			if a <= 4 and b >= 0 :
				# Disk in F should be smaller than Disk in T
				if b == 5 or F[a] < T[b]:
					return True
		return False



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
		print(f"{' '*self.max_disks}A {' '*self.max_disks} ",end='')
		print(f"{' '*self.max_disks}B {' '*self.max_disks} ",end='')
		print(f"{' '*self.max_disks}C {' '*self.max_disks} ")



	def run(self) :
		print(f"TOWER OF HANOI by Shakeeb Arsalan arsshakeeb149@protonmail.com")

		while True :
			self.draw_tower()
			print(self.rod_data)
			print(self.rod_state)

			print("To Move a Disk from one Rod1 to Rod2, enter <Rod1><Rod2> or Q to quit.")
			print("e.g. To Move Disk from A to B, enter AB")
        	
			cmd = input('>').upper().strip()

			if cmd == 'Q':
				break


			if self.valid_move(cmd) :
				self.move_disk(cmd[0],cmd[1])

			else:
				print("Invalid Move or Command!")