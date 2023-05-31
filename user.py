from models.UserRepo import UserRepo
from schemas.schemas import UserSchema
from flask import request
import time
from swagger_client_SSE import swagger_client as sseClient
from swagger_client_L3S import swagger_client_1 as l3SClient
import json
from swagger_client_SSE.swagger_client.rest import ApiException

userRepo = UserRepo()
userSchema = UserSchema()
userListSchema = UserSchema(many=True)
USER_NOT_FOUND = "User not found for id: {}"


def get(id):

    configuration = sseClient.Configuration()
    configuration.host = 'https://staging.sse.uni-hildesheim.de:9010'
    api_client = sseClient.ApiClient(configuration=configuration)
    api_instance = sseClient.SkillApi(api_client=api_client)
    try:
    # Get list of exposure types
        print(api_instance.api_client.configuration.host)
        api_response = api_instance.skill_mgmt_controller_get_skill('1')
        print(api_response)
       
        return api_response
    except ApiException as e:
       
        return ("Exception when calling Api-> %s\n" % e)
    
def update(id):
    user_data = userRepo.fetchById(id)
    user_req_json = request.get_json()
    if user_data:
        user_data.name = user_req_json['name']
        userRepo.update(user_data)
        return userSchema.dump(user_data)
    return {'message': USER_NOT_FOUND.format(id)}, 404

def delete(id):
    user_data = userRepo.fetchById(id)
    if user_data:
        userRepo.delete(id)
        return {'message': 'Item deleted successfully'}, 200
    return {'message': USER_NOT_FOUND.format(id)}, 404

def create():
    user_req_json = request.get_json()
    user_data = userSchema.load(user_req_json)
    userRepo.create(user_data)
    return userSchema.dump(user_data),201

def getAll():
    configuration = l3SClient.Configuration()
    configuration.host = 'https://staging.sse.uni-hildesheim.de:9040'
    api_client = l3SClient.ApiClient(configuration=configuration)
    api_instance = l3SClient.UpstreamApi(api_client=api_client)
    try:
    # Get list of exposure types
        print(api_instance.api_client.configuration.host)
        api_response = api_instance.get_test_upstream()
       
       
        return api_response
    except ApiException as e:
       
        return ("Exception when calling Api-> %s\n" % e)
    
    
    