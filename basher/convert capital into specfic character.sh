declare -a arr
while read x 
do
    a=$(echo -n "$x" | sed 's/[A-Z]/./')
    arr+=($a)
done
echo "${arr[@]}"