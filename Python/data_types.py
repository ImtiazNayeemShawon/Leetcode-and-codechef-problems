# Python Built-in Data Types Examples

# Text Type: Used to represent textual data.
string_var = "Hello, World!"  # str

# Numeric Types: Used to represent numbers.
int_var = 42                 # int (integer numbers)
float_var = 3.14159          # float (floating point numbers)
complex_var = 2 + 3j         # complex (complex numbers with real and imaginary parts)

# Sequence Types: Used to store multiple items in a specific order.
# List: Mutable, ordered, allows duplicate elements.
list_var = [1, 2, 3]         # list (mutable sequence of items)
# Tuple: Immutable, ordered, allows duplicate elements.
tuple_var = (1, 2, 3)        # tuple (immutable sequence of items)
# Range: Immutable, ordered, generates a sequence of numbers.
range_var = range(5)         # range (sequence of numbers, commonly used in loops)

# Mapping Type: Used to store key-value pairs.
dict_var = {"a": 1, "b": 2}  # dict (dictionary, mutable mapping of keys to values)

# Set Types: Used to store unordered collections of unique items.
# Set: Mutable, unordered, does not allow duplicates.
set_var = {1, 2, 3}          # set (mutable set of unique items)
# Frozenset: Immutable version of set.
frozenset_var = frozenset([1, 2, 3])  # frozenset (immutable set of unique items)

# Boolean Type: Used to represent truth values.
bool_var = True              # bool (True or False)

# Binary Types: Used to store binary data.
# Bytes: Immutable sequence of bytes.
bytes_var = b"hello"         # bytes (immutable sequence of bytes)
# Bytearray: Mutable sequence of bytes.
bytearray_var = bytearray(5) # bytearray (mutable sequence of bytes)
# Memoryview: View object for binary data.
memoryview_var = memoryview(bytes_var) # memoryview (view object for binary data)

# None Type: Used to represent the absence of a value.
none_var = None              # NoneType

# Print all types
if __name__ == "__main__":
    variables = [
        string_var, int_var, float_var, complex_var,
        list_var, tuple_var, range_var,
        dict_var, set_var, frozenset_var,
        bool_var, bytes_var, bytearray_var, memoryview_var, none_var
    ]
    for var in variables:
        print(f"{repr(var):<30} -> {type(var)}")

# Differences between similar data types:
# List vs Tuple:
#   - List is mutable (can be changed), Tuple is immutable (cannot be changed).
#   - Both are ordered and allow duplicate elements.
# Set vs Frozenset:
#   - Set is mutable, Frozenset is immutable.
#   - Both are unordered and do not allow duplicate elements.
# Bytes vs Bytearray:
#   - Bytes is immutable, Bytearray is mutable.
#   - Both represent sequences of bytes.