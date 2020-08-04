from mycroft import MycroftSkill, intent_file_handler


class MqttBroker(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('broker.mqtt.intent')
    def handle_broker_mqtt(self, message):
        self.speak_dialog('broker.mqtt')


def create_skill():
    return MqttBroker()

