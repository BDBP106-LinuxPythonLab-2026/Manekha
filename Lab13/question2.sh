#!/bin/bash

#i)

awk '$2<25 {print}' awk.txt

#ii)

awk '$3=="Physics" {print}' awk.txt

#iii)

awk 'print $1","$2","$3}' awk.txt > data2.csv
