read s1
read s2
read s3

counter=0

if [ $s1 -eq $s2 ]
then 
    ((counter=counter+1))
fi 

if [ $s2 -eq $s3 ]
then 
    ((counter=counter+1))
fi

if [ $s3 -eq $s1 ]
then 
    ((counter=counter+1))
fi

case $counter in
    0)
    echo "SCALENE"
    ;;
    1)
    echo "ISOSCELES"
    ;;
    2)
    echo "EQUILATERAL"
    ;;
    3)
    echo "EQUILATERAL"
    ;;
esac

# if [ $s1 -eq $s2 ]&&[ $s2 -eq $s3 ]
# then 
#     echo "EQUILATERAL"
# elif [ $s1 -eq $s2 ]&&[]