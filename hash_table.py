#This code is partially sourced and cited from the following reference provided by WGU
# C950 - Webinar-1 - Let’s Go Hashing
# W-1_ChainingHashTable_zyBooks_Key-Value.py
# Ref: zyBooks: Figure 7.8.2: Hash table using chaining.


class hash_table:
    def __init__(self, initial_capacity=10):
        self.table = []
        for i in range(initial_capacity):
            self.table.append([])

    def insert(self, key, item):
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]
        for val in bucket_list:
            # print (key_value)
            if val[0] == key:
                val[1] = item
                return True

        if len(bucket_list > 3):
            self.resize(len(self.table)+1)
        self.insert(key, item)
        return True

    def search(self, key):
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]
        for kv in bucket_list:
            if kv[0] == key:
                return kv[1]
        return None

    def resize(self, new_size):
        new_table = [None] * new_size

        for item in self.table:
            if item is not None:
                key, value = item
                new_index = hash(key) % new_size
                new_table[new_index] = (key, value)

        self.table = new_table
    def remove(self, key):
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        for kv in bucket_list:
            if kv[0] == key:
                bucket_list.remove([kv[0], kv[1]])