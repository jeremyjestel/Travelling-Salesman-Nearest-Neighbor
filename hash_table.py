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

        if (len(bucket_list) > 3):
            self.resize(len(self.table)+1)
        key_value = [key, item]
        bucket_list.append(key_value)
        return True

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


    def search(self, key):
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]
        for kv in bucket_list:
            if kv[0] == key:
                return kv[1]
        return None