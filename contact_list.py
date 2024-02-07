class ContactList:
    def __init__(self, name, contacts=None):
        self._name = name
        self._contacts = [] if contacts is None else contacts

    def add_contact(self, contact):
        self._contacts.append(contact)
        self._contacts.sort(key=lambda x: x['name'])

    def remove_contact(self, name):
        self._contacts = [contact for contact in self._contacts if contact['name'] != name]

    def find_shared_contacts(self, other_list):
        shared_contacts = []
        for contact in self._contacts:
            for other_contact in other_list.get_contacts:
                if contact['name'] == other_contact['name'] and contact['number'] == other_contact['number']:
                    shared_contacts.append(contact)
                    break
        return shared_contacts

    @property
    def get_name(self):
        return self._name

    @get_name.setter
    def set_name(self, name):
        self._name = name

    @property
    def get_contacts(self):
        return self._contacts

    @get_contacts.setter
    def set_contacts(self, contacts):
        self._contacts = contacts