
class Appointment(object):
    def __init__(self, day, month, year,time, clinic_type,appt_ID):
        self.day = day
        self.month = month
        self.year = year
        self.time = time
        self.clinic_type = clinic_type
        self.appt_ID = appt_ID