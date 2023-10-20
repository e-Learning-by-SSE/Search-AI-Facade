import unittest
import xmlrunner  # Import the xmlrunner module
from app import app  # Import your Flask app instance
from flask.testing import FlaskClient
from unittest.mock import MagicMock, patch
import shutil
import os
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
class SSE_Gateway_TestModule(unittest.TestCase):

    def setUp(self):
        self.app = app
        self.client = self.app.test_client()
        self.app_context = self.app.app_context()
        self.app_context.push()

    def tearDown(self):
        self.app_context.pop()
        # Code to execute after each test
        

    @patch('sse_gateway.api_instance.skill_mgmt_controller_list_repositories')
    def test_get_repository_by_owner(self, mock_list_repositories):
        mock_response = MagicMock()
        mock_response.repositories = ["repo1", "repo2"]
        mock_list_repositories.return_value = mock_response

        result = getRepositoryByOwner(ownerId=123)

        self.assertEqual(result.status_code, 200)
        expected_data = {"repositories": ["repo1", "repo2"]}  # Define the expected JSON data
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

        result = getRepository(id=123)

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

    @patch('sse_gateway.api_instance.skill_mgmt_controller_adapt_repo')
    def test_adapt_repository(self, mock_adapt_repo):
        mock_request_data = {
        "field1": "value1",
        "field2": "value2",
        # Add any other required fields here
    }
        mock_response = MagicMock()
    # Set mock_response attributes to match the expected response
        mock_adapt_repo.return_value = mock_response

        result = adaptRepository()

        self.assertEqual(result.status_code, 200)
    # Check if the response data matches the expected data
        self.assertEqual(result.json, mock_response)

    @patch('sse_gateway.api_instance.skill_mgmt_controller_delete_repo')
    def test_delete_repository(self, mock_delete_repo):
        mock_repository_id = 123  # Replace with a valid repository ID
        mock_response = MagicMock()
        # Set mock_response attributes to match the expected response
        mock_delete_repo.return_value = mock_response

        result = deleteRepository(repositoryId=mock_repository_id)

        self.assertEqual(result.status_code, 200)
        # Check if the response data matches the expected data
        self.assertEqual(result.json, mock_response)

    @patch('sse_gateway.api_instance.skill_mgmt_controller_add_skill')
    def test_create_skill(self, mock_add_skill):
        mock_request_data = {
            "repositoryId": 123,  # Replace with a valid repository ID
            "name": "Skill Name",
            "level": "Intermediate",
            "description": "Skill description",
            # Add any other required fields here
        }
        mock_response = MagicMock()
        # Set mock_response attributes to match the expected response
        mock_add_skill.return_value = mock_response

        result = createSkill(repositoryId=mock_request_data["repositoryId"])

        self.assertEqual(result.status_code, 200)
        # Check if the response data matches the expected data
        self.assertEqual(result.json, mock_response)

    @patch('sse_gateway.api_instance.skill_mgmt_controller_get_skill')
    def test_find_skill(self, mock_get_skill):
        mock_skill_id = 123  # Replace with a valid skill ID
        mock_response = MagicMock()
        # Set mock_response attributes to match the expected response
        mock_get_skill.return_value = mock_response

        result = findSkill(id=mock_skill_id)

        self.assertEqual(result.status_code, 200)
        # Check if the response data matches the expected data
        self.assertEqual(result.json, mock_response)

    @patch('sse_gateway.api_instance.skill_mgmt_controller_get_skill')
    def test_get_skill(self, mock_get_skill):
        mock_skill_id = 123  # Replace with a valid skill ID
        mock_response = MagicMock()
        # Set mock_response attributes to match the expected response
        mock_get_skill.return_value = mock_response

        result = getSkill(id=mock_skill_id)

        self.assertEqual(result.status_code, 200)
        # Check if the response data matches the expected data
        self.assertEqual(result.json, mock_response)

    @patch('sse_gateway.api_instance.skill_mgmt_controller_delte_skill')
    def test_delete_skill(self, mock_delete_skill):
        mock_skill_id = 123  # Replace with a valid skill ID
        mock_response = MagicMock()
        # Set mock_response attributes to match the expected response
        mock_delete_skill.return_value = mock_response

        result = delSkill(id=mock_skill_id)

        self.assertEqual(result.status_code, 200)
        # Check if the response data matches the expected data
        self.assertEqual(result.json, mock_response)

    @patch('sse_gateway.user_api_instance.user_mgmt_controller_add_qualification')
    def test_create_qualification(self, mock_add_qualification):
        mock_request_data = {
            "field1": "value1",
            "field2": "value2",
            # Add any other required fields here
        }
        mock_response = MagicMock()
        # Set mock_response attributes to match the expected response
        mock_add_qualification.return_value = mock_response

        result = createQualification()

        self.assertEqual(result.status_code, 200)
        # Check if the response data matches the expected data
        self.assertEqual(result.json, mock_response)

    @patch('sse_gateway.lu_api_instance.search_learning_unit_controller_list_learning_units')
    def test_get_all_learning_units(self, mock_list_learning_units):
        mock_response = MagicMock()
        # Set mock_response attributes to match the expected response
        mock_list_learning_units.return_value = mock_response

        result = getAllLU()

        self.assertEqual(result.status_code, 200)
        # Check if the response data matches the expected data
        self.assertEqual(result.json, mock_response)


def pre_process(output_directory):
# Check whether the specified path exists or not
    isExist = os.path.exists(output_directory)
    if not isExist:
   # Create a new directory because it does not exist
        os.makedirs(output_directory)
    
    print("The new directory is created!")


def post_process(output_directory):
    print('Print2')
    
    directory_path = output_directory
    files = os.listdir(directory_path)
    
    # Check if there is exactly one file in the directory
    if len(files) == 1:
    # Get the file name (the only element in the list)
        file_name = files[0]
    # Now, 'file_name' contains the name of the file in the directory
        print("Found one file:", file_name)
        print(os.path.isfile(file_name))
        os.rename(output_directory+file_name, output_directory+"new_file.xml")  
        
        shutil.copy2(output_directory+"new_file.xml", './test.xml') # complete target filename given
        try:
           
            shutil.rmtree(output_directory)
            print('Folder and its content removed')
        except:
            print('Folder not deleted')
    else:
        print("There is not exactly one file in the directory.")

if __name__ == '__main__':
    print('main')
    output_directory = './test/' 
    pre_process(output_directory)
    


    print('Print1')
    
    # Create a test suite with your test class
    test_suite = unittest.TestLoader().loadTestsFromTestCase(SSE_Gateway_TestModule)
    
    # Use the custom XMLTestRunner to generate XML reports
    xmlrunner.XMLTestRunner(output=output_directory, verbosity=2).run(test_suite)
    post_process(output_directory)