
from flask import jsonify, request

from swagger_client_L3S import l3s_swagger_client as l3SClient
from swagger_client_L3S import l3s_search_swagger_client as l3SSearchClient
import dataclasses, json
from pprint import pprint
from swagger_client_L3S.l3s_swagger_client.rest import ApiException
import os






def testUP():

    configuration = l3SClient.Configuration()
    configuration.host = os.getenv('L3S_GATEWAY')
    api_client = l3SClient.ApiClient(configuration=configuration)
    api_instance_up = l3SClient.UpstreamApi(api_client=api_client)

    configuration = l3SSearchClient.Configuration()
    configuration.host = os.getenv('L3S_GATEWAY')
    api_client = l3SSearchClient.ApiClient(configuration=configuration)
    
    try:
    # Get list of exposure types
        print(api_instance_up.api_client.configuration.host)
        api_response = api_instance_up.get_test_upstream()
        print(api_response)
        pprint(api_response)
        
        return api_response
       
    except ApiException as e:
       
        return ("Exception when calling Api-> %s\n" % e)




def testDown():

    configuration = l3SClient.Configuration()
    configuration.host = os.getenv('L3S_GATEWAY')
    api_client = l3SClient.ApiClient(configuration=configuration)
    
    api_instance_down = l3SClient.DownstreamApi(api_client=api_client)
    
    try:
    # Get list of exposure types
        print(api_instance_down.api_client.configuration.host)
        api_response = api_instance_down.get_test_upstream()
        print(api_response)
        pprint(api_response)
        
        return api_response
       
    except ApiException as e:
       
        return ("Exception when calling Api-> %s\n" % e)



    
