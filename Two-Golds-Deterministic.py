import Environment3
# Create deterministic environment with two gold and commence value iteration
env = Environment3.Gridworld(epsilon = 0, gold_positions = [12, 23])
policy, v = calculate(environment = env, theta = 1e-10, gamma = 1)

# Split returned arrays to print out only first 25 (before gold collected)
policy = policy[:25]
v = v[:25]

# Loop to aesthetically display results
for i in range(0, len(policy)):
    print("State:", i, "\tValue:", v[i], "\tPolicy:", policy[i])
