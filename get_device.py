import requests
import json
from get_token import get_token
def main():
    cert_path="/home/debian/sandboxdnac.cisco.crt"
    token=get_token()
    api_url="https://sandboxdnac.cisco.com"
    headers={"Content-Type":"application/json","X-Auth-Token":token}
    get_resp=requests.get(f"{api_url}/dna/intent/api/v1/network-device",headers=headers,verify=cert_path)
    list_of_device=get_resp.json()["response"]
    if get_resp.ok:
        for device in list_of_device:
            print(f"Device-Type is {device['type']} , IP address is {device['managementIpAddress']} and serial number is {device['serialNumber']}")
    else:
        print(f'Device data fetch failed with code {get_resp.status_code}')
        print(f'Failure body = {get_resp.text}')

if __name__=="__main__":
    main()
