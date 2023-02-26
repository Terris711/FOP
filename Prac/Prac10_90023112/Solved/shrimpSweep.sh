
low_pop=10
hi_pop=30
step_pop=2

echo "Paramaters are:"
echo "Population : $low_pop , $hi_pop , $step_pop"
outfile="shrimp_pop$low_pop-$hi_pop.csv"
echo "Initial Population,Final Population" > $outfile

for p in `seq $low_pop $step_pop $hi_pop`;
do

echo "Experiment: $p"
Result=`python3 shrimpBase.py "$p" "n"`
echo "$Result"
echo "$Result" >> $outfile

done
~                                                                               
~                                                                               
~                                                                               
~                                                                               
-- INSERT --                                                  17,27         All
