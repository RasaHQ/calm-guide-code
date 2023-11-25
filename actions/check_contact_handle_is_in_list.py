from typing import Any, Dict, List, Text

from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet
from rasa_sdk.executor import CollectingDispatcher

from .db import get_contacts


class CheckContactHandleIsInList(Action):
    def name(self) -> str:
        return "check_contact_handle_is_in_list"

    def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[str, Any]
    ) -> List[Dict[Text, Any]]:
        contacts = get_contacts(tracker.sender_id)
        contact_handle = tracker.get_slot("send_flowers_contact_handle")
        existing_handles = {c.handle for c in contacts}
        return [SlotSet("return_value",
                        contact_handle and contact_handle in existing_handles)]
