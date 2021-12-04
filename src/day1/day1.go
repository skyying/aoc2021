package main
import (
    "fmt"
    "bufio"
    "os"
    "strconv"
)

func readInput() []int {
    file, _ := os.Open("in")
    scanner := bufio.NewScanner(file)
    scanner.Split(bufio.ScanLines)
    var list []int
    for scanner.Scan() {
        text := scanner.Text()
        if s, err := strconv.Atoi(text); err == nil {
            list = append(list, s)
        }
    }
    file.Close()
    return list
}

func part_one(numbers []int) int {
    count := 0
    for i := 1; i<len(numbers); i++ {
        if numbers[i-1] < numbers[i] {
            count ++
        }
    }
    return count
}

func part_two(numbers []int) int {
    count := 0
    for i := 3; i<len(numbers); i++ {
        if sum(numbers[i-3:i]) < sum(numbers[i-2:i+1]) {
            count+=1
        }
    }
    return count
}

func sum(numbers []int) int {
    total := 0
    for _, n := range numbers {
        total += n
    }
    return total
}

func main() {
    inputs := readInput()

    fmt.Println(part_one(inputs))
    fmt.Println(part_two(inputs))

}

