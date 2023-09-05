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
from swagger_client_SSE.swagger_client.models.skill_repository_dto import SkillRepositoryDto


class SSE_Gateway_TestModule(unittest.TestCase):

    def setUp(self):

        self.app = app
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

    @patch('sse_gateway.getRepositoryByOwner')
    def test_get_repository_by_owner(self, expected_data):

        result = getRepositoryByOwner(ownerId=1)

        self.assertEqual(result.status_code, 200)

        # Define the expected JSON data
        expected_data = {
            "repositories": [
                {
                    "access_rights": "PRIVATE",
                    "description": "Example to demonstrate competence modelling capabilities",
                    "id": "1",
                    "name": "Java OO Repository",
                    "owner": "1",
                    "taxonomy": "Bloom",
                    "version": "v1"
                },
                {
                    "access_rights": "PRIVATE",
                    "description": "Example created by Luisa",
                    "id": "2",
                    "name": "Open DigiMedia",
                    "owner": "1",
                    "taxonomy": "Bloom",
                    "version": "v1"
                },
                {
                    "access_rights": "PRIVATE",
                    "description": "Example created for the MI-Lecture by Dr. Jörg Cassens",
                    "id": "3",
                    "name": "MI Repository",
                    "owner": "1",
                    "taxonomy": "Bloom",
                    "version": "v1"
                }
            ]
        }
        self.assertDictEqual(result.json, expected_data)

    @patch('sse_gateway.getRepository')
    def test_get_repository(self, expected_data):

        result = getRepository(id=2)

        self.assertEqual(result.status_code, 200)
        expected_data = {'access_rights': None,
                         'description': 'Example created by Luisa',
                         'id': '2',
                         'name': 'Open DigiMedia',
                         'owner': '1',
                         'skills': ['2003',
                                    '2002',
                                    '2010',
                                    '2011',
                                    '2012',
                                    '2006',
                                    '2004',
                                    '2007',
                                    '2005',
                                    '2013',
                                    '2008',
                                    '2014',
                                    '2001',
                                    '2009',
                                    '2015',
                                    '2016',
                                    '2021',
                                    '2017',
                                    '2018',
                                    '2019',
                                    '2020',
                                    '2023',
                                    '2022',
                                    '2024',
                                    '2025',
                                    '2026',
                                    '2027',
                                    '2028',
                                    '2029',
                                    '2031',
                                    '2033',
                                    '2032',
                                    '2030',
                                    '2034',
                                    '2035',
                                    '2036',
                                    '2038',
                                    '2040',
                                    '2039',
                                    '2041',
                                    '2042',
                                    '2037',
                                    '2043',
                                    '2044',
                                    '2046',
                                    '2045',
                                    '2049',
                                    '2047',
                                    '2048',
                                    '2055',
                                    '2063',
                                    '2072',
                                    '2077',
                                    '2088',
                                    '2096',
                                    '2099',
                                    '2108',
                                    '2114',
                                    '2135',
                                    '2139',
                                    '2147',
                                    '2154',
                                    '2163',
                                    '2169',
                                    '2180',
                                    '2191',
                                    '2199',
                                    '2050',
                                    '2057',
                                    '2066',
                                    '2073',
                                    '2082',
                                    '2091',
                                    '2101',
                                    '2116',
                                    '2121',
                                    '2123',
                                    '2126',
                                    '2136',
                                    '2140',
                                    '2151',
                                    '2160',
                                    '2173',
                                    '2181',
                                    '2189',
                                    '2198',
                                    '2051',
                                    '2059',
                                    '2067',
                                    '2080',
                                    '2094',
                                    '2103',
                                    '2111',
                                    '2120',
                                    '2124',
                                    '2129',
                                    '2138',
                                    '2146',
                                    '2162',
                                    '2167',
                                    '2175',
                                    '2184',
                                    '2200',
                                    '2501',
                                    '2502',
                                    '2503',
                                    '2504',
                                    '2505',
                                    '2506',
                                    '2507',
                                    '2508',
                                    '2509',
                                    '2510',
                                    '2511',
                                    '2512',
                                    '2052',
                                    '2060',
                                    '2065',
                                    '2076',
                                    '2084',
                                    '2090',
                                    '2097',
                                    '2107',
                                    '2115',
                                    '2117',
                                    '2118',
                                    '2125',
                                    '2130',
                                    '2133',
                                    '2144',
                                    '2155',
                                    '2159',
                                    '2166',
                                    '2176',
                                    '2188',
                                    '2193',
                                    '2201',
                                    '2053',
                                    '2062',
                                    '2071',
                                    '2078',
                                    '2087',
                                    '2098',
                                    '2106',
                                    '2131',
                                    '2141',
                                    '2148',
                                    '2158',
                                    '2170',
                                    '2174',
                                    '2185',
                                    '2194',
                                    '2056',
                                    '2064',
                                    '2074',
                                    '2085',
                                    '2092',
                                    '2102',
                                    '2109',
                                    '2128',
                                    '2143',
                                    '2152',
                                    '2157',
                                    '2165',
                                    '2171',
                                    '2182',
                                    '2190',
                                    '2196',
                                    '2054',
                                    '2070',
                                    '2079',
                                    '2083',
                                    '2095',
                                    '2105',
                                    '2113',
                                    '2119',
                                    '2122',
                                    '2127',
                                    '2137',
                                    '2149',
                                    '2164',
                                    '2178',
                                    '2183',
                                    '2192',
                                    '2058',
                                    '2069',
                                    '2081',
                                    '2093',
                                    '2104',
                                    '2110',
                                    '2132',
                                    '2145',
                                    '2153',
                                    '2161',
                                    '2168',
                                    '2177',
                                    '2186',
                                    '2197',
                                    '2061',
                                    '2068',
                                    '2075',
                                    '2086',
                                    '2089',
                                    '2100',
                                    '2112',
                                    '2134',
                                    '2142',
                                    '2150',
                                    '2156',
                                    '2172',
                                    '2179',
                                    '2187',
                                    '2195',
                                    '2202'],
                         'taxonomy': 'Bloom',
                         'version': 'v1'}
      
        self.assertEqual(result.json.owner, expected_data['owner'])

    @patch('sse_gateway.api_instance.skill_mgmt_controller_add_skill')
    def test_create_skill(self, skill_data):

        # Define the skill data to be passed to skill_mgmt_controller_add_skill
        skill_data: SkillCreationDto = {
            "owner": "1",
            "name": "1121222133t13",
            "level": 0,
            "description": "stzering",
            "nestedSkills": [
            ]
        }

        api_response: SkillDto = self.api_instance.skill_mgmt_controller_add_skill(
            skill_data, '1')

        expected_data = {
            "name": "121222133t13",
            "level": 0,
            "description": "stzering",
            "nestedSkills": [],
            "repositoryId": "1"
        }
        self.assertEqual(api_response.name, expected_data['name'])
        self.assertEqual(api_response.level, expected_data['level'])

    @patch('sse_gateway.api_instance.skill_mgmt_controller_create_repository')
    def test_create_Repository(self, repo_data):

        # Define the skill data to be passed to skill_mgmt_controller_create_repository
        repo_data: SkillRepositoryCreationDto = {

            "description": "testRepo",
            "name": "IntegrationsTestRepo",
            "ownerId": "10",
            "version": "1"
        }

        api_response: SkillRepositoryDto = self.api_instance.skill_mgmt_controller_create_repository(
            repo_data)

        expected_data = {
            "access_rights": 'null',
            "description": "testRepo",
            "id": "???",
            "name": "IntegrationsTestRepo",
            "owner": "10",
            "taxonomy": "Bloom",
            "version": "1"
        }
        self.assertEqual(api_response.name, expected_data['name'])
        self.assertEqual(api_response.description, expected_data['description'])
        self.assertEqual(api_response.version, expected_data['version'])
        self.assertEqual(api_response.owner, expected_data['owner'])


def pre_process(output_directory):
    # Check whether the specified path exists or not
    isExist = os.path.exists(output_directory)
    if not isExist:
       # Create a new directory because it does not exist
        os.makedirs(output_directory)


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
    output_directory = './test/'
    pre_process(output_directory)
    test_suite = unittest.TestLoader().loadTestsFromTestCase(SSE_Gateway_TestModule)

    xmlrunner.XMLTestRunner(output=output_directory,
                            verbosity=2).run(test_suite)
    post_process(output_directory)
