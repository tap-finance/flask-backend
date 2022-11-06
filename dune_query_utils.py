from dotenv import load_dotenv
import requests
import os
import time
import json

load_dotenv()

API_KEY = os.getenv("DUNE_API_KEY") 
HEADER = {"x-dune-api-key" : API_KEY}

BASE_URL = "https://api.dune.com/api/v1/"

def make_api_url(module, action, ID):

    url = BASE_URL + module + "/" + ID + "/" + action

    return url

def execute_query_with_params(query_id, param_dict):
    """
    Takes in the query ID. And a dictionary containing parameter values.
    Calls the API to execute the query.
    Returns the execution ID of the instance which is executing the query.
    """

    url = make_api_url("query", "execute", query_id)
    response = requests.post(url, headers=HEADER, json={"query_parameters" : param_dict})
    execution_id = response.json()['execution_id']

    return execution_id

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

def get_query_status(execution_id):
    """
    Takes in an execution ID.
    Fetches the status of query execution using the API
    Returns the status response object
    """

    url = make_api_url("execution", "status", execution_id)
    response = requests.get(url, headers=HEADER)

    return json.loads(response.content)['state']


def get_query_results(execution_id):
    """
    Takes in an execution ID.
    Fetches the results returned from the query using the API
    Returns the results response object
    """

    url = make_api_url("execution", "results", execution_id)
    response = requests.get(url, headers=HEADER)

    return response

def query_request_start(query_id,param_dict):
    execution_id = execute_query_with_params(query_id,param_dict)
    
    execution_status = get_query_status(execution_id)

    while(execution_status != 'QUERY_STATE_COMPLETED'):
        time.sleep(0.1)
        execution_status = get_query_status(execution_id)
    
    data = get_query_results(execution_id)

    return data