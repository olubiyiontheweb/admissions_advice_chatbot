# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.events import UserUtteranceReverted
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.knowledge_base.storage import InMemoryKnowledgeBase
from rasa_sdk.knowledge_base.actions import ActionQueryKnowledgeBase

class ActionQueryCourses(ActionQueryKnowledgeBase):
    def __init__(self):
        # load knowledge base with data from the given file
        courses_db = InMemoryKnowledgeBase("hull_courses.json")

        # overwrite the representation function of the hotel object
        # by default the representation function is just the name of the object
        courses_db.set_representation_function_of_object(
            "hotel", lambda obj: obj["name"] + " (" + obj["city"] + ")"
        )

        super().__init__(courses_db)
        
class ActionQueryFaculties(ActionQueryKnowledgeBase):
    def __init__(self):
        # load the faculty knowledge base with data from the given file
        faculties_db = InMemoryKnowledgeBase("hull_faculties.json")

        # overwrite the representation function of the hotel object
        # by default the representation function is just the name of the object
        faculties_db.set_representation_function_of_object(
            "hotel", lambda obj: obj["name"] + " (" + obj["city"] + ")"
        )

        super().__init__(faculties_db)