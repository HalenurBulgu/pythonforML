# -*- coding: utf-8 -*-

setA = { 1,2,3}
setB = {3,5}
print(setA - setB)
print(setA.difference(setB))
print(setB.difference(setA))

#kesişim hariç-farkların birleşimi
setA = { 1,2,3}
setB = {3,5}
print(setA ^ setB)
print(setB.symmetric_difference(setA))
