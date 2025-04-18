import requests
import json
import random
import string

# Splunk HEC Endpoint
splunk_url = "https://prd-p-538gt.splunkcloud.com:8088/services/collector"
splunk_token = "e88b5a64-db3d-4db7-961b-1565af3e7ca1"  # Use your actual token

headers = {
    "Authorization": f"Splunk {splunk_token}",
    "Content-Type": "application/json"
}

# Function to generate a honeytoken
def generate_honeytoken():
    return "HT-" + ''.join(random.choices(string.ascii_letters + string.digits, k=12))

# Generate a honeytoken
honeytoken = generate_honeytoken()

# Log data to Splunk
data = {
    "event": {
        "honeytoken": honeytoken,
        "status": "generated",
        "source": "fine_tuned_gpt2",
        "sourcetype": "honeytoken"
    },
    "sourcetype": "honeytoken",
    "index": "main"
}

# Send event to Splunk
response = requests.post(splunk_url, headers=headers, data=json.dumps(data), verify=False)

print("Response:", response.status_code, response.text)
