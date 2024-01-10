# Import numpy and matplotlib.pyplot
import numpy as np
import matplotlib.pyplot as plt

# Initialize all_walks and set seed
np.random.seed()
all_walks = []

# Simulate random walk 500 times
for i in range(1):
    random_walk = [0]
    for x in range(100):
        step = random_walk[-1]
        dice = np.random.randint(1, 7)

        # Determine the direction of the next step
        if dice <= 2:
            step = max(0, step - 1)
        elif dice <= 5:
            step = step + 1
        else:
            step = step + np.random.randint(1, 7)

        # Implement clumsiness
        if np.random.rand() <= 0.001:
            step = 0

        random_walk.append(step)

    all_walks.append(random_walk)

# Create and plot np_aw_t
np_aw = np.array(all_walks)
np_aw_t = np.transpose(np_aw)

# Show how the steps evolve with time
plt.plot(np_aw_t)
plt.show()

# # Select last row from np_aw_t: ends
# ends = np_aw_t[-1, :]

# # Plot histogram of ends, display plot
# print(ends)
# plt.hist(ends)
# plt.show()

# # Calculate the odds of reaching 60 steps
# odds = np.mean(ends >= 60)
# print(odds)
