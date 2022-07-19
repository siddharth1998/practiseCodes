declare -a A
while read x 
do 
 A+=($x)
done
printf "%s\n" "${A[@]}" | sed '/a/d'