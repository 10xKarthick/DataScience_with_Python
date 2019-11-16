import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style

r = np.random.rand(10)

print(r)

style.use('ggplot')

plt.plot(r,'r',label='line one',linewidth=2)

plt.xlabel('Range')

plt.ylabel('Numbers')

plt.title('First Plot')

plt.legend()

plt.show()