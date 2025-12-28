# Algorithm Complexity (Time & Space)

This document is about algorithmic **time complexity** (cost) and **space complexity** (memory cost). 

---

## 1. What Big‑O Means

**Big‑O notation** describes how an algorithm’s **resource usage grows** as the input size `n` increases.

* **Time Complexity** → how execution time grows
* **Space Complexity** → how memory usage grows

Big‑O focuses on **growth rate**, not exact runtime or memory values.

---

## 2. Common Time Complexities

| Big‑O          | Name         | Explanation                           | Example                          |
| -------------- | ------------ | ------------------------------------- | -------------------------------- |
| **O(1)**       | Constant     | Runtime does not depend on input size | Array index access               |
| **O(log n)**   | Logarithmic  | Input size reduced each step          | Binary search                    |
| **O(n)**       | Linear       | Grows proportionally with input       | Loop over array                  |
| **O(n log n)** | Linearithmic | Divide + process                      | Merge sort                       |
| **O(n²)**      | Quadratic    | Nested loops                          | Bubble sort                      |
| **O(n³)**      | Cubic        | Triple nested loops                   | Matrix multiplication (naive)    |
| **O(2ⁿ)**      | Exponential  | Every element doubles work            | Recursive subsets                |
| **O(n!)**      | Factorial    | All permutations                      | Traveling Salesman (brute force) |

---

## 3. Common Space (Memory) Complexities

| Big‑O        | Meaning            | Typical Cause             |
| ------------ | ------------------ | ------------------------- |
| **O(1)**     | Constant memory    | Fixed number of variables |
| **O(n)**     | Linear memory      | Arrays, lists, buffers    |
| **O(n²)**    | Quadratic memory   | 2D matrices               |
| **O(log n)** | Logarithmic memory | Recursive call stack      |

> ⚠️ Space complexity includes **auxiliary space** (extra memory) and sometimes **call stack usage**.

---

## 4. Time vs Space Tradeoff

Often you can reduce **time** by using more **memory**, or reduce **memory** by using more **time**.

Example:

* Hash table lookup → **O(1) time**, **O(n) space**
* Linear search → **O(n) time**, **O(1) space**

---

## 5. Simple Examples

### Example 1: Linear Loop

* **Time:** O(n)
* **Space:** O(1)

Reason: One loop, no extra memory allocation.

---

### Example 2: Nested Loops

* **Time:** O(n²)
* **Space:** O(1)

Reason: Loop inside a loop, fixed variables only.

---

### Example 3: Recursive Algorithm

* **Time:** O(n)
* **Space:** O(n)

Reason: Function calls stored on the call stack.

---

## 6. How to Analyze Complexity (Checklist)

### Time Complexity

* Count loops
* Watch nested loops → multiply
* Ignore constants (O(2n) → O(n))
* Focus on the **worst case**

### Space Complexity

* Count additional data structures
* Include recursion stack
* Ignore input size unless copied

---

## 7. Best, Average, and Worst Case

| Case        | Meaning                       |
| ----------- | ----------------------------- |
| **Best**    | Minimum work (rarely used)    |
| **Average** | Expected behavior             |
| **Worst**   | Maximum cost (most important) |

Big‑O usually refers to the **worst case**.

---

## 8. Quick Memory Aid

* One loop → **O(n)**
* Loop inside loop → **O(n²)**
* Divide input in half → **O(log n)**
* Store input → **O(n) space**
