from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import json
from datetime import date, datetime
import calendar


class ActionOpenHours(Action):
    

    def name(self) -> Text:
        return "when_open"

    def showOpenHours(self):
        
        f = open('C:/Users/pioka/Rasa_Projects/demo/actions/opening_hours.json')
        dataDict = json.load(f)
        tmpString = "We are open:\n"
        tmpString += ( "Monday: " + str(dataDict["items"]["Monday"]["open"])+ " to " + str(dataDict["items"]["Monday"]["close"]) + "\n")
        tmpString += ( "Tuesday: " + str(dataDict["items"]["Tuesday"]["open"])+ " to " + str(dataDict["items"]["Tuesday"]["close"]) + "\n")
        tmpString += ( "Wednesday: " + str(dataDict["items"]["Wednesday"]["open"])+ " to " + str(dataDict["items"]["Wednesday"]["close"]) + "\n")
        tmpString += ( "Thursday : " + str(dataDict["items"]["Thursday"]["open"])+ " to " + str(dataDict["items"]["Thursday"]["close"]) + "\n")
        tmpString += ( "Friday: " + str(dataDict["items"]["Friday"]["open"])+ " to " + str(dataDict["items"]["Friday"]["close"]) + "\n")
        tmpString += ( "Saturday: " + str(dataDict["items"]["Saturday"]["open"])+ " to " + str(dataDict["items"]["Saturday"]["close"]) + "\n")
        tmpString += ( " On Sunday we are close")

        f.close

        return tmpString

    def checkOpen(self):
        f = open('C:/Users/pioka/Rasa_Projects/demo/actions/opening_hours.json')
        dataDict = json.load(f)
        my_date = date.today()
        time = datetime.now()
        today = str(calendar.day_name[my_date.weekday()])
        nowHour = int(time.strftime("%H"))
        hourOpening = dataDict["items"][today]["open"]
        hourClosing = dataDict["items"][today]["close"]
        print(nowHour)

        if nowHour >= hourOpening and nowHour < hourClosing:
            print("We are open now")
        else:
            print("We are close now")



        f.close



    

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

          
            tmpString = self.showOpenHours()
            self.checkOpen()

            dispatcher.utter_message(text = tmpString )
            
           

            return []
    

class CheckIfOpen(Action):

    def name(self) -> Text:
        return "check_open"
        

    def checkOpen(self):
        f = open('C:/Users/pioka/Rasa_Projects/demo/actions/opening_hours.json')
        dataDict = json.load(f)
        my_date = date.today()
        time = datetime.now()
        today = str(calendar.day_name[my_date.weekday()])
        nowHour = int(time.strftime("%H"))
        hourOpening = dataDict["items"][today]["open"]
        hourClosing = dataDict["items"][today]["close"]
        

        if nowHour >= hourOpening and nowHour < hourClosing:
            return "We are open now"
            
        else:
            return "We are close now"
            

        f.close


    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

            dispatcher.utter_message(text = self.checkOpen() )

            

           

            return []

class ActionShowMenu(Action):

    def name(self) -> Text:
        return "show_Menu"
        

    def showMenu(self):
        f = open('C:/Users/pioka/Rasa_Projects/demo/actions/menu.json')
        dataDict = json.load(f)
        menu = ""
        for x in dataDict["items"]:
            menu += str(x["name"] + "        " + str(x["price"])) + "\n"
         
        return menu

        f.close


    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

            dispatcher.utter_message(text = self.showMenu() )

            dispatcher.utter_message(text = " Do you wanna something?")

            return []

class ActionOrder(Action):

    def name(self) -> Text:
        return "order"
        


    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

            

            
            client_choice = tracker.get_slot("choice")
            dispatcher.utter_message(text=f"You chose {client_choice}")
            print(client_choice)
            

            

           

            return []


