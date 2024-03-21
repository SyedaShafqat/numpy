import numpy as np
from numpy import random

import numpy as np
from numpy import random

# Generate a random array
x = random.randint(100, size=(100))

print("Original array:")
print(x)
print('the sorted array is below:')
print(np.sort(x))

x_copy = np.copy(x)

x_copy = np.unique(x_copy)

print('The array after removing duplicates:')
print(x_copy)

