import graphql_queries
import requests
import json

def getLensProfileData(address):
    data = {
        'query':graphql_queries.LensProfileDataQuery,
        'variables': {
            'address':address
        }
    }
    response = requests.post(graphql_queries.LensAPIURL,json=data)
    return json.loads(response.content)['data']
