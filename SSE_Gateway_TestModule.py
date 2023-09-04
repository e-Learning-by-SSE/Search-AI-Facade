import unittest
import xmlrunner  # Import the xmlrunner module
from app import app  # Import your Flask app instance
from flask.testing import FlaskClient
from unittest.mock import MagicMock, patch
from swagger_client_SSE import swagger_client as sseClient
import shutil
import os
from flask import Flask, current_app
from flask import jsonify, request
import json
from sse_gateway import (
    getRepositoryByOwner,
    getRepository,
    createRepository,
    adaptRepository,
    deleteRepository,
    createSkill,
    findSkill,
    getSkill,
    delSkill,
    createQualification,
    getAllLU
)
from swagger_client_SSE.swagger_client.models.skill_creation_dto import SkillCreationDto
from swagger_client_SSE.swagger_client.models.skill_dto import SkillDto
from swagger_client_SSE.swagger_client.models.skill_repository_creation_dto import SkillRepositoryCreationDto


class SSE_Gateway_TestModule(unittest.TestCase):

    def setUp(self):

        self.app = app
        with self.app.app_context():
            # within this block, current_app points to app.

            print(self.app.name)

        self.client = self.app.test_client()
        self.app_context = self.app.app_context()
        self.app_context.push()

        self.configuration = sseClient.Configuration()
        self.configuration.host = os.getenv(
            'SSE_SKILL_SERVICE', 'https://staging.sse.uni-hildesheim.de:9011')
        self.api_client = sseClient.ApiClient(configuration=self.configuration)
        self.api_instance = sseClient.SkillApi(api_client=self.api_client)

    def tearDown(self):
        self.app_context.pop()

    @patch('sse_gateway.api_instance.skill_mgmt_controller_list_repositories')
    def test_get_repository_by_owner(self, mock_list_repositories):
        mock_response = MagicMock()
        mock_response.repositories = ["repo1", "repo2"]
        mock_list_repositories.return_value = mock_response

        result = getRepositoryByOwner(ownerId=123)

        self.assertEqual(result.status_code, 200)

        # Define the expected JSON data
        expected_data = {"repositories": ["repo1", "repo2"]}
        self.assertDictEqual(result.json, expected_data)

    @patch('sse_gateway.api_instance.skill_mgmt_controller_load_repository')
    def test_get_repository(self, mock_load_repository):
        mock_response = MagicMock()
        mock_response.owner = "owner_value"
        mock_response.id = 123
        mock_response.taxonomy = "taxonomy_value"
        mock_response.description = "description_value"
        mock_response.name = "name_value"
        mock_response.version = "version_value"
        mock_response.skills = ["skill1", "skill2"]
        mock_load_repository.return_value = mock_response

        result = getRepository(id=1)

        self.assertEqual(result.status_code, 200)
        expected_data = {
            "owner": "owner_value",
            "id": 123,
            "taxonomy": "taxonomy_value",
            'access_rights': None,
            "description": "description_value",
            "name": "name_value",
            "version": "version_value",
            "skills": ["skill1", "skill2"]
        }
        self.assertDictEqual(result.json, expected_data)

    @patch('sse_gateway.api_instance.skill_mgmt_controller_add_skill')
    def test_create_skill(self, skill_data):
        print('test_create_skill')

        # Define a mock response for the add_skill call

        # Configure the mock to return the mock_response when add_skill is called

        # Define the skill data to be passed to createSkill
        skill_data: SkillCreationDto = {
            "owner": "1",
            "name": "11t22311111",
            "level": 0,
            "description": "stzering",
            "nestedSkills": [
            ]
        }

        # Call the createSkill function with the skill data
       
        api_response : SkillDto = self.api_instance.skill_mgmt_controller_add_skill(
            skill_data, '1')
       
        print(api_response)
        # Assert that the function returns a JSON response with the expected data
      
        expected_data = {
            "name": "11t22311111",
            "level": 0,
            "description": "stzering",
            "nestedSkills": [],
            "repositoryId": "1"
        }
        
        print(expected_data)
        self.assertEqual(api_response.name,expected_data['name'] )
        self.assertEqual(api_response.level, expected_data['level'])


def pre_process(output_directory):
    # Check whether the specified path exists or not
    isExist = os.path.exists(output_directory)
    if not isExist:
       # Create a new directory because it does not exist
        os.makedirs(output_directory)
    print("The new directory is created!")


def post_process(output_directory):
    directory_path = output_directory
    files = os.listdir(directory_path)
    # Check if there is exactly one file in the directory
    if len(files) == 1:

        file_name = files[0]
        os.rename(output_directory+file_name, output_directory+"new_file.xml")

        shutil.copy2(output_directory+"new_file.xml", './test.xml')
        try:
            shutil.rmtree(output_directory)
        except:
            print('Folder not deleted')
    else:
        print("There is not exactly one file in the directory.")


if __name__ == '__main__':
    print('main')
    output_directory = './test/'
    pre_process(output_directory)
    # Create a test suite with your test class
    test_suite = unittest.TestLoader().loadTestsFromTestCase(SSE_Gateway_TestModule)

    xmlrunner.XMLTestRunner(output=output_directory,
                            verbosity=2).run(test_suite)
    post_process(output_directory)
