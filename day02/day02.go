package main
import (
    "fmt"
    "bufio"
    "os"
    "strings"
    "strconv"
)

func readInput() [][]string {
    file, _ := os.Open("in")
    scanner := bufio.NewScanner(file)
    scanner.Split(bufio.ScanLines)
    var commands [][]string
    for scanner.Scan() {
        text := scanner.Text()
        commands = append(commands, strings.Split(text, " "))
    }
    file.Close()
    return commands
}

func partOne () int {
    commands := readInput()
    horizon, depth := 0, 0
    for _, command := range commands {
        direction := command[0]
        x, _ := strconv.Atoi(command[1])
        if direction == "forward" {
            horizon += x
        } else if direction == "down" {
            depth += x
        } else {
            depth -= x
        }
    }

    fmt.Println(horizon * depth)
    return horizon * depth
}

func partTwo() int {
    commands := readInput()
    horizon, depth, aim := 0, 0, 0
    for _, command := range commands {
        direction := command[0]
        x, _ := strconv.Atoi(command[1])
        if direction == "forward" {
            horizon += x
            depth  += x * aim
        } else if direction == "down" {
            aim += x
        } else {
            aim -= x
        }
    }
    fmt.Println(horizon * depth)
    return horizon * depth
}

func main () {
    partOne()
    partTwo()
}

