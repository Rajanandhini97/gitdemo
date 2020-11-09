
values = [22, 25, "Aishu", 8, 6]
# List is a data type that allows multiple values and can be different data types

print(values[0]) #22

print(values[-1]) #6

print(values[2]) #Aishu

print(values[1:3]) # 25 aishu

values.insert(3, "Nallusamy")
print(values)

values.append("tata")
print(values)
values[2] = "Aishwarya"
del values[1]

print(values)

# Tuple Datatype
val = (1, 2, 3, "Nandhini")
print(val)

# val[3] = "NANDHINI"
# print(val)

# Dictionary datatype

d = {"a": 2, 4: "bcd", "c": "Hello Montreal"}
print(d[4])
print(d["c"])

dict = {}

dict["first name"] = "Nandhini"
dict["Last name"] = "Nallusamy"
print(dict)
print(dict["first name"])