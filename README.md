# ph-recognition

Show ph value from the image based on the its color. Using machine learning algorithms

### From where I got datasets ?

I downloaded images of ph-scale from [here](https://www.shutterstock.com/search/ph+scale) then I croped into small pictures so for example the 0 value is 0.jpg


### Training methods

Firstly I decided to use machine learning supervised algorithms such as Gradient Boosting Regressor (*process_data.ipynb*) and SVM (*svm.ipynb*). 

Then I used unsupervised ML algorithms like KMeans (*unsupervised_learning.ipynb*)

Also I try to build neural network in Keras. (*neural_network.ipynb*)

Add multilabel classification (*classification.ipynb*)

## GUI 
GUI was built in PyQT library. Clicking on the image generate pH value, which is shown on the bottom of the app.
![Screenshot](/images/screenshot.png)


### To do next

Add more datasets

Write own ML algorithm
