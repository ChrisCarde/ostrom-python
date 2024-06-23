# swagger_client.OrdersApi

All URIs are relative to *https://sandbox.ostrom-api.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_order_by_external_user_id**](OrdersApi.md#get_order_by_external_user_id) | **GET** /users/{externalUserId}/orders/{orderId} | Retrieve user order information by external user id
[**get_orders_by_external_user_id**](OrdersApi.md#get_orders_by_external_user_id) | **GET** /users/{externalUserId}/orders | Retrieve user orders information by external user id

# **get_order_by_external_user_id**
> GetOrdersItemResponse get_order_by_external_user_id(external_user_id, order_id)

Retrieve user order information by external user id

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
api_instance = swagger_client.OrdersApi(swagger_client.ApiClient(configuration))
external_user_id = NULL # object | Partner user unique identifier
order_id = NULL # object | ID of the order

try:
    # Retrieve user order information by external user id
    api_response = api_instance.get_order_by_external_user_id(external_user_id, order_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrdersApi->get_order_by_external_user_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **external_user_id** | [**object**](.md)| Partner user unique identifier | 
 **order_id** | [**object**](.md)| ID of the order | 

### Return type

[**GetOrdersItemResponse**](GetOrdersItemResponse.md)

### Authorization

[ClientAccessToken](../README.md#ClientAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_orders_by_external_user_id**
> GetOrdersResponse get_orders_by_external_user_id(external_user_id)

Retrieve user orders information by external user id

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
api_instance = swagger_client.OrdersApi(swagger_client.ApiClient(configuration))
external_user_id = NULL # object | Partner user unique identifier

try:
    # Retrieve user orders information by external user id
    api_response = api_instance.get_orders_by_external_user_id(external_user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrdersApi->get_orders_by_external_user_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **external_user_id** | [**object**](.md)| Partner user unique identifier | 

### Return type

[**GetOrdersResponse**](GetOrdersResponse.md)

### Authorization

[ClientAccessToken](../README.md#ClientAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

