import os

#file = open('temp_file.txt', 'w')

#file.write('HELLOW WORLD')

#file.close()

file = open('temp_file.txt', 'r', encoding='UTF-8')

print(file.readlines())