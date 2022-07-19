# cat $1 | sort -n -k3
cat $1 | sort -t$'\t'  -k2 -nr
