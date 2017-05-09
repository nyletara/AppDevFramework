import json
from flask import Flask, request, render_template
import requests
import ConfigParser

'''
* create instance of configparser
* reads values from configuration file
* this is the file that contains all the ports and hosts that are required to run the servers
'''

config_file_path = '/configurations.txt'

config = ConfigParser.ConfigParser()
config.readfp(open(config_file_path))

'''
* reads values from configuration file
* since we are running multiple instances, it is easiest to pass in ports through the config file
'''

ORCHESTRATOR_PORT=config.get('PORT Values', 'OrchestratorPort')
HOST=config.get('HOST Values', 'CurrentHost')

'''
* create an instance of the class
* argument __name__ allows the name of the instance
  to change depending on if it's started as an application
  or imported as a module
'''

application = Flask(__name__)


'''
* modify the app's configuration values
* uses dict.update() mothod for multiple values
'''

application.config.update(
    DEBUG=True,
    SECRET_KEY='<SECRET_KEY>'
)

'''
* app.route binds a function to a URL
* this route is the main route that is called by the user
* parameters can be passed in the form of /URL/param1/param2
* since this is the orchestrator GET and POST requests are made to communicate with the other services
* this ensures that no services are coupled and we are following an SOA
'''

@application.route('/URL/<arg_one>/<arg_two>', methods=['GET', 'POST'])
def orchestrator(arg_one, arg_two):
    data_from_service_one = requests.get('<SERVICE_URL>')
    data_from_service_two = requests.post('<SERVICE_URL>', json={"<data_to_send>"})
    return data_to_send

'''
* the server needs to be started by running "python application.py"
'''

if __name__ == '__main__':
    app.run(port=ORCHESTRATOR_PORT, host=HOST)
