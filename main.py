import random
print("기차 예약 시스템")
places=["인천","서울","용인","대전","대구","울산","부산"]
guest_information=[]
trains=[]
isfirst=True
isplace = False
for i in range(50):
    time=random.randint(10,21)
    time_change=(f"{time}:00")
    place1=random.choice(places)
    place2=random.choice(places)
    while place1==place2:
        place1=random.choice(places)
        place2=random.choice(places)
    trains.append([place1,place2,time_change,abs(places.index(place1)-places.index(place2))])
def reservation(name):
    global guest_information,isfirst,isplace
    isplace=False
    guest=[]
    print(f"장소 선택 : {places}")
    start=input("출발지 : ")
    for place in places:
        if place == start:
            isplace=True
    if isplace == True:
        guest.append(name)
        guest.append(start)
        price=0
        print("-------------------------")
        able=[]
        for place in places:
            if guest[1]==place:
                for i in range(len(trains)):
                    if trains[i][0]==place:
                        print(f"{len(able)+1}. 출발지 : {trains[i][0]}, 목적지 : {trains[i][1]}, 출발 시간 : {trains[i][2]}")
                        able.append(trains[i])
        print("-------------------------")
        choice=int(input("기차 선택(번호로) : "))
        for i in range(len(able)):
            if choice-1==i:
                price=able[i][3]*10000
                guest.append(able[i][1])
                guest.append(able[i][2])

        while True:
            seat=input("좌석 선택 [특석/일반석] : ")
            if seat=="특석":
                price+=20000
                break
            elif seat=="일반석":
                price+=5000
                break
            else:
                print("오류")
        guest.append(seat)
        guest.append(price)
        guest_information.append(guest)
        print(f"이름 : {guest[0]}, 출발지 : {guest[1]}, 목적지 : {guest[2]}, 출발 시간 : {guest[3]}, 좌석 : {guest[4]}, 가격 : {guest[5]}")

        if isfirst == True:
            isfirst = False
            with open("guest.txt","w", encoding="utf-8") as file :
                file.write(f"이름 : {guest[0]}, 출발지 : {guest[1]}, 목적지 : {guest[2]}, 출발 시간 : {guest[3]}, 좌석 : {guest[4]}, 가격 : {guest[5]}\n")
        elif isfirst==False:
            with open("guest.txt","a", encoding="utf-8") as file :
                file.write(f"이름 : {guest[0]}, 출발지 : {guest[1]}, 목적지 : {guest[2]}, 출발 시간 : {guest[3]}, 좌석 : {guest[4]}, 가격 : {guest[5]}\n")
        input("위 내용을 확인하셨으면 [엔터]를 눌러주세요...")
    else:
        print("오류")
def check():
    for inf in guest_information:
        if inf[0]==name:
            print(f"이름 : {inf[0]}, 출발지 : {inf[1]}, 목적지 : {inf[2]}, 출발 시간 : {inf[3]}, 좌석 : {inf[4]}, 가격 : {inf[5]}")

while True:
    name=input("이름 : ")
    #메뉴 처리
    print("1. 기차 예약 ")
    print("2. 예약 확인")
    print("3. 나가기")
    try:
        menu=int(input("메뉴 선택(번호) : "))  
        if menu == 1:
            reservation(name)
        elif menu == 2:
            check()
        elif menu == 3:
            break
        else:
            print("오류")
    except ValueError:
        print("숫자를 입력해주세요")
    print()
    print("-------------------------")
    print()
