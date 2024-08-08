#import the necessary libraries
from sklearn.datasets import make_moons
import matplotlib.pyplot as plt
# generate 2d classification dataset
X, y = make_moons(n_samples=500, shuffle=True,
				noise=0.15, random_state=42)
# Plot the generated datasets
plt.scatter(X[:, 0], X[:, 1], c=y)
plt.show()
