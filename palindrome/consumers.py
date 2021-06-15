import json
from django.core.cache import cache
from channels.generic.websocket import WebsocketConsumer


class PalinConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

    def disconnect(self, code):
        pass

    def receive(self, text_data=None, bytes_data=None):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        self.send(text_data=json.dumps({'message': message + '  is Plidrom:  ' + self.Is_Palidrom(message)}))

    def Is_Palidrom(self, text):

        obj = cache.get(text)
        if not obj:
            len_input = len(text)
            for i in range(0, int(len_input / 2)):
                if not (text[i] == text[len_input - i - 1]):
                    cache.set(text, 'false1')
                    return 'false'
            cache.set(text, 'true1')
            return "true"
        return obj