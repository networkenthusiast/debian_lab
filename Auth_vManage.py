import requests
def authenticate_vmanage():
    cred_list=[]
    cookie_url = "https://10.10.20.90/j_security_check"
    token_url ="https://10.10.20.90/dataservice/client/token"
    payload_for_cookie = 'j_username=admin&j_password=C1sco12345'
    payload_for_token = {}
    headers_for_cookie = {
        'Content-Type': 'application/x-www-form-urlencoded'
        }
    cookie_response=requests.post(cookie_url,headers=headers_for_cookie,data=payload_for_cookie,verify=False)
    cookie=((cookie_response.headers['set-cookie']).split(';'))[0]
    headers_for_token ={
        'Content-Type': 'application/json',
        'Cookie': cookie
    }
    token_response =requests.get(token_url,headers=headers_for_token,data=payload_for_token,verify=False)
    token = token_response.text
    cred_list.append(cookie)
    cred_list.append(token)
    return(cred_list)

def main():
    cred_list = authenticate_vmanage()
    print(f"Cookie is {cred_list[0]} and token is {cred_list[1]}")

if __name__=="__main__":
    main()
