read expression
# echo $expression
echo $expression | bc -l | awk '{printf("%0.3f",$1)}'
# echo expr( expression )