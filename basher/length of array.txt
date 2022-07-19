
declare -a A
count=1
while read x
do 
A+=($x)
# ((count=$count+1))
done
# echo $count
echo "${#A[@]}"
# echo $((${#A[@]}+1))