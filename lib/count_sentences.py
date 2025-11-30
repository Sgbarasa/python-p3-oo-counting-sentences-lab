class MyString:
    def __init__(self, value=""):
        self._value = ""
        if value:
            self.value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        if not isinstance(new_value, str):
            print("The value must be a string.")
        else:
            self._value = new_value

    # ---- Sentence Type Checkers ---- #

    def is_sentence(self):
        return self._value.endswith(".")

    def is_question(self):
        return self._value.endswith("?")

    def is_exclamation(self):
        return self._value.endswith("!")

    # ---- Sentence Counter ---- #

    def count_sentences(self):
        if not self._value:
            return 0

        import re
        # Split on ., ?, ! but remove empty fragments
        sentences = re.split(r'[.!?]+', self._value)
        sentences = [s.strip() for s in sentences if s.strip()]

        return len(sentences)
