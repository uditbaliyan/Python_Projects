
If you want to understand how Python’s `list` is implemented “under the hood,” here’s a guided dive — starting from the high-level design down to C internals you can browse. If you like, I can also point you to the CPython source code lines and walk you through them.

---

## High-level design: what a Python list *is*

* In CPython (the standard implementation), a Python `list` is backed by a **dynamic array** (an array that can grow) of pointers (object references), not a linked list. ([laurentluce.com][1])
* Because Python values are all objects (instances of `PyObject` or subtype), the array holds `PyObject *` pointers. This means the list doesn’t need to know in advance whether elements are `int`, `str`, `dict`, etc. All elements are just pointers to objects. ([Medium][2])
* The list structure tracks how many items are currently in use (its “size” or “length”), and how many slots are allocated (which may be ≥ size) for potential growth. ([laurentluce.com][1])

Because all pointers (`PyObject *`) are of the same machine size (e.g. 8 bytes on a 64-bit system), the underlying array is homogeneous in that sense, even though the pointees can be heterogeneous.

So when you do:

```python
lst = [1, "hello", 3.14]
```

the `list` contains, internally, three pointers:

```
lst.ob_item[0] → PyObject for integer 1  
lst.ob_item[1] → PyObject for string "hello"  
lst.ob_item[2] → PyObject for float 3.14
```

---

## Core C struct and invariants (CPython internals)

Here’s roughly how CPython defines a `list` internally. (See `Include/listobject.h` in CPython source.) ([GitHub][3])

```c
typedef struct {
    PyObject_VAR_HEAD
    PyObject **ob_item;     /* pointer to array of PyObject* */
    Py_ssize_t allocated;   /* how many slots are allocated in ob_item */
} PyListObject;
```

Here:

* `PyObject_VAR_HEAD` is a macro that includes the standard object header plus a field `ob_size` (for variable-length objects) which holds the *current length* (number of elements).
* `ob_item` points to a heap-allocated C array of `PyObject *`.
* `allocated` is how many slots (capacity) have been allocated in that array.
* The invariant is: `0 ≤ ob_size ≤ allocated`. The “list length” (what `len(lst)` returns) is `ob_size`.

When CPython needs to grow (or shrink) the list, it may allocate a new `ob_item` array (bigger or smaller) and copy pointers. ([rcoh.me][4])

One interesting detail: CPython uses **over-allocation** (i.e. allocate more slots than strictly needed) to reduce how often it has to reallocate. In many cases, resizing will be by a factor, not by just +1. ([rcoh.me][4])

In one analyzed implementation, the growth formula is:

```c
new_allocated = newsize + (newsize >> 3) + ( (newsize < 9) ? 3 : 6 )
```

Meaning roughly “current size + 12.5% + a small constant.” ([rcoh.me][4])

Thus the growth sequence (of allocated capacity) might go like: 0, 4, 8, 16, 25, 35, 46, 58, 72, 88 … ([laurentluce.com][1])

CPython also keeps a small free-list (cache) of recently deallocated list objects to reduce overhead of frequent allocations. ([svn.python.org][5])

---

## Operations: indexing, append, insert, remove, resizing

### Indexing / element access

Because the `ob_item` array is contiguous and pointers are uniform size, getting `lst[i]` becomes:

1. Check that `0 ≤ i < ob_size`
2. Return `ob_item[i]` (a `PyObject *`)
3. (Possibly increment reference count depending on context)

This is an (O(1)) (constant-time) operation. ([antonz.org][6])

Because the pointees are arbitrary objects, no special logic is needed about data types at this level — it just deals with pointers.

### Appending (`list.append`)

When you append an element `x`:

1. Let `n = ob_size`
2. Check if `n + 1` fits within `allocated`.

   * If yes: insert `ob_item[n] = x`, increment `ob_size`
   * If no: call `list_resize(...)` to reallocate a bigger `ob_item` array, then insert.
3. Increase object reference count etc.

Because of overallocation, most append operations don’t trigger a reallocation. The cost of occasional reallocations is amortized, making append *amortized* (O(1)). ([rcoh.me][4])

### Insertion / removal

If you insert or remove in the middle (or at the front), items to the right of the insertion/deletion point must be shifted (i.e. memmove or loop of pointer copies). That makes insertion/removal in the interior (O(n)) in the worst case. ([GeeksforGeeks][7])

After removals, CPython may shrink the allocated array if too much space is wasted (i.e. if new size < half of `allocated`). ([laurentluce.com][1])

### Other behaviors (e.g. slicing, building lists at compile-time)

* For a literal list expression (e.g. `[1,2,3]`), CPython’s bytecode uses `BUILD_LIST` which allocates the list of the required size and then directly sets elements (via `PyList_SET_ITEM`) rather than repeatedly appending. ([Stack Overflow][8])
* During list construction and slicing, there may be special optimizations or shortcuts.

---

## How does the list “know” the type of each element (e.g. int, str, etc.)?

It doesn’t, at the list-level. The list simply holds `PyObject *` pointers. Each object itself has runtime metadata (its type, methods, data) in its object header. The list abstraction doesn’t need to inspect types to store or traverse; only when operations (like comparisons, method calls, arithmetic) are invoked on the elements does Python use dynamic dispatch to the proper type-specific code.

Thus, mixed-type lists are natural: a list of `[42, "hello", {}]` is just a pointer array to an `int` object, a `str` object, and a `dict` object. The fact that they’re different types is handled by each object’s internal structure, not by the list.

---

## Suggested readings and source browsing

Here are some articles and resources you can read further or view alongside CPython source:

* *“Python list implementation”* by **Laurent Luce** — good explanation with diagrams of the `PyListObject` structure and resizing behavior. ([laurentluce.com][1])
* *Notes on CPython List Internals* by Russell Cohen — good deeper reading. ([rcoh.me][4])
* The CPython source file `Objects/listobject.c` (and its header `Include/listobject.h`) to see the actual code for `list_resize`, `list_insert`, etc.
* CPython-Internals “list” documentation in some GitHub repos (e.g. `BasicObject/list/list.md`) ([GitHub][9])

If you like, I can fetch you a version of `listobject.c` annotated with commentary and we can walk it together. Do you want me to do that?

[1]: https://www.laurentluce.com/posts/python-list-implementation/?utm_source=chatgpt.com "Python list implementation - Laurent Luce's Blog"
[2]: https://medium.com/pythoneers/how-does-list-in-python-store-items-with-different-data-types-1afdd0b777f4?utm_source=chatgpt.com "How does the list in python store items with different data ..."
[3]: https://github.com/python/cpython/blob/main/Include/listobject.h?utm_source=chatgpt.com "cpython/Include/listobject.h at main - GitHub"
[4]: https://rcoh.me/posts/notes-on-cpython-list-internals/?utm_source=chatgpt.com "Notes on CPython List Internals - Russell Cohen"
[5]: https://svn.python.org/projects/python/trunk/Objects/listobject.c?utm_source=chatgpt.com "listobject.c - Python"
[6]: https://antonz.org/list-internals/?utm_source=chatgpt.com "How Python list works - Anton Zhiyanov"
[7]: https://www.geeksforgeeks.org/python/internal-working-of-list-in-python/?utm_source=chatgpt.com "Internal working of list in Python - GeeksforGeeks"
[8]: https://stackoverflow.com/questions/45176010/python-list-initialization-with-values-implementation-process?utm_source=chatgpt.com "Python list initialization with values--implementation process?"
[9]: https://github.com/zpoint/CPython-Internals/blob/master/BasicObject/list/list.md?utm_source=chatgpt.com "CPython-Internals/BasicObject/list/list.md at master - GitHub"
