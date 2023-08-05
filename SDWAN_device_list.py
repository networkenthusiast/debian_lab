import requests
import json
from Auth_vManage import authenticate_vmanage
def get_device_list():
    device_list_url = "https://10.10.20.90/dataservice/device"
    user_url ="https://10.10.20.90/dataservice/admin/user"
    device_list_payload ={}
    new_user_payload =json.dumps({
        "group": ["netadmin"],
        "description": "Rest_API_User",
        "userName": "apiuser2",
        "password": "password",
        "locale": "en_US",
        "resGroupName": "global"
        })
    cred_list = authenticate_vmanage()
    device_list_headers ={
        'X-XSRF-TOKEN': cred_list[1],
        'Cookie': cred_list[0]
    }
    device_list_response =requests.get(device_list_url,headers=device_list_headers,data=device_list_payload,verify=False)
    requests.post(user_url,headers=device_list_headers,data=new_user_payload,verify=False)  # creating new netadmin user
    return(device_list_response.json()['data'])

def main():
    dict_device_list = get_device_list()
    for i in dict_device_list:
        print(f"{i['host-name']} has System ip {i['system-ip']} and status is {i['status']}")

if __name__=="__main__":
    main()
