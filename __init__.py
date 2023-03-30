from mycroft import MycroftSkill, intent_file_handler


class ChatGpt(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('gpt.chat.intent')
    def handle_gpt_chat(self, message):
        utterance = message.data.get('utterance')
        response = ''

        self.speak_dialog('gpt.chat', data={
            'response': response,
            'utterance': utterance
        })


def create_skill():
    return ChatGpt()

