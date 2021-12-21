print('結賬系統')
cost = int(input('請輸入商品價格:'))
if cost >= 2000:
    print('您的商品已打折。')
    print(cost*0.9)
else :
    print(cost)
print('謝謝惠顧')
