  #!/usr/bin/bash
   year=$1
   month=$2
   
   dir=plot_$1_$2

   cp plotweather.sh $dir
   cd $dir
   wget http://www.bom.gov.au/climate/dwo/$1$2/text/IDCJDW6111.$1$2.csv
   grep "2020-02" infile.csv > data.csv
   awk -F "," '{print $3,$4,$11,$17}' data.csv > data4.csv
   gnuplot -p plotcmd.txt
   gnuplot -e "set terminal png size 400,300; set output 'xyz.png'; plot [-4:4] exp(-x**2 / 2)"

