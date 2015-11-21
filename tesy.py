#-*- coding:utf-8 -*-
shoplist = ['apple', 'mango', 'carrot', 'banana']
print ('The first item I will buy is', shoplist[0])
olditem = shoplist[0]
del shoplist[0]  #del的是引用，而不是对象
print ('I bought the',olditem)
print ('My shopping list is now', shoplist)
print(shoplist[0])