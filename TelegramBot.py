import requests
import telegram

token_id = '739048528:AAFNZykMy9pPbywqBDRCTn8dhOiEwZrp4CM'

def getChatId():
    uri = "https://api.telegram.org/bot" + token_id + "/getUpdates"
    response = requests.get(uri).json()
    chat_id = response["result"][0]["message"]["chat"]["id"]
    return str(chat_id)


def send_violation_text():
    print ("hello")

    bot_chatID = getChatId()
    bot_message = "Mask Violation"

    send_text = 'https://api.telegram.org/bot' + \
                token_id + '/sendMessage?chat_id=' + \
                bot_chatID + '&parse_mode=Markdown&text=' + \
                bot_message


    response = requests.get(send_text)
    telegram.bot.serialization

    print (response.json())


#if __name__ == '__main__':
#    main()
