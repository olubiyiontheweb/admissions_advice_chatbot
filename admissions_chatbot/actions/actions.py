# This files contains your custom actions programmed with python

import difflib
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.knowledge_base.storage import InMemoryKnowledgeBase

list_of_course_names = []

class ActionQueryCourseDetails(Action):
    def name(self) -> Text:
        return "action_query_course_details"
    
    def __init__(self):
        load_course_name_list()
        
    def run(self, dispatcher, tracker, domain):
        course = tracker.get_slot("course")
        course_det = {}
        
        # display a list of all available courses
        
        dispatcher.utter_custom_message("Here are the list of courses available")
        dispatcher.utter_custom_message(str(list_of_course_names))
        return []
        
class ActionQueryFacultyCourses(Action):
    def name(self) -> Text:
        return "action_query_faculty_courses"
    
    def __init__(self):
        load_course_name_list()
        
    def run(self, dispatcher, tracker, domain):
        print("action_query_faculty_courses")

class ActionQueryFacultyUrl(Action):
    def name(self) -> Text:
        return "action_query_faculty_url"
    
    def __init__(self):
        # load courses from file
        courses_db = InMemoryKnowledgeBase("hull_courses_faculties.json")

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="Hello World!")

        return []
    
class ActionQueryCourseUrl(Action):
    def name(self) -> Text:
        return "action_query_course_url"
    
    def __init__(self):
        hull_base_url = "https://www.hull.ac.uk"
        load_course_name_list()
        
    def run(self, dispatcher, tracker, domain):
        print("action_query_course_url")

class ActionQueryCourseFee(Action):
    def name(self) -> Text:
        return "action_query_course_fee"
    
    def __init__(self):
        load_course_name_list()
        
    def run(self, dispatcher, tracker, domain):
        print("action_query_course_fee")
    
class ActionQueryCourseDuration(Action):
    def name(self) -> Text:
        return "action_query_course_duration"
    
    def __init__(self):
        load_course_name_list()
        
    def run(self, dispatcher, tracker, domain):
        print("action_query_course_duration")
    
class ActionQueryCourseIntake(Action):
    def name(self) -> Text:
        return "action_query_course_intake"
    
    def __init__(self):
        self.courses_data = load_course_name_list()
        
    def run(self, dispatcher, tracker, domain):
        course = tracker.get_slot("course")
        courses = []
        
        if course is not None:
            courses = difflib.get_close_matches(course, list_of_course_names)
            
            if len(courses) > 0:
                course_index = list_of_course_names.index(courses[0])
                dispatcher.utter_message("The course {0} is available in the following intakes: {1}".format(course, self.courses_data[course_index]["intake"]))                
                return [SlotSet("course_intake", self.courses_data[course_index]["intake"]), SlotSet("course_fee", "Home student: {0}, International Student: {1}".format(self.courses_data[course_index]["home_fee"], self.courses_data[course_index]["international_fee"]))]
            else:
                dispatcher.utter_message("Sorry, I don't know about that course")
        
        return []
    
class ActionQueryCourseStartDate(Action):
    def name(self) -> Text:
        return "action_query_course_start_date"
    
    def __init__(self):
        load_course_name_list()
        
    def run(self, dispatcher, tracker, domain):
        print("action_query_course_start_date")
        
def load_course_name_list():
    # load courses from file
    courses_db = InMemoryKnowledgeBase("hull_courses_faculties.json")
    
    for course_obj in courses_db.data:
        list_of_course_names.append(course_obj["course"])
        
    return courses_db.data