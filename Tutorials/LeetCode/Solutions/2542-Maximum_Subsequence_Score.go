import "sort"

func maxScore(nums1 []int, nums2 []int, k int) int64 {
	n := len(nums1)

	pairs := make([][2]int, n)
	for i := 0; i < n; i++ {
		pairs[i] = [2]int{nums2[i], nums1[i]}
	}

	sort.Slice(pairs, func(i, j int) bool {
		return pairs[i][0] > pairs[j][0]
	})

	heap := make([]int, 0)
	var sum int64 = 0
	var ans int64 = 0

	push := func(x int) {
		heap = append(heap, x)
		i := len(heap) - 1
		for i > 0 {
			p := (i - 1) / 2
			if heap[p] <= heap[i] {
				break
			}
			heap[p], heap[i] = heap[i], heap[p]
			i = p
		}
	}

	pop := func() int {
		res := heap[0]
		last := heap[len(heap)-1]
		heap = heap[:len(heap)-1]
		if len(heap) > 0 {
			heap[0] = last
			i := 0
			for {
				l := 2*i + 1
				r := 2*i + 2
				smallest := i
				if l < len(heap) && heap[l] < heap[smallest] {
					smallest = l
				}
				if r < len(heap) && heap[r] < heap[smallest] {
					smallest = r
				}
				if smallest == i {
					break
				}
				heap[i], heap[smallest] = heap[smallest], heap[i]
				i = smallest
			}
		}
		return res
	}

	for _, p := range pairs {
		push(p[1])
		sum += int64(p[1])

		if len(heap) > k {
			sum -= int64(pop())
		}

		if len(heap) == k {
			score := sum * int64(p[0])
			if score > ans {
				ans = score
			}
		}
	}

	return ans
}