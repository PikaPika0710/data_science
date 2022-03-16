#Convert string to ascii num
#Toán tử vecto hoá (element-wise)

import numpy as np

# def convert_to_ascii(text):
#     num = []
#     for char in text:
#         num.append(ord(char))
#     return num

str = "Tran Cong Viet"
li = [ord(char) for char in str]
print(li)

