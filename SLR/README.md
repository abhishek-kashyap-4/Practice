In this project, we try to achieve simple linear regression using 3 different methods:
  1. Using sklearn
  2. Coding the Math from the scratch
  3. Using deep learning model without hidden layer
  

Using sklearn:

    LinearRegression class in sklearn was used. 


![sklearn train image](/SLR/images/sklearn_train.png) 
![sklearn test image](/SLR/images/sklearn_test.png)


Coding from the scratch:

  The Math was coded from the scratch.
  
![scratch train image](/SLR/images/scratch_train.png)
![scratch test image](SLR//images/scratch_test.png)


Using a ANN (keras):
    
    Line fits better as the epochs are increased till 200 epochs (approx). The loss seems to be converging at 0.48
    
epochs:10
![keras train image 10](/SLR/images/keras_train_10.png)
![keras test image 10](/SLR/images/keras_train_10.png)
epochs:50
![keras train image 50](/SLR/images/keras_train_50.png)
![keras test image 50](/SLR/images/keras_train_50.png)
epochs: 100
![keras train image 100](/SLR/images/keras_train_100.png)
![keras test image 100](/SLR/images/keras_train_100.png)
epochs:200
![keras train image 200](/SLR/images/keras_train_200.png)
![keras test image 200](/SLR/images/keras_train_200.png)
epochs:500
![keras train image 500](/SLR/images/keras_train_500.png)
![keras test image 500](/SLR/images/keras_train_500.png)
