from beverages import HotBeverage, Coffee, Tea, Chocolate, Cappuccino
import random

class CoffeeMachine:
	def __init__(self):
		self.served = 0
	
	class EmptyCup(HotBeverage):
		def __init__(self, price=0.90, name="empty cup"):
			HotBeverage.__init__(self, price, name)

		def description(self):
			return ("An empty cup?! Gimme my money back!.")

	class BrokenMachineException(Exception):
		def __init__(self, error="This coffee machine has to be repaired."):
			Exception.__init__(self, error)

	def repair(self):
		self.served = 0
		print("Machine has been repaired.")

	def serve(self, product):
		self.served += 1
		if self.served > 10:
			raise self.BrokenMachineException()
		if random.randint(0, 1) == 1:
			return product()
		else:
			return self.EmptyCup()

def main():
	products = {0 : HotBeverage, 1 : Coffee, 2 : Tea, 3 : Chocolate, 4 : Cappuccino}
	for i in range(2):
		try:
			machine = CoffeeMachine()
			for i in range(15):
				print(machine.serve(products.get(random.randint(0, 4))))
		except Exception as e:
			print(e)
			machine.repair()
	

if __name__ == '__main__':
	main()
