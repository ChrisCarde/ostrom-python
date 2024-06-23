# coding: utf-8

"""
    Ostrom API

    The Ostrom API is designed to allow our customer and partners to develop apps that integrates with our smart energy management platform. The API has a RESTful architecture and utilizes OAuth2 authorization.   # noqa: E501

    OpenAPI spec version: 2023-11-01T00:00:00.000Z
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.auth_api import AuthApi  # noqa: E501
from swagger_client.rest import ApiException


class TestAuthApi(unittest.TestCase):
    """AuthApi unit test stubs"""

    def setUp(self):
        self.api = AuthApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_o_auth2_token(self):
        """Test case for create_o_auth2_token

        Obtain OAuth2 Access Token  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
