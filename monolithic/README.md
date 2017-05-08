# Framework for a Monolithic Application using Flask


## Project Structure Convention

    .
    ├── app.py                # Flask application
    ├── static                # subfolder for webpage styling
    │   ├── css               # subfolder for css files
    │   ├── js                # subfolder for js files
    ├── template              # subfolder for html files
    │   ├── index.html        # html file for index.html (called in app.py)
    ├── requirements.txt      # stores all dependencies
    ├── configurations.txt    # configuration file with keys (not tracked by git)
    └── .gitignore            # tells Git which files to ignore


## File: configurations.txt

The configurations.txt file contains all keys that should not be pushed to GitHub. These keys include API keys, secret keys, or any extra information.

The format of the file should be:
```text
[API Keys]
some_api_key=abcDEFghiJKL
```

To access these keys, import ConfigParser and pull the values:
```python
import ConfigParser
config = ConfigParser.ConfigParser()
config.readfp(open(r'./configurations.txt'))
api_key = config.get('API Keys', 'some_api_key')
```


## File: requirements.txt

The requirements.txt file contains all the dependencies and their versions. To save the dependency versions needed, you can output your versions into this file:
```shell
pip freeze > requirements.txt
```
