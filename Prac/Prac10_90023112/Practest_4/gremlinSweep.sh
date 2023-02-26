#!/bin/bash
# Prac Test 4 - Parameter sweep driver code

exp_dir=gremlin`date "+%Y-%m-%d_%H.%M.%S"`

mkdir $exp_dir

cp gremlinBase.py $exp_dir
cp gremlinSweep.sh $exp_dir
cd $exp_dir
low_pop=$1
hi_pop=$2
step_pop=$3

echo "Parameters are: "
echo "Population : " $low_pop $hi_pop $step_pop
outfile="gremlin_pop"$low_pop"-"$hi_pop".csv"
echo "Initial Population,Good Gremlins,Bad Gremlins" > $outfile

for p in `seq $low_pop $step_pop $hi_pop`;
do
    echo "Experiment: " $p
	# TODO: Add code to run gremlinBase.py with parameters
done
