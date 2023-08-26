# 1. ♻️반복문

<br>

## 1.1. 🎇반복문이란?

> #### 컴퓨터가 가장 잘하는 것 중 하나가 똑같은 작업을 반복하는 것이다. 프로그래밍 언어에서 반복문은 같은 블록의 코드를 반복해서 수행할 때 사용된다.

> ### 파이썬의 반복문에는 다음의 두 가지가 존재 한다.

```
1. for문

2. while문
```

---

<br>

> 프로그램에서 반복문을 사용하지 않았을 경우와 반복문을 사용했을 경우를 서로 비교해보자.

- #### 반복문을 사용하지 않은 경우

```py
print('안녕하세요!')
print('안녕하세요!')
print('안녕하세요!')
print('안녕하세요!')
print('안녕하세요!')

# 실행결과
# 안녕하세요!
# 안녕하세요!
# 안녕하세요!
# 안녕하세요!
# 안녕하세요!
```

- #### 반복문을 사용한 경우

```py
for x in range(5):
    print('안녕하세요!')

# 실행결과
# 안녕하세요!
# 안녕하세요!
# 안녕하세요!
# 안녕하세요!
# 안녕하세요!
```

> ### 이처럼 반복문을 사용하면 복잡한 코드를 효율적이고 간편하게 사용할수 있다.

---

<br>

## 1.2. 🎇for문

> for는 '~ 하는 동안' 이란 의미를 갖는다. 파이썬을 포함한 많은 프로그래밍 언어에서 사용되는 for문은 주어진 조건에 따라 문장들을 반복 수행하게 된다.

---

<br>

### 🌟1.2.1. for문의 기본 구조

```py
sum = 0

for i in range(1 , 11) :
    sum = sum + i
    print('i의 값 : %d => 합계 : %d' % (i , sum))

# 실행결과
# i의 값 : 1 => 합계 : 1
# i의 값 : 2 => 합계 : 3
# i의 값 : 3 => 합계 : 6
# i의 값 : 4 => 합계 : 10
# i의 값 : 5 => 합계 : 15
# i의 값 : 6 => 합계 : 21
# i의 값 : 7 => 합계 : 28
# i의 값 : 8 => 합계 : 36
# i의 값 : 9 => 합계 : 45
# i의 값 : 10 => 합계 : 55
```

- 위에서 사용된 for문의 서식은 다음과 같다

```
for 변수 i in range(반복횟수의 범위) :
(tab) 문장 1
(tab) 문장 2
    ......
```

> range( )함수가 나타내는 반복 횟수의 범위 동안 문장 1 , 문장 2 , ..... 가 반복 수행된다. 이떄 변수는 반복 루프 동안 반복 횟수의 범위에 있는 값을 가진다

---

<br>

### 🌟1.2.2. range( ) 함수

```py
for i in range(10) :
    print(i , end = " ")
print()
---------------------------

for i in range(1 , 11) :
    print(i , end = " ")
print()
---------------------------

for i in range(1 , 10 , 2) :
    print(i , end = " ")
print()
---------------------------

for i in range(20 , 0 , -2) :
    print(i , end = " ")
print()
---------------------------

# 실행결과
# 0 1 2 3 4 5 6 7 8 9
# 1 2 3 4 5 6 7 8 9 10
# 1 3 5 7 9
# 20 18 16 14 12 10 8 6
```

---

<br>

- 위 코드에서 사용된 range( ) 함수는 다음의 세 가지 형식으로 사용된다

```
서식 1

for 변수 i in range(종료값) :
(tab) 문장 1 ,  문장 2
```

> range(종료값)은 0에서 종료값 - 1 의 정수 범위를 갖게 된다. 그리고 변수는 각 반복 루프에서 range( )범위에 있는 각각의 값을 가지게 된다. 예를 들어 range(10) 은 0 에서 9 까지의 정수 범위를 의미한다.

<br>

```
서식 2

for 변수 in range(시작값 ,  종료값) :
(tab) 문장 1 , 문장 2 , ....
```

> range(시작값 , 종료값)은 시작값에서 종료값 - 1의 정수 범위를 갖는다.

---

<br>

```
서식 3

for 변수 in range(시작값 ,  종료값 , 증가_감소) :
(tab) 문장 1 , 문장 2 , ....
```

> range(시작값 , 종료값 , 증가*감소)는 시작값에서 종료값 - 1 사이의 정수 범위를 갖는데 각 정수 사이의 간격은 증가*감소에 의해 결정된다. 예를 들어 range(1 , 11 , 2)는 1에서 10 까지의 정수 중에서 2씩 증가하는 범위를 나타내기 때문에 정수 1, 3, 5 , 7 , 9 의 값을 의미한다.

---

<br>

## 1.3. 🎇이중 for문

> 이중 for문은 for문을 이중으로 사용하는 것을
> 말한다.

### 1.3.1. 🌟이중 for문을 사용한 코드

```py
print('-' * 30)

for a in range(2 , 10) :
    for b in range(1 , 10) :
        print('%d x %d = %d' %(a , b , a * b))

print('-' * 30)

#실행결과
# 2 x 1 = 2
# 2 x 2 = 4
# 2 x 3 = 6
# 2 x 4 = 8
# 2 x 5 = 10
# 2 x 6 = 12
# 2 x 7 = 14
# 2 x 8 = 16
# 2 x 9 = 18
# 3 x 1 = 3
# 3 x 2 = 6
# 3 x 3 = 9
# 3 x 4 = 12
# 3 x 5 = 15
# 3 x 6 = 18
# 3 x 7 = 21
# 3 x 8 = 24
# 3 x 9 = 27
# 4 x 1 = 4
# 4 x 2 = 8
# 4 x 3 = 12
# 4 x 4 = 16
# 4 x 5 = 20
# 4 x 6 = 24
# 4 x 7 = 28
# 4 x 8 = 32
# 4 x 9 = 36
# 5 x 1 = 5
# 5 x 2 = 10
# 5 x 3 = 15
# 5 x 4 = 20
# 5 x 5 = 25
# 5 x 6 = 30
# 5 x 7 = 35
# 5 x 8 = 40
# 5 x 9 = 45
# 6 x 1 = 6
# 6 x 2 = 12
# 6 x 3 = 18
# 6 x 4 = 24
# 6 x 5 = 30
# 6 x 6 = 36
# 6 x 7 = 42
# 6 x 8 = 48
# 6 x 9 = 54
# 7 x 1 = 7
# 7 x 2 = 14
# 7 x 3 = 21
# 7 x 4 = 28
# 7 x 5 = 35
# 7 x 6 = 42
# 7 x 7 = 49
# 7 x 8 = 56
# 7 x 9 = 63
# 8 x 1 = 8
# 8 x 2 = 16
# 8 x 3 = 24
# 8 x 4 = 32
# 8 x 5 = 40
# 8 x 6 = 48
# 8 x 7 = 56
# 8 x 8 = 64
# 8 x 9 = 72
# 9 x 1 = 9
# 9 x 2 = 18
# 9 x 3 = 27
# 9 x 4 = 36
# 9 x 5 = 45
# 9 x 6 = 54
# 9 x 7 = 63
# 9 x 8 = 72
# 9 x 9 = 81
```

---

<br>

## 1.4. 🎇while문

> while문은 for문과 함께 많이 사용되는 반복문으로서 사용 형태는 다음과 같다.

```
while 조건식 :
(tab) 문장 1
(tab) 문장 2
      ......
```

> while문은 조건식이 참인 동안 들여쓰기 되어 있는 문장 1 , 문장 2 , ... 이 반복 수행된다.

---

<br>

### 1.4.1. 🌟while문의 기본 구조

```py
sum = 0
i = 1

while i <= 10 :
    sum = sum + i
    print('i의 값 : %2d => 합계 : %d' %(i , sum))

    i = i + 1

# 실행결과
# i의 값 :  1 => 합계 : 1
# i의 값 :  2 => 합계 : 3
# i의 값 :  3 => 합계 : 6
# i의 값 :  4 => 합계 : 10
# i의 값 :  5 => 합계 : 15
# i의 값 :  6 => 합계 : 21
# i의 값 :  7 => 합계 : 28
# i의 값 :  8 => 합계 : 36
# i의 값 :  9 => 합계 : 45
# i의 값 : 10 => 합계 : 55
```

---

> while문은 기본적으로 세 가지 구성 요소를 가지고 있다.

```
변수_초기화

while 조건식 :
(tab) 문장 1
(tab) 문장 2
      .....
(tab) 변수값_증가_감소
```

---

<br>

## 1.5. 🎇break문으로 빠져 나가기

> for문이나 while문을 사용하다 보면 반복 루프를 수행 중 중간에 루프를 빠져나가고 싶은 경우가 종종 생긴다. 이 떄 사용하는 것이 break문이다. 일반적으로 break문은 if문과 같이 사용되어 반복 로푸가 진행되는 동안 조건식을 만족하면 반복 루프를 빠져 나가게 한다.

---

### 1.5.1. 🌟break문으로 반복 루프 빠져 나가기

```py
for i in range(1 , 1001) :
    print(i)

    if i == 10 :
        break

# 실행결과
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
```