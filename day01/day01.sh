#!/bin/bash

set -e
readarray -t inputs <./in

function part_one() {
  count=0
  for i in "${!inputs[@]}"; do
    ((i > 0)) && ((inputs[i - 1] < inputs[i])) && count=$((count + 1))
  done
  echo "Part one: $count"
}

function part_two() {
  count=0
  for i in "${!inputs[@]}"; do
    ((i > 3)) && ((inputs[i - 3] < inputs[i])) && count=$((count + 1))
  done
  echo "Part two: $count"
}

part_one
part_two
