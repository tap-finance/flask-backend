# flask-backend
Dune + TheGraph query implementation via Flask
# Environment Variables
Before running, create .env file with Dune API Key as:


``DUNE_API_KEY="Your Key"``

# Build 

Install Gunicorn and run 


``gunicorn -w 4 dune_api:app``

