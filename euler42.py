import csv
import string
import math

def isTri(num):
    n = (1+math.sqrt(1+8*num))/2
    if n%1 == 0:
        return True
    else:
        return False

    
alpha = dict(enumerate(list(' '+string.ascii_uppercase)))
alpha = {v: k for k, v in alpha.items()}

with open('p042_words.txt', 'r') as f:
  reader = csv.reader(f)
  word_list = list(reader)

words = word_list[0]

trinums = 0

for word in words:
    wval = 0
    for letter in word:
        wval += alpha[letter]
    if isTri(wval):
        trinums += 1
