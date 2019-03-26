import mlflow
import os
import sys
import mlflow.sklearn

if __name__ == "__main__":
    a=int(sys.argv[1])
    mlflow.log_param("val1",a)
    b=int(sys.argv[2])
    mlflow.log_param("val2",b)
    c=a*b
    print("Multiplication :"+str(c))
    cwd = os.getcwd()    
    with open(cwd+'/spam.txt', 'w') as f:
        f.write("Fan of Python")
    mlflow.log_metric("mutiplication",c)
    mlflow.sklearn.log_model(c, "model")
