class Appointment:
    # defining the appointment attributes
    def __init__(self, appointmentType, staff, patient):
        self.appointmentType = appointmentType
        self.staff = staff
        self.patient = patient
        self.completed = False
        self.date = None