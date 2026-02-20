def findSmallestMissingPositive(orderNumbers):
    # Write your code here
    #orderNumbers = [3, 4, -1, 1]
    positives = {num for num in orderNumbers if num > 0}
    candidate = 1
    while candidate in positives:
        candidate += 1
    return candidate