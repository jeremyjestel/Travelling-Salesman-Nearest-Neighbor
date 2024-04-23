
class ChainingHashTable:
    def __init__(self, initial_capacity=100):
        self.table = []
        for i in range(initial_capacity):
            self.table.append([])


    def insert(self, key, item):
        bucket = hash(key) % len(self.table)
        key_value = [key, item]
        while True:
            if bucket == len(self.table):
                bucket = 0
            if self.table[bucket] == None:
                self.table[bucket] = key_value
                break
            else:
                bucket += 1
        return True

    def search(self, key):
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        for kv in bucket_list:
            if kv[0] == key:
                return kv[1]
        return None

    def remove(self, key):
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]
        for kv in bucket_list:
            # print (key_value)
            if kv[0] == key:
                bucket_list.remove([kv[0], kv[1]])


bestMovies = [
    [1, "CITIZEN KANE - 1941"],
    [2, "CASABLANCA - 1942"],
    [3, "THE GODFATHER - 1972"],
    [4, "GONE WITH THE WIND - 1939"],
    [5, "LAWRENCE OF ARABIA - 1962"],
    [6, "THE WIZARD OF OZ - 1939"],
    [7, "THE GRADUATE - 1967"],
    [8, "ON THE WATERFRONT- 1954"],
    [9, "SCHINDLER'S LIST -1993"],
    [10, "SINGIN' IN THE RAIN - 1952"],
    [11, "STAR WARS - 1977"]
]

myHash = ChainingHashTable()

print("\nInsert:")
myHash.insert(bestMovies[0][0], bestMovies[0][1])  # 2nd bucket; Key=1, item="CITIZEN KANE - 1941"
print(myHash.table)
