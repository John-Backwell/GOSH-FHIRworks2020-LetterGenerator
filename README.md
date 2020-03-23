# GOSH-FHIRworks2020-LetterGenerator

An example of how FHIR patient data can be used to quickly generate Doctors Letters etc given a docX template.

Prerequisites:
    - Python FHIR parser https://pypi.org/project/FHIR-Parser/ (thanks to Ethan for this one)
    - Python docx and docxtpl libraries https://python-docx.readthedocs.io/en/latest/     
    https://docxtpl.readthedocs.io/en/latest/
    - goshDrives FHIRworks .NET project  https://github.com/goshdrive/FHIRworks_2020

How to begin generating letters:
    - Clone repo, and follow the instructions found in the readme of FHIRworks to ensure that the dummy patient data is loaded into a local webpage
    - Open a terminal and navigate to the folder that contains generateAppointmentLetter.py, and use >python generateAppointmentLetter.py to have a go at generating a series of doctors letters based on the first 5 pages of dummy patient data. The generated letters will be in the generated folder. The main function in generateAppointmentLetter has an example of how generateApptLetter can be used.
    
generateApptLetter takes the following parameters:

patientID - the unique identifier of the patient (string)
doctor - Doctor object that holds the info for filling the doctor fields
appointment - appointment object that holds the info for filling the appointment info fields
template - name of the docX template that you wish to use to generate the letters (string)

Please note that currently you need to create the doctor and appointment objects yourself before calling generateApptLetter as these bits of information are not currently included in the FHIR patient data. In the future hopefully that data will be included in FHIR data, or this project could be extended to read in JSON doctor and appointment objects.

Further Info:
  - Currently only 1 docX template in the templates folder, if you wish to create your own, use the existing one as a guideline. The available variable names to be auto-filled in the letters are:
  
address1
address2
address3
post_code
patient_prefix
patient_surname
doctors_phone_number
doctors_address1
doctors_address2
dr_name
day
month
year
time
clinic_type
signature

Where each of these needs to be in two braces - e.g {{address1}} will be replaced in the template by the first line of the patients address.

the {{signature}} field comes from the signatures folder in the project - If the name of your doctor matches an image file in that folder (which will hopefully be the digital signature of the doctor!), {{signature}} will be replaced by the image.
