type Bitset struct {
	size    int
	ones    map[int]bool
	count   int
	flipped bool
}

func Constructor(size int) Bitset {
	return Bitset{
		size:    size,
		ones:    make(map[int]bool),
		count:   0,
		flipped: false,
	}
}

func (this *Bitset) Fix(idx int) {
	if this.flipped {
		if this.ones[idx] {
			delete(this.ones, idx)
			this.count++
		}
	} else {
		if !this.ones[idx] {
			this.ones[idx] = true
			this.count++
		}
	}
}

func (this *Bitset) Unfix(idx int) {
	if this.flipped {
		if !this.ones[idx] {
			this.ones[idx] = true
			this.count--
		}
	} else {
		if this.ones[idx] {
			delete(this.ones, idx)
			this.count--
		}
	}
}

func (this *Bitset) Flip() {
	this.flipped = !this.flipped
	this.count = this.size - this.count
}

func (this *Bitset) All() bool {
	return this.count == this.size
}

func (this *Bitset) One() bool {
	return this.count > 0
}

func (this *Bitset) Count() int {
	return this.count
}

func (this *Bitset) ToString() string {
	result := make([]byte, this.size)

	for i := 0; i < this.size; i++ {
		inMap := this.ones[i]

		if this.flipped {
			if inMap {
				result[i] = '0'
			} else {
				result[i] = '1'
			}
		} else {
			if inMap {
				result[i] = '1'
			} else {
				result[i] = '0'
			}
		}
	}

	return string(result)
}

/**
 * Your Bitset object will be instantiated and called as such:
 * obj := Constructor(size);
 * obj.Fix(idx);
 * obj.Unfix(idx);
 * obj.Flip();
 * param_4 := obj.All();
 * param_5 := obj.One();
 * param_6 := obj.Count();
 * param_7 := obj.ToString();
 */