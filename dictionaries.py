# Dictionaries
band = {
    "vocals": "Plant",
    "guitar": "Page"
}
band2 = dict(vocals="Plant", guitar="Page")
print(band)
print(band2)
# Access items
print(band["vocals"])
print(band.get("guitar"))
# List all keys
print(band.keys())
# List all values
print(band.values())
# List of key/value pairs as tuples
print(band.items())
# Verify a key exits
print("verify")
print("guitar" in band)
print("hello" in band)
# Change values
print("change values")
band["vocals"] = "Flower"
band.update({"bass": "JPJ"})
print(band)
# Remove items
print("remove items")
print(band.pop("bass"))
print(band)
band["drums"] = "Clout"
print(band)
print(band.popitem()) # tuple
print(band)
del band2
# copy dicts
print("copy dicts")
band2 = band.copy()
band2["drums"] = "Dave"
print(band)
print(band2)
# or use the dict() constructor function
band3 = dict(band)
print(band3)
# nested dicts
member1 = {
    "name": "Plant",
    "instrument": "vocals"
}
member2 = {
    "name": "Page",
    "instrument": "guitar"
}
band = {
    "member1": member1,
    "member2": member2
}
print(band)
print(band["member1"]["name"])
# Sets
nums = {1, 2, 3, 4}
nums2 = set((1,2,3,4))
print(nums)
print(nums2)
print(type(nums))
print(len(nums))
# No duplicates allowed
nums3 = {1,2,2,3}
print(nums3)
# True is a dupe of 1, false is a dupe of zero
nums4 = {1, True, 2, False, 3, 4, 0}
print(nums4)
# but you cannot refer to an element in a set with an index position or a key
# add a new element to a set
nums.add(8)
print(nums)
# add element from one set to another
morenums = {5,6,7}
nums.update(morenums)
print(nums)
# you can use update with lists, tuples and dictionaries, too
# merge two sets to create a new set
one = {1,2,3}
two = {4,5,6}
mynewset = one.union(two)
print(mynewset)
# keep only duplicates
set1 = {1,2,2,3}
set2 = {1,4,2,6,7}
set1.intersection_update(set2)
print(set1)
# keep everything execpt dups
set1.symmetric_difference_update(set2)
print(set1)