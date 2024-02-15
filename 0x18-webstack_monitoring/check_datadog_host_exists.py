#!/usr/bin/env bash
import requests

# Datadog API base URL
API_BASE_URL = "https://api.datadoghq.com/api/v1"

# Datadog API key
API_KEY = "YOUR_API_KEY_HERE"

# Datadog application key
APP_KEY = "YOUR_APPLICATION_KEY_HERE"

# Hostname to check
HOSTNAME = "421255-web-01"

def check_host_exists(hostname):
    # Endpoint to get list of hosts
    url = f"{API_BASE_URL}/hosts"

    # Request headers
    headers = {
        "Content-Type": "application/json",
        "DD-API-KEY": API_KEY,
        "DD-APPLICATION-KEY": APP_KEY
    }

    # Request parameters
    params = {
        "filter": f"name:{hostname}"
    }

    # Make GET request to Datadog API
    response = requests.get(url, headers=headers, params=params)

    # Check if request was successful
    if response.status_code == 200:
        # Check if host exists in the response
        hosts = response.json().get("hosts", [])
        for host in hosts:
            if host.get("name") == hostname:
                return True
    return False

if __name__ == "__main__":
    if check_host_exists(HOSTNAME):
        print("Host exists")
    else:
        print("Host does not exist")
