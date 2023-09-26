import matplotlib.pyplot as plt
import numpy as np
from mpldatacursor import datacursor

data = np.outer(range(10), range(1, 5))

plt.plot(data)
plt.title('Click somewhere on a line')

datacursor()

plt.show()