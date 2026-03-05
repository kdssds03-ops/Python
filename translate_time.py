# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 12:38:35 2026

@author: kdssd
"""

min = int(input("분 단위 시간 : "))

hour = min // 60
min %= 60

print(f'{hour}시간 {min}분')
