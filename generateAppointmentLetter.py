from fhir_parser import FHIR
import docx
from docxtpl import DocxTemplate, InlineImage
import Doctor as Dr
import Appointment as appt
from docx.shared import Mm


def setDoctor(patientID, doctor):
    patient = getPatient(patientID)
    patient.Doctor = doctor


def getPatient(patientID):
    fhir = FHIR('https://localhost:5001/api/', verify_ssl=False)
    try:
        patient = fhir.get_patient(patientID)
    except:
        patient = None
    return patient


def removeNumbersFromName(name):
    result = ''.join([char for char in name if not char.isdigit()])
    return result


def setPatientContext(patientID):
    patient = getPatient(patientID)
    patient_info = ["", "", "", "", "", "", ""]
    try:
        patient_info[0] = patient.addresses[0].lines[0]
        patient_info[1] = patient.addresses[0].city
        patient_info[2] = patient.addresses[0].state
        patient_info[3] = patient.addresses[0].postal_code
        patient_info[4] = patient.name.prefix
        patient_info[5] = removeNumbersFromName(patient.name.family)
        patient_info[6] = patient.name.given[0]
    except:
        pass
    return patient_info


def setDoctorContext(doctor):
    doctor_info = doctor_info = ["", "", "", ""]
    try:
        doctor_info[0] = doctor.phone_num
        doctor_info[1] = doctor.practice_address[0]
        doctor_info[2] = doctor.practice_address[1]
        doctor_info[3] = doctor.name
    except:
        pass
    return doctor_info


def setApptContext(appointment):
    appointment_info = ["", "", "", "", "",""]
    try:
        appointment_info[0] = appointment.day
        appointment_info[1] = appointment.month
        appointment_info[2] = appointment.year
        appointment_info[3] = appointment.time
        appointment_info[4] = appointment.clinic_type
        appointment_info[5] = appointment.appt_ID
    except:
        pass
    return appointment_info


def generateApptLetterDocX(patientID, doctor, appointment, template):
    tpl = DocxTemplate(template)
    patient_info = setPatientContext(patientID)
    doctor_info = setDoctorContext(doctor)
    appointment_info = setApptContext(appointment)
    if(doctor.signature != None):
        signature = InlineImage(tpl, doctor.signature,
                                height=Mm(30), width=Mm(100))
    else:
        signature = ""
    context = {
        'address1': patient_info[0],
        'address2': patient_info[1],
        'address3': patient_info[2],
        'post_code': patient_info[3],
        'patient_prefix': patient_info[4],
        'patient_surname': patient_info[5],
        'doctors_phone_number': doctor_info[0],
        'doctors_address1': doctor_info[1],
        'doctors_address2': doctor_info[2],
        'dr_name': doctor_info[3],
        'day': appointment_info[0],
        'month': appointment_info[1],
        'year': appointment_info[2],
        'time': appointment_info[3],
        'clinic_type': appointment_info[4],
        'signature': signature
    }
    save_path = "generated/" + patient_info[6] + patient_info[5] + ".docx"
    tpl.render(context)
    tpl.save(save_path)

if __name__ == "__main__":
    doctorJB = Dr.Doctor("Backwell", "Gastroenterology", [
                         "123 Street", "W1 456"], "0123456789", "Guy's Hospital")
    appointment1 = appt.Appointment(
        "1st", "January", "2020", "12:00", "Gastro Clinic", "8f789d0b-3145-4cf2-8504-13159edaa747")
    fhir = FHIR('https://localhost:5001/api/', verify_ssl=False)
    patients = fhir.get_patient_page(5)
    for patient in patients:
        generateApptLetterDocX(patient.uuid,
                       doctorJB, appointment1, "templates/doctorAppointment.docx")
