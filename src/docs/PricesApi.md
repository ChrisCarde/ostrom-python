# swagger_client.PricesApi

All URIs are relative to *https://sandbox.ostrom-api.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_spot_prices**](PricesApi.md#get_spot_prices) | **GET** /spot-prices | Retrieve day-ahead spot price information

# **get_spot_prices**
> GetSpotPriceResponse get_spot_prices(start_date, end_date, resolution, zip=zip)

Retrieve day-ahead spot price information

Allowed role: `USER` or `PARTNER`

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
api_instance = swagger_client.PricesApi(swagger_client.ApiClient(configuration))
start_date = NULL # object | start date ISO format on UTC timezone. e.g. 2023-11-01T00:00:00.000Z
end_date = NULL # object | end date ISO format on UTC timezone. e.g. 2023-11-02T00:00:00.000Z
resolution = NULL # object | The unit of time the data will be aggregated
zip = NULL # object | Zip code used to fetch Ostrom base price, gridFees, tax and levies. If not provided the respective values are returned as zero. (optional)

try:
    # Retrieve day-ahead spot price information
    api_response = api_instance.get_spot_prices(start_date, end_date, resolution, zip=zip)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PricesApi->get_spot_prices: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | [**object**](.md)| start date ISO format on UTC timezone. e.g. 2023-11-01T00:00:00.000Z | 
 **end_date** | [**object**](.md)| end date ISO format on UTC timezone. e.g. 2023-11-02T00:00:00.000Z | 
 **resolution** | [**object**](.md)| The unit of time the data will be aggregated | 
 **zip** | [**object**](.md)| Zip code used to fetch Ostrom base price, gridFees, tax and levies. If not provided the respective values are returned as zero. | [optional] 

### Return type

[**GetSpotPriceResponse**](GetSpotPriceResponse.md)

### Authorization

[ClientAccessToken](../README.md#ClientAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

