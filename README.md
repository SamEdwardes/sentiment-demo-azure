# Sentiment Analysis Demo

Simple python web app demonstrating flask and sentiment analysis.

## Steps

The below steps are a general outline of how to create a sentiment analysis app using python, flask, and Azure. The list below is not 100% comprehensive. Check out this [YouTube Video](https://youtu.be/eUitxqLxICo) from Microsoft for a complete demo.

Create a virtual environment using conda. Enter the following into the terminal:

> conda create --name sentiment-analysis-env python=3.7
<br> conda install -c anaconda flask
<br> conda install -c conda-forge textblob

Write the python code that will be used to generate the flask app and sentiment analysis.

>*see src folder*

Get the requirements need to create the web app by typing the following into the terminal:

> pip freeze > requirements.txt

Deploy to Azure. You will need to have an account with Azure, you can sign up for a 30 day free trial. Run on the terminal:

> az webapp up -n senimentdemo


