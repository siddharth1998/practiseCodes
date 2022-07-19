declare -a A
while read x 
do 
 A+=($x)
done
printf "%s " "${A[@]:3:5}"