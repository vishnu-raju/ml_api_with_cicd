git clone git@github.com:vishnu-raju/ml_api_with_cicd.git
cd ml_api_with_cicd
make all
az webapp up --name vnrmlapi --resource-group AzureDevops --runtime "PYTHON:3.7"