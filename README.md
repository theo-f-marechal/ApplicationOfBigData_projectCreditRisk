# ApplicationOfBigData_projectCreditRisk
A repository for Ly Jean, Tang Jérémy, and Maréchal Théo's "Application of big Data" project.

## Goals :
 * Building a classical ML project that respects basic ML Coding best practices
 * Integrate MLFlow to your project
 * Integrate ML Interpretability to your project

## Project architecture

  * **ApplicationOfBigData_projectCreditRisk** : the root directory of the project
    * **Data** : the directory containing all the data used for the project
      * **application_train.csv** : The initial train dataset, its contain information about loans and loans applicants (at application time), each line is a unique application 
      * **dataset_prepared.csv** : The previous dataset but with all useless (for that project) features removed, empty or null data are filled when possible, and absurd numerical data removed 
      * **dataset_final.csv** : The previous dataset but with a one-hot encoding of the categorical features, it's the dataset used for training and testing models
      * **application_test.csv** : The initial test dataset, its contain information about loans and loans applicants (at application time), each line is a unique application 
      * **dataset_test_prepared.csv** : The previous test dataset but with all useless (for that project) features removed, empty or null data are filled when possible, and absurd numerical data removed 
      * **dataset_test_final.csv** : The previous test dataset but with a one-hot encoding of the categorical features, it's the dataset used for training and testing models
    * **Model** : the directory containing all the models trained for that project saved as pickled files
      * **GradientBoosting.pkl** : A gradient boosting model
      * **RandomForest.pkl** : A random forest model 
      * **XGBoost.pkl** : An Extra Gradient Boosting model
    * **Notebook** : The directory containing the 6 notebooks used for that project 
      * **Data_preparation.ipynb** : A notebook which collect the data from application_train.csv come from a [Kaggle contest](.csv and create dataset_prepared.csv
      * **Features_engineering.ipynb** : A notebook that collects the data from dataset_prepared.csv and creates dataset_final.csv
      * **Model_training.ipynb**: A notebook that splits the data from dataset_final.csv into a test and a training dataset, then used the training dataset to train the 3 models and test their performances on a validation dataset created with the train_test_split
      * **Predict.ipynb** : A notebook that imports the trained models and make some predictions on random data from the dataset_test_final.csv
      * **Mlflow.ipynb** : A notebook used to evaluate the trained models
      * **SHAP.ipynb** : A notebook that uses Shap to graphically explain the trained models
      * **mlruns** : A directory created when using MLflow which contains the runs' logs
    * **Pictures** : A directory containing the Readme's pictures
    * **doc** : A directory containing sphinx
    * **ReadMe.md** : The file you are currently reading
    * **environment.yml** : A yml file used to build the Conda environment used by Jupyter.
    * **setup_env.sh** : A bash file that setups the project workspace by creating files not stocked on the git, the Conda environment, and linking the Conda env and Jupyter.
    * **.gitignore** : A file that is used to exclude files that shan't be on the git either because they're not relevant (like Jupyter's logs) or because they're too big (like the models and datasets)

## How to set up the project

 1. Git clone the project into a directory using the following command : ```git clone "https://github.com/theo-f-marechal/ApplicationOfBigData_projectCreditRisk.git"```
 2. Run the setup_env.sh file
 3. The running that file should have created 2 new repositories : Data and Model. Add application_train.csv to the Data repository.
 4. Launch Jupyter notebook using the following command ```jupyter notebook``` and make sure that the kernel used is the conda env named ABD.
 5. Run the notebooks in the following order : Data_preparation => Features_engineering => Model_training ; the last 3 notebooks can then be run in whichever order you prefer.
 6. If you've run the Mlflow notebook, you can then access the MLflow ui using the following URL : ```http://localhost:5000```

## Project output 

### MLflow ui
![MLflow ui](https://raw.githubusercontent.com/theo-f-marechal/ApplicationOfBigData_projectCreditRisk/main/Pictures/chrome_XOrm5i5MAY.png)

### Shap
![XGBoost Tree explainer](https://raw.githubusercontent.com/theo-f-marechal/ApplicationOfBigData_projectCreditRisk/main/Pictures/chrome_KVE3DxDIVm.png)
![XGBoost Summary plot](https://raw.githubusercontent.com/theo-f-marechal/ApplicationOfBigData_projectCreditRisk/main/Pictures/chrome_6HdzLO87xQ.png)

## Sources

 * Application_train.csv come from a [Kaggle contest](https://www.kaggle.com/c/home-credit-default-risk/data)
 * Part of the code is largely inspired by the labs done throughtout the Application of Big Data course.
