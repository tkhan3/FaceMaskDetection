import requests

def main():

    #uri = "https://api.telegram.org/bot739048528:AAFNZykMy9pPbywqBDRCTn8dhOiEwZrp4CM/getUpdates"

    token_id = "739048528:AAFNZykMy9pPbywqBDRCTn8dhOiEwZrp4CM"
    uri = "https://api.telegram.org/bot" + token_id + "/getUpdates"
    print (uri)
    response = requests.get(uri)
    print (response.json())
    json_response = response.json()
    print (json_response["result"][0]["message"]["chat"]["id"])

if __name__ == '__main__':
    main()
