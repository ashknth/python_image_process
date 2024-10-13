import random
import pickle

class Doctor:
    def __init__(self, name):
        self.name = name
        self.history = []

    def add_to_history(self, patient_input):
        """Adds patient input to history."""
        self.history.append(patient_input)

    def generate_reply(self, patient_input):
        """Generates a reply to the patient, occasionally referencing past conversations."""
        self.add_to_history(patient_input)

        if len(self.history) > 5 and random.random() < 0.3:  # Random chance to refer to earlier inputs
            earlier_statement = random.choice(self.history[:-1])
            return f"Earlier you said that '{earlier_statement}'. Can you tell me more about that?"
        else:
            return self.change_person(patient_input)

    def change_person(self, statement):
        """Changes pronouns in the statement for conversation."""
        replacements = {
            "I": "you", "me": "you", "my": "your", "am": "are",
            "you": "I", "your": "my", "are": "am"
        }
        words = statement.split()
        changed_words = [replacements.get(word.lower(), word) for word in words]
        return ' '.join(changed_words)

    def save_history(self):
        """Save the doctor's history to a file using pickling."""
        filename = f"{self.name}.dat"
        with open(filename, 'wb') as f:
            pickle.dump(self, f)

    @staticmethod
    def load_history(name):
        """Load the doctor's history from a file if it exists."""
        filename = f"{name}.dat"
        try:
            with open(filename, 'rb') as f:
                return pickle.load(f)
        except FileNotFoundError:
            return Doctor(name)

