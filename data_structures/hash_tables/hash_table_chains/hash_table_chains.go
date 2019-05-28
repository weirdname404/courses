package main

import (
	"fmt"
)

type HashTable struct {
	cardinality int
	arr         []*Chain
	prime       int
	multiplier  int
}

type Chain struct {
	next  *Chain
	value string
}

func (ht *HashTable) Hash(valuePtr *string) int {
	var acc int
	asciiCodes := []rune(*valuePtr)
	for i := len(asciiCodes) - 1; i >= 0; i-- {
		acc = (acc * ht.multiplier + int(asciiCodes[i])) % ht.prime
	}
	return acc % ht.prime % ht.cardinality
}

func (ht *HashTable) Add(value string) {
	newChain := Chain{value: value}
	i := ht.Hash(&value)
	chainPtr := ht.arr[i]

	if chainPtr != nil {
		for chainPtr != nil {
			if chainPtr.value == value {
				return
			} else {
				chainPtr = chainPtr.next
			}
		}
		newChain.next = ht.arr[i]
	}

	ht.arr[i] = &newChain
}

func (ht *HashTable) Find(value string) string {
	chainPtr := ht.arr[ht.Hash(&value)]
	for chainPtr != nil {
		if chainPtr.value == value {
			return "yes"
		}

		chainPtr = chainPtr.next
	}

	return "no"
}

func (ht *HashTable) Delete(value string) {
	i := ht.Hash(&value)
	chainPtr := ht.arr[i]
	var prevPtr *Chain

	for chainPtr != nil {
		if chainPtr.value == value {
			if prevPtr != nil {
				prevPtr.next = chainPtr.next
			} else {
				ht.arr[i] = chainPtr.next
			}
			return

		} else {
			prevPtr = chainPtr
			chainPtr = chainPtr.next
		}
	}
}

func (ht *HashTable) Check(i int) {
	chainPtr := ht.arr[i]
	res := ""

	for chainPtr != nil {
		res += chainPtr.value
		if chainPtr.next != nil {
			res += " "
		} else {
			break
		}
		chainPtr = chainPtr.next
	}

	fmt.Println(res)
}

func main() {
	var n int
	var m int
	var value, command string

	_, _ = fmt.Scanln(&m)
	_, _ = fmt.Scanln(&n)

	ht := HashTable{cardinality: m, prime: 1000000007, multiplier: 263}
	ht.arr = make([]*Chain, ht.cardinality)

	for i := 0; i < n; i++ {
		_, _ = fmt.Scan(&command)
		if command == "check" {
			var valueInt int
			_, _ = fmt.Scanln(&valueInt)
			ht.Check(valueInt)

		} else {
			_, _ = fmt.Scanln(&value)
			if command == "add" {
				ht.Add(value)

			} else if command == "find" {
				fmt.Println(ht.Find(value))

			} else {
				ht.Delete(value)
			}
		}
	}
}
