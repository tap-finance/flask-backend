from dotenv import load_dotenv
from flask import Flask
import requests
from markupsafe import escape
import time
import os

load_dotenv()
app = Flask(__name__)

API_KEY = os.getenv("DUNE_API_KEY") 
HEADER = {"x-dune-api-key" : API_KEY}

BASE_URL = "https://api.dune.com/api/v1/"

def make_api_url(module, action, ID):

    url = BASE_URL + module + "/" + ID + "/" + action

    return url

def execute_query(query_id):
    """
    Takes in the query ID.
    Calls the API to execute the query.
    Returns the execution ID of the instance which is executing the query.
    """

    url = make_api_url("query", "execute", query_id)
    response = requests.post(url, headers=HEADER)
    execution_id = response.json()['execution_id']

    return execution_id

def get_query_results(execution_id):
    """
    Takes in an execution ID.
    Fetches the results returned from the query using the API
    Returns the results response object
    """

    url = make_api_url("execution", "results", execution_id)
    response = requests.get(url, headers=HEADER)

    return response

@app.route("/sudoswap_analytics", methods= ['GET'])
def sudoswap_volume():
    query_id = '1531117'
    
    execution_id = execute_query(query_id)
    
    # mucho cuidado
    time.sleep(2)
    
    data = get_query_results(execution_id)

    print(data.content)
    return data.content
        
@app.route("/sudoswap_tvl", methods= ['GET'])
def sudoswap_tvl():
    query_id = '1531350'
    
    execution_id = execute_query(query_id)
    
    # mucho cuidado
    time.sleep(2)
    
    data = get_query_results(execution_id)

    print(data.content)
    return data.content
        
