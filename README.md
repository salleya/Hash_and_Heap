# Hash_and_Heap

## Hash Map Implementation:  hash_map.py

This hash map uses a hash table of buckets (dynamic array), each containing a linked list of hash links to resolve collisions. Each hash link stores the key-value pair (string and object) and a pointer to the next link in the list.

![ScreenShot1](https://github.com/salleya/Hash_and_Heap/blob/master/ScreenShot1.png)

Includes the following methods:
- put()
- get()
- remove()
- contains_key()
- clear()
- empty_buckets()
- resize_table()
- table_load()
- get_keys()


## Min Heap Implementation:  min_heap.py

This min heap uses a dynamic array to implement a complete binary tree heap. The value in each internal node is smaller than or equal to the values of that node’s children.  

![ScreenShot1](https://github.com/salleya/Hash_and_Heap/blob/master/ScreenShot2.png)
![ScreenShot1](https://github.com/salleya/Hash_and_Heap/blob/master/ScreenShot3.png)

Includes the following methods:
- add()
- get_min()
- remove_min()
- build_heap()


## Singly Linked List and Dynamic Array "helper" data structures: sll_and_da_include.py

**Linked List** methods include:
- insert()
- remove()
- contains()
- length()
- __iter()__

**Dynamic Array** methods include:
- append()
- pop()
- swap()
- get_at_index()
- set_at_index()
- length()
