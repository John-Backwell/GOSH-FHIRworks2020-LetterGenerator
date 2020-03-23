import os.path as path

class Doctor(object):
    def __init__(self, name, speciality, practice_address, phone_num, practice_name):
        self.name = name
        self.specialty = speciality
        self.practice_address = practice_address
        self.phone_num = phone_num
        self.practice_name = practice_name
        sig_path = "signatures/" + self.name + ".png"
        if(path.exists(sig_path)):
            self.signature = sig_path
        else:
            self.signature = None


            