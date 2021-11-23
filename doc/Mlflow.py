#!/usr/bin/env python
# coding: utf-8

# # MlFlow

# In[1]:


import mlflow
import pickle
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split


# ### Retrieving the csv data in the notebook 

# In[2]:


df_trimed = pd.read_csv("../Data/dataset_final.csv")
x_train, x_test, y_train, y_test = train_test_split(df_trimed.loc[:,df_trimed.columns != 'TARGET'], df_trimed['TARGET'], test_size = 0.3, random_state = 50)


# ### Creation of a function evaluate, to create logs in the MlFlow ui

# In[3]:


def evaluate(x_test, y_test, model):
    """
    This fonction is used to call mlflow with a model and data to test it
    
    :param x_test: a dataframe containing the test feature, defaults to None
    :type x_test: a pandas dataframe
    :param y_test: a dataframe containing the target feature, defaults to None
    :type y_test: a pandas dataframe
    :param model: a trained model, defaults to None
    :type model: a model
    :return: None
    :rtype: None
    """

    import os
    import warnings
    import sys

    import pandas as pd
    import numpy as np
    from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

    import mlflow
    import mlflow.sklearn
    
    import logging
    logging.basicConfig(level=logging.WARN)
    logger = logging.getLogger(__name__)

    def eval_metrics(actual, pred):
        rmse = np.sqrt(mean_squared_error(actual, pred))
        mae = mean_absolute_error(actual, pred)
        r2 = r2_score(actual, pred)
        return rmse, mae, r2

    with mlflow.start_run():

        # Evaluate Metrics
        predicted_qualities = model.predict(x_test)
        (rmse, mae, r2) = eval_metrics(y_test, predicted_qualities)

        # Print out metrics
        print("  RMSE: %s" % rmse)
        print("  MAE: %s" % mae)
        print("  R2: %s" % r2)

        # Log parameter, metrics, and model to MLflow
        mlflow.log_metric("rmse", rmse)
        mlflow.log_metric("r2", r2)
        mlflow.log_metric("mae", mae)

        mlflow.sklearn.log_model(model, "model")


# ### Use of the evaluate fonction

# In[4]:


XGBoost = pickle.load(open('../Model/XGBoost.pkl', 'rb'))
run = evaluate(x_test, y_test, XGBoost)
run


# In[ ]:




