
from flask import jsonify, request

from swagger_client_SSE import swagger_client as sseClient
import dataclasses
import json
from swagger_client_SSE.swagger_client.models.skill_dto import SkillDto
from pprint import pprint
from swagger_client_SSE.swagger_client.models.skill_repository_dto import SkillRepositoryDto
from swagger_client_SSE.swagger_client.rest import ApiException

configuration = sseClient.Configuration()
configuration.host = 'https://staging.sse.uni-hildesheim.de:9011'
api_client = sseClient.ApiClient(configuration=configuration)
api_instance = sseClient.SkillApi(api_client=api_client)
lu_api_instance = sseClient.LearningUnitApi(api_client=api_client)


def getRepositoryByOwner(ownerId):

    try:
        # Get list of exposure types
        print(api_instance.api_client.configuration.host)
        api_response = api_instance.skill_mgmt_controller_get_skill('1')
        print(str(api_response))
        d = SkillDto(id=api_response.id, nested_skills=api_response.nested_skills,
                     name=api_response.name, level=api_response.level, description=api_response.description)
        print(d.nested_skills)
        response = jsonify(d.to_dict())
        response.status_code = 200  # or 400 or whatever

        print(response)
        return response

    except ApiException as e:

        return ("Exception when calling Api-> %s\n" % e)


def getRepository(id):

    try:
        # Get list of exposure types
        print(api_instance.api_client.configuration.host)
        api_response = api_instance.skill_mgmt_controller_get_skill('id')
        print(str(api_response))
        d = SkillDto(id=api_response.id, nested_skills=api_response.nested_skills,
                     name=api_response.name, level=api_response.level, description=api_response.description)
        print(d.nested_skills)
        response = jsonify(d.to_dict())
        response.status_code = 200  # or 400 or whatever

        print(response)
        return response

    except ApiException as e:

        return ("Exception when calling Api-> %s\n" % e)


def createRepository():


    repo_req_json = request.get_json()
    print (repo_req_json)
    try:
        # Get list of exposure types
        api_response = api_instance.skill_mgmt_controller_create_repository(repo_req_json)
        print(str(api_response))
        d = SkillRepositoryDto(owner=api_response.owner, id=api_response.id,
                     taxonomy=api_response.taxonomy, description=api_response.description, name=api_response.name, version=api_response.version)
        
        response = jsonify(d.to_dict())
        response.status_code = 200  # or 400 or whatever

        print(response)
        return response

    except ApiException as e:

        return ("Exception when calling Api-> %s\n" % e)


def createSkill(id):

    try:
        # Get list of exposure types
        print(api_instance.api_client.configuration.host)
        api_response = api_instance.skill_mgmt_controller_get_skill('1')
        print(str(api_response))
        d = SkillDto(id=api_response.id, nested_skills=api_response.nested_skills,
                     name=api_response.name, level=api_response.level, description=api_response.description)
        print(d.nested_skills)
        response = jsonify(d.to_dict())
        response.status_code = 200  # or 400 or whatever

        print(response)
        return response

    except ApiException as e:

        return ("Exception when calling Api-> %s\n" % e)


def findSkill(id):

    try:
        # Get list of exposure types
        print(api_instance.api_client.configuration.host)
        api_response = api_instance.skill_mgmt_controller_get_skill(id)
        print(str(api_response))
        d = SkillDto(id=api_response.id, nested_skills=api_response.nested_skills,
                     name=api_response.name, level=api_response.level, description=api_response.description)
        print(d.nested_skills)
        response = jsonify(d.to_dict())
        response.status_code = 200  # or 400 or whatever

        print(response)
        return response

    except ApiException as e:

        return ("Exception when calling Api-> %s\n" % e)


def getSkill(id):

    try:
        # Get list of exposure types
        print(api_instance.api_client.configuration.host)
        api_response = api_instance.skill_mgmt_controller_get_skill('1')
        print(str(api_response))
        d = SkillDto(id=api_response.id, nested_skills=api_response.nested_skills,
                     name=api_response.name, level=api_response.level, description=api_response.description)
        print(d.nested_skills)
        response = jsonify(d.to_dict())
        response.status_code = 200  # or 400 or whatever

        print(response)
        return response

    except ApiException as e:

        return ("Exception when calling Api-> %s\n" % e)

def delSkill(id):

    try:
        # Get list of exposure types
        print(api_instance.api_client.configuration.host)
        api_response = api_instance.skill_mgmt_controller_get_skill('1')
        print(str(api_response))
        d = SkillDto(id=api_response.id, nested_skills=api_response.nested_skills,
                     name=api_response.name, level=api_response.level, description=api_response.description)
        print(d.nested_skills)
        response = jsonify(d.to_dict())
        response.status_code = 200  # or 400 or whatever

        print(response)
        return response

    except ApiException as e:

        return ("Exception when calling Api-> %s\n" % e)



def getAllLU():

    try:
        api_response = lu_api_instance.search_learning_unit_controller_list_learning_units()

        response = jsonify(api_response.to_dict())
        response.status_code = 200  # or 400 or whatever

        print(response)
        return response

    except ApiException as e:

        return ("Exception when calling Api-> %s\n" % e)
