from math import hypot
cate= float(input('digite o cateto oposto '))
cate2= float(input('digite o cateto adjacente '))
hip= hypot(cate,cate2)
print(f'se o cateto oposto é {cate} e o adjacente é {cate2} a hipotenusa é {hip:.2f}')