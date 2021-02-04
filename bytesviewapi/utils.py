import json
import sys

PY3 = sys.version_info[0] == 3

if PY3:

    def is_valid_string(lang):
        return isinstance(lang, str)

    def is_valid_json(data):
        try:
            json_object = json.loads(data)
        except ValueError as e:
            return False
        return True
    
    def is_valid_dict(data):
        return isinstance(data,dict)