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

class TooManyRequestError429(object):
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
        'type': 'object',
        'detail': 'object'
    }

    attribute_map = {
        'type': 'type',
        'detail': 'detail'
    }

    def __init__(self, type=None, detail=None):  # noqa: E501
        """TooManyRequestError429 - a model defined in Swagger"""  # noqa: E501
        self._type = None
        self._detail = None
        self.discriminator = None
        if type is not None:
            self.type = type
        if detail is not None:
            self.detail = detail

    @property
    def type(self):
        """Gets the type of this TooManyRequestError429.  # noqa: E501

        The type of the error  # noqa: E501

        :return: The type of this TooManyRequestError429.  # noqa: E501
        :rtype: object
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this TooManyRequestError429.

        The type of the error  # noqa: E501

        :param type: The type of this TooManyRequestError429.  # noqa: E501
        :type: object
        """

        self._type = type

    @property
    def detail(self):
        """Gets the detail of this TooManyRequestError429.  # noqa: E501

        A human-readable message providing more details about the error  # noqa: E501

        :return: The detail of this TooManyRequestError429.  # noqa: E501
        :rtype: object
        """
        return self._detail

    @detail.setter
    def detail(self, detail):
        """Sets the detail of this TooManyRequestError429.

        A human-readable message providing more details about the error  # noqa: E501

        :param detail: The detail of this TooManyRequestError429.  # noqa: E501
        :type: object
        """

        self._detail = detail

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
        if issubclass(TooManyRequestError429, dict):
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
        if not isinstance(other, TooManyRequestError429):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
