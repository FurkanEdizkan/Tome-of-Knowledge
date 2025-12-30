func maxDistance(arrays [][]int) int {
    globalMin := arrays[0][0]
    globalMax := arrays[0][len(arrays[0])-1]
    maxDist := 0
    
    for i := 1; i < len(arrays); i++ {
        currentMin := arrays[i][0]
        currentMax := arrays[i][len(arrays[i])-1]
        
        // Calculate distance
        dist1 := currentMax - globalMin
        dist2 := globalMax - currentMin
        
        // Update max distance
        maxDist = max(maxDist, max(dist1, dist2))
        
        globalMin = min(globalMin, currentMin)
        globalMax = max(globalMax, currentMax)
    }
    
    return maxDist
}

func max(a, b int) int {
    if a > b {
        return a
    }
    return b
}

func min(a, b int) int {
    if a < b {
        return a
    }
    return b
}