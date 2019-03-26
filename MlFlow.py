import mlflow
import os
import sys
import mlflow.sklearn
import matplotlib.pyplot as plt
import os 

if __name__ == "__main__":
    a=int(sys.argv[1])
    mlflow.log_param("val1",a)
    b=int(sys.argv[2])
    mlflow.log_param("val2",b)
    c=a*b
    print("Multiplication :"+str(c))
    cwd = os.getcwd()    
    plt.plot(5, 10,'go--', linewidth=2, markersize=12)
    plt.savefig(cwd+'/foo.png')
    mlflow.log_metric("mutiplication",c)
    mlflow.sklearn.log_model(c, "model")
