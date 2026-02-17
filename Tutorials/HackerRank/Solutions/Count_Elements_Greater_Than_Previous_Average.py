def countResponseTimeRegressions(responseTimes):
    total = 0
    count = 0
    
    for i in range(len(responseTimes)):
        if i >= 1:
            avg = total / i
            if responseTimes[i] > avg:
                count +=1
        total += responseTimes[i] 
    
    return count