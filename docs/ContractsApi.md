# swagger_client.ContractsApi

All URIs are relative to *https://sandbox.ostrom-api.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_contract_by_external_user_id**](ContractsApi.md#get_contract_by_external_user_id) | **GET** /users/{externalUserId}/contracts/{contractId} | Retrieve user contract information by external user id
[**get_contract_energy_consumption**](ContractsApi.md#get_contract_energy_consumption) | **GET** /contracts/{contractId}/energy-consumption | Retrieve user contract smart meter consumption
[**get_contract_energy_consumption_by_external_user_id**](ContractsApi.md#get_contract_energy_consumption_by_external_user_id) | **GET** /users/{externalUserId}/contracts/{contractId}/energy-consumption | Retrieve user contract smart meter consumption by external user id
[**get_contracts**](ContractsApi.md#get_contracts) | **GET** /contracts | Retrieve user contracts information
[**get_contracts_by_external_user_id**](ContractsApi.md#get_contracts_by_external_user_id) | **GET** /users/{externalUserId}/contracts | Retrieve user contracts information by external user id

# **get_contract_by_external_user_id**
> GetContractsItemResponse get_contract_by_external_user_id(external_user_id, contract_id)

Retrieve user contract information by external user id

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
api_instance = swagger_client.ContractsApi(swagger_client.ApiClient(configuration))
external_user_id = NULL # object | Partner user unique identifier
contract_id = NULL # object | ID of the contract

try:
    # Retrieve user contract information by external user id
    api_response = api_instance.get_contract_by_external_user_id(external_user_id, contract_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContractsApi->get_contract_by_external_user_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **external_user_id** | [**object**](.md)| Partner user unique identifier | 
 **contract_id** | [**object**](.md)| ID of the contract | 

### Return type

[**GetContractsItemResponse**](GetContractsItemResponse.md)

### Authorization

[ClientAccessToken](../README.md#ClientAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_contract_energy_consumption**
> GetContractsEnergyConsumptionResponse get_contract_energy_consumption(contract_id, start_date, end_date, resolution)

Retrieve user contract smart meter consumption

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
api_instance = swagger_client.ContractsApi(swagger_client.ApiClient(configuration))
contract_id = NULL # object | ID of the contract
start_date = NULL # object | start date ISO format on UTC timezone. e.g. 2023-11-01T00:00:00.000Z
end_date = NULL # object | end date ISO format on UTC timezone. e.g. 2023-11-02T00:00:00.000Z
resolution = NULL # object | The unit of time the data will be aggregated

try:
    # Retrieve user contract smart meter consumption
    api_response = api_instance.get_contract_energy_consumption(contract_id, start_date, end_date, resolution)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContractsApi->get_contract_energy_consumption: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | [**object**](.md)| ID of the contract | 
 **start_date** | [**object**](.md)| start date ISO format on UTC timezone. e.g. 2023-11-01T00:00:00.000Z | 
 **end_date** | [**object**](.md)| end date ISO format on UTC timezone. e.g. 2023-11-02T00:00:00.000Z | 
 **resolution** | [**object**](.md)| The unit of time the data will be aggregated | 

### Return type

[**GetContractsEnergyConsumptionResponse**](GetContractsEnergyConsumptionResponse.md)

### Authorization

[ClientAccessToken](../README.md#ClientAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_contract_energy_consumption_by_external_user_id**
> GetContractsEnergyConsumptionResponse get_contract_energy_consumption_by_external_user_id(external_user_id, contract_id, start_date, end_date, resolution)

Retrieve user contract smart meter consumption by external user id

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
api_instance = swagger_client.ContractsApi(swagger_client.ApiClient(configuration))
external_user_id = NULL # object | Partner user unique identifier
contract_id = NULL # object | ID of the contract
start_date = NULL # object | start date ISO format on UTC timezone. e.g. 2023-11-01T00:00:00.000Z
end_date = NULL # object | end date ISO format on UTC timezone. e.g. 2023-11-02T00:00:00.000Z
resolution = NULL # object | The unit of time the data will be aggregated

try:
    # Retrieve user contract smart meter consumption by external user id
    api_response = api_instance.get_contract_energy_consumption_by_external_user_id(external_user_id, contract_id, start_date, end_date, resolution)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContractsApi->get_contract_energy_consumption_by_external_user_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **external_user_id** | [**object**](.md)| Partner user unique identifier | 
 **contract_id** | [**object**](.md)| ID of the contract | 
 **start_date** | [**object**](.md)| start date ISO format on UTC timezone. e.g. 2023-11-01T00:00:00.000Z | 
 **end_date** | [**object**](.md)| end date ISO format on UTC timezone. e.g. 2023-11-02T00:00:00.000Z | 
 **resolution** | [**object**](.md)| The unit of time the data will be aggregated | 

### Return type

[**GetContractsEnergyConsumptionResponse**](GetContractsEnergyConsumptionResponse.md)

### Authorization

[ClientAccessToken](../README.md#ClientAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_contracts**
> GetContractsResponse get_contracts()

Retrieve user contracts information

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
api_instance = swagger_client.ContractsApi(swagger_client.ApiClient(configuration))

try:
    # Retrieve user contracts information
    api_response = api_instance.get_contracts()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContractsApi->get_contracts: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**GetContractsResponse**](GetContractsResponse.md)

### Authorization

[ClientAccessToken](../README.md#ClientAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_contracts_by_external_user_id**
> GetContractsResponse get_contracts_by_external_user_id(external_user_id)

Retrieve user contracts information by external user id

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
api_instance = swagger_client.ContractsApi(swagger_client.ApiClient(configuration))
external_user_id = NULL # object | Partner user unique identifier

try:
    # Retrieve user contracts information by external user id
    api_response = api_instance.get_contracts_by_external_user_id(external_user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContractsApi->get_contracts_by_external_user_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **external_user_id** | [**object**](.md)| Partner user unique identifier | 

### Return type

[**GetContractsResponse**](GetContractsResponse.md)

### Authorization

[ClientAccessToken](../README.md#ClientAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

