# BearRobotics
<br><br>
파이썬으로 하나의 메소드안에 잔액조회, 입금, 출금을 전부 만들어보았다. pincard가 올바르지 않을때 에러를 출력하며, 잔액보다 많은 액수를 출금하려 하면 함수가 종료된다. 

<br><br>
사용자의 정보를 db라고 하자
```
db = [[1, {'Kim1': 5000, 'kim2': 10000}]]
```
<br><br>
pincard를 받아올때, 정상 pincard면 pin이라는 flag가 1로 설정된다. 정상적으로 카드가 읽혔다면 사용자가 계좌를 선택한다.
<br><br>

```
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
```
pin flag가 0인경우, 카드를 반환한다.
<br><br>
```
    # Pincard에 대한 에러
    if pin == 0:  # pin의 값을 비교
        print("카드 정보 에러, 다시 시도하거나 카드를 재발급 받으세요")
        return  

```
<br><br>
1,2,3으로 잔액조회와 입금 출금을 결정하며, 조회 시 아까 찾아둔 balance를 출력한다.
<br><br>
```
print("잔액보기는 1, 입금은 2, 출금은 3을 누르세요")
    choice = int(input())
    
    if choice == 1:
        print("남은 잔액은 " + str(balance) + "입니다.")
```
<br><br>
다음은 입금 메소드이다
<br><br>
```
 elif choice == 2:
        print("입금 후 확인을 누르세요.")
        money = int(input())
        balance += money
        db[userNum][1][userName] += money
        print("입금이 완료되었습니다. " + "잔액은" + str(db[userNum][1][userName])+"달러 입니다.")
```
<br><br>
다음은 출금이다. 잔액이 부족하면 에러가 발생한다.
<br><br>
    elif choice == 3:
        print("출금할 금액을 입력하세요.")
        money = int(input())
        if money > balance:
            print("잔액이 부족합니다. 다시 시도해 주세요")
        else:
            print("출금이 완료되었습니다.")
            db[userNum][1][userName] -= money
<br><br><br><br>
# Test
<br><br>
온라인 파이썬 인터프레터로 맨 윗줄의 db를 베이스로 테스트 해보았다.
<br><br>
![image](https://github.com/user-attachments/assets/da9a8ceb-1ce9-4445-8661-eecbfe489c70)

<br><br>




    
   

