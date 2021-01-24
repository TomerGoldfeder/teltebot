import requests

base = "https://api.telegram.org/"


class TelegramBot:
    def __init__(self, token, user_id):
        self.token = token
        self.user_id = user_id

    def send_message(self, message=""):
        url = "{}bot{}/sendMessage".format(base, self.token)

        data = {"chat_id": self.user_id, "text": message}

        try:
            req = requests.post(url, data)
            req.raise_for_status()
        except Exception as e:
            print(e)

    def send_image(self, image, caption=""):
        url = "{}bot{}/sendPhoto".format(base, self.token)

        data = {"chat_id": self.user_id, "caption": caption}

        try:
            req = requests.post(url, data, files={"photo": open(image, 'rb')})
            req.raise_for_status()
        except Exception as e:
            print(e)
