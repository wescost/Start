import re

s="eeaareraahdaaakskkjaaghggkaakkw"
array=re.split("a+",s)
print(array)

array=re.split("a{3}",s)
print(array)

array=re.split("a*",s)
print(array)

