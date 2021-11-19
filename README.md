# ApplicationOfBigData_projectCreditRisk
A repository for Ly Jean, Tang Jérémy, and Maréchal Théo's "Application of big Data" project.

The datasets used come from : https://www.kaggle.com/c/home-credit-default-risk/data

## Goals :
 * Building a classical ML projects which respects basic ML Coding best practices
 * Integrate MLFlow to your project
 * Integrate ML Interpretability to your project

## Project architecture

  * **ApplicationOfBigData_projectCreditRisk** : the root directory of the project
    * **Data** : the directory containing all the data used for the project
      * **application_train.csv** : The initial dataset, it contain information about loans and loans applicants (at application time), each line is a unique application 
      * **dataset_prepared.csv** : The previous dataset but with all useless (for that project) features removed, empty or null data filled when possible, and absurd numerical data removed 
      * **dataset_final.csv** : The previous dataset but with a one-hot encoding of the categorical features, it's the dataset used for training and testing models
    * **Model** : the directory containing all the models trained for that project saved as pickled files
      * **GradientBoosting.pkl** : A gradient boosting model
      * **RandomForest.pkl** : A random forest model 
      * **XGBoost.pkl** : An Extra Gradient Boosting model
    * **Notebook** : The directory containg the 6 notebooks used for that project 
      * **Data_preparation.ipynb** : A notebook which collect the data from application_train.csv come from a [Kaggle contest](.csv and create dataset_prepared.csv
      * **Features_engineering.ipynb** : A notebook which collect the data from dataset_prepared.csv and create dataset_final.csv
      * **Model_training.ipynb**: A notebook which splited the data from dataset_final.csv into a test and a train dataset, then used the the train dataset to train the 3 models 
      * **Predict.ipynb** : A notebook wich import the trained models and test their performances on the test dataset 
      * **Mlflow.ipynb** : A notebook which used to evaluate the trained models
      * **SHAP.ipynb** : A notebook which uses Shap to graphically explained the trained models
      * **mlruns** : A directory created when using MLflow which contains the runs' logs
    * **ReadMe.md** : The file you are currently reading
    * **environment.yml** : A xml file which used to build the conda environnement used by jupyter.
    * **setup_env.sh** : A bash file which setup the project workspace by creating files not stocked on the git, the conda environment, and linking the conda env and jupyter.
    * **.gitignore** : A file which is used to exclude files which shan't be on the git either because they're not relevant (like jupyter's logs) or because they're to big (like the models and datasets)

## How to set up the project

 1. Git clone the project into a directory using the following command : ```git clone "https://github.com/theo-f-marechal/ApplicationOfBigData_projectCreditRisk.git"```
 2. Run the setup_env.sh file
 3. The runnning that file should have created 2 new repositories : Data and Model. Add application_train.csv to the Data repository.
 4. Launch jupyter notebook using the following command ```jupyter notebook``` and make sure that the kernel used is the conda env named ABD.
 5. Run the notebooks in the following order : Data_preparation => Features_engineering => Model_training ; the last 3 notebook can then be run in whichever order you prefer.
 6. If you've run the Mlflow notebook, you can then acces the MLflow ui using the following URL : ```http://localhost:5000```

## Project output 

### MLflow ui

### Shap
![Tree explainer](https://raw.githubusercontent.com/theo-f-marechal/ApplicationOfBigData_projectCreditRisk/main/Pictures/chrome_19Ihascy51.png)

## Sources

 * Application_train.csv come from a [Kaggle contest](https://www.kaggle.com/c/home-credit-default-risk/data)
 * Part of the code is largely inspired by the labs done throughtout the Application of Big Data course.
