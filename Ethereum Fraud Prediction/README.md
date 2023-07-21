# Predicting Ethereum Fraud
# Project:
Cryptocurrencies: their popularity and their impact on our marketplaces and economies ebb and flow. Some months they’re up, some they’re down, and sometimes nobody is interested. But sometimes, everybody is scrambling to buy, everybody wants in on the rollercoaster. Some of the projects are interesting, some hold potential, and others are just scams.
This project examines one well-known cryptocurrency, Ethereum, and trains a random forest classifier model to predict, with a high degree of accuracy, whether any given Ethereum transaction is fraudulent based information publicly available on the Ethereum blockchain. It contains extensive data visualization and exploration through the use of histograms and boxplots to identify useful features, as well as principle component analysis and recursive feature elimination with cross validation to deal with the large numbers of features that emerged due to one-hot encoding. The utility of the model is assessed through the usual metrics of precision, recall, and f1 score, as well as examining the performance of the model graphically through confusion matrices and ROC graphs.

# How to Use:
Simply download the file and its associated data, and when running the notebook remember to copy and paste the data path on your local system into the initial data read.
 The notebook should then run without issue, with the exception of the 47th and 48th code cells that were left in place to demonstrate the failures experienced due to NaN’s in my data while attempting to engage in feature selection and transformation. Once those errors emerge, simply move on to the immediately subsequent cells and begin running the notebook again from there.

# Data:
The data used to train this model was uploaded to Kaggle by Vagif Aliyev, and can be found here: https://www.kaggle.com/datasets/vagifa/ethereum-frauddetection-dataset.
The data itself was collected using Etherscan API, and ehterscamdb API.

# License:
The data I used was made available under the Database: Open Database, Contents: Database Contents license. Please remember to cite the appropriate parties if using their work.
