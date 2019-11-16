import matplotlib.pyplot as plt
from matplotlib import style

customers = [123,645,950,1290,1630,1450,1034,1295,465,205,80]

hours = [7,8,9,10,11,12,13,14,15,16,17]

style.use('ggplot')

# plt.plot(hours,customers,color='r',linestyle=':')

# Alpha and annotate
plt.plot(hours,customers,color='r',alpha=.4)

plt.annotate('Max',ha='center',va='bottom',xytext=(8,1500),xy=(11,1630),arrowprops={'facecolor':'green'})

# plt.axis([8.0,17.5,50,2000])

plt.xlabel('Hours')

plt.ylabel('Customers')

plt.title('Second Plot')

plt.legend()

plt.show()