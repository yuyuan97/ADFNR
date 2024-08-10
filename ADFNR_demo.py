####################################
### The final demo of ADFNR  ####
####################################
from scipy.io import loadmat
from ADFNR import normalize,ADFNR

load_data = loadmat('Example.mat')
traindata = load_data['Example']
print("Raw data")
print(traindata)

traindata[:,1] = normalize(traindata[:,1])
traindata[:,2] = normalize(traindata[:,2])

lam = 0.3
AS = ADFNR(traindata, lam)
print("abnormal score (AS)")
print(AS)




















