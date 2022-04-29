class Tower_Of_Hanoi:
	'''Implementation of Tower Of Hanoi
		Maximum tower height - 20'''
	def __init__(self,max_disks=5) :
		
		# Tower height restriction
		self.max_disks = max_disks

		if self.max_disks <= 0 or self.max_disks > 20 :
			self.max_disks = 5


		# Disks in each rod
		self.rod_data = {
			'A' : [i+1 for i in range(self.max_disks)],
			'B' : [0 for i in range(self.max_disks)],
			'C' : [0 for i in range(self.max_disks)],
		}

		# Keep track of the top of each rod
		self.rod_state = {
			'A' : 0,
			'B' : self.max_disks,
			'C' : self.max_disks,
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
			if a <= self.max_disks-1 and b >= 0 :
				# Disk in F should be smaller than Disk in T
				if b == self.max_disks or F[a] < T[b]:
					return True
		return False



	def print_disk(self,N) :
		'''Print Indiviual Disks based on their length'''
		if N == 0 :
			ch = '||'
		elif N >= 10 :
			ch = f"{N}"

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
		print(f"TOWER OF HANOI by Shakeeb Arsalan : arsshakeeb149@protonmail.com")
		print(f"\nMove all the disks in Rod A to Rod C using Rod B. You can only move")
		print(f"one disk at a time, cannot place a bigger disk on a smaller one and ")
		print(f"in the end all the disks in Rod C must be in the same order as they ")
		print(f"were in Rod A.")

		while True :
			print()
			self.draw_tower()
			print("To Move a Disk from one Rod1 to Rod2, enter <Rod1><Rod2> or Q to quit.")
			print("e.g. To Move Disk from A to B, enter AB")
        	
			cmd = input('>').upper().strip()

			if cmd == 'Q':
				break


			if self.valid_move(cmd) :
				self.move_disk(cmd[0],cmd[1])

				# Check for win condition
				if self.rod_state['C'] == 0 :
					print("\nTOWER COMPLETED, YOU WIN!!")

					# Draw the completed tower
					print()
					self.draw_tower()
					break # End Game

			else:
				print("!!INVALID MOVE OR COMMAND!!")

			print('-'*70)