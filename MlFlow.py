


import mlflow
import os
import sys

if __name__ == "__main__":
    a=int(sys.argv[1])
    mlflow.log_param("val1",a)
    b=int(sys.argv[2])
    mlflow.log_param("val2",b)
    c=a*b
    print("Multiplication :"+str(c))
    mlflow.log_metric("mutiplication",c)









