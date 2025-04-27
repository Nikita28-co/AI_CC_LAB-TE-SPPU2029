def diagnose(symptoms):
    symptoms = [s.lower() for s in symptoms]

    # Define rules
    if {"fever", "cough", "fatigue", "sore throat"}.issubset(symptoms):
        return "You might have the Flu."
    elif {"fever", "cough", "shortness of breath", "loss of taste"}.issubset(symptoms):
        return "You might have COVID-19."
    elif {"sneezing", "runny nose", "itchy eyes"}.issubset(symptoms):
        return "You might have Allergies."
    elif {"headache", "nausea", "sensitivity to light"}.issubset(symptoms):
        return "You might have a Migraine."
    elif {"fever", "rash", "joint pain"}.issubset(symptoms):
        return "You might have Dengue Fever."
    elif {"stomach pain", "nausea", "diarrhea"}.issubset(symptoms):
        return "You might have Food Poisoning."
    else:
        return "Symptoms do not match any known condition in this system. Please consult a doctor."

# User input
print("Medical Diagnosis Expert System")
print("Enter symptoms separated by commas (e.g., fever, cough, fatigue):")
user_input = input("Symptoms: ")
user_symptoms = [sym.strip() for sym in user_input.split(',')]

# Get diagnosis
result = diagnose(user_symptoms)

# Output
print("\nDiagnosis Result:")
print(result)
