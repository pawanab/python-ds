class HashInitial(object):
    def __init__(self, key: str, value=None):
        self.key = key
        self.value = value

    @property
    def hash(self) -> int:
        """return entry's hash"""
        return len(self.key)

    def __repr__(self):
        return f"<HashInitial hash={self.hash}, key={self.key}, value={self.value}>"

    def __str__(self):
        return str(self.value)

    def __eq__(self, other: object) -> bool:
        """Check equation with other entries, e.g dict['a'] == dict['b']"""
        if not isinstance(other, HashInitial):
            return NotImplemented
        return self.value == other.value

    def compare_hash(self, other: object) -> bool:
        """compare keys and hashes with different entry"""
        if not isinstance(other, HashInitial):
            return NotImplemented
        return self.key == other.key and self.hash == other.hash


class HashTable(object):
    def __init__(self, size=10):
        self.entries = [None for _ in range(size * 2)]
        self.size = size
        self.actual_size = size * 2
        self.filled_entries = 0

    def __getitem__(self, key: str) -> HashInitial:
        """subscript method - object[key]
        use hashing function to find the index"""
        first = HashInitial(key)
        index = first.hash % self.actual_size
        index_val = self.entries[index]

        while index_val and not first.compare_hash(index_val):
            index = (index + 1) % self.actual_size
            index_val = self.entries[index]

        if index_val == None:
            raise KeyError
            # both keys and hashes match
        return index_val

    def __setitem__(self, key: str, value: any) ->int:
        """allow insertion of items with object[key] = value"""
        if self.filled_entries == self.size:
            # no more room
            raise KeyError

        entry = HashInitial(key, value)
        index = entry.hash % self.actual_size
        existing_entry = self.entries[index]

        if existing_entry and not entry.compare_hash(existing_entry):
            # don't overlap existing values
            index = (index + 1) % self.actual_size
            existing_entry = self.entries[index]
        self.entries[index] = entry
        self.filled_entries += 1

        return index
