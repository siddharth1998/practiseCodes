awk 'BEGIN {
num=0
}
{
num=($2+$3+$4)/3
if (num >= 80){
grade="A"
print $a " : " grade;
}
else if (num < 80 && num>=60){
grade="B"
print $a " : " grade;}
else if (num < 60 && num >=50){
grade="A"
print $a " : " grade;}
else{
grade="FAIL"
print $a " : " grade }
}'