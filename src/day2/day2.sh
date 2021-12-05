#!/bin/bash

inputs=$(cat ./in)
set -e
commands=()
for line in ${inputs[@]}; do
  commands+=($line)
done

function part_one() {
  for ((i = 0; i < ${#commands[@]}; i += 2)); do
    cmd=${commands[i]}
    value=${commands[i + 1]}
    x=${value:=0}
    case $cmd in
    forward)
      horizon=$((horizon + x))
      ;;
    down)
      depth=$((depth + x))
      ;;
    up)
      depth=$((depth - x))
      ;;
    esac
  done
  echo "Part one:" $((horizon * depth))
}

function part_two() {
  aim=0
  horizon=0
  depth=0
  for ((i = 0; i < ${#commands[@]}; i += 2)); do
    cmd=${commands[i]}
    value=${commands[i + 1]}
    x=${value:=0}
    case $cmd in
    forward)
      horizon=$((horizon + x))
      depth=$((depth + (x * aim)))
      ;;
    down)
      aim=$((aim + x))
      ;;
    up)
      aim=$((aim - x))
      ;;
    esac
  done
  echo "Part two:" $((horizon * depth))
}

part_one
part_two
