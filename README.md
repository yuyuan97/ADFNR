# ADFNR

## Abstract
Anomaly detection is a significant data mining task with great application potential. 
However, the presence of uncertain information, such as random and fuzzy, in real data usually poses a great challenge to existing anomaly detection methods. 
As an important model of granular computing theory, fuzzy neighborhood rough sets can effectively handle uncertain data. 
It has been successfully applied to data pre-processing tasks such as attribute reduction or feature selection. 
In response to the shortcomings of existing anomaly detection methods that cannot effectively handle uncertain information such as random and fuzzy, 
this paper proposes an unsupervised anomaly detection algorithm based on a novel fuzzy neighborhood rough sets model. 
At first, parameterized fuzzy relations are introduced to inscribe fuzzy neighborhood information granules. 
By establishing the relationship between different granules, 
the fuzzy neighborhood lower and upper approximations are defined to construct a fuzzy neighborhood rough set model for decision-free information systems. 
The lower approximation ratio is further proposed and used to construct the anomaly score, 
which characterizes the anomaly degree of the objects by aggregating the granule intensity of anomalies with corresponding weights. 
Finally, an unsupervised anomaly detection algorithm is designed for heterogeneous data based on the proposed fuzzy neighborhood rough set model. 
The results of extensive experiments illustrate that the proposed algorithm outperforms the other eight comparison algorithms and can effectively handle uncertain information.

## Usage
You can run ADFNR_demo.py or WFRDA.py:
```
load_data = loadmat('FREAD_Example.mat')
trandata = load_data['trandata']

traindata[:,1] = normalize(traindata[:,1])
traindata[:,2] = normalize(traindata[:,2])

lam = 0.3
AS = ADFNR(traindata, lam)
print("abnormal score (AS)")
print(AS)
```
You can get outputs as follows:
```
abnormal score (AS)
[[0.31248827]
 [0.16309545]
 [0.20232938]
 [0.18562742]
 [0.16285631]
 [0.19842026]]
```

## Contact
If you have any questions, please contact yuanyuanyy@zju.edu.cn or yuanzhong@scu.edu.cn.
