read len
# echo $x
declare -a arr
# while read a
# do 
#     arr+=($a)
# done
x=''
declare -a arr2 
readarray -t arr
count=0
for i in ${arr[@]}
do 
    ((count=$count+1))
    if [ $count -eq $len ]
    then 
        x+="$i"
    else
        x+="$i\n"
    fi    
    # echo $i | uniq
    
    # if ()
done
# echo $count
echo -e  $x | sort |  uniq -u | bc
# echo $arr
# printf '%s\n' "${arr[@]}" | sort | uniq  -u 
# printf '%s\n' "${arr[@]}" | awk '{++fq[$0]} END{for(i in fq) if (fq[i]==1) print i}'