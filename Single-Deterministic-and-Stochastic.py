import Environment
import numpy as np

def calculate(environment, theta = 1e-10, gamma = 1):
    '''Performs value iteration on the given Gridworld environments'''
    # Initialise variables
    policy_values = environment.get_initial_array()
    terminal_states = environment.get_terminal_states()
    available_actions = environment.get_available_actions()
    policy_action = ['n'] * len(policy_values)
    
    while(True):
        delta = 0
        delta_values = []
        
        # Iterate through each non-terminal state
        for state in range(0, len(policy_values)):
            if state not in terminal_states:
                original_value = policy_values[state]
                state_actions = []
                
                # Iterate through each action for the state
                for action in available_actions:
                    adjacents = environment.get_adjacent_states(state, action)
                    action_sum = 0
                    
                    # Iterate through each adjacent state for the state-action pair
                    for adj in adjacents:
                        new_state, probability, reward = adj
                        action_sum += probability * (reward + (gamma * policy_values[new_state]))
                    
                    # Add sum of state-action pair values
                    state_actions.append(action_sum)
                    
                # Take maximum state-action for new policy and calculate action and delta
                policy_values[state] = max(state_actions)
                max_index = state_actions.index(max(state_actions))
                policy_action[state] = available_actions[max_index]
                delta_values.append(abs(original_value - policy_values[state]))
            
        delta = max(delta_values)
        if (delta < theta):
            break
    
    return (policy_action, policy_values)

# Create deterministic environment and commence value iteration
env = Environment.Gridworld(epsilon = 0)
policy, v = calculate(environment = env, theta = 1e-10, gamma = 1)

# Loop to aesthetically display results
for i in range(0, len(policy)):
    print("State:", i, "\tValue:", v[i], "\tPolicy:", policy[i])
	
# Create stochastic environment and commence value iteration
env = Environment.Gridworld(epsilon = 0.2)
policy, v = calculate(environment = env, theta = 1e-10, gamma = 1)

# Loop to aesthetically display results
for i in range(0, len(policy)):
    print("State:", i, "\tValue: %0.10f" % v[i], "\tPolicy:", policy[i])