# Server Based Service-Oriented Application

This section turns the monolithic application that was previously built into a standalone Server-based Service Oriented Application. In other words, each feature (or service) that built up the initial monolithic application is now split into individual servers that communicate with each other. This provides a variety of benefits which are highlighted in the following paper: *SOA paper link*

This section still uses Flask Application Servers that allow users to host applications locally or on cloud servers, hence, maximizes as much code-reuse as possible. 

## Project Structure Convention

    .
    ├── orchestrator                # Orchestrator folder to connect with services
    │   ├── application.py              # Flask application for orchestrator 
    ├── service_one                 # Folder for a designated service one
    │   ├── application.py              # Flask application for Service One
    ├── service_two                 # Folder for a designated service two
    │   ├── application.py              # Flask application for Service Two
    ├── service_three               # Folder for a designated service three
    │   ├── application.py              # Flask application for Service Three
    ├── configurations.txt          # Configuration file with keys (not tracked by git)
    └── .gitignore                  # tells Git which files to ignore
    
   Note: AWS Elastic Beanstalk requires the file name to be called "application.py" internally

#### The Orchestrator

The Orchestrator is the first component of this architecture but will be the last to be completed. The orchestrator facilitates communication between the User Interface and all the different services that make up the application. Within orchestrator/application.py, there are different GET and POST requests designed to post and retrieve data from the services. Users have the option to update these and extrapolate to include more services


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
## To Run:
Run each service separately and then run the orchestrator to communicate with the launched services. For example:
In Tab 1:
```python
cd service_one
python application.py
```
In Tab 2:
```python
cd service_two
python application.py
```
In Tab 3:
```python
cd service_three
python application.py
```
In Tab 4:
```python
cd orchestrator
python application.py
```

