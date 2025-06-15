
from verticals.healthcare.ehr_tools import extract_patient_info

class ExecutorAgent:
    def __init__(self):
        pass

    def execute(self, ehr_text):
        return extract_patient_info(ehr_text)
