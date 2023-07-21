import requests
def get_token():
    api_url="https://sandboxdnac.cisco.com/dna"
    auth=("devnetuser","Cisco123!")
    header={"Content-Type":"application/json"}
    cert_path="/home/debian/sandboxdnac.cisco.crt"
    api_response=requests.post(f"{api_url}/system/api/v1/auth/token", auth=auth,headers=header,verify=cert_path)
    token = api_response.json()["Token"]
    return token

def main():
    token = get_token()
    print(token)

if __name__ =="__main__":
    main()
