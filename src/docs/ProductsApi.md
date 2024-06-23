# swagger_client.ProductsApi

All URIs are relative to *https://sandbox.ostrom-api.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_product_prices**](ProductsApi.md#get_product_prices) | **GET** /products | Retrieve product prices

# **get_product_prices**
> GetProductPriceResponse get_product_prices(zip, number_of_residents=number_of_residents, yearly_consumption=yearly_consumption)

Retrieve product prices

Allowed role: `PARTNER`

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: ClientAccessToken
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.ProductsApi(swagger_client.ApiClient(configuration))
zip = NULL # object | The postal code where the tariff will be calculated
number_of_residents = NULL # object | The number of people in the household, if not provided the default value will be 1 (optional)
yearly_consumption = NULL # object | The amount of yearly consumption of the household, if not provided the default value will be 1400 kWh (optional)

try:
    # Retrieve product prices
    api_response = api_instance.get_product_prices(zip, number_of_residents=number_of_residents, yearly_consumption=yearly_consumption)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductsApi->get_product_prices: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **zip** | [**object**](.md)| The postal code where the tariff will be calculated | 
 **number_of_residents** | [**object**](.md)| The number of people in the household, if not provided the default value will be 1 | [optional] 
 **yearly_consumption** | [**object**](.md)| The amount of yearly consumption of the household, if not provided the default value will be 1400 kWh | [optional] 

### Return type

[**GetProductPriceResponse**](GetProductPriceResponse.md)

### Authorization

[ClientAccessToken](../README.md#ClientAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

