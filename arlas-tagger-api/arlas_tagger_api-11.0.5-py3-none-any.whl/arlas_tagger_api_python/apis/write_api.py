# coding: utf-8

"""
    ARLAS Tagger API

    (Un)Tag fields of ARLAS collections

    OpenAPI spec version: 11.0.5
    Contact: contact@gisaia.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import sys
import os
import re

# python 2 and python 3 compatibility library
from six import iteritems

from ..configuration import Configuration
from ..api_client import ApiClient


class WriteApi(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient()
            self.api_client = config.api_client

    def tag_post(self, collection, **kwargs):
        """
        Tag
        Search and tag the elements found in the collection, given the filters
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.tag_post(collection, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str collection: collection (required)
        :param TagRequest body:
        :param bool pretty: Pretty print
        :return: UpdateResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.tag_post_with_http_info(collection, **kwargs)
        else:
            (data) = self.tag_post_with_http_info(collection, **kwargs)
            return data

    def tag_post_with_http_info(self, collection, **kwargs):
        """
        Tag
        Search and tag the elements found in the collection, given the filters
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.tag_post_with_http_info(collection, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str collection: collection (required)
        :param TagRequest body:
        :param bool pretty: Pretty print
        :return: UpdateResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['collection', 'body', 'pretty']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method tag_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'collection' is set
        if ('collection' not in params) or (params['collection'] is None):
            raise ValueError("Missing the required parameter `collection` when calling `tag_post`")


        collection_formats = {}

        path_params = {}
        if 'collection' in params:
            path_params['collection'] = params['collection']

        query_params = []
        if 'pretty' in params:
            query_params.append(('pretty', params['pretty']))

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json;charset=utf-8'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json;charset=utf-8'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api('/write/{collection}/_tag', 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='UpdateResponse',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def untag_post(self, collection, **kwargs):
        """
        Untag
        Search and untag the elements found in the collection, given the filters
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.untag_post(collection, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str collection: collection (required)
        :param TagRequest body:
        :param bool pretty: Pretty print
        :return: UpdateResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.untag_post_with_http_info(collection, **kwargs)
        else:
            (data) = self.untag_post_with_http_info(collection, **kwargs)
            return data

    def untag_post_with_http_info(self, collection, **kwargs):
        """
        Untag
        Search and untag the elements found in the collection, given the filters
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.untag_post_with_http_info(collection, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str collection: collection (required)
        :param TagRequest body:
        :param bool pretty: Pretty print
        :return: UpdateResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['collection', 'body', 'pretty']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method untag_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'collection' is set
        if ('collection' not in params) or (params['collection'] is None):
            raise ValueError("Missing the required parameter `collection` when calling `untag_post`")


        collection_formats = {}

        path_params = {}
        if 'collection' in params:
            path_params['collection'] = params['collection']

        query_params = []
        if 'pretty' in params:
            query_params.append(('pretty', params['pretty']))

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json;charset=utf-8'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json;charset=utf-8'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api('/write/{collection}/_untag', 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='UpdateResponse',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)
