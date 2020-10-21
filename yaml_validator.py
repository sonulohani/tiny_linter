from validator import Validator

import yaml


class YamlValidator(Validator):
    def validate(self):
        try:
            yaml.loads(self._content)
        except ValueError as err:
            return err