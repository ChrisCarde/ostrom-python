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

class GetOrdersItemResponse(object):
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
        'type': 'object',
        'product_code': 'object',
        'status': 'object',
        'customer_first_name': 'object',
        'customer_last_name': 'object',
        'address': 'GetOrdersAddressResponse'
    }

    attribute_map = {
        'id': 'id',
        'type': 'type',
        'product_code': 'productCode',
        'status': 'status',
        'customer_first_name': 'customerFirstName',
        'customer_last_name': 'customerLastName',
        'address': 'address'
    }

    def __init__(self, id=None, type=None, product_code=None, status=None, customer_first_name=None, customer_last_name=None, address=None):  # noqa: E501
        """GetOrdersItemResponse - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._type = None
        self._product_code = None
        self._status = None
        self._customer_first_name = None
        self._customer_last_name = None
        self._address = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if type is not None:
            self.type = type
        if product_code is not None:
            self.product_code = product_code
        if status is not None:
            self.status = status
        if customer_first_name is not None:
            self.customer_first_name = customer_first_name
        if customer_last_name is not None:
            self.customer_last_name = customer_last_name
        if address is not None:
            self.address = address

    @property
    def id(self):
        """Gets the id of this GetOrdersItemResponse.  # noqa: E501

        The id of the order  # noqa: E501

        :return: The id of this GetOrdersItemResponse.  # noqa: E501
        :rtype: object
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this GetOrdersItemResponse.

        The id of the order  # noqa: E501

        :param id: The id of this GetOrdersItemResponse.  # noqa: E501
        :type: object
        """

        self._id = id

    @property
    def type(self):
        """Gets the type of this GetOrdersItemResponse.  # noqa: E501

        type of the order  # noqa: E501

        :return: The type of this GetOrdersItemResponse.  # noqa: E501
        :rtype: object
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this GetOrdersItemResponse.

        type of the order  # noqa: E501

        :param type: The type of this GetOrdersItemResponse.  # noqa: E501
        :type: object
        """

        self._type = type

    @property
    def product_code(self):
        """Gets the product_code of this GetOrdersItemResponse.  # noqa: E501

        Product code of the order  # noqa: E501

        :return: The product_code of this GetOrdersItemResponse.  # noqa: E501
        :rtype: object
        """
        return self._product_code

    @product_code.setter
    def product_code(self, product_code):
        """Sets the product_code of this GetOrdersItemResponse.

        Product code of the order  # noqa: E501

        :param product_code: The product_code of this GetOrdersItemResponse.  # noqa: E501
        :type: object
        """

        self._product_code = product_code

    @property
    def status(self):
        """Gets the status of this GetOrdersItemResponse.  # noqa: E501

        Status of the order  # noqa: E501

        :return: The status of this GetOrdersItemResponse.  # noqa: E501
        :rtype: object
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this GetOrdersItemResponse.

        Status of the order  # noqa: E501

        :param status: The status of this GetOrdersItemResponse.  # noqa: E501
        :type: object
        """

        self._status = status

    @property
    def customer_first_name(self):
        """Gets the customer_first_name of this GetOrdersItemResponse.  # noqa: E501

        Customer first name  # noqa: E501

        :return: The customer_first_name of this GetOrdersItemResponse.  # noqa: E501
        :rtype: object
        """
        return self._customer_first_name

    @customer_first_name.setter
    def customer_first_name(self, customer_first_name):
        """Sets the customer_first_name of this GetOrdersItemResponse.

        Customer first name  # noqa: E501

        :param customer_first_name: The customer_first_name of this GetOrdersItemResponse.  # noqa: E501
        :type: object
        """

        self._customer_first_name = customer_first_name

    @property
    def customer_last_name(self):
        """Gets the customer_last_name of this GetOrdersItemResponse.  # noqa: E501

        Customer last name  # noqa: E501

        :return: The customer_last_name of this GetOrdersItemResponse.  # noqa: E501
        :rtype: object
        """
        return self._customer_last_name

    @customer_last_name.setter
    def customer_last_name(self, customer_last_name):
        """Sets the customer_last_name of this GetOrdersItemResponse.

        Customer last name  # noqa: E501

        :param customer_last_name: The customer_last_name of this GetOrdersItemResponse.  # noqa: E501
        :type: object
        """

        self._customer_last_name = customer_last_name

    @property
    def address(self):
        """Gets the address of this GetOrdersItemResponse.  # noqa: E501


        :return: The address of this GetOrdersItemResponse.  # noqa: E501
        :rtype: GetOrdersAddressResponse
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this GetOrdersItemResponse.


        :param address: The address of this GetOrdersItemResponse.  # noqa: E501
        :type: GetOrdersAddressResponse
        """

        self._address = address

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
        if issubclass(GetOrdersItemResponse, dict):
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
        if not isinstance(other, GetOrdersItemResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other