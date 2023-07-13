from sklearn import metrics
from jiwer import cer
  
# list of integers of actual and calculated
actual = [2, 3, 5, 5, 9]
calculated = [3, 3, 8, 7, 6]
ground_truth=[1,0,1,0,1]
predicated_probablity=[[0.7,0.3],[0.5,0.5],[0.3,0.7],[0.6,0.4],[0.4,0.6]]
  
# calculate MAE
error = metrics.mean_absolute_error(actual, calculated)
  
# display
print("Mean absolute error : " + str(error))

error=metrics.mean_squared_error(actual,calculated)
print("Mean squared error : " + str(error))

error=metrics.r2_score(actual,calculated)
print("R squared score : " + str(error))

acc=metrics.accuracy_score(actual,calculated)
print("accuracy",acc)

cohan=metrics.cohen_kappa_score(actual,calculated)
print("cohen kappa score:",cohan)

log_loss=metrics.log_loss(ground_truth,predicated_probablity)
print("log loss",log_loss)

reference = "hello world good night moon"
hypothesis = "hello world good day sun"
print("character error rate: ",cer(reference, hypothesis))