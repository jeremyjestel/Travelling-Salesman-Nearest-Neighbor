#This code is partially sourced and cited from the following reference provided by WGU
# C950 - Webinar-1 - Let’s Go Hashing
# W-1_ChainingHashTable_zyBooks_Key-Value.py
# Ref: zyBooks: Figure 7.8.2: Hash table using chaining.
from classes.package import package

class hash_table:
    #initialize the hash table
    def __init__(self, initial_capacity=10):
        self.table = []
        for i in range(initial_capacity):
            self.table.append([])

    #insert a key and value into the hash table
    def insert(self, key, item):
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]
        for val in bucket_list:
            # print (key_value)
            if val[0] == key:
                val[1] = item
                return True
        key_value = [key, item]
        bucket_list.append(key_value)
        for i in range(len(self.table)):
            if (len(bucket_list) > 3):
                self.resize(len(self.table)+1)
                i = 0
        return True

    #resize the table until all buckets are chained less than 4 deep
    def resize(self, new_size):
        new_table = []
        for i in range(new_size):
            new_table.append([])
        for item in self.table:
            for pair in item:
                if pair is not None:
                    key, value = pair
                    new_index = hash(key) % new_size
                    bucket_list = new_table[new_index]
                    key_value = [key, value]
                    bucket_list.append(key_value)
        self.table = new_table

        #Find a value with key in table
    def search(self, key):
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]
        for kv in bucket_list:
            if kv[0] == key:
                return kv[1]
        return None
    #adds all rows in file as packages in table
    def pop_table(self, pack_file):
        i = 0
        packages = [None] * len(pack_file)
        for row in pack_file:
            packages[i] = package(row)
            self.insert(packages[i].id, packages[i])
            i += 1
    #change the status of an array of packages to en route
    def enroute(self, packs):
        for pack in packs:
            obj = self.search(pack)
            obj.status = "En Route"