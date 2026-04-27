print("기차 예약 시스템")
name=input("이름 : ")
places=["서울","부산","대구","대전","강원"]
guest_information=[]
trains = [["서울","부산","11:00",5],["강원","서울","14:00",3],["부산","대구","16:00",2],["대전","부산","17:00",3],["대구","대전","19:00",1]]
guest=[]
print(places)
start=input("출발지 : ")
guest.append(name)
guest.append(start)
price=0
print("-------------------------")
able=[]
if guest[1]=="서울":
    if trains[0][0]=="서울":
        print(f"{len(able)+1}. 출발지 : {trains[0][0]}, 목적지 : {trains[0][1]}, 출발 시간 : {trains[0][2]}")
        able.append(trains[0])
    if trains[1][0]=="서울":
        print(f"{len(able)+1}. 출발지 : {trains[1][0]}, 목적지 : {trains[1][1]}, 출발 시간 : {trains[1][2]}")
        able.append(trains[1])
    if trains[2][0]=="서울":
        print(f"{len(able)+1}. 출발지 : {trains[2][0]}, 목적지 : {trains[2][1]}, 출발 시간 : {trains[2][2]}")
        able.append(trains[2])
    if trains[3][0]=="서울":
        print(f"{len(able)+1}. 출발지 : {trains[3][0]}, 목적지 : {trains[3][1]}, 출발 시간 : {trains[3][2]}")
        able.append(trains[3])
    if trains[4][0]=="서울":
        print(f"{len(able)+1}. 출발지 : {trains[4][0]}, 목적지 : {trains[4][1]}, 출발 시간 : {trains[4][2]}")
        able.append(trains[4])
if guest[1]=="부산":
    if trains[0][0]=="부산":
        print(f"{len(able)+1}. 출발지 : {trains[0][0]}, 목적지 : {trains[0][1]}, 출발 시간 : {trains[0][2]}")
        able.append(trains[0])
    if trains[1][0]=="부산":
        print(f"{len(able)+1}. 출발지 : {trains[1][0]}, 목적지 : {trains[1][1]}, 출발 시간 : {trains[1][2]}")
        able.append(trains[1])
    if trains[2][0]=="부산":
        print(f"{len(able)+1}. 출발지 : {trains[2][0]}, 목적지 : {trains[2][1]}, 출발 시간 : {trains[2][2]}")
        able.append(trains[2])
    if trains[3][0]=="부산":
        print(f"{len(able)+1}. 출발지 : {trains[3][0]}, 목적지 : {trains[3][1]}, 출발 시간 : {trains[3][2]}")
        able.append(trains[3])
    if trains[4][0]=="부산":
        print(f"{len(able)+1}. 출발지 : {trains[4][0]}, 목적지 : {trains[4][1]}, 출발 시간 : {trains[4][2]}")
        able.append(trains[4])
if guest[1]=="대구":
    if trains[0][0]=="대구":
        print(f"{len(able)+1}. 출발지 : {trains[0][0]}, 목적지 : {trains[0][1]}, 출발 시간 : {trains[0][2]}")
        able.append(trains[0])
    if trains[1][0]=="대구":
        print(f"{len(able)+1}. 출발지 : {trains[1][0]}, 목적지 : {trains[1][1]}, 출발 시간 : {trains[1][2]}")
        able.append(trains[1])
    if trains[2][0]=="대구":
        print(f"{len(able)+1}. 출발지 : {trains[2][0]}, 목적지 : {trains[2][1]}, 출발 시간 : {trains[2][2]}")
        able.append(trains[2])
    if trains[3][0]=="대구":
        print(f"{len(able)+1}. 출발지 : {trains[3][0]}, 목적지 : {trains[3][1]}, 출발 시간 : {trains[3][2]}")
        able.append(trains[3])
    if trains[4][0]=="대구":
        print(f"{len(able)+1}. 출발지 : {trains[4][0]}, 목적지 : {trains[4][1]}, 출발 시간 : {trains[4][2]}")
        able.append(trains[4])
if guest[1]=="대전":
    if trains[0][0]=="대전":
        print(f"{len(able)+1}. 출발지 : {trains[0][0]}, 목적지 : {trains[0][1]}, 출발 시간 : {trains[0][2]}")
        able.append(trains[0])
    if trains[1][0]=="대전":
        print(f"{len(able)+1}. 출발지 : {trains[1][0]}, 목적지 : {trains[1][1]}, 출발 시간 : {trains[1][2]}")
        able.append(trains[1])
    if trains[2][0]=="대전":
        print(f"{len(able)+1}. 출발지 : {trains[2][0]}, 목적지 : {trains[2][1]}, 출발 시간 : {trains[2][2]}")
        able.append(trains[2])
    if trains[3][0]=="대전":
        print(f"{len(able)+1}. 출발지 : {trains[3][0]}, 목적지 : {trains[3][1]}, 출발 시간 : {trains[3][2]}")
        able.append(trains[3])
    if trains[4][0]=="대전":
        print(f"{len(able)+1}. 출발지 : {trains[4][0]}, 목적지 : {trains[4][1]}, 출발 시간 : {trains[4][2]}")
        able.append(trains[4])
if guest[1]=="강원":
    if trains[0][0]=="강원":
        print(f"{len(able)+1}. 출발지 : {trains[0][0]}, 목적지 : {trains[0][1]}, 출발 시간 : {trains[0][2]}")
        able.append(trains[0])
    if trains[1][0]=="강원":
        print(f"{len(able)+1}. 출발지 : {trains[1][0]}, 목적지 : {trains[1][1]}, 출발 시간 : {trains[1][2]}")
        able.append(trains[1])
    if trains[2][0]=="강원":
        print(f"{len(able)+1}. 출발지 : {trains[2][0]}, 목적지 : {trains[2][1]}, 출발 시간 : {trains[2][2]}")
        able.append(trains[2])
    if trains[3][0]=="강원":
        print(f"{len(able)+1}. 출발지 : {trains[3][0]}, 목적지 : {trains[3][1]}, 출발 시간 : {trains[3][2]}")
        able.append(trains[3])
    if trains[4][0]=="강원":
        print(f"{len(able)+1}. 출발지 : {trains[4][0]}, 목적지 : {trains[4][1]}, 출발 시간 : {trains[4][2]}")
        able.append(trains[4])
print("-------------------------")
choice=int(input("기차 선택(번호로) : "))
if choice==1:
    price=able[0][3]*10000
    guest.append(able[0][1])
    guest.append(able[0][2])
elif choice==2:
    price=able[1][3]*10000
    guest.append(able[0][1])
    guest.append(able[0][2])
seat=input("좌석 선택 [특석/일반석] : ")
if seat=="특석":
    price+=20000
elif seat=="일반석":
    price+=5000
else:
    print("오류")
guest.append(seat)
guest.append(price)
print(guest)
guest_information.append(guest)
print(f"출발지 : {guest[1]} 목적지 : {guest[2]}, 출발 시간 : {guest[3]}, 좌석 : {guest[4]}, 가격 : {guest[5]}")
