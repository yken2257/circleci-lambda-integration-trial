import json
import requests

def lambda_handler(event, context):
    response = requests.get("https://www.kke.co.jp/")
    print("Hello, World!")
    print(response.text)    
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }