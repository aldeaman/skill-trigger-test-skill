from mycroft import MycroftSkill, intent_handler


class SkillTriggerTest(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_handler('test.trigger.skill.intent')
    def handle_test_trigger_skill(self, message):
        self.speak_dialog('test.trigger.skill')


def create_skill():
    return SkillTriggerTest()

