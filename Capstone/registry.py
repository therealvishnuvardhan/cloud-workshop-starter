import json
import os
import boto3

table = boto3.resource("dynamodb").Table(os.environ["TABLE_NAME"])


def reply(status, body):
    return {
        "statusCode": status,
        "headers": {"Content-Type": "application/json"},
        "body": json.dumps(body),
    }


def lambda_handler(event, context):
    method = event["requestContext"]["http"]["method"]
    path = event.get("rawPath", "/")

    if method == "OPTIONS":
        return {"statusCode": 204, "body": ""}

    if path == "/health":
        return reply(200, {"status": "ok"})

    if path == "/students" and method == "GET":
        items = table.scan()["Items"]
        for s in items:
            s["age"] = int(s["age"])
        items.sort(key=lambda s: s["id"])
        return reply(200, items)

    if path == "/students" and method == "POST":
        data = json.loads(event.get("body") or "{}")
        missing = [f for f in ("id", "name", "age", "email") if not data.get(f)]
        if missing:
            return reply(400, {"error": "missing fields: " + ", ".join(missing)})
        table.put_item(Item={
            "id": str(data["id"]).upper(),
            "name": data["name"],
            "age": int(data["age"]),
            "email": data["email"],
        })
        print(f"Registered student {data['id']}")
        return reply(201, {"message": "Student registered", "id": str(data["id"]).upper()})

    return reply(404, {"error": "not found"})
