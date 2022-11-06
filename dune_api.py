from flask import Flask
import graphql_requests
import requests
from dune_query_utils import execute_query, get_query_status, get_query_results, query_request_start
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route("/sudoswap_analytics_24hr/<limit>", methods= ['GET'])
@cross_origin()
def sudoswap_volume(limit):
    query_id = '1531117'

    param_dict = {"limit":limit}
    data = query_request_start(query_id,param_dict)  

    return data.content
        
@app.route("/sudoswap_analytics_tvl/<limit>", methods= ['GET'])
@cross_origin()
def sudoswap_tvl(limit):
    query_id = '1532688'

    param_dict = {"limit":limit}
    data = query_request_start(query_id,param_dict)  

    return data.content

@app.route("/lens_profile_data/<address>",methods=['GET'])
@cross_origin()
def lens_profile_data(address):
    return graphql_requests.getLensProfileData(address)
        
