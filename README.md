[![Python application](https://github.com/quyetnn1102/udacity-azure-devops-project2/actions/workflows/python-app.yml/badge.svg)](https://github.com/quyetnn1102/udacity-azure-devops-project2/actions/workflows/python-app.yml)
# Overview

In this project, you will build a Github repository from scratch and create a scaffolding that will assist you in performing both Continuous Integration and Continuous Delivery. You'll use Github Actions along with a Makefile, requirements.txt and application code to perform an initial lint, test, and install cycle. Next, you'll integrate this project with Azure Pipelines to enable Continuous Delivery to Azure App Service.

## Project Plan
It is very helpful to have a project plan and task tracking so in this project we will use Excel spreadsheet and Trello board for that:

* [Trello Board](https://trello.com/b/iZRpZVWd/udacity-azure-devops-building-ci-cd-pipeline)
    
* [Project Plan](https://github.com/quyetnn1102/udacity-azure-devops-project2/blob/00fbe25748ecfdd474f84583fada82a37c0d1958/Azure-Devops-CICD-project-plan.xlsx)

## Instructions

![CI diagram](./screenshots/ci-diagrams.png)
![CD diagram](./screenshots/cd-diagrams.png)

### 2.1.	Configuring GitHub
    - Log into Azure Cloud Shell
    - Create a ssh key

```bash
ssh-keygen -t rsa -b 2048 -C "yourgithub_Id@gmail.com"
```
![alt text](./screenshots/id_rsa_pub.png)

Copy the public key to your GitHub Account -> Settings -> SSH and GPG keys (https://github.com/settings/keys)


Once SSH Key configured in Github then clone project into Azure Cloud Shell 
```bash
git clone git@github.com:quyetnn1102/udacity-azure-devops-project2.git
```
![alt text](./screenshots/clone_project.png)

Create a Python Virtual Environment to run your application

```bash
make setup
```
![alt text](./screenshots/make_setup.png)


And then activate the virtual environment
```bash
source ~/.udacity-azure-devops-project2/bin/activate
```
![alt text](./screenshots/active_virtualenv.png)

Run following command to install project dependencies
```bash
make all
```

![alt text](./screenshots/make_all.png)

Run Application and make a test using below command

Run application
```bash
export FLASK_APP=app.py
	flask run
```
![alt text](./screenshots/flask_run_local.png)

Make a prediction test
```bash
sh make_prediction.sh
```
![alt text](./screenshots/make_test_local.png)

Now time to deploy the application to Azure App Service using below command
```bash
az webapp up -n quyetnn-udacity-project2 -g Azuredevops --sku FREE
```

![alt text](./screenshots/deploy_code_to_azappservice.png)


![alt text](./screenshots/azure_app_home.png)


Make a prediction test for deployed app running on Azure App Services
```bash
sh make_predict_azure_app.sh
```

![alt text](./screenshots/make_test_azure.png)

Output of streamed log files from deployed application in Azure App Service 
```bash
az webapp log tail --name quyetnn-udacity-project2 --resource-group Azuredevops
```

![alt text](./screenshots/appservice_tail_log.png)


Set up the CI pipeline with GitHub Actions and result when push to the repository:
![alt text](./screenshots/github_action_output.png)


Load test using locust
```bash
pip install locust
```

Move to directory contains locustfile.py before run command:
```bash
locust
```
Open Locust app http://localhost:8089/ then config test with your deployed host `https://quyetnn-udacity-project2.azurewebsites.net/`
![alt text](./screenshots/locust_config_test.png)

The output test
![alt text](./screenshots/locust_load_test.png)

* Successful deploy of the project in Azure Pipelines.  [Note the official documentation should be referred to and double checked as you setup CI/CD](https://docs.microsoft.com/en-us/azure/devops/pipelines/ecosystems/python-webapp?view=azure-devops).

* Running Azure App Service from Azure Pipelines automatic deployment

* Successful prediction from deployed flask app in Azure Cloud Shell.  [Use this file as a template for the deployed prediction](https://github.com/udacity/nd082-Azure-Cloud-DevOps-Starter-Code/blob/master/C2-AgileDevelopmentwithAzure/project/starter_files/flask-sklearn/make_predict_azure_app.sh).
The output should look similar to this:







## Enhancements

The project can be configured to work with GitFlow, so if you commit to a particular branch, the code can continue to be deployed in the corresponding environment (DEV, QA, Staging or PROD).

## Demo 

<TODO: Add link Screencast on YouTube>


