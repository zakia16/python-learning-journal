'''
# What is Pickle?
`pickle` is used for **serializing and deserializing** Python objects.
It converts in-memory objects into a byte stream that can be stored or transmitted.

# Key Concepts
- Serialization (`pickle.dumps`, `pickle.dump`)
- Deserialization (`pickle.loads`, `pickle.load`)
- Used for saving Python objects to files or sending over networks
- Not safe for untrusted data
'''

import pickle

# Initializing data to be stored in database
Omkar = {'key': 'Omkar', 'name': 'Omkar Pathak', 'age': 21, 'pay': 40000}
Jagdish = {'key': 'Jagdish', 'name': 'Jagdish Pathak', 'age': 50, 'pay': 50000}

# Creating a database dictionary
db = {}
db['Omkar'] = Omkar
db['Jagdish'] = Jagdish

# Serializing (converting to bytes)
b = pickle.dumps(db)  # b is of type <class 'bytes'>

# Deserializing (loading back to Python object)
myEntry = pickle.loads(b)

# Printing the loaded data
print(myEntry)
