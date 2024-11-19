import json


class Observation:
    def __init__(self, id, coding_system, coding_code, coding_display,
                 subject_reference, subject_display, value, value_unit,
                 value_system, value_code):
        self._id = id
        self._coding = {
            "system": coding_system,
            "code": coding_code,
            "display": coding_display
        }
        self._subject = {
            "reference": subject_reference,
            "display": subject_display
        }
        self._valueQuantity = {
            "value": value,
            "unit": value_unit,
            "system": value_system,
            "code": value_code
        }

    # Getters
    def get_id(self):
        return self._id

    def get_coding(self):
        return self._coding

    def get_subject(self):
        return self._subject

    def get_value_quantity(self):
        return self._valueQuantity

    # Setters
    def set_id(self, id):
        self._id = id

    def set_coding(self, coding_system, coding_code, coding_display):
        self._coding["system"] = coding_system
        self._coding["code"] = coding_code
        self._coding["display"] = coding_display

    def set_subject(self, subject_reference, subject_display):
        self._subject["reference"] = subject_reference
        self._subject["display"] = subject_display

    def set_value_quantity(self, value, value_unit, value_system, value_code):
        self._valueQuantity["value"] = value
        self._valueQuantity["unit"] = value_unit
        self._valueQuantity["system"] = value_system
        self._valueQuantity["code"] = value_code

    # Function to represent the Observation in proper JSON format
    def to_json(self):
        observation_dict = {
            "resourceType": "Observation",
            "id": self._id,
            "status": "final",
            "code": {
                "coding": [
                    {
                        "system": self._coding["system"],
                        "code": self._coding["code"],
                        "display": self._coding["display"]
                    }
                ]
            },
            "subject": {
                "reference": self._subject["reference"],
                "display": self._subject["display"]
            },
            "valueQuantity": {
                "value": self._valueQuantity["value"],
                "unit": self._valueQuantity["unit"],
                "system": self._valueQuantity["system"],
                "code": self._valueQuantity["code"]
            }
        }
        return json.dumps(observation_dict, indent=2)


# Example usage
observation_example = Observation(
    id="bp-observation-1234",
    coding_system="http://loinc.org",
    coding_code="85354-9",
    coding_display="Blood pressure panel",
    subject_reference="Patient/1234",
    subject_display="John Doe",
    value=120,
    value_unit="mmHg",
    value_system="http://unitsofmeasure.org",
    value_code="mm[Hg]"
)

# Output JSON with proper double quotes
json_output = observation_example.to_json()
# print(json_output)
