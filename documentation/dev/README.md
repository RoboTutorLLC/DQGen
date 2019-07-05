# DQGen Developer Guide
This project has been tested using Python3.7.

To get started, clone the repository and `pip install requirements.txt` from the root directory.

## DQGen Web Service Implementation
The code for DQGen engine is in [/source_code](/source_code), and the code for web service can be found at [/webapp](/webapp) and [/web](/web). The website is written in Django framework. Currently, we are running this web server on localhost, and we can access the website at http://127.0.0.1:8000, but you can feel free to deploy this web service on a public server.

DQGen processes requests at [/source_code/processor.py](/source_code/processor.py) The database will be queried in a fixed time interval and fetch one unprocessed request with the longest waiting time from database, then put the input file, configuration file, and email address of this request to DQGen engine. When DQGen finishes processing the request, the processor will send the generated output file to the specified email address.

The [configuration file](source_code/src/global.properties) contains database login info and the resource file path.

## Running DQGen
1. Set up the connection between localhost and DQGen MySQL server.
    - `ssh -N -L localhost:3307:localhost:3306 username@dqgen.oli.cmu.edu`
    - This command will take the DQGen MySQL server as our local host, and we can connect it in our local host at port number 3307 and 3306. In this way, our DQGen engine can set up a connection to local host and access MySQL database in DQGen MySQL server.

2. Start the DQGen web service.
    - `python3 manage.py runserver`
    - Run this command from the root directory to access the website at http://127.0.0.1:8000

## Notes
If you make any modification to DQGen/web/models.py you should run:
```
python3 manage.py makemigrations
python3 manage.py migrate
```