from typing import Any, Dict, List, Text

from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet
from rasa_sdk.executor import CollectingDispatcher

from .db import get_contacts


class ListContacts(Action):
    def name(self) -> str:
        return "list_contacts"

    def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[str, Any]
    ) -> List[Dict[Text, Any]]:
        starting_chars = tracker.get_slot("list_contacts_starting_chars")
        contacts = get_contacts(tracker.sender_id)
        if starting_chars:
            contacts = [c for c in contacts
                        if c.name.lower().startswith(starting_chars.lower())]
        if len(contacts) > 0:
            contacts_list = "".join([f"- {c.name} ({c.handle}) \n" for c in contacts])
            return [SlotSet("contacts_list", contacts_list)]
        else:
            return [SlotSet("contacts_list", None)]
