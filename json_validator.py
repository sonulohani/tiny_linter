from validator import Validator

import json


class JsonValidator(Validator):
    def validate(self):
        try:
            json.loads(self._content)
        except ValueError as err:
            return err