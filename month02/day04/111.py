import re

print(re.findall('[A-Z][a-z]*', "How are you,Jame."))
print(re.findall('[A-Z][a-z]+', "How are you,Jame.ABC,A,C,B"))

print(re.findall("[0-9]+", "小明身高:175cm 体重:70kg"))

print(re.findall("-?[0-9]+", "当前海拔:83m,温度:-22度"))

print(re.findall("1[0-9]{10}", "13067854336,15067854336,17067854336"))

print(re.findall('[0-9]{4}-[0-9]{1,2}-[0-9]{1,2}', "2020-12-1"))

print(re.search(r'(\d{1,3}\.){3}\d{1,3}', "92.18.22.65").group())
