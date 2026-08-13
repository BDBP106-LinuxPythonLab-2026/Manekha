#!/bin/bash

Speed=3*10^8
Mass=1
Energy=$(bc << EOF
mass=1
speed=3*10^8
mass*speed^2
EOF
)

echo "Speed: "$Speed
echo "Mass: "$Mass
echo "The energy-mass equivalence of the given object is: Mass*Speed^2 = "$Energy
