import re
text = """We love$ Pakistan !
and We want to leave this $ country to be a good Citizen"""
print(re.findall("W",text,))
print(re.findall("W",text,re.IGNORECASE))

#single Dot is used to get signle characters one by one
print(re.findall(".",text))

#two dots chareater is used to get two charaters together
print(re.findall("..",text))

#.+ will take the emlements untill the is no \n or line break
print(re.findall(".+",text,re.IGNORECASE))

#c.+ will start from c and when line break or \n
print(re.findall("c.+",text,re.IGNORECASE))

print(re.findall(".+!$",text,re.IGNORECASE))