import unittest
from app import app  # Import your Flask app instance
from flask.testing import FlaskClient
from unittest.mock import MagicMock, patch
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


if __name__ == '__main__':
    
    unittest.main()
