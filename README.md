# flask-backend
Dune + TheGraph query implementation via Flask.
cd into repo and pip3 install -r requirements.txt

# Environment Variables
Before running, create .env file with Dune API Key as:


``DUNE_API_KEY="Your Key"``

# Build 

Install Gunicorn and run 


``gunicorn -w 4 dune_api:app``

