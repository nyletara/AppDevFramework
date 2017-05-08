# import Flask
from flask import Flask, render_template
# import ConfigParser
import ConfigParser


'''
* create instance of configparser
* reads values from configuration file
'''
config = ConfigParser.ConfigParser()
config.readfp(open(r'./configurations.txt'))

secret_key = config.get('KEYS', 'secret_key')


'''
* create an instance of the class
* argument __name__ allows the name of the instance
  to change depending on if it's started as an application
  or imported as a module
'''
app = Flask(__name__)


'''
* modify the app's configuration values
* uses dict.update() mothod for multiple values
'''
app.config.update(
    DEBUG=True,
    SECRET_KEY=secret_key
)


'''
* app.route binds a function to a URL
* this route renders the HTML page index.html
'''
@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


'''
* this route returns plain text
'''
@app.route('/text', methods=['GET'])
def getText():
    return "Hello World"


'''
* <variable_name> denotes a variable value in the URL
* returns the variable value
'''
@app.route('/getVariable/<variable_name>/', methods=['GET','POST'])
def getVariable():
    return 'Variable Value %s' % variable_name


'''
* feature 1
'''
@app.route('/feature1/', methods=['GET','POST'])
def feature1():
    return 'Feature 1'


'''
* feature 2
'''
@app.route('/feature2/', methods=['GET','POST'])
def feature2():
    return 'Feature 2'


'''
* runs the statements if the __name__ is set to the string '__main__'
* AKA if the script is being run directly
* (opposed to being imported into another module)
'''
if __name__ == '__main__':
    app.run()


