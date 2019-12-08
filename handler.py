import json

values = ["v1", "v2", "v3"]

def getValueById(event, context):
    id = int(event["pathParameters"]["id"])
    return {
        "statusCode": 200,
        "body": values[id]
    }

def getValues(event, context):
    return {
        "statusCode": 200,
        "body": json.dumps(values)
    }
