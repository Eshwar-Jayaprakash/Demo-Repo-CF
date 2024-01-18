
import boto3
import json

# Create an AWS Organizations client
client = boto3.client('organizations')

# Define your SCP
scp = {
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Deny",
            "Action": "bedrock:*",
            "Resource": "*"
        }
    ]
}

# Convert the SCP to a JSON string
scp_json = json.dumps(scp)

# Create the SCP
response = client.create_policy(
    Content=scp_json,
    Description='eshwar-test-SCP',
    Name='MySCP',
    Type='SERVICE_CONTROL_POLICY',
)

# Print the response
print(response)