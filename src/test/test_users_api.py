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
from swagger_client.api.users_api import UsersApi  # noqa: E501
from swagger_client.rest import ApiException


class TestUsersApi(unittest.TestCase):
    """UsersApi unit test stubs"""

    def setUp(self):
        self.api = UsersApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_disconnect_user(self):
        """Test case for disconnect_user

        Disconnect user from partner client application  # noqa: E501
        """
        pass

    def test_get_me(self):
        """Test case for get_me

        Retrieve user information  # noqa: E501
        """
        pass

    def test_link_user(self):
        """Test case for link_user

        Link user to a partner client application  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()