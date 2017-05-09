# Framework for a Serverless Service-Oriented Application

This section turns the server based service oriented  application that was previously built into a standalone serverless Service Oriented Application. In other words, each feature (or service) that was previously built and hosted on its own server, is now converted into Lambda functions hosted on AWS. This "serverless" technology is one of the most effective SOA models in the upcoming age, due to its cost and scalability benefits. 

## Project Structure Convention

.
├── orchestrator          				# subfolder for orchestrator
│   ├── configurations.txt              # configurations.txt file
│   ├── orchestrator_lambda.py          # orchestrator file containing lambda functions
├── service_one          				# subfolder for service one
│   ├── configurations.txt              # configurations.txt file
│   ├── service_one_lambda.py           # service one lambda functions
├── service_two          				# subfolder for service two
│   ├── configurations.txt              # configurations.txt file
│   ├── service_two_lambda.py      	    # service two lambda functions
├── service_three          				# subfolder for service three
│   ├── configurations.txt              # configurations.txt file
│   ├── service_three_lambda.py         # service three lambda functions
└── .gitignore            				# tells Git which files to ignore


## File: configurations.txt

The configurations.txt file contains all keys that should not be pushed to GitHub. These keys include API keys, secret keys, or any extra information.

The format of the configurations.txt file should be:
```text
[API Keys]
some_api_key=abcDEFghiJKL
```

To access these keys in a python file, import ConfigParser and pull the values:
```python
import ConfigParser
config = ConfigParser.ConfigParser()
config.readfp(open(r'./configurations.txt'))
api_key = config.get('API Keys', 'some_api_key')
```
Each of the subfolders contains a configurations.txt file as it is required by each lambda function. Unlike previous deployments, however, the path for config files in Lamda are very specific and so have already been handled for the user by this framework. 

## The Orchestrator (orchestrator_lambda.py)

The Orchestrator is the first component of this architecture but will be the last to be completed. The orchestrator facilitates communication between the User Interface as well as among all the different services that make up the application. Similar to how it was structured in the Server-based SOA model, this orchestrator communicates between each of the services through GET/POST calls. We will look into how to call Lambda functions through REST Endpoints later on in this section. Each lambda function requires a "handler" which allows AWS to know the entry point to the functoin as well as pass in the parameters that you require. Since our goal was to easily switch from Server-based SOA to Serverless SOA, however, our handlers simply serve the function of calling the "main" functions that we had written in the previous model. This ensures we are maximizing code reuse. 

For testing purposes, a main function has also been included so that users can locally test their functions before deploying on AWS Lambda. In other words, users can treat these functions as any python functions that they may be familiar to working with, such as by running:
```python
python orchestrator_lambda.py
```
The user should comment out the "main" entry point to the function before deploying on lambda.

## Service One (service_one_lambda.py)

This is a standard service, such as ones we had in the Server-based SOA model. Hence, it is a specific feature for the application that is being built. Similar to the orchestrator, it has a handler that parses the required input and then passes it on to the previously written function that handles the nitty-gritty details of the feature. 

For testing purposes, a main function has also been included so that users can locally test their functions before deploying on AWS Lambda. In other words, users can treat these functions as any python functions that they may be familiar to working with.

## Service Two (service_two_lambda.py)

This is a standard service, such as ones we had in the Server-based SOA model. Hence, it is a specific feature for the application that is being built. Similar to the orchestrator, it has a handler that parses the required input and then passes it on to the previously written function that handles the nitty-gritty details of the feature. 

For testing purposes, a main function has also been included so that users can locally test their functions before deploying on AWS Lambda. In other words, users can treat these functions as any python functions that they may be familiar to working with. 

## Service Three (service_three_lambda.py)

This is a standard service, such as ones we had in the Server-based SOA model. Hence, it is a specific feature for the application that is being built. Similar to the orchestrator, it has a handler that parses the required input and then passes it on to the previously written function that handles the nitty-gritty details of the feature. 

For testing purposes, a main function has also been included so that users can locally test their functions before deploying on AWS Lambda. In other words, users can treat these functions as any python functions that they may be familiar to working with. 

## Deploying on AWS Lambda

### Creating a Lambda Deployment Package

### Linking up to API Gateway
