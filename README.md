# MSDS-434-BankMarketingProject

# Overview
This project focuses on leveraging machine learning and cloud applications to predict conversions in a Bank Marketing dataset. Amazon Web Services (AWS) is used for data storage and to develop a serverless application with Lambda, while Google Colab is leveraged for machine learning with Pytorch.

[Click Here to Preview Google Colab Notebook](https://colab.research.google.com/drive/1J3LGfd6ayPH37g5g3Xr_0oOvSThFm1Lb#scrollTo=WhCj0XnvYgQ8)

[Click Here to Access Tableau Public Link](https://public.tableau.com/app/profile/kevin.tong7552/viz/MSDS434BankMarketingFinalProject/Dashboard1?publish=yes)

# Table of Contents
1. About the Dataset
2. Technologies Used
3. Workflows


# About the Dataset
The Bank Marketing dataset is provided by the UC Irvine Machine Learning Repository. The dataset consists of 45211 rows and 16 features of which can be used for predictive modeling. An additional column is added that notes whether the contact led to a conversion or not.

[Click Here to Access Bank Marketing Dataset](https://archive.ics.uci.edu/dataset/222/bank+marketing)

# Technologies Used

## Amazon Web Services (AWS)
AWS is used as the main cloud platform for data processing, storage, and application modeling.

### S3 Buckets
S3 is used for dataset storage (as CSVs). A training dataset is saved in S3 for modeling purposes, while 15 other CSVs are stored for testing and predictions.

### Lambda Function
A lambda function is created that is automatically triggered to process CSVs when a new file is uploaded to a certain S3 bucket.

![lambda](https://github.com/tongkevn/MSDS-434-BankMarketingProject/blob/622e9a2134080386bd53724bccecb531d3148085/lambdafunction.png)

### Cloudwatch
Cloudwatch is leveraged to monitor traffic and usage of the lambda function.

![cloudwatch screenshot](https://github.com/tongkevn/MSDS-434-BankMarketingProject/blob/504f2f9aa5f367595388e732556a6dec7f441c32/cloudwatch.png)

## Google Colab
As an alternative to AWS Sagemaker, which can be cost prohibitive, Google Colab is leveraged to develop a Pytorch machine learning model, run predictions on a sample dataset, and subsequently upload to S3. The problem is set up as a binary classification model, which is predicting a conversion (“1”) or not (“0”)

## Tableau
Results from the machine learning model are visualized to the end user with Tableau. The primary audience can be a marketing manager for instance, who is interested in learning how the model is performing and would like additional summary statistics.

# Workflow
To simulate a real world situation the workflow is designed as follows:

1. Google Colab will read a training CSV hosted in S3 and generate a Pytorch model. The model achieves ~95% accuracy.
2. An unseen dataset is then loaded from S3 into Google Colab for the model to make predictions. An additional column is added to the dataset that notes a conversion or not.
3. Google Colab will then upload a CSV version of the dataset to an S3 bucket.
4. Once a CSV is uploaded, an AWS Lambda function is automatically triggered. The function will concatenate all the CSVs in the bucket, and upload to a third bucket.
5. AWS Cloudwatch visualizations are utilized for Lambda function monitoring and usage.
6. Tableau will read the combine CSV, and is then leveraged for end user visualizations and summary statistics tables to gain Bank Marketing campaign insights.
