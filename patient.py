from prescription import Prescription
from appointment import Appointment

class Patient:

    # define the patient with it's attributes
    def __init__(self, name, address, phone):
        self.name = name
        self.address = address
        self.phone = phone
        self.prescriptions = []
        self.doctor = None
        
    def requestRepeat(self, prescription):
        # in order to request a repeat verify that prescription has been given the patient
        if prescription in self.prescriptions:
            return prescription
        return None

    def requestAppointment(self, appointmentType):
        # request an appointment
        appointment = Appointment(appointmentType, None, self)
        return appointment

    def checkRegistration(self):
        # check if the patient is registered
        return self.doctor is not None
