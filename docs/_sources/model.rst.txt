Model
=====
Linear Regression
-----------------
Linear regression is a linear approach to modelling the relationship between a scalar response and one or more explanatory variables. The case of one explanatory variable is called simple linear regression.

.. image:: images/9.png

Linear regression is the next step up after correlation. It is used when we want to predict the value of a variable based on the value of another variable. The variable we want to predict is called the dependent variable (or sometimes, the outcome variable). Linear regression consists of finding the best-fitting straight line through the points. The best-fitting line is called a regression line.

Evaluation
----------
Since we are attempting to perform regression which outputs continuous value within a given range. Our main goal is to minimize the error which is defined by the Loss Function.

We have used Mean Squared Error(MSE) as a metric to evaluate the results of the prediction. MSE is the sum of squared distances between our target variable and predicted values.
