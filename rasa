class ActionRunSqlQuery(Action):
    def name(self):
        return "action_run_sql_query"

    def run(self, dispatcher, tracker, domain):
        # get the query from the domain
        query = domain['sql_query']

        # get the database connection
        conn = pymssql.connect(server='your_server_name', user='your_username', password='your_password', database='your_database_name')
        cursor = conn.cursor()

        # execute the query
        cursor.execute(query)

        # fetch the results
        results = cursor.fetchall()

        # save the results in a slot
        tracker.slots['query_results'] = results

        # close the database connection
        conn.close()

        # return the first 10 results to the user
        results_str = self.format_results(results[:10])
        dispatcher.utter_message(results_str)

        # set the slot to keep track of the index of the last result shown
        tracker.slots['last_result_index'] = 10

        # set the active loop to show more results
        return [SlotSet("requested_slot", "next_results")]

    def format_results(self, results):
        # format the results as a string
        results_str = ""
        for row in results:
            row_str = ""
            for val in row:
                row_str += str(val) + "\t"
            results_str += row_str + "\n"
        return results_str
#######################################
#NLU data (data/nlu.yml):
- intent: next_results
  examples: |
    - next
    - show me more
    - next 10
    - show 10 more
#Stories (data/stories.yml):    
- story: show results
  steps:
  - intent: search_db
  - action: action_run_sql_query
  - action: action_show_results
  - intent: next_results
  - action: action_show_next_results

#########################################
from typing import Dict, Any, Text, List, Union
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
import pyodbc

class ActionShowResults(Action):
    def name(self) -> Text:
        return "action_show_results"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        results = tracker.get_slot("results") or []
        next_index = tracker.get_slot("next_index") or 0

        # Check if we need to retrieve more data from the database
        if len(results) <= next_index:
            # Retrieve data from database
            # ...
            # Save retrieved data to results slot
            # ...
        
        # Retrieve the next 10 results to display to the user
        next_results = results[next_index:next_index+10]
        
        if not next_results:
            # If there are no more results to show, reset the next_index slot
            dispatcher.utter_message("There are no more results to show.")
            return [SlotSet("next_index", 0)]
        
        # Update the next_index slot to the next page
        next_index += 10
        return_slots = [SlotSet("results", results), SlotSet("next_index", next_index)]

        # Send the next 10 results to the user
        message = "Here are the next 10 results:\n"
        for result in next_results:
            message += f"- {result}\n"
        dispatcher.utter_message(message)
        
        return return_slots
####################################

#story:
- story: show results
  steps:
  - intent: show_results
  - action: action_show_results
  - intent: next_results
  - action: action_show_results
#################################
class ActionShowNextResults(Action):
    def name(self) -> Text:
        return "action_show_next_results"

    async def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        results = tracker.get_slot("results")
        start = tracker.get_slot("start_index")
        end = tracker.get_slot("end_index")
        if results is None:
            dispatcher.utter_message(text="No results found.")
            return []

        if end >= len(results):
            dispatcher.utter_message(text="No more results found.")
            return []

        start += 10
        end += 10
        tracker.slots["start_index"] = start
        tracker.slots["end_index"] = end

        message = ""
        for i in range(start, end):
            message += f"{i+1}. {results[i]}\n"
        message += "Would you like to see the next 10 results?"
        dispatcher.utter_message(text=message)

        return []
#######################################
#domain.yml

intents:
- greet
- goodbye
- inform
- query_results
- next_results

entities:
- account_number
- place

slots:
  account_number:
    type: text
  place:
    type: text
  query_results:
    type: list
  result_index:
    type: int

responses:
  utter_greet:
  - text: "Hello! How can I assist you?"
  
  utter_goodbye:
  - text: "Goodbye! Have a nice day."

  utter_ask_account_number:
  - text: "Please provide your account number."

  utter_ask_place:
  - text: "Which place are you looking for?"
  
  utter_confirm_place:
  - text: "Did you mean {place}?"
  
  utter_query_results:
  - text: "Here are the top 10 results:\n{query_results}"

  utter_no_results:
  - text: "Sorry, no results found."
  
  utter_ask_next_results:
  - text: "Do you want to see the next 10 results?"
  
  utter_show_next_results:
  - text: "{query_results}"
  
actions:
- action_ask_account_number
- action_ask_place
- action_confirm_place
- action_run_sql_query
- action_show_results
- action_show_next_results
- action_reset_results

templates:
  utter_ask_account_number:
    - text: "Please provide your account number."
    
  utter_ask_place:
    - text: "Which place are you looking for?"
    
  utter_confirm_place:
    - text: "Did you mean {place}?"
  
  utter_query_results:
    - text: "Here are the top 10 results:\n{query_results}"
    
  utter_no_results:
    - text: "Sorry, no results found."
  
  utter_ask_next_results:
    - text: "Do you want to see the next 10 results?"
  
  utter_show_next_results:
    - text: "{query_results}"
