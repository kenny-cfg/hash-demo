def my_hash(string):
    hash_value = 0
    for letter in string:
        hash_value += ord(letter)
    return hash_value % 5


class MySet:
    def __init__(self):
        self.storage = []
        for number in range(5):
            self.storage.append([])

    def put(self, item):
        hash_value = my_hash(item)
        bucket = self.storage[hash_value]
        for bucket_item in bucket:
            if item == bucket_item:
                return
        bucket.append(item)

    def has(self, item):
        hash_value = my_hash(item)
        bucket = self.storage[hash_value]
        for bucket_item in bucket:
            if item == bucket_item:
                return True
        return False


if __name__ == '__main__':
    print(ord('A'))