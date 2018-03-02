import numpy as np

class Gridworld(object):
	def __init__ (self, num_rows = 5, num_cols = 5, epsilon = 0.2):
		'''Initializes grid environment with bomb and gold'''
		# Initialize Grid
		self.num_rows = num_rows
		self.num_cols = num_cols
		self.num_cells = self.num_cols * self.num_rows
		self.epsilon = epsilon

		#Load initial position of gold and bomb (fixed) in 1D array
		self.bomb_positions = np.array([18])
		self.gold_positions = np.array([23])
		self.terminal_states = np.array([self.bomb_positions, self.gold_positions])

		#Specify rewards
		self.rewards = np.zeros(self.num_cells)
		self.rewards[self.bomb_positions] = -10
		self.rewards[self.gold_positions] = 10

		#Specify available actions
		self.actions = ["n", "e", "s", "w"]

	def get_available_actions(self):
		'''Return available actions'''
		return self.actions

	def get_terminal_states(self):
		'''Return terminal states on the board in 1D array'''
		return self.terminal_states.ravel()

	def get_initial_array(self):
		'''Creates and returns blank game board of appropriate size'''
		board = np.zeros(self.num_cells, dtype = float)
		return board
		
	def get_adjacent_states(self, state, action):
		'''Returns the adjacent state information of the given state-action pair'''
		adjacents = []
		reward = -1
		# Get adjacent state from each directions
		adjacents.append(self.get_north(state, action, reward))
		adjacents.append(self.get_east(state, action, reward))
		adjacents.append(self.get_south(state, action, reward))
		adjacents.append(self.get_west(state, action, reward))
			
		# Return the four new_states with associated probability and reward for state-action pair
		return adjacents
		
	def get_north(self, state, action, reward):
		'''Returns the adjacent state to the north of the given state'''
		new_state = state + self.num_cols
		
		# Keep current position if top of grid reached 
		if new_state >= self.num_cells:
			new_state = state
			
		# Assign probability
		if action == "n":
			probability = 1 - self.epsilon + (self.epsilon / len(self.actions))
		else:
			probability = self.epsilon / len(self.actions)
		
		# Set reward and return
		reward += self.rewards[new_state]
		return (new_state, probability, reward)
		
	def get_east(self, state, action, reward):
		'''Returns adjacent state to the east of the given state'''
		new_state = candidate_position = state + 1
		
		# Keep current position if right of grid reached
		if new_state % self.num_cols <= 0:
			new_state = state
		
		# Assign probability
		if action == "e":
			probability = 1 - self.epsilon + (self.epsilon / len(self.actions))
		else:
			probability = self.epsilon / len(self.actions)
			
		# Set reward and return
		reward += self.rewards[new_state]
		return (new_state, probability, reward)
		
	def get_south(self, state, action, reward):
		'''Returns adjacent state to the south of the given state'''
		new_state = state - self.num_cols
		
		# Keep current position if bottom of grid reached
		if new_state < 0:
			new_state = state
		
		# Assign probability
		if action == "s":
			probability = 1 - self.epsilon + (self.epsilon / len(self.actions))
		else:
			probability = self.epsilon / len(self.actions)	
		
		# Set reward and return
		reward += self.rewards[new_state]
		return (new_state, probability, reward)
		
	def get_west(self, state, action, reward):
		'''Returns adjacent state to the west of the given state'''
		new_state = state - 1
		
		# Keep current position if the left of grid reached
		if new_state % self.num_cols >= self.num_cols - 1:
			new_state = state
		
		# Assign probability
		if action == "w":
			probability = 1 - self.epsilon + (self.epsilon / len(self.actions))
		else:
			probability = self.epsilon / len(self.actions)
		
		# Set reward and return
		reward += self.rewards[new_state]
		return (new_state, probability, reward)