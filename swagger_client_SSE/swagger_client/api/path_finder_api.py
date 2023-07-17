# coding: utf-8

"""
    Skill Repository

    The API description of the Skill Repository.  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class PathFinderApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def path_finder_controller_all_skills_done(self, repo_id, **kwargs):  # noqa: E501
        """path_finder_controller_all_skills_done  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.path_finder_controller_all_skills_done(repo_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str repo_id: (required)
        :return: list[object]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.path_finder_controller_all_skills_done_with_http_info(repo_id, **kwargs)  # noqa: E501
        else:
            (data) = self.path_finder_controller_all_skills_done_with_http_info(repo_id, **kwargs)  # noqa: E501
            return data

    def path_finder_controller_all_skills_done_with_http_info(self, repo_id, **kwargs):  # noqa: E501
        """path_finder_controller_all_skills_done  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.path_finder_controller_all_skills_done_with_http_info(repo_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str repo_id: (required)
        :return: list[object]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['repo_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method path_finder_controller_all_skills_done" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'repo_id' is set
        if ('repo_id' not in params or
                params['repo_id'] is None):
            raise ValueError("Missing the required parameter `repo_id` when calling `path_finder_controller_all_skills_done`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'repo_id' in params:
            path_params['repoId'] = params['repo_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/PathFinder/allSkillsDone/{repoId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[object]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def path_finder_controller_check_graph(self, skill_id, **kwargs):  # noqa: E501
        """path_finder_controller_check_graph  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.path_finder_controller_check_graph(skill_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str skill_id: (required)
        :return: CheckGraphDto
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.path_finder_controller_check_graph_with_http_info(skill_id, **kwargs)  # noqa: E501
        else:
            (data) = self.path_finder_controller_check_graph_with_http_info(skill_id, **kwargs)  # noqa: E501
            return data

    def path_finder_controller_check_graph_with_http_info(self, skill_id, **kwargs):  # noqa: E501
        """path_finder_controller_check_graph  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.path_finder_controller_check_graph_with_http_info(skill_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str skill_id: (required)
        :return: CheckGraphDto
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['skill_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method path_finder_controller_check_graph" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'skill_id' is set
        if ('skill_id' not in params or
                params['skill_id'] is None):
            raise ValueError("Missing the required parameter `skill_id` when calling `path_finder_controller_check_graph`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'skill_id' in params:
            path_params['skillId'] = params['skill_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/PathFinder/checkGraph/{skillId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CheckGraphDto',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def path_finder_controller_get_connected_graph_for_skill(self, skill_id, **kwargs):  # noqa: E501
        """path_finder_controller_get_connected_graph_for_skill  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.path_finder_controller_get_connected_graph_for_skill(skill_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str skill_id: (required)
        :return: GraphDto
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.path_finder_controller_get_connected_graph_for_skill_with_http_info(skill_id, **kwargs)  # noqa: E501
        else:
            (data) = self.path_finder_controller_get_connected_graph_for_skill_with_http_info(skill_id, **kwargs)  # noqa: E501
            return data

    def path_finder_controller_get_connected_graph_for_skill_with_http_info(self, skill_id, **kwargs):  # noqa: E501
        """path_finder_controller_get_connected_graph_for_skill  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.path_finder_controller_get_connected_graph_for_skill_with_http_info(skill_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str skill_id: (required)
        :return: GraphDto
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['skill_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method path_finder_controller_get_connected_graph_for_skill" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'skill_id' is set
        if ('skill_id' not in params or
                params['skill_id'] is None):
            raise ValueError("Missing the required parameter `skill_id` when calling `path_finder_controller_get_connected_graph_for_skill`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'skill_id' in params:
            path_params['skillId'] = params['skill_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/PathFinder/getConnectedGraphForSkill/{skillId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='GraphDto',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def path_finder_controller_get_connected_graph_for_skillwith_resolved_elements(self, skill_id, **kwargs):  # noqa: E501
        """path_finder_controller_get_connected_graph_for_skillwith_resolved_elements  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.path_finder_controller_get_connected_graph_for_skillwith_resolved_elements(skill_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str skill_id: (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.path_finder_controller_get_connected_graph_for_skillwith_resolved_elements_with_http_info(skill_id, **kwargs)  # noqa: E501
        else:
            (data) = self.path_finder_controller_get_connected_graph_for_skillwith_resolved_elements_with_http_info(skill_id, **kwargs)  # noqa: E501
            return data

    def path_finder_controller_get_connected_graph_for_skillwith_resolved_elements_with_http_info(self, skill_id, **kwargs):  # noqa: E501
        """path_finder_controller_get_connected_graph_for_skillwith_resolved_elements  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.path_finder_controller_get_connected_graph_for_skillwith_resolved_elements_with_http_info(skill_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str skill_id: (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['skill_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method path_finder_controller_get_connected_graph_for_skillwith_resolved_elements" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'skill_id' is set
        if ('skill_id' not in params or
                params['skill_id'] is None):
            raise ValueError("Missing the required parameter `skill_id` when calling `path_finder_controller_get_connected_graph_for_skillwith_resolved_elements`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'skill_id' in params:
            path_params['skillId'] = params['skill_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/PathFinder/getConnectedGraphForSkillwithResolvedElements/{skillId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='object',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def path_finder_controller_get_connected_skill_graph_for_skill(self, skill_id, **kwargs):  # noqa: E501
        """path_finder_controller_get_connected_skill_graph_for_skill  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.path_finder_controller_get_connected_skill_graph_for_skill(skill_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str skill_id: (required)
        :return: GraphDto
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.path_finder_controller_get_connected_skill_graph_for_skill_with_http_info(skill_id, **kwargs)  # noqa: E501
        else:
            (data) = self.path_finder_controller_get_connected_skill_graph_for_skill_with_http_info(skill_id, **kwargs)  # noqa: E501
            return data

    def path_finder_controller_get_connected_skill_graph_for_skill_with_http_info(self, skill_id, **kwargs):  # noqa: E501
        """path_finder_controller_get_connected_skill_graph_for_skill  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.path_finder_controller_get_connected_skill_graph_for_skill_with_http_info(skill_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str skill_id: (required)
        :return: GraphDto
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['skill_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method path_finder_controller_get_connected_skill_graph_for_skill" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'skill_id' is set
        if ('skill_id' not in params or
                params['skill_id'] is None):
            raise ValueError("Missing the required parameter `skill_id` when calling `path_finder_controller_get_connected_skill_graph_for_skill`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'skill_id' in params:
            path_params['skillId'] = params['skill_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/PathFinder/getConnectedSkillGraphForSkill/{skillId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='GraphDto',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def path_finder_controller_get_path_to_skill(self, **kwargs):  # noqa: E501
        """path_finder_controller_get_path_to_skill  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.path_finder_controller_get_path_to_skill(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: PathDto
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.path_finder_controller_get_path_to_skill_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.path_finder_controller_get_path_to_skill_with_http_info(**kwargs)  # noqa: E501
            return data

    def path_finder_controller_get_path_to_skill_with_http_info(self, **kwargs):  # noqa: E501
        """path_finder_controller_get_path_to_skill  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.path_finder_controller_get_path_to_skill_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: PathDto
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method path_finder_controller_get_path_to_skill" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/PathFinder/getPathforJava', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PathDto',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)