class Message():
    text: str
    chatId: str

    def __init__(self, chatId='', text=''):
        self.text = text
        self.chatId = chatId

    def __str__(self):
        return "From {}: \'{}\'".format(self.chatId, self.text)