#!/bin/bash
# Prac Test 4 - Parameter sweep driver code

low_pop=10
hi_pop=30
step_pop=2

echo "Parameters are: "
echo "Population :  $low_pop,$hi_pop,$step_pop"
outfile="shrimp_pop"$low_pop"-"$hi_pop".csv"
echo "Initial Population, Final Population" > $outfile

for p in `seq $low_pop $step_pop $hi_pop`;
do
    echo "Experiment: " $p
    Simulation=`python3 shrimpBase.py "$p" "N"`
    echo "$Simulation"
    echo "$Simulation" >> $outfile
done
