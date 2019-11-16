import scipy.io as sio
import numpy as np

# save a mat file
vect = np.arange(10)
sio.savemat('test.mat',{'vect':vect})

# loading back the mat file
print(sio.loadmat('test.mat'))

#see the contents 
print(sio.whosmat('test.mat'))
