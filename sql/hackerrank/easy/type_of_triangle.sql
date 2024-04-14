Select case when (A+B <=C)  or (B+C <= A) or (C+A <= B) then 'Not A Triangle' 
when (A=B) and (B=C) then 'Equilateral'
when (A=B and C!=A) or (C=B and A!=C) or (A=C and A!=B) then 'Isosceles'
else 'Scalene'
END
from TRIANGLES
