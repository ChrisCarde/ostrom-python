# swagger_client.UsersApi

All URIs are relative to *https://sandbox.ostrom-api.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**disconnect_user**](UsersApi.md#disconnect_user) | **DELETE** /users/{externalUserId}/disconnect | Disconnect user from partner client application
[**get_me**](UsersApi.md#get_me) | **GET** /me | Retrieve user information
[**link_user**](UsersApi.md#link_user) | **POST** /users/link | Link user to a partner client application

# **disconnect_user**
> disconnect_user(external_user_id)

Disconnect user from partner client application

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
api_instance = swagger_client.UsersApi(swagger_client.ApiClient(configuration))
external_user_id = NULL # object | Partner user unique identifier

try:
    # Disconnect user from partner client application
    api_instance.disconnect_user(external_user_id)
except ApiException as e:
    print("Exception when calling UsersApi->disconnect_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **external_user_id** | [**object**](.md)| Partner user unique identifier | 

### Return type

void (empty response body)

### Authorization

[ClientAccessToken](../README.md#ClientAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_me**
> GetMeResponse get_me()

Retrieve user information

Allowed role: `USER`

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
api_instance = swagger_client.UsersApi(swagger_client.ApiClient(configuration))

try:
    # Retrieve user information
    api_response = api_instance.get_me()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->get_me: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**GetMeResponse**](GetMeResponse.md)

### Authorization

[ClientAccessToken](../README.md#ClientAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **link_user**
> UserLinkResponse link_user(body=body)

Link user to a partner client application

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
api_instance = swagger_client.UsersApi(swagger_client.ApiClient(configuration))
body = swagger_client.UsersLinkBody() # UsersLinkBody |  (optional)

try:
    # Link user to a partner client application
    api_response = api_instance.link_user(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->link_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UsersLinkBody**](UsersLinkBody.md)|  | [optional] 

### Return type

[**UserLinkResponse**](UserLinkResponse.md)

### Authorization

[ClientAccessToken](../README.md#ClientAccessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

