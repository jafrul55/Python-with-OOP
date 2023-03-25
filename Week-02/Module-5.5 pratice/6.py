sample_dict = {
   "name":"Kelly",
   "age":25,
   "salary":8000,
   "city":"New york"
}

keys = ["name","salary"]

dict ={k:sample_dict[k] for k in keys}
print(dict)