import json

def getValues(event, context):
    return {
        "statusCode": 200,
        "body": json.dumps(["v1", "v2", "v3"])
    }
