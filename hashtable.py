class HashTable:
    def __init__(self, size):
        self.size = size
        self.num_elements = 0
        self.arr = [[] for i in range(self.size)]

    # Generates a hashcode from the given key
    def get_string_hash(self, key):
        h_key = 0
        prime = 31
        # Iterate through key string
        for letter in key:
            h_key = h_key + ord(letter) * prime  # convert to unicode and multiply by prime
        h_key = h_key & 0x7FFFFFFF  # make hash key positive
        return h_key % self.size  # mod hash key by table size

    # Simple hashing function knowing that the key will always be a unique integer
    def get_hash(self, key):
        x = int(key)
        return x % self.size

    # Add an item into the hashtable
    def __setitem__(self, key, value):
        if self.load_factor() > 1:
            self.resize_table(self.size * 2)
        h_key = self.get_hash(key)
        kv = (key, value)
        # Check to see if key already exists, if so, replace value
        for index, element in enumerate(self.arr[h_key]):
            if element[0] == key:
                self.arr[h_key][index] = kv
                return

        self.arr[h_key].append(kv)
        self.num_elements += 1

    # Retrieve an item from the hashtable
    def __getitem__(self, key):
        hash = self.get_hash(key)
        for element in self.arr[hash]:
            if element[0] == key:
                return element[1]

    # Remove an item from the hashtable
    def __delitem__(self, key):
        h_key = self.get_hash(key)
        for element_key, element_val in self.arr[h_key]:
            if element_key == key:
                self.arr[h_key].remove((element_key, element_val))
        self.num_elements -= 1

    # Resize the table
    def resize_table(self, new_size):
        self.size = new_size
        temp_array = [[] for i in range(new_size)]

        for list_element in self.arr:
            for element in list_element:
                h_key = self.get_hash(element[0])
                kv = (element[0], element[1])
                temp_array[h_key].append(kv)

        self.arr = temp_array

    # Calculates the load factor of the hashtable
    def load_factor(self):
        return self.num_elements / self.size




