print('-' * 40)
print('   cm    mm    m   inch')
print('-' * 40)

for cm in range(1 , 101) :
    mm = cm * 10.0
    m = cm * 0.01
    inch = cm * 0.3937
    print('%d , %d , %d , %.2f')