import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','Library_management_system.settings')

import django
django.setup()


import pandas as pd
from django.contrib.auth.models import User
from library.models import StudentProfile


def register_students(student_info):
    t = User.objects.create_user(username = student_info[0],first_name = student_info[1], last_name = student_info[2], email = student_info[3], password = student_info[4])
    t.save()
    user = User.objects.get(username = student_info[0])
    t = StudentProfile.objects.create(user=user)
    t.save()

def populate():
    data = pd.read_csv('stdinfo.csv')
    for i in range(data.shape[0]):
        st_info = [data[j][i] for j in data]
        register_students(st_info)

if __name__ == "__main__":
    print("Populating Script")
    populate()
    print("Populating complete")



