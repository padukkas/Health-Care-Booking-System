from prescription import Prescription
from random import randrange

# health care class
class HealthcareProfessional:
    # define name, employee number and appointment schedule
    def __init__(self, name, employee_number, appointment_schedule):
        self.name = name
        self.employee_number = employee_number
        self.appointment_schedule = appointment_schedule

    def ViewAppointments(self):
        appointments = []
        # loop through the appointments
        for appointment in self.appointment_schedule.appointments:
            if appointment.staff == self:
                # add appointment to the appointment list
                appointments.append(appointment);
        return appointments

    # Note, consulations don't result in a prescription being issued. The doctor will still need to issue the prescription
    def consultation(self):
        # find next available appointment
        appointment = self.appointment_schedule.FindNextAvailable(self)
        # No more appointments for today
        if appointment is None:
            return
        # set appointment completed
        appointment.completed = True
        # initiate the drugs list
        drugs = []
        # add list items to the drugs list
        drug_list = ['drug 1', 'drug 2', 'drug 3', 'drug 4', 'drug 5', 'drug 6', 'drug 7', 'drug 8', 'drug 9', 'drug 10']
        # loop the drugs in order to randomly assing drugs to the patient
        for index in range(randrange(0, 8)):
            index = randrange(0, len(drug_list))
            drugs.append(drug_list[index])
            drug_list.remove(drug_list[index])
        # return the randomly selected drugs
        return drugs

# doctor class
class Doctor(HealthcareProfessional):
    # initiating the doctor
    def __init__(self, name, employee_number, appointment_schedule):
        # initiating the prescription class inside doctor
        self.prescriptions = []
        # initiating the patients class inside doctor
        self.patients = []
        super().__init__(name, employee_number, appointment_schedule)

    # initiating the IssuePrescription class
    def IssuePrescription(self, prescription_type, patient, quantity, dosage):
        # verifying the patient is existing
        if patient in self.patients:
            prescription = Prescription(prescription_type, patient, self, quantity, dosage)
            # adding the prescription to the patient
            patient.prescriptions.append(prescription)
            self.prescriptions.append(prescription)
    # Registering patient to a doctor
    def RegisterPatient(self, patient):
        # enforcing the doctor can only have 500 patients rule
        if not patient.doctor and len(self.patients) < 500:
            # if the doctor have less than 500 patients then enroll patient
           self.patients.append(patient)
           patient.doctor = self 

class Nurse(HealthcareProfessional):
    # initiating the nurse with it's attributes
    def __init__(self, name, employee_number, appointment_schedule):
        super().__init__(name, employee_number, appointment_schedule)