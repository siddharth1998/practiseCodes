sed
sed 's//' --> swap 
sed '//d' --> delete

uniq
uniq -c --> counter
uniq -i --> insensitivity
uniq -f --> case sensitiv 
uniq -u --> non repet

paste
paste -s --> paste line side by side
paste -d "\t\n" --> add delimeter
paste -d';' - - - ---> this can be used to add 3 column with dilimeter

Arrays
declaring array -->
=> declare -a A
print whole array -->
=> printf "%s " "${A[@]}"
Array slicing -->
=> ${A[@]:1:8}

IF ELSE
Normal if statement-->
if []
then 
{}
fi 
---
if else statement -->
if [ condition ]
then 
	{}
else
	{}
fi
--
if else if -->
if [ condition ]
	{}
elif [ condition ]
	{}
else 
	{}
fi 