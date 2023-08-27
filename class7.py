import pandas as pd

#dictonary
data = {
    "roll_num":[1,2,3],
    "name":["a","b","c"],
    "course":["AI","DS","ML"]
}

print(data)

df = pd.DataFrame(data)
print(df)

d = {
    "name":"hasan",
    100: "age",
    #tuple
    (1,2,3) : "ABCD"
}

#you can't add list to dictionary
print(d)

#list is mutable: it means it can change
#immutable: it means it cant change


#list = [elem1,elem2,....]
#tuple = (elem1, elem2, ....)
#dictionary - {"key":"value", key:value}
#set = {"elem1", "elem2",.....}