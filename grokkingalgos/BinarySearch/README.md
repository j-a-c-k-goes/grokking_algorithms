# Binary Search

## What is Binary Search?

Binary search is an algorithm dependent upon a sorted input, like a list if elements. If the element is contained within the list, a binary search will return the position the element's location. 

## Why is it Effective?

Binary searching eliminates half the guesses needed during the process of locating a target. The search also occurs in logarithmic time, which is exponentially faster than linear time. 

Comparing logarithmic time to linear time: 

```
    Searching for 1_000_000_000 items, using Big O Notation

    Linear time: O(n)     ----> 1(1_000_000_000)            = 1_000_000_000 operations
    Log time:    O(log n) ----> log base 2 of 1_000_000_000 = ~ 30 operations

    Note: Algorithms speed are measured in growth of operations, not pure units of time. 
```

## Limitations

Binary search works only on sorted lists.