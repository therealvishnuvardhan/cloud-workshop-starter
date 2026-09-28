import json
import random
from datetime import datetime, timezone

FACTS = [
    "Amazon S3 launched in 2006 and was one of the very first AWS services.",
    "S3 stands for Simple Storage Service.",
    "A single Lambda call can run for at most 15 minutes.",
    "Each AWS region is split into several Availability Zones, each with its own power and networking.",
    "India has two AWS regions: Mumbai (ap-south-1) and Hyderabad (ap-south-2).",
    "Kubernetes was designed at Google and released as open source in 2014.",
    "Docker was first released in 2013.",
    "The first call to a new Lambda function is slower. That is called a cold start.",
]


def lambda_handler(event, context):
    path = event.get("rawPath", "/")

    if path == "/health":
        return {"statusCode": 200, "body": json.dumps({"status": "ok"})}

    params = event.get("queryStringParameters") or {}
    name = params.get("name", "student")
    print(f"Greeting requested for {name}")

    return {
        "statusCode": 200,
        "headers": {"Content-Type": "application/json"},
        "body": json.dumps({
            "message": f"Hello, {name}! This answer came from your AWS Lambda function.",
            "fact": random.choice(FACTS),
            "servedAt": datetime.now(timezone.utc).strftime("%H:%M:%S UTC"),
        }),
    }
