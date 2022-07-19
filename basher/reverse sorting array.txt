declare -a A
# declare -a B
# declare -p A
while read x 
do 
    A+=($x)
    # declare -p A
done
# for i in ${A[@]}
# do 
#     echo $i
# done
# B= sort  ${A[@]}
printf '%s\n' "${A[@]}" | sort -nr