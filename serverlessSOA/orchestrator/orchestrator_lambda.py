import json
import requests
import ConfigParser
import os

'''
* create instance of configparser
* reads values from configuration file
* this is the file that contains all the ports and hosts that are required to run the servers
* lambda functions, since they don't run on a server, require a specific route (provided) for the config_file_path
'''

config_file_path = os.environ['LAMBDA_TASK_ROOT'] + './configurations.txt'

config = ConfigParser.ConfigParser()
config.readfp(open(config_file_path))


'''
* The biggest change between moving to Lambda SOA is the addition of a handler, which always has the form below
* the handler takes in an event, and a context, which provides the user with information. 
* the format of the handler must always be the same, since AWS requires it to be so
* To maximize code reuse, the best way to structure the additional handler is by using it to parse the arguments 
* that were previously passed through the route. These can then call the same feature function that was previously
* written for the server based SOA architecture
'''

def orchestrator_handler(event, context):
	arg_one = event['key_for_arg_one']
	arg_two = event['key_for_arg_two']
	data_to_send = orchestrator(arg_one, arg_two)
	return data_to_send

'''
* this is the same function we had before for the orchestrator, but note how it no longer requires any dependency on Flask
* Lambda is all about the "serverless" technology. Cool right? See our main documentation for more. 
'''	

def orchestrator(arg_one, arg_two):
    data_from_service_one = requests.get('<SERVICE_URL>')
    data_from_service_two = requests.post('<SERVICE_URL>', json={"<data_to_send>"})
    return data_to_send

'''
* Main is not required in lambda functions, but how do we test then? Locally we can test the same way we test any python
* function, by calling it in main. Use this to test if your fucntions work, once they work locally, you are ready to create
* a deployment package for this lambda function. See our main documentation for more. Comment Main before deploying. 
'''

if __name__ == '__main__':
    arg_one = 'string'
    arg_two = 'string'
    print orchestrator(arg_one, arg_two)
