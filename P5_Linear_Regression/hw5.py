import sys
import csv
import matplotlib.pyplot as plt
import numpy as np


if __name__ == "__main__":

# Q2
    x=[]    
    y=[]
    with open(sys.argv[1]) as f:
        Line_reader = csv.reader(f,delimiter = ',')
        headers = next(Line_reader)
        for row in Line_reader:
            x.append(int(row[0]))
            y.append(int(row[1]))


    plt.plot(x,y)
    plt.ylabel('Number of frozen days')
    plt.xlabel('Year')
    plot_frozen = plt. savefig ("plot.jpg")

    #Q3a

    X = []

    for i in range(len(x)):
        X.append(np.transpose(np.array([1,x[i]])))

    X=np.array(X)
    print ("Q3a:")
    print(X)

    #Q3b
    Y=[]
    for i in range(len(y)):
        Y.append(y[i])

    Y=np.array(Y)
    print ("Q3b:")
    print (Y)

    #Q3C

    Z= np.dot(np.transpose(X),X)
    print ("Q3c:")
    print (Z)


    #Q3d

    I= np.linalg.inv(Z)
    print ("Q3d:")
    print(I)

    #Q3e
    PI= np.dot(I,np.transpose(X))
    print ("Q3e:")
    print(PI)

    hat_beta = np.dot(PI,Y)
    print ("Q3f:")
    print(hat_beta)

    #q4


    x_test = 2022
    y_test = hat_beta[0]+hat_beta[1]*x_test
    print("Q4: " + str(y_test))

    #Q5
    sign = 0
    if(hat_beta[1]<0):
        sign = '<'
    elif(hat_beta[1]>0):
        sign = '>'
    elif(hat_beta[1]==0):
        sign = '='

    print("Q5a: " + str(sign))

    print("Q5b: " + str("This means that the slope of linear regression is negative, and we can predict the days of Mendota lake covered with ice are decreasing."))

    x_star=-(hat_beta[0]/hat_beta[1])
    print("Q6a: " + str(x_star))

    print("Q6b: " + str("It is a compelling prediction. In 5(a), the slope is negative, so we can predict the days covered with ice will continue to decrease, thus predicting that Lake Mendota will no longer freeze in the future."))
