# Hash Tables

## What is a Hash Table?

Hash tables are basic complex data structure, which utilize key-value mappings in order to search, insert, and / or delete data.

The hash function is what maps the values, technically. Because of this, the hash table knows where to store elements. this is also why hash tables are good at chekcing for duplicates. 

Other names for a hash table:
* Hash Maps
* Maps
* Dictionaries
* Associative Arrays

Most languages handle the implementation of the hash table, so you never have to do this independently. 

## Use Cases

* Building directories like phone books
* DNS Resolution
* Voting Systems
* Caching

## Hash Collisions

It is unrealistic to write a hash function which always maps different keys to different slots in the array. but ideally, a hash function would map keys evenly throughout the hash. 

When two keys have been assigned the same slot, a __collision__ is said to occur. One solution to handling collisions? When multiple keys map to the same slot, begin a linked list @ that slot. 

Collisions can be avoided by using good hash functions, and keeping a low __load factor__. The load factor represents the number of unoccupied slots within a hash table's array(s). 

To calculate: `number_of_items_in_hash_table / number_of_slots_in_array`. If the number is greator than `0.7`, it is time to rehash (or expand) the array. A basic rule is to make an array that is double the size of the current array. 

## Hash Table Performance

The best-case scanrio for a hash table is constant time, `O(1)`. this means each operation on the table requires the same amount of time, regardless of how many elements are present. Thus, hash tables are as fast as linked lists at inserts and deletes; and arrays at searching. 

At worst-case, hash tables perform in linear time, `O(n)`. To avoid the worst-case, collisions also need to be avoided.



