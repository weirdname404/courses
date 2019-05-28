package main

import (
	"fmt"
)

func main() {
	var arr [10000000]string
	var key, n int
	var value, c, res string

	_, _ = fmt.Scanln(&n)

	for i := 0; i < n; i++ {
		_, _ = fmt.Scanln(&c, &key, &value)
		if c == "add" {
			arr[key] = value
		} else if c == "find" {
			value := arr[key]
			if value == "" {
				res = "not found"
			} else {
				res = value
			}
			fmt.Println(res)

		} else if c == "del" {
			arr[key] = ""
		}
	}
}
