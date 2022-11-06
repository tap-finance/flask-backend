from flask import Flask
import requests
from dune_query_utils import execute_query, get_query_status, get_query_results, query_request_start

app = Flask(__name__)

@app.route("/sudoswap_analytics_24hr", methods= ['GET'])
def sudoswap_volume():
    query_id = '1531117'
    
    data = query_request_start(query_id)    

    return data.content
        
@app.route("/sudoswap_analytics_tvl", methods= ['GET'])
def sudoswap_tvl():
    query_id = '1532688'
    
    data = query_request_start(query_id)  

    return data.content
        
