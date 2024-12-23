class Patient:
    def __init__(self, name, age, disease):
        self.name = name
        self.age = age
        self.disease = disease

    def __repr__(self):
        return self.name


def search_patients_by_disease(patients, disease):
    patients_with_disease = [patient.name for patient in patients if patient.disease == disease]
    return patients_with_disease


patients_data = [
    Patient("Alice", 30, "Flu"),
    Patient("Bob", 45, "Diabetes"),
    Patient("Charlie", 35, "Flu")
]

search_disease = "Flu"

patients_with_fluidisease = search_patients_by_disease(patients_data, search_disease)

print(f"Patients with {search_disease}: {patients_with_fluidisease}")
