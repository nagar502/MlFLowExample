


import mlflow
import os
import sys
import matplotlib.pyplot as plt

if __name__ == "__main__":
    a=int(sys.argv[1])
    mlflow.log_param("val1",a)
    b=int(sys.argv[2])
    mlflow.log_param("val2",b)
    c=a*b
    print("Multiplication :"+str(c))
    mlflow.log_metric("mutiplication",c)
    plt.plot(a, b)
    plt.xlabel('A')
    plt.ylabel('B')
    plt.title('Mutiplication Values')
    plt.savefig('info.png')
    mlflow.log_artifact("info.png")








