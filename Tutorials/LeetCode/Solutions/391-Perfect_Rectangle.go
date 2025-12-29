func isRectangleCover(rectangles [][]int) bool {
    // Track area and corner points
    totalArea := 0
    minX, minY := int(1e5), int(1e5)
    maxA, maxB := int(-1e5), int(-1e5)
    
    // Use map to track corner occurrences
    corners := make(map[[2]int]int)
    
    for _, rect := range rectangles {
        x, y, a, b := rect[0], rect[1], rect[2], rect[3]
        
        // Calculate total area
        totalArea += (a - x) * (b - y)
        
        // Find bounding box
        minX = min(minX, x)
        minY = min(minY, y)
        maxA = max(maxA, a)
        maxB = max(maxB, b)
        
        // Track all 4 corners of this rectangle
        points := [][2]int{
            {x, y},   // bottom-left
            {x, b},   // top-left
            {a, y},   // bottom-right
            {a, b},   // top-right
        }
        
        for _, p := range points {
            corners[p]++
        }
    }
    
    // Check if total area matches bounding rectangle area
    expectedArea := (maxA - minX) * (maxB - minY)
    if totalArea != expectedArea {
        return false
    }
    
    // The 4 outer corners of the perfect rectangle
    outerCorners := map[[2]int]bool{
        {minX, minY}: true,
        {minX, maxB}: true,
        {maxA, minY}: true,
        {maxA, maxB}: true,
    }
    
    // Check corner conditions
    for point, count := range corners {
        if outerCorners[point] {
            // Outer corners must appear exactly once
            if count != 1 {
                return false
            }
        } else {
            // Inner points must appear 2 or 4 times
            if count != 2 && count != 4 {
                return false
            }
        }
    }
    
    return true
}

func min(a, b int) int {
    if a < b {
        return a
    }
    return b
}

func max(a, b int) int {
    if a > b {
        return a
    }
    return b
}
