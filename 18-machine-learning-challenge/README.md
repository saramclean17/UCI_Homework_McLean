# Machine Learning Homework
## SVM and Logistical Regression Models Comparison

## SVM
* The first step after reading the data to a dataframe was to decide on the features to keep for the model. For example, this exo_planet data has koi_tce_plnt_num column that was not useful as a feature so I removed it.
* After deciding which features to keep next step was assigning X and y values for the model to perform split data to get train and test data for the model.
* The next step was to scale and normalize the data to create more accurate model that has less gaps between data points, so they all have acurate weights for the model. 
 - Initially, using MinMaxScaler to scale the data with SVM model, the training and testing scores were around 0.85. Changing to StandardScaler to scale the data resulted in better scores, 
* Training Data Score: 0.8916650772458516,Testing Data Score: 0.8947368421052632.
* Using GridSearchCV to tune the model parameters and changing the grid parameters C and gamma didn't result in better scores.

## Logistical Regression
* For this model, data cleaning and preprocessing steps were the same as SVM model.
* Using StandardScaler resulted in better scores than MinMaxScaler, so I used StandardScaler to scale and normalize the data.
* The scores for training and testing data were :Training Data Score: 0.887659736791913, Testing Data Score: 0.8895881006864989.
* Using GridSearchCV to tune the model's parameters, plus changing C values and increasing the number of iterations max_iter didn't improve scores enough.

## Final Analysis
As a result, the two models didn't have any significant difference between them for this data, and even utlizing hyperparameters tuning didn't help the differentiate the models. I can state that the SVM model performs sligtly better based on this particular outcome.
