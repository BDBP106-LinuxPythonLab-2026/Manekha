#!/bin/bash

awk '$6=="PHE" {print}' 1HK0.cif > PHE_atoms.xyz
