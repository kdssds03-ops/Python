# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 12:57:01 2026

@author: kdssd
"""

# 계산기 프로그램 
def add(n1, n2):  # 덧셈
    print('덧셈 결과 : ', n1 + n2)

def sub(n1, n2):  # 뺄셈
    print('뺄셈 결과 : ', n1 - n2)

def mul(n1, n2):  # 곱셈
    print('곱셈 결과 : ', n1 * n2)

def div(n1, n2):  # 나눗셈
    print('나눗셈 결과 : ', n1 / n2)

def calculator(): # 계산기
    while True :
        op = int(input("연산자를 선택하세요. 1.덧셈, 2.뺄셈, 3.곱셈, 4.나눗셈, 0. 종료: "))
        if op == 0 : break
        n1 = int(input("숫자를 입력하세요. : "))
        n2 = int(input("숫자를 입력하세요. : "))
    
        if(op == 1): add(n1, n2)       
        elif(op == 2): sub(n1, n2)
        elif(op == 3): mul(n1, n2)
        elif(op == 4): div(n1, n2)

calculator()