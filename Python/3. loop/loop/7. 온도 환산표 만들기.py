print('-' * 30)
print(' 섭씨 화씨')
print('-' * 30)

for c in range(-20 , 31 , 5) :
    f = c * 9.0 / 5.0 + 32.0
    print('%5d %6.1f' % (c , f))

# 실행결과

#-----------------------------
 #섭씨 화씨
#------------------------------
  # -20   -4.0
  # -15    5.0
  # -10   14.0
   # -5   23.0
    # 0   32.0
    # 5   41.0
    # 10   50.0
   # 15   59.0
    # 20   68.0
    # 25   77.0
    # 30   86.0