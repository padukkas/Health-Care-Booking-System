class Prescription:
    # defining the prescription attributes
    def __init__(self, prescription_type, patient, doctor, quantity, dosage):
        self.prescription_type = prescription_type
        self.patient = patient
        self.doctor = doctor
        self.quantity = quantity
        self.dosage = dosage