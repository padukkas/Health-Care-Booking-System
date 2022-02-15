class Receptionist:

    # define the receptionists attributes
    def __init__(self, name, employee_number, appointment_schedule):
        self.name = name
        self.employee_number = employee_number
        self.appointment_schedule = appointment_schedule

    def makeAppointment(self, appointment, bookToday = False):
        appointment = self.appointment_schedule.AddAppointment(appointment, bookToday)
        return appointment

    def cancelAppointment(self, appointment):
        self.appointment_schedule.CancelAppointment(appointment)
        return appointment