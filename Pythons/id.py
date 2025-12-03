ids =  [4353, 2314, 2956, 3382, 9362, 3900]
ids.remove(3382)
print(ids)
id = ids.index(9362)
print(id)
ids.insert(id+1,4492)
print(ids)
ids.extend([3345,5567])
print(ids)

ids.reverse()
print(ids)
ids.sort()
print(ids)