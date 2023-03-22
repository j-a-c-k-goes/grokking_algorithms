# Recursion

## What is Recursion?
Recursion happens when a function is self-referring. 

Recursion is thought to be a simpler solution to a loop-based approach. It is not always simpler solution — recursion could run forever ( like an infinite loop ), because the function is referring to itself. 

To prevent infinite loops, a __base case__ and __recursive case__ are established within the recursive body. _Think of these as break statements (like in a while loop)._

```
Example: Recursive Solution.
--------------------
def lookForKey(box):
    for item in box:
        if item_is_a_box:
            look_for_key(item)
        elif item_is_a_key:
            print("Found key!")
```

## What Does Recursion Affect?
When using recursion, you are using the __call stack__, a data structure. The call stack is utilized internally by the computer, _push an item onto the stack. Ok, that item is no longer needed, pop it from the stack. Run next process._

__Remember:__ When a function is called from another function, the calling function is paused, and exists as partially completed.  

## What if the Call Stack is Too Tall?
The stack is convenient, as it keeps track of function calls, bypassing having to do this on your own end. However, too much stacking can utilize an inefficient amount of memory. If this happens, using standard loops instead of recursion. 

## What Recursion is Not?
* A performance benefit.