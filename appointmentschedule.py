import datetime
from random import randint

class AppointmentSchedule:
    # instantiate the appointments list
    appointments = []

    def AddAppointment(self, appointment, bookToday = False):
        # if the appointment type is of Emergency then give an appointment of the same date
        appointment.date = self.GetNextAvailability(appointment.appointmentType == 'EMERGENCY', bookToday)
        # add the appointment to the appointments list
        self.appointments.append(appointment)
        return appointment
        
    def CancelAppointment(self, appointment):
        # remove the appointment from the list
        self.appointments.remove(appointment)
        return appointment

    # Find next spot availaible in calendar
    def GetNextAvailability(self, emergency = False, bookToday = False):
        today = datetime.datetime.now()
        if emergency or bookToday:
            # if the appoinemnt type is emergency (or we override and book for today) then give an appointment of the same date
            return today
        else:
            # if the appoinemnt type is not of emergency then give an appointment between 1-7 days and 1-3 hours
            return today + datetime.timedelta(days=randint(1, 7), hours=randint(1, 3))
    
    # Find next appointment for staff member
    def FindNextAvailable(self, staff):
        # loop through the appoinments list
        self.appointments.sort(key=lambda x: x.appointmentType, reverse=False)
        for appointment in self.appointments:
            # check if the appointment is not completed and the appointment is for today
            if not appointment.completed and appointment.date.strftime("%d/%m/%Y") == datetime.datetime.now().strftime("%d/%m/%Y"):
                # if the appointment is not completed then assign staff 
                appointment.staff = staff
                return appointment
        return None