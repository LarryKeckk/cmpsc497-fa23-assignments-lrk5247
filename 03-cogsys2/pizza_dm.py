import python_actr
from python_actr.actr import *
from python_actr.actr.hdm import *

class PizzaBuilder_DM(ACTR):
	goal = Buffer()
	retrieval = Buffer()
	DM_module = HDM(retrieval)
	my_pizza = []

	def cook_pizza(self, pizza_ingred):
		'''
		Takes in list of "ingrediants" and outputs a "pizza"
		Inputs: pizza_ingred [list of strings]
		Output: cooked_pizza [string]
		'''
		# Whats going on here? - https://docs.python.org/3/library/stdtypes.html#str.join
		return ("_".join(pizza_ingred))

	def init():
		DM.module.set_finst_size(22)
		DM.module.set_finst_time(100)
		#Add memory chunks to declarative memory module
		# (More chunks needed in DM!)
		DM_module.add("prev:crust next:marinara")
		DM_module.add("prev:marinara next:mozzarella")
		DM_module.add("prev:mozzarella next:pepperoni")
		DM_module.add("prev:pepperoni next:onion")

		DM_module.add("prev:crust next:bbq")
		DM_module.add("prev:bbq next:cheddar")
		DM_module.add("prev:cheddar next:bacon")
		DM_module.add("prev:bacon next:onion")
	
		#Set goal so that we can prep ingredients
		goal.add("start_pizza")

	def prep_ingredients(goal="start_pizza" ):
		#start building our pizza!
		goal.set("build_pizza")
		#Request next step from DM 
		
	###Rules to request from declarative memory for next step/ingredient and place that ingredient on your pizza and make sure you can more on to cooking pizza

	def request_next_step(self, goal=goal, retrieval=retrieval, prev_step=None, next_step=None):
    
		if goal.is_empty() and retrieval.is_empty():
			goal.set("end_pizza_building")
		else:
			prev_step = retrieval[0]["prev"]
			next_step = retrieval[0]["next"]
			goal.set("add_ingredient", prev_step=prev_step, next_step=next_step)

    
	def add_ingredient(goal="add_ingredient", prev_step=None, next_step=None):
        # Add the ingredient to the pizza (modify as needed)
		self.my_pizza.append(next_step)
		goal.set("build_pizza")  # Set the goal for the next step
        

    
	def cook_pizza_step(goal="cook_pizza"):
		my_pizza = self.cook_pizza(my_pizza)
		print("Mmmmmm my " + my_pizza + " pizza is gooooood!")
		self.stop()

class EmptyEnvironment(python_actr.Model):
	pass

env_name = EmptyEnvironment()
agent_name = PizzaBuilder_DM()
env_name.agent = agent_name
python_actr.log_everything(env_name)
env_name.run()
