# Count Elements Greater Than Previous Average

Given an array of positive integers, return the number of elements that are strictly greater than the average of all previous elements. Skip the first element.

Example

    Input

        responseTimes = [100, 200, 150,300]

    Output

        2

Explanation

    - Day 0: 100 (no previous days, skip) 
    - Day 1: 200 > average(100) = 100 → count = 1 
    - Day 2: 150 vs average(100, 200) = 150 → not greater → count = 1 
    - Day 3: 300 > average(100, 200, 150) = 150 → count = 2 Return 2.

Input Format

    The first line contains an integer n (0 ≤ n ≤ 1000), the number of days.
    If n > 0, the next n lines contains an integer representing responseTimes[i].
    If n = 0, the second line is omitted or empty.

Example

    4
    100
    200
    150
    300

here 4 is the length of array, followed by the elements of array on each line.

Constraints

- 0 <= responseTimes.length <= 1000
- 1 <= responseTimes[i] <= 10^9 for 0 <= i < responseTimes.length

Output Format

- A single integer depicting the count of days.

Sample Input 0

    0

Sample Output 0

    0

Sample Input 1

    1
    100

Sample Output 1

    0