# swagger_client.AuthApi

All URIs are relative to *https://sandbox.ostrom-api.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_o_auth2_token**](AuthApi.md#create_o_auth2_token) | **POST** /oauth2/token | Obtain OAuth2 Access Token

# **create_o_auth2_token**
> OAuth2TokenResponse create_o_auth2_token(grant_type=grant_type)

Obtain OAuth2 Access Token

Allowed role: `USER` or `PARTNER`

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: OAuth2BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.AuthApi(swagger_client.ApiClient(configuration))
grant_type = NULL # object |  (optional)

try:
    # Obtain OAuth2 Access Token
    api_response = api_instance.create_o_auth2_token(grant_type=grant_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthApi->create_o_auth2_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **grant_type** | [**object**](.md)|  | [optional] 

### Return type

[**OAuth2TokenResponse**](OAuth2TokenResponse.md)

### Authorization

[OAuth2BasicAuth](../README.md#OAuth2BasicAuth)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

