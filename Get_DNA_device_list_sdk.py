import requests
from dnacentersdk import api
def main():
    cert_path="/home/debian/sandboxdnac.cisco.crt"
    dnac = api.DNACenterAPI(
        base_url="https://sandboxdnac.cisco.com",
        username="devnetuser",
        password="Cisco123!",
        verify=cert_path
    )
    device = dnac.devices.get_device_list()
    for devices in device['response']:
        print(f"Device id is {devices['id']} and mgmt ip address {devices['managementIpAddress']}")

if __name__=="__main__":
    main()
