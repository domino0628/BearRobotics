db = [[1, {'Kim1': 5000, 'kim2': 10000}]]

def solution(pincard):
    # 핀카드에 대한 flag
    pin, balance, userNum, userName = 0, 0, 0, ''
    
    for i in range(len(db)):
        if db[i][0] == pincard:
            pin = 1
            userNum = i
            print("사용계좌 선택")
            name = input()
            if name in db[i][1]:
                balance = db[i][1][name]
                userName = name
            break  # 계좌 찾으면 반복문 종료

    # Pincard에 대한 에러
    if pin == 0:  # pin의 값을 비교
        print("카드 정보 에러, 다시 시도하거나 카드를 재발급 받으세요")
        return  

    print("잔액보기는 1, 입금은 2, 출금은 3을 누르세요")
    choice = int(input())
    
    if choice == 1:
        print("남은 잔액은 " + str(balance) + "입니다.")
    elif choice == 2:
        print("입금 후 확인을 누르세요.")
        money = int(input())
        balance += money
        db[userNum][1][userName] += money
        print("입금이 완료되었습니다. " + "잔액은" + str(db[userNum][1][userName])+"달러 입니다.") 
    elif choice == 3:
        print("출금할 금액을 입력하세요.")
        money = int(input())
        if money > balance:
            print("잔액이 부족합니다. 다시 시도해 주세요")
        else:
            print("출금이 완료되었습니다.")
            db[userNum][1][userName] -= money

# 예제
solution(1)    
