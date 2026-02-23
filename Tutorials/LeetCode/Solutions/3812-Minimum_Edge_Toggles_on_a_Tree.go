func minimumFlips(n int, edges [][]int, start string, target string) []int {
	adj := make([][]struct{ to, idx int }, n)
	for i, e := range edges {
		u, v := e[0], e[1]
		adj[u] = append(adj[u], struct{ to, idx int }{v, i})
		adj[v] = append(adj[v], struct{ to, idx int }{u, i})
	}

	need := make([]int, n)
	sum := 0
	for i := 0; i < n; i++ {
		need[i] = int(start[i]-'0') ^ int(target[i]-'0')
		sum += need[i]
	}

	if sum%2 == 1 {
		return []int{-1}
	}

	res := []int{}
	visited := make([]bool, n)

	var dfs func(int) int
	dfs = func(u int) int {
		visited[u] = true
		cur := need[u]

		for _, e := range adj[u] {
			v := e.to
			if visited[v] {
				continue
			}
			childParity := dfs(v)

			if childParity == 1 {
				res = append(res, e.idx)
				cur ^= 1
			}
		}
		return cur
	}

	rootParity := dfs(0)

	if rootParity != 0 {
		return []int{-1}
	}

	sort.Ints(res)
	return res
}