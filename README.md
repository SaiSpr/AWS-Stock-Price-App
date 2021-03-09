# aws-stock-web-app

# Demo

Launch the web app:

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/saispr/aws-stock-price-app/main/app.py)

# Reproducing this web app
To recreate this web app on your own computer, do the following.

### Create conda environment
Firstly, we will create a conda environment called *stock*
```
conda create -n stock python=3.7.9
```
Secondly, we will login to the *stock* environement
```
conda activate stock
```
### Install prerequisite libraries

Download requirements.txt file

```
wget https://github.com/SaiSpr/AWS-Stock-Price-App/blob/main/requirements.txt

```

Pip install libraries
```
pip install -r requirements.txt
```

###  Download and unzip contents from GitHub repo

Download and unzip contents from https://github.com/SaiSpr/AWS-Stock-Price-App

###  Launch the app

```
streamlit run app.py
```
