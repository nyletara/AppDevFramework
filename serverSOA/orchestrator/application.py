import json
from flask import Flask, request, render_template
import requests
import ConfigParser

config_file_path = '/configurations.txt'

config = ConfigParser.ConfigParser()
config.readfp(open(config_file_path))

ORCHESTRATOR_PORT=config.get('PORT Values', 'OrchestratorPort')
HOST=config.get('HOST Values', 'CurrentHost')

application = Flask(__name__)
application.config.update(
    DEBUG=True,
    SECRET_KEY='<SECRET_KEY>'
)

@application.route('/URL/<arg_one>/<arg_two>', methods=['GET', 'POST'])
def orchestrator(arg_one, arg_two):
    data_from_service_one = requests.get('<SERVICE_URL>')
    data_from_service_two = requests.post('<SERVICE_URL>', json={"<data_to_send>"})
    return data_to_send

if __name__ == '__main__':
    app.run(port=ORCHESTRATOR_PORT, host=HOST)
