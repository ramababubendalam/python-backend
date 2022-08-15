# python-backend
Creates Apigateway and Lambda Trigger to get Server UnixTime and TimeZone

Python Function https://github.com/ramababubendalam/python-backend/blob/main/Python/getPossix.py retrieves the Server time(Unix format) and Server Time Zone in json format.

This Python Function is attached to an apigateway service with get mehtod to trigger the lambda function.

AWS Template https://github.com/ramababubendalam/python-backend/blob/main/template.yml is used to deploy cloudformation stack which creates apigateway and lambda trigger.

Auto deployment is enabled to deploy based on the push commit.

https://github.com/ramababubendalam/python-backend/blob/main/.github/workflows/main.yml

Once the deployment is completed successfully, Apigateway URL can be accessed to get the Server Time and Time Zone in json format

Example:

 https://76icaj1r1k.execute-api.eu-west-2.amazonaws.com/dev01/v1  ( this url is still live)
 
 Output:

{
    "epochTime": 1660565415,
    "ServerTimeZone": "UTC"
}
