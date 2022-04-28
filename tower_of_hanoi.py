class Tower_Of_Hanoi:
	def __init__(self,max_rods=5) :
		self.rods_data = {
			'A' : [i for i in range(max_rods,0,-1)]
			'B' : []
			'C' : []
		}

	def move_disk(self,f,t) :
		'''Move disk from rod (f) to rod (t)'''
		disk = self.rods_data[f].pop()
		self.rods_data[t].append(disk)

	


