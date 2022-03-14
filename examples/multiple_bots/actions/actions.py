from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.types import DomainDict


class ActionGreet(Action):

    def name(self) -> Text:
        return "action_greet"

    def run(
            self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(response="utter_greet_en")
        return []


class ActionSetNameSlot(Action):
    def name(self) -> Text:
        return "action_set_name_slot"

    async def run(
            self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: DomainDict
    ) -> List[Dict[Text, Any]]:
        return [SlotSet("nome_usuario", "Jonas")]
