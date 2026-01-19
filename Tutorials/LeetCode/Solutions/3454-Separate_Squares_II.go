import "sort"

func separateSquares(squares [][]int) float64 {
	type Event struct {
		y      int64
		x1, x2 int64
		delta  int
	}

	events := []Event{}
	xs := []int64{}

	for _, s := range squares {
		x := int64(s[0])
		y := int64(s[1])
		l := int64(s[2])

		events = append(events,
			Event{y, x, x + l, 1},
			Event{y + l, x, x + l, -1},
		)
		xs = append(xs, x, x+l)
	}

	sort.Slice(xs, func(i, j int) bool { return xs[i] < xs[j] })
	uniq := []int64{}
	for _, v := range xs {
		if len(uniq) == 0 || uniq[len(uniq)-1] != v {
			uniq = append(uniq, v)
		}
	}

	idx := map[int64]int{}
	for i, v := range uniq {
		idx[v] = i
	}

	n := len(uniq)
	cnt := make([]int, 4*n)
	lenSeg := make([]int64, 4*n)

	var update func(node, l, r, ql, qr, v int)
	update = func(node, l, r, ql, qr, v int) {
		if ql >= r || qr <= l {
			return
		}
		if ql <= l && r <= qr {
			cnt[node] += v
		} else {
			m := (l + r) / 2
			update(node*2, l, m, ql, qr, v)
			update(node*2+1, m, r, ql, qr, v)
		}

		if cnt[node] > 0 {
			lenSeg[node] = uniq[r] - uniq[l]
		} else if l+1 == r {
			lenSeg[node] = 0
		} else {
			lenSeg[node] = lenSeg[node*2] + lenSeg[node*2+1]
		}
	}

	sort.Slice(events, func(i, j int) bool {
		return events[i].y < events[j].y
	})

	type Slab struct {
		y1, y2 int64
		width  int64
	}

	slabs := []Slab{}
	var prevY int64
	var curWidth int64

	for i, e := range events {
		if i > 0 && e.y > prevY {
			slabs = append(slabs, Slab{prevY, e.y, curWidth})
		}
		update(1, 0, n-1, idx[e.x1], idx[e.x2], e.delta)
		curWidth = lenSeg[1]
		prevY = e.y
	}

	var total int64
	for _, s := range slabs {
		total += s.width * (s.y2 - s.y1)
	}

	half := float64(total) / 2
	var acc float64

	for _, s := range slabs {
		area := float64(s.width) * float64(s.y2-s.y1)
		if acc+area >= half {
			return float64(s.y1) + (half-acc)/float64(s.width)
		}
		acc += area
	}

	return 0
}
