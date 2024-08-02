import numpy as np
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram
import csv

def load_data(filepath):
    x=[]
    with open(filepath) as f:
        DictReader_obj = csv.DictReader(f)
        for item in DictReader_obj:
            x.append(dict(item))
    return x

def calc_features(row):
    x_1= int(row['Attack'])
    x_2= int(row['Sp. Atk'])
    x_3= int(row['Speed'])
    x_4= int(row['Defense'])
    x_5= int(row['Sp. Def'])
    x_6= int(row['HP'])
    
    x = np.array([x_1,x_2,x_3,x_4,x_5,x_6],dtype=np.int64)
    return x

def hac(features):
    # make distance matrix
    A=[]
    B = [1 for i in range(len(features))]
    for i in range(len(features)):
        A.append(np.dot(np.transpose(features[i]),features[i]))

    dist = np.outer(np.transpose(A),B) + np.outer(np.transpose(B),A) - 2*np.dot(features,np.transpose(features))
    dist= np.sqrt(dist)

    Z = np.zeros((len(features)-1,4))
    cls=[]
    #initial
    for i in range(len(features)):
        cls.append([i,[i]])

    # for loop for output Z 
    for t in range (len(features)-1):
        # set min for this iteration
        min=np.inf
        #search upper triangle
        for i in range(0, len(cls)-1):
            for j in range(i + 1,len(cls)):
                temp1=cls[i][1]
                temp2=cls[j][1]
                max=-np.inf
                for s in range(len(temp1)):    
                    for u in range(len(temp2)):
                        if(dist[temp1[s]][temp2[u]]>max):
                            max=dist[temp1[s]][temp2[u]]
                if(min>max):
                    min=max
                    z0=i
                    z1=j
            if(z0>z1):
                temp=z0
                z0=z1
                z1=temp

        Z[t,0]=cls[z0][0]
        Z[t,1]=cls[z1][0]
        Z[t,2]=min

        cls.append([len(features)+t,cls[z0][1]+cls[z1][1]])
        Z[t,3]=len(cls[z0][1])+len(cls[z1][1]) 
        del cls[z1]
        del cls[z0] 

    return Z

def imshow_hac(Z, names):
    fig,a =plt.subplots()
    dendrogram(Z, labels=names, leaf_rotation=90)
    plt.tight_layout()
    plt.show()
