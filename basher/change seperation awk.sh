# awk 'BEGIN{
#     original=""
#     account=1
# }{
#     if (account%2==0 ){
#         account=1
#         original=original";"$a
#         val=original
#         print val 
#         original=""
#     }
#     else{
#         original=$a
#         account++
#     }
# }'

# awk 'ORS=NR%2?";":"\n"'
cat /dev/stdin | awk '{
    if (NR%2==0){

        printf $0"\n";
    }
    else{
 
        printf $0";";
    }
}
'