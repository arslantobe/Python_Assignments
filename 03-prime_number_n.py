# -*- coding: utf-8 -*-
"""prime_number_n.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1tzMSl0Y8g4nLm8cA3XyxuQl6jFaVN-rp
"""

n=int(input("sayı gir:"))     # n'e kadar olan asal sayıları bulma 

p1=[]
for i in range(1,n+1):
  a=0
  for ii in range(1,i+1):
    if i%ii==0:
      a+=1
  if (i==0) or (i==1) or a>=3:
      print(i,"asal değil")
  else:
      p1.append([i])
print(f"n={n} asal sayılar:{p1}")