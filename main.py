from healthcareprofessional import Doctor, HealthcareProfessional, Nurse
from receptionist import Receptionist
from patient import Patient
from prescription import Prescription
from appointmentschedule import AppointmentSchedule
from random import randrange

appointment_schedule = AppointmentSchedule()

# defining the doctors
doctor1 = Doctor("Test Doctor 1", "123", appointment_schedule)
doctor2 = Doctor("Test Doctor 2", "456", appointment_schedule)

# defining the nurse
nurse1 = Nurse("Test Nurse 1", "1234", appointment_schedule)

# defining the receptionist
receptionist = Receptionist("Test Receptionist", "0123", appointment_schedule)

# defining the patients
patient = Patient("Tests Patient 1", "123 Test Ave", "123-456-7890")
patient1 = Patient("Tests Patient 2", "456 Test Ave", "456-125-7848")

print("-----------------------Refilling prescription to Patient 3-----------------------")
# existing patient, with existing prescription
patient3 = Patient("Tests Patient 3", "789 Test Ave", "456-125-7800")
doctor2.RegisterPatient(patient3)
patient3.prescriptions.append(Prescription("DRUG1", patient3, doctor2, "1", "10ml"))
# 1 pre-existing prescription
print(patient3.name, " currently has: ", len(patient3.prescriptions), " prescriptions")
# 1 - patient needs repeat
prescription = patient3.requestRepeat(patient3.prescriptions[0])
if prescription != None:
  doctor2.IssuePrescription(prescription.prescription_type, patient3, "2", "10ml")

# 2 - prescription (original & repeated)
print(patient3.name, " currently has: ", len(patient3.prescriptions), " prescriptions")
print()

# request appointment of type emergency
appointment = patient.requestAppointment("EMERGENCY")

# Check regisitration
if patient.doctor is None:
  # if the patient has not been registered then register to Doctor 1
  doctor1.RegisterPatient(patient)

# receptionist is making appointments depending on appointment type
receptionist.makeAppointment(appointment)
appointmentTwo = patient.requestAppointment("STANDARD")
receptionist.makeAppointment(appointmentTwo)
appointmentFour = patient1.requestAppointment("EMERGENCY")
receptionist.makeAppointment(appointmentFour)
appointmentThree = patient1.requestAppointment("STANDARD")
# override booking system to have availability for today
receptionist.makeAppointment(appointmentThree, True)

print("-----------------------Printing booked appointment dates-----------------------")
# assigning dates for the appointments
print("Confirming appointment type ", appointment.appointmentType, " booked for ", appointment.date)
print("Confirming appointment type ", appointmentTwo.appointmentType, " booked for ", appointmentTwo.date)
print("Confirming appointment type ", appointmentThree.appointmentType, " booked for ", appointmentThree.date)
print("Confirming appointment type ", appointmentFour.appointmentType, " booked for ", appointmentFour.date)

print()

print("-----------------------Cancelling Appointment-----------------------")
# Total booked appointments before cancelling appointmentTwo
print("Total booked appointments: ", len(appointment_schedule.appointments))
receptionist.cancelAppointment(appointmentTwo)
# Total booked appointments after cancelling appointmentTwo
print("Total booked appointments: ", len(appointment_schedule.appointments))

print()

print("-----------------------Consultation Information-----------------------")
# showing the patients earlier prescriptions
print(appointment.patient.name, "currently has: ", len(appointment.patient.prescriptions), " prescriptions")
print()

print(nurse1.name,"is consulting appointment")
print()
recommended_prescriptions = nurse1.consultation()

# Have the doctor go to his next appointment
doctor1.consultation()
doctor2.consultation()
doctor1.consultation()

# storing the staff members consultaions according the staff members schedule
outcome = nurse1.consultation()
outcome1 = doctor2.consultation()
outcome2 = doctor1.consultation()

# check if the doctor recommended prescriptions
if recommended_prescriptions:
  # if the prescription is recommended then issue those prescriptions to the patient
  for prescription in recommended_prescriptions:
    # only the doctor can issue prescriptions
    doctor1.IssuePrescription(prescription, patient, randrange(1, 10), 2.5)
  print(patient.name, "currently has:", len(appointment.patient.prescriptions), " prescriptions")
  print()

  # print prescription information in a readable format
  for prescription in patient.prescriptions:
    print(prescription.prescription_type, " | Dosage: ", prescription.dosage, " | Quantity: ", prescription.quantity)

  # check if there is at least one prescription issued to the patient
  if len(patient.prescriptions) >= 1:
    requested_prescription = patient.requestRepeat(patient.prescriptions[0])
    # if there is atleast one prescription issued to the patient then the doctor can issue a refill to that prescription
    if requested_prescription:
      print()
      print(doctor1.name, " re-issued prescription of", requested_prescription.prescription_type, "to ", patient.name)
      doctor1.IssuePrescription(requested_prescription.prescription_type, patient, requested_prescription.quantity, requested_prescription.dosage)
# if the doctor did not recoment any prescription
else:
  print("No prescriptions recommended today")

print()
# check if the appointment has been completed
print("Appointment 1 completed?", appointment.completed)

print()

print("-----------------------Doctor 2 reached maximum patients-----------------------")
# check if the patients dont go over the 500 limit for doctor 2
for x in range(505):
  # adding a patient to doctor two who already has the maximum of 500 patients
  doctor2.RegisterPatient(Patient("1", "1", "1"))
print("Maximum number of", len(doctor2.patients), "patients are registered for doctor 2")
print()

# show that there are no available appointments for today
for staff in [doctor1, doctor2, nurse1]:
  if outcome is None:
    print("No more available appointments to consult on today for", staff.name)

print()

print("-----------------------Appointment Status and Information-----------------------")
# printing the staff members appointment information
for staff in [doctor1, doctor2, nurse1]:
  appointments = staff.ViewAppointments()
  if appointments:
    for app in staff.ViewAppointments():
      print(staff.name, " completed appointment of type: ", app.appointmentType)
print()