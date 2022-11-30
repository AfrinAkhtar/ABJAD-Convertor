from info import data
#User is asked to input an arabic phrase
phrase = input("Arabic Phrase: ")
#Total numerical value of phrase is num 
num = 0
#Function convert runs through data tuples and adds value to num
def convert(phrase):
  global num
  for element in phrase:
    x = 0
    while x < (len(data)-1):
      if data[x][0] == element:
        num = num + data[x][1]
        x += 1
      else:
        x += 1
     
convert(phrase)
print(num)

