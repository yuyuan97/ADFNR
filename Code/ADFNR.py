####################################
### The final version of ADFNR  ####
####################################
import numpy as np
import copy

def similarity(a,x,flag): #Calculate similarity
    """
    :param a: attribute 1
    :param x: attribute 2
    :param flag: markers to distinguish between nominal and numerical attributes
    :return: the similarity between a and x
    """
    if flag==0:
        if a==x:
            sim=1
        else:
            sim=0
    else:
        sim=1-abs(a-x)
    return sim

def normalize(x):
    """
    :param x: attribute
    :return: normalized attribute
    """
    x_max = np.max(x)
    x_min = np.min(x)
    x = (x - x_min) / (x_max - x_min)
    return x


def ADFNR(data,epsilon):
    """
    :param data: data
    :param epsilon: fuzzy neighborhood radius
    :return: abnormal score (AS)
    """
    data = np.array(data)
    n,m = data.shape
    weight1 = np.zeros((n,m))
    weight2 = np.zeros((n,m))
    delta = np.zeros((1,m))
    ID = (data <= 1).all(axis=0) & (data.max(axis=0) != data.min(axis=0))
    delta[0][ID] = 1

    # Calculate the similarity matrix for individual attributes
    names = locals()
    for col in range(0,m):
        r = np.eye(n)
        names['Set%s' % col] = np.zeros((n,n))
        names['Set_ori%s' % col] = np.zeros((n,n))
        for j in range(0,n):
            a = data[j,col]
            x = data[:,col]
            for k in range(j+1,n):
                r[j,k] = similarity(a,x[k],delta[:,col])
                r[k,j] = r[j,k]
        names['Set_ori%s' % col] = copy.deepcopy(r)
        r[r<epsilon]= 0
        names['Set%s' % col] = copy.deepcopy(r)

    # Calculate the fuzzy neighborhood lower approximation ratio
    names = locals()
    for col in range(0,m):
        A = list(range(0,m))
        A.remove(col)
        A_r1 = copy.deepcopy(A)
        names['Ratio%s' % col] = np.zeros((n,1))
        Set_tem = names['Set%s' % col]
        Set_temp,ia,ic = np.unique(Set_tem, axis=0, return_index=True, return_inverse=True, return_counts=False)
        A_r2 = copy.deepcopy(A_r1)

        Set_tmp = names['Set_ori%s' % A_r2[0]]
        for j in range(1,len(A_r2)):
            Set_t = names['Set_ori%s' % A_r2[j]]
            Set_tmp = np.minimum(Set_tmp, Set_t)
        Set_tmp[Set_tmp<epsilon]= 0

        for i in range (0,Set_temp.shape[0]):
            i_tem = np.where(ic == i)
            Low_A = 0
            compare_bool = Set_tmp <= np.tile(Set_temp[i,:],(n,1))
            Low_A = np.sum(np.all(compare_bool, axis=1))
            names['Ratio%s' % col][i_tem,0] = Low_A/n
            weight1[i_tem,col] = (np.sum(Set_temp[i,:])/n)
            weight2[i_tem,col] = 1 - np.power((np.sum(Set_temp[i,:])/n),1/3)

    # Calculate the granule intensity of anomaly (GIA) and anomaly score (AS)
    GIA = np.zeros((n,m))
    AS = np.zeros((n, 1))
    for i in range(0,n):
        for k in range(0,m):
            Ratio = names['Ratio%s' % k]
            GIA[i, k] = 1 - (Ratio[i, 0]/ m) * weight1[i, k]
        AS_v = np.sum(GIA[i, :] * weight2[i, :]) / m
        AS[i] = AS_v

    return AS




















