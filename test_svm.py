from svmutil import *
svm_model.predict = lambda self, x: svm_predict([0], [x], self)[0][0]

prob = svm_problem([1,-1], [[1,0,1], [-1,0,-1]])

param = svm_parameter()
param.kernel_type = LINEAR
param.C = 10
param.b = 1

m=svm_train(prob, param)

m.predict([1,1,1])