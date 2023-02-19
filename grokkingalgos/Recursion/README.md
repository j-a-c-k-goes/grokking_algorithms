# Recursion

## What is Recursion?
Recursion happens when a function is self-referring. 

Recursion is thought to be a simpler solution to a loop-based approach. It is not always simpler, however. 

Recursion could run forever, because the function is referring to itself. So, a __base case__ and __recursive case__ are foundational statements within the recursive body; think of these as break statements (like in a while loop).

```
Recursive solution.
--------------------
def lookForKey(box):
    for item in box:
        if itemIsABox:
            lookForKey(item)
        elif itemIsAKey:
            print("Found key!")
```


## What does recursion affect?

When using recursion, you are using the __call stack__, a data structure. The call stack is utilized internally by the computer, _push an item onto the stack. Ok, that item is no longer needed, pop it from the stack. Run next process._

__Remember:__ When a function is called from another function, the calling function is paused, and exists as partially completed.  

## When the Call Stack is Too Tall
The stack is convenient, as it keeps track of function calls, bypassing having to do this on your own end. However, too much stacking can use up an inefficient amount of memory. If this happens, using standard loops instead of recursion is a solution. 

## What Recursion is not?
* A performance benefit.