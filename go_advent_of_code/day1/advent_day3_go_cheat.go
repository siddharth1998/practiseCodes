package main

import (
	"bufio"
	"io"
	"log/slog"
	"regexp"
	"os"
	"strconv"
)

const FIND_OPS_PART1 = `(mul\(\d+,\d+\))`
const FIND_OPS_PART2 = `((?:don't|do|mul)\(\d*,?\d*\))`
const PARSE_MULTIPLIER = `mul\((\d+),(\d+)\)`

func findOps(inputReader io.Reader, reString string) []string {
	scanner := bufio.NewScanner(inputReader)
	re := regexp.MustCompile(reString)
	ops := make([]string, 0, 10)

	for scanner.Scan() {
		line := scanner.Text()
		ops = append(ops, re.FindAllString(line, -1)...)
	}

	return ops
}

func parseMultiply(ops []string, reString string) [][]int {
	parsedOps := make([][]int, 0, len(ops))
	re := regexp.MustCompile(reString)

	for _, op := range ops {
		matches := re.FindStringSubmatch(op)
		matchesInt := AtoiSlice(matches[1:])
		parsedOps = append(parsedOps, matchesInt)
	}

	return parsedOps
}

func multiplySum(ops [][]int) (sum int) {
	for _, op := range ops {
		sum += multiply(op)
	}
	return
}

func multiply(op []int) (result int) {
	result = 1
	for _, op := range op {
		result *= op
	}
	return result
}

func partOne() {
	inputReader := NewInputReader()
	foundOps := findOps(inputReader, FIND_OPS_PART1)
	multiplyOps := parseMultiply(foundOps, PARSE_MULTIPLIER)
	sum := multiplySum(multiplyOps)

	slog.Info("part1: calculated result for input", "sum", sum)
}

func NewInputReader() *os.File {
	inputReader, err := os.Open("input.txt")

	if err != nil {
		slog.Error("got an error while trying to open input file", "Error", err)
	}

	return inputReader
}

func AtoiSlice(d []string) []int {
	intSlice := make([]int, len(d))
	for i, e := range d {
		convertedElement, err := strconv.Atoi(e)
		if err != nil {
			slog.Error("error converting string to int", "error", err)
		}
		intSlice[i] = convertedElement
	}
	return intSlice
}

func partTwo() {
	inputReader := NewInputReader()
	defer inputReader.Close()

	foundOps := findOps(inputReader, FIND_OPS_PART2)

	// Now that we have all found ops including the don't() and do()
	// we can loop threw them all and enable and disable instructions.
	// We start with instructions enabled until we hit a don't() then
	// re-enable when we hit a do() again.
	enabledOps := make([]string, 0, len(foundOps)/2)
	enabled := true
	for _, op := range foundOps {
		if op == "do()" {
			enabled = true
		} else if op == "don't()" {
			enabled = false
		} else {
			if enabled {
				enabledOps = append(enabledOps, op)
			}
		}
	}

	multiplyOps := parseMultiply(enabledOps, PARSE_MULTIPLIER)
	su := multiplySum(multiplyOps)

	slog.Info("part2: calculated result for input", "sum", su)
}

func main() {
	partOne()
	partTwo()
}