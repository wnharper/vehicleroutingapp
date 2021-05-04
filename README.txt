D1: EXPLANATION OF DATA STRUCTURE
The hash table creates an array of lists which hold objects. A simple hashing function takes the key, in this case,
a unique integer ID, and converts it into an index in order to access the list. The list is able to store multiple
objects (packages) in case there are any duplicate indexes produced by the hashing function. This is a form of collision control
known as chaining.
The hash table also has a resizing function based on load factor. Load factor is calculated by dividing the number of elements
by the size of the current table. Once the load factor exceeds a load of one, the table is resized.

The hash table uses the key value to access the corresponding object in constant time versus a list which will need to
be iterated through and have an linear access time o(n).



