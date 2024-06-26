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
from swagger_client.api.prices_api import PricesApi  # noqa: E501
from swagger_client.rest import ApiException


class TestPricesApi(unittest.TestCase):
    """PricesApi unit test stubs"""

    def setUp(self):
        self.api = PricesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_spot_prices(self):
        """Test case for get_spot_prices

        Retrieve day-ahead spot price information  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
