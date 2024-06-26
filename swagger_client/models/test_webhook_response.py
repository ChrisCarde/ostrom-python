# coding: utf-8

"""
    Ostrom API

    The Ostrom API is designed to allow our customer and partners to develop apps that integrates with our smart energy management platform. The API has a RESTful architecture and utilizes OAuth2 authorization.   # noqa: E501

    OpenAPI spec version: 2023-11-01T00:00:00.000Z
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class TestWebhookResponse(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'id': 'object',
        'client_application_id': 'object',
        'url': 'object'
    }

    attribute_map = {
        'id': 'id',
        'client_application_id': 'clientApplicationId',
        'url': 'url'
    }

    def __init__(self, id=None, client_application_id=None, url=None):  # noqa: E501
        """TestWebhookResponse - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._client_application_id = None
        self._url = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if client_application_id is not None:
            self.client_application_id = client_application_id
        if url is not None:
            self.url = url

    @property
    def id(self):
        """Gets the id of this TestWebhookResponse.  # noqa: E501

        The id of the webhook  # noqa: E501

        :return: The id of this TestWebhookResponse.  # noqa: E501
        :rtype: object
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this TestWebhookResponse.

        The id of the webhook  # noqa: E501

        :param id: The id of this TestWebhookResponse.  # noqa: E501
        :type: object
        """

        self._id = id

    @property
    def client_application_id(self):
        """Gets the client_application_id of this TestWebhookResponse.  # noqa: E501

        The id of the partner's client application that owns the webhook  # noqa: E501

        :return: The client_application_id of this TestWebhookResponse.  # noqa: E501
        :rtype: object
        """
        return self._client_application_id

    @client_application_id.setter
    def client_application_id(self, client_application_id):
        """Sets the client_application_id of this TestWebhookResponse.

        The id of the partner's client application that owns the webhook  # noqa: E501

        :param client_application_id: The client_application_id of this TestWebhookResponse.  # noqa: E501
        :type: object
        """

        self._client_application_id = client_application_id

    @property
    def url(self):
        """Gets the url of this TestWebhookResponse.  # noqa: E501

        The url where the webhook events will be sent  # noqa: E501

        :return: The url of this TestWebhookResponse.  # noqa: E501
        :rtype: object
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this TestWebhookResponse.

        The url where the webhook events will be sent  # noqa: E501

        :param url: The url of this TestWebhookResponse.  # noqa: E501
        :type: object
        """

        self._url = url

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(TestWebhookResponse, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, TestWebhookResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
