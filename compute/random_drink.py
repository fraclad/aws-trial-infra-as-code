import json
import random

def random_drink():
    drinks = ["tea", "boba", "juice", "coffee", "yeos", "beer", "slushies"]
    return random.choice(drinks)

def lambda_handler(event, context):
    drink = random_drink()
    message = f"you should drink {drink}"
    
    return {
        "statusCode": 200,
        "body": json.dumps({"message": message, "drink": drink})
    }