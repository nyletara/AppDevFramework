# import Flask
from flask import Flask, render_template
# import ConfigParser
import ConfigParser


'''
* Create instance of configparser
* Reads values from configuration file
'''
config = ConfigParser.ConfigParser()
config.readfp(open(r'./configurations.txt'))

secret_key = config.get('APP CONFIG', 'secret_key')
app_port = int(config.get('APP CONFIG', 'port'))

'''
* Create an instance of the class
* Argument __name__ allows the name of the instance
  to change depending on if it's started as an application
  or imported as a module
'''
app = Flask(__name__)


'''
* Modify the app's configuration values
* Uses dict.update() mothod for multiple values
'''
app.config.update(
    DEBUG=True,
    SECRET_KEY=secret_key
)


'''
* app.route binds a function to a URL
* This route renders the HTML page index.html
'''
@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


'''
* This route returns plain text
'''
@app.route('/text', methods=['GET'])
def getText():
    return "Hello World"


'''
* <variable_name> denotes a variable value in the URL
* Returns the variable value
'''
@app.route('/getVariable/<variable_name>/', methods=['GET','POST'])
def getVariable():
    return 'Variable Value %s' % variable_name


'''
* Feature 1
'''
@app.route('/feature1/', methods=['GET','POST'])
def feature1():
    return 'Feature 1'


'''
* Feature 2
'''
@app.route('/feature2/', methods=['GET','POST'])
def feature2():
    return 'Feature 2'


'''
* Runs the statements if the __name__ is set to the string '__main__'
* AKA if the script is being run directly
* (opposed to being imported into another module)
'''
if __name__ == '__main__':
    app.run(port=app_port)


