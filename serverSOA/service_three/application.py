import json
from flask import Flask, request, render_template
import requests
import ConfigParser

'''
* create instance of configparser
* reads values from configuration file
* this is the file that contains all the ports and hosts that are required to run the servers
'''

config_file_path = '../configurations.txt'

config = ConfigParser.ConfigParser()
config.readfp(open(config_file_path))

'''
* reads values from configuration file
* since we are running multiple instances, it is easiest to pass in ports through the config file
'''

PORT=config.get('PORT Values', 'ServiceThreePort')
HOST=config.get('HOST Values', 'ServiceThreeHost')

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
* since we are now using a service, it is important to understand that only one feature is handled by this server
* hence, only one task is to be done by this function
'''

@application.route('/URL/<arg_one>/<arg_two>', methods=['GET', 'POST'])
def feature_three(arg_one, arg_two):
    # TODO Implementation for the second feature goes here
    return data_to_send

'''
* the server needs to be started by running "python application.py"
'''

if __name__ == '__main__':
    app.run(port=PORT, host=HOST)
