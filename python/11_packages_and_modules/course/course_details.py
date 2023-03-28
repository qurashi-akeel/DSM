import sys, os
from os.path import abspath, join, dirname


sys.path.insert(0, abspath(join(dirname(__file__), '..')))
from payment import pay_details

def c_info():
    print('11_packages_and_modules > course > course_details.py > c_info')

pay_details.p_info()
