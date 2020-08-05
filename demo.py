# -*- coding: UTF-8 -*-

"""
@author : plm
@software : PyCharm
@file : demo.py
@time : 2020/8/5 11:10
"""

import os
import glob

os.chdir('/home/pitt')
getcwd = os.getcwd()
print(getcwd)
os.system('ls -l')

glob_glob = glob.glob('*.py')
print(glob_glob)

