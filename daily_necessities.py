# -*- coding: utf-8 -*-
"""
Created on Sat Dec  9 14:00:42 2023

@author: kdssd
"""
import random

print("<회원가입>")

Id = input("아이디를 입력하세요 : ")
password = input("비밀번호를 입력하세요 : ")

print("회원가입 성공!")

while True:
    print("<로그인>")
    input_id = input("아이디를 입력하세요 : ")
    input_pass = input("비밀번호를 입력하세요 : ")
    
    if input_id == Id and input_pass == password:
        print("로그인 성공!")
        break
    else:
        print("로그인 실패!")

while True:
    kind = int(input("카테고리 선택 <1. 생필품> <2. 분리수거> <3. 지출관리> <4. 오늘의 메뉴 추천> <5. 내 주변 편의시설> <6. 종료> : "))
    
    if kind == 1: 
        necessaries = int(input("생필품 선택 <1. 주방용품> <2. 위생용품> <3. 청소용품> <4. 가전제품> : "))
        
        if necessaries == 1:
            use = int(input("종류 선택 <1. 부엌칼> <2. 주방가위> <3. 집게> <4. 국자> <5. 냄비> <6. 도마> : "))    
            if use == 1:
                print("쿠팡 : 12,000원, 지마켓 : 13,140원")
                print("최저가 : 12,000원")
            elif use == 2:
                print("쿠팡 : 4,200원, 지마켓 : 3,800원")
                print("최저가 : 3,800원")
            elif use == 3:
                print("쿠팡 : 6,690원, 지마켓 : 7,400원")
                print("최저가 : 3,800원")
            elif use == 4:
                print("쿠팡 : 3,300원, 지마켓 : 3,560원")
                print("최저가 : 3,300원")
            elif use == 5:
                print("쿠팡 : 3,400원, 지마켓 : 3,730원")
                print("최저가 : 3,800원")
            else:
                print("쿠팡 : 1,300원, 지마켓 : 1,200원")
                print("최저가 : 1,200원")
        elif necessaries == 2:
            use = int(input("종류 선택 : <1. 휴지> <2. 물티슈> <3. 칫솔> <4. 샴푸> <5. 면도기> <6. 비누> : "))
            if use == 1:
                print("쿠팡 : 16,900원, 지마켓 : 17,000원")
                print("최저가 : 16,900원")
            elif use == 2:
                print("쿠팡 : 10,900원, 11번가 : 12,000원")
                print("최저가 : 10,900원")
            elif use == 3:
                print("쿠팡 : 1,216원, 지마켓 : 1,420원")
                print("최저가 : 1,216원")
            elif use == 4:
                print("쿠팡 : 5,900원, 지마켓 : 7,200원")
                print("최저가 : 5,900원")
            elif use == 5:
                print("쿠팡 : 5,421원, 11번가 : 5,000원")
                print("최저가 : 3,800원")
            else:
                print("쿠팡 : 990원, 11번가 : 900원")
                print("최저가 : 3,800원")
        elif necessaries == 3:
            use = int(input("종류 선택 : <1. 세제> <2. 락스> <3. 섬유유연제> <4. 빗자루> <5. 휴지통> <6. 빨래망> : "))
            
            if use == 1:
                print("쿠팡 : 9,200원, 지마켓 : 8,900원")
                print("최저가 : 8,900원")
            elif use == 2:
                print("쿠팡 : 7,500원, 지마켓 : 7,600원")
                print("최저가 : 7,500원")
            elif use == 3:
                print("쿠팡 : 5,200원, 지마켓 : 5,000원")
                print("최저가 : 5,000원")
            elif use == 4:
                print("쿠팡 : 1,770원, 지마켓 : 1,900원")
                print("최저가 : 1,770원")
            elif use == 5:
                print("쿠팡 : 5,200원, 지마켓 : 5,800원")
                print("최저가 : 5,200원")
            else:
                print("쿠팡 : 1,200원, 지마켓 : 1,400원")
                print("최저가 : 1,200원")
        else:
            use = int(input("종류 선택 : <1. 전자레인지> <2. 세탁기> <3. 청소기> <4. 헤어드라이기> <5. 선풍기> <6. 에어프라이어> : "))
            
            if use == 1:
                print("쿠팡 : 49,900원, 지마켓 : 51,400원")
                print("최저가 : 49,900원")
            elif use == 2:
                print("쿠팡 : 269,900원, 지마켓 : 270,000원")
                print("최저가 : 269,900원")
            elif use == 3:
                print("쿠팡 : 79,000원, 11번가 : 69,000원")
                print("최저가 : 69,000원")
            elif use == 4:
                print("쿠팡 : 12,640원, 11번가 : 13,000원")
                print("최저가 : 12,640원")
            elif use == 5:
                print("쿠팡 : 28,000원, 11번가 : 28,900원")
                print("최저가 : 28,000원")
            else:
                print("쿠팡 : 36,100원, 지마켓 : 38,000원")
                print("최저가 : 36,100원")
                    
    elif kind == 2:
        region = int(input("지역 선택 <1. 죽전> <2. 보정> <3. 오리> <4. 미금> <5. 수내> <6. 정자> <7. 서현> <8. 기흥> : "))
        
        if region == 1:
            print("정기수거일 : 월, 수, 금")
            print("예약수거일 : 화, 목, 토")
            print("지정시간(하절기) : 20:00시 이후")
            print("지정시간(동절기) : 18:00시 이후")
        elif region == 2:
            print("정기수거일 : 화, 목, 금")
            print("예약수거일 : 월, 수, 토")
            print("지정시간(하절기) : 20:00시 이후")
            print("지정시간(동절기) : 18:00시 이후")
        elif region == 3:
            print("정기수거일 : 월, 목, 금")
            print("예약수거일 : 화, 수, 토")
            print("지정시간(하절기) : 20:00시 이후")
            print("지정시간(동절기) : 18:00시 이후")
        elif region == 4:
            print("정기수거일 : 월, 수, 일")
            print("예약수거일 : 화, 목, 토")
            print("지정시간(하절기) : 20:00시 이후")
            print("지정시간(동절기) : 18:00시 이후")
        elif region == 5:
            print("정기수거일 : 월, 목, 일")
            print("예약수거일 : 화, 수, 토")
            print("지정시간(하절기) : 20:00시 이후")
            print("지정시간(동절기) : 18:00시 이후")
        elif region == 6:
            print("정기수거일 : 월, 화, 수")
            print("예약수거일 : 목, 금, 토")
            print("지정시간(하절기) : 20:00시 이후")
            print("지정시간(동절기) : 18:00시 이후")
        elif region == 7:
            print("정기수거일 : 목, 금, 토")
            print("예약수거일 : 월, 화, 수")
            print("지정시간(하절기) : 20:00시 이후")
            print("지정시간(동절기) : 18:00시 이후")
        elif region == 8:
            print("정기수거일 : 월, 수, 목")
            print("예약수거일 : 화, 토, 일")
            print("지정시간(하절기) : 20:00시 이후")
            print("지정시간(동절기) : 18:00시 이후")
            
    elif kind == 3:
        while True:
            access = int(input("계좌 내역 승인 <1. YES> <2. NO> : "))
            if access == 1:
                break
        
        category = int(input("열람할 내역 선택 <1. 식비> <2. 편의점, 마트, 잡화> <3. 취미, 여가> : "))
        if category == 1:
            print("맥도날드 : -7,800원, 계좌 잔액 : 627,200원, 시간 : 11월 20일 16:18")
        elif category == 2:
            print("교보문고 : -12,000원, 계좌 잔약 : 635,000원, 시간 : 11월 20일 15:30")
        else:
            print("노래연습장 : -3,000원, 계좌 잔액 : 638,000원, 시간 : 11월 20일 15:12")
            
    elif kind == 4:
        choice = int(input("오메추 <1. 내 주변 맛집> <2. 레시피 추천> <3. 랜덤 추천> : "))
        
        if choice == 1:
            menu = int(input("주변 맛집 <1. 한식> <2. 일식> <3. 중식> <4. 양식> : "))
            
            if menu == 1:
                print("신쭈꾸미 주꾸미요리 : 용인 수지구 죽전동, 평점 : 4.47")
                print("선영이네 김치짜글이 전문점 : 용인 수지구 죽전동, 평점 : 4.8")
                print("손가네칼국수 : 용인 수지구 죽전동, 평점 : 4.54")
            elif menu == 2:
                print("아리가또맘마 죽전 단대점 : 용인 수지구 죽전동, 평점 : 4.48")
                print("호식당 : 용인 수지구 죽전동, 평점 : 4.51")
                print("겐코쇼쿠도 단국대점 : 용인 수지구 죽전동, 평점 : unknwon")
            elif menu == 3:
                print("홍콩반점0410 죽전단대점 : 용인 수지구 죽전동, 평점 : unknown")
                print("천향 마라탕 용인점 : 용인 수지구 죽전동, 평점 : 4.43")
                print("동북양꼬치(죽전점) : 용인 수지구 죽전동, 평점 : 4.47")
            else:
                print("오블리끄 : 용인 수지구 죽전동, 평점 : 4.56")
                print("피펜 : 용인 수지구 죽전동, 평점 : unknown")
                print("브라더양식당 : 용인 수지구 죽전동, 평점 : 4.38")
        elif choice == 2:
            print("김치볶음밥 레시피")
            print("1. 김치를 썰어준다.")
            print("2. 팬에 기름을 두르고 김치를 넣고 중불에 볶아준다.")
            print("3. 설탕 1숟갈 반을 넣고 신맛을 날려준다.")
            print("4. 고추장 1큰술 고춧가루 1/2큰술 넣고 색을 맞춘다.")
            print("5. 밥을 볶아준다.")
            print("6. 간을 보고 단맛 or 간이 부족하면 올리고당, 물엿 or 소금으로 조절한다.")
        else:
            rand = random.randint(1, 4)
            if rand == 1:
                print("오늘은 '한식' 어떠세요?")
            elif rand == 2:
                print("오늘은 '일식' 어떠세요?")
            elif rand == 3:
                print("오늘은 '중식' 어떠세요?")
            else:
                print("오늘은 '양식' 어떠세요?")
        
    elif kind == 5:
        convenient = int(input("편의시설 <1. 편의점> <2. 코인 세탁방> <3. 약국> <4. 할인마트> : "))
        
        if convenient == 1:
            print("세븐일레븐 용인단국사랑점 : 용인 수지고 죽전동, 거리 : 150m")
            print("이마트24 용인단국대점 : 용인 수지고 죽전동, 거리 : 150m")
            print("CU 단대보람점 : 용인 수지고 죽전동, 거리 : 150m")
        elif convenient == 2:
            print("워시엔조이 셀프빨래방 용인죽전점 : 용인 수지구 죽전동, 거리 : 150m")
        elif convenient == 3:
            print("대학약국 : 용인 수지고 죽전동, 거리 : 150m")
        else:
            print("세븐일레븐 용인단국사랑점 : 용인 수지고 죽전동, 거리 : 350m")
            print("우미현W마트 : 용인 수지고 죽정동, 거리 : 190m")
            
    else:
        break