# -*- coding: utf-8 -*-
"""missing_char.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1tslC0_HZwexwegktyTljndccneO0exy-
"""

#missing_char

def missing_char(word, n):
      list1=list(word)
      list1.pop(n)
      list1="".join(list1)
      return list1
print(missing_char('kalemlik',5))