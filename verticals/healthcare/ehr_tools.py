
def extract_patient_info(ehr_text):
    risks = []
    if "hypertension" in ehr_text.lower():
        risks.append("hypertension")
    if "asthma" in ehr_text.lower():
        risks.append("asthma")

    return {
        "summary": "Patient history summarized.",
        "risks": risks
    }
