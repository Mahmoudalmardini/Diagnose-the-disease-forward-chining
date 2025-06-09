import tkinter as tk
from tkinter import messagebox
import datetime

# ---------- Knowledge Base: Rules (set of symptoms → disease) ----------
rules = [
    ({"cough", "fever", "congestion"}, "Influenza"),
    ({"sneezing", "runny nose", "mild fatigue"}, "Common Cold"),
    ({"fever", "loss of smell", "dry cough"}, "COVID-19"),
    ({"sore throat", "fever", "red throat"}, "Throat Infection"),
    ({"headache", "fatigue", "nausea"}, "Migraine"),
    ({"abdominal pain", "vomiting", "diarrhea"}, "Food Poisoning"),
    ({"sneezing", "itchy eyes", "runny nose"}, "Allergy"),
    ({"facial pain", "congestion", "headache"}, "Sinus Infection"),
    ({"wheezing", "shortness of breath", "chest tightness"}, "Asthma"),
    ({"persistent cough", "chest discomfort", "mucus"}, "Bronchitis"),
    ({"cough with phlegm", "fever", "chills"}, "Pneumonia"),
    ({"high fever", "joint pain", "skin rash"}, "Dengue"),
    ({"frequent urination", "extreme thirst", "weight loss"}, "Diabetes"),
    ({"headache", "dizziness", "nosebleeds"}, "Hypertension"),
    ({"lower right abdominal pain", "nausea", "loss of appetite"}, "Appendicitis"),
]

# ---------- Treatments for each disease ----------
treatments = {
    "Influenza": "Rest, fluids, antiviral meds (if severe)",
    "Common Cold": "Rest, warm fluids, over-the-counter meds",
    "COVID-19": "Isolate, rest, monitor oxygen, consult doctor",
    "Throat Infection": "Salt gargle, pain relief, antibiotics if needed",
    "Migraine": "Dark room, hydration, pain relievers",
    "Food Poisoning": "Oral rehydration, avoid solid food, consult if severe",
    "Allergy": "Antihistamines, avoid allergens, eye drops",
    "Sinus Infection": "Steam inhalation, nasal spray, antibiotics if bacterial",
    "Asthma": "Inhalers, avoid triggers, medical supervision",
    "Bronchitis": "Cough suppressants, rest, hydration",
    "Pneumonia": "Antibiotics, rest, medical monitoring",
    "Dengue": "Fluids, pain relievers, hospital care if severe",
    "Diabetes": "Insulin, blood sugar monitoring, healthy diet",
    "Hypertension": "Medication, low-salt diet, regular checkups",
    "Appendicitis": "Surgery (appendectomy), antibiotics",
}

# ---------- Forward Chaining Inference Function ----------
def forward_chaining(facts, rules):
    diagnoses = []
    for condition, result in rules:
        # If all symptoms in a rule are found in the input, add the disease
        if condition.issubset(facts) and result not in diagnoses:
            diagnoses.append(result)
    return diagnoses

# ---------- Save diagnosis session to a file ----------
def save_to_file(symptoms, diagnoses):
    with open("patients_log.txt", "a") as f:
        f.write(f"Date: {datetime.datetime.now()}\n")
        f.write(f"Symptoms: {', '.join(symptoms)}\n")
        if diagnoses:
            for d in diagnoses:
                f.write(f"Diagnosis: {d}\n")
                f.write(f"Treatment: {treatments[d]}\n")
        else:
            f.write("Diagnosis: Not found\n")
        f.write("-" * 40 + "\n")

# ---------- Main Diagnosis Logic ----------
def diagnose():
    input_text = entry.get()
    
    # Show warning if input is empty
    if not input_text.strip():
        messagebox.showwarning("Input Error", "Please enter symptoms.")
        return

    # Convert input string to set of lowercase symptoms
    symptoms = set(s.strip().lower() for s in input_text.split(','))

    # Run forward chaining inference
    results = forward_chaining(symptoms, rules)

    # Save results to file
    save_to_file(symptoms, results)

    # Display diagnosis result
    if results:
        result_text = ""
        for d in results:
            result_text += f"✅ Diagnosis: {d}\n💊 Treatment: {treatments[d]}\n\n"
    else:
        result_text = "⚠️ No diagnosis could be made."

    # Show result in a popup message box
    messagebox.showinfo("Diagnosis Result", result_text)

# ---------- GUI Setup ----------
root = tk.Tk()
root.title("Medical Expert System")
root.geometry("560x320")

# Label for instructions
label = tk.Label(root, text="Enter symptoms (comma-separated):", font=("Arial", 12))
label.pack(pady=10)

# Entry field for user input
entry = tk.Entry(root, width=65)
entry.pack(pady=5)

# Button to trigger diagnosis
button = tk.Button(root, text="Diagnose", command=diagnose, bg="#4CAF50", fg="white", font=("Arial", 12))
button.pack(pady=15)

# Run the application
root.mainloop()