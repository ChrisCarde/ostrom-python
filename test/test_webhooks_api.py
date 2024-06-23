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
from swagger_client.api.webhooks_api import WebhooksApi  # noqa: E501
from swagger_client.rest import ApiException


class TestWebhooksApi(unittest.TestCase):
    """WebhooksApi unit test stubs"""

    def setUp(self):
        self.api = WebhooksApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_webhook(self):
        """Test case for create_webhook

        Create a new webhook  # noqa: E501
        """
        pass

    def test_delete_webhook(self):
        """Test case for delete_webhook

        Delete a webhook  # noqa: E501
        """
        pass

    def test_get_webhook(self):
        """Test case for get_webhook

        Retrieve a webhook  # noqa: E501
        """
        pass

    def test_get_webhooks(self):
        """Test case for get_webhooks

        Retrieve all webhooks  # noqa: E501
        """
        pass

    def test_test_webhook(self):
        """Test case for test_webhook

        Test a webhook  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()