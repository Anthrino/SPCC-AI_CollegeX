
print("\nA two-player game: From a starting no. each player can subtract"\
      "a prime no (<10) provided the difference is positive. The player unable to do so looses.")

val = int(input("\nEnter the starting number from 1-10 : "))


class Node:

	def __init__(self, val, lev):
		self.value = val
		self.level = lev
		self.player = "none"
		self.branches = []
		for x in [2, 3, 5, 7]:
			if x <= self.value:
				self.branches.append(Node(self.value - x, self.level+1))

		if self.branches.__len__() == 0:
			if self.level % 2 == 1:
				self.points = -1
			else:
				self.points = 1

		else:
			if lev % 2 == 0:
				self.player = "Min"
				self.points = max([getattr(x, "points") for x in self.branches])
			else:
				self.player = "Max"
				self.points = min([getattr(x, "points") for x in self.branches])

	def minmax(self, curr_move):

		print("\n\nRemainder : " + str(self.value))
		if self.player == "Max":
			for x in self.branches:

				if getattr(x, "points") == 1:
					print("\nMy Turn> I played "+str(self.value - getattr(x, "value")))
					x.minmax(self.player)
					return

		elif self.player == "Min":

			val = int(input("\nYour turn> Enter the number from (2,3,5,7) to subtract from '" + str(self.value) + "' : "))
			while val > self.value or val not in [2, 3, 5, 7]:
				print("Incorrect move.")
				val = int(input("\nEnter the number from (2,3,5,7) to subtract from '" + str(self.value) + "' : "))
			for x in self.branches:
				if getattr(x, "value") == self.value - val:
					x.minmax(self.player)
					return
		else:
			if self.branches.__len__() == 0 and curr_move == "Max":
				print("No possible moves. I win! :D")
				return
			elif self.branches.__len__() == 0 and curr_move == "Min":
				print("No possible moves. You win! :(")
				return

	def draw(self):
		print(str(self.value) + "["+str(self.level)+"] : "+str(self.points) + " | ", end="")
		for x in self.branches:
			x.draw()

root = Node(val, 0)

print("\nNodes by DFS parsing : ")
root.draw()

root.minmax("Min")
