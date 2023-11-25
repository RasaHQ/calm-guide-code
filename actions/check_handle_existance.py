from typing import Any, Dict, List, Text

from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet
from rasa_sdk.executor import CollectingDispatcher


class CheckHandleExistence(Action):
    def name(self) -> str:
        return "check_handle_existence"

    def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[str, Any]
    ) -> List[Dict[Text, Any]]:
        handle = tracker.get_slot("add_contact_handle")
        return [SlotSet("return_value", len(handle) < 10)]
