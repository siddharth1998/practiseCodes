def data(operations,x):
    Opcount=0
    Xcount=1
    product_list=[]
    while( Opcount < len( operations )):
            
            if operations[Opcount]=="push":
                if Xcount==0:
                    min_val=x[0]
                    max_val=x[0]
                elif(Xcount<len(x)):
                    min_val=min(x[:Xcount])
                    max_val=max(x[:Xcount])
                else:
                    min_val=min(x)
                    max_val=max(x)
                    
                Xcount+=1
            
            elif operations[Opcount]=="pop":
                Xcount-=1
                val=x[Xcount]
                x.remove(val) # removing the first val 
                
                x.remove(val)# removing the second val 
                
                min_val=min(x[:Xcount])
                max_val=max(x[:Xcount])
            product_list.append(min_val*max_val)
                
            Opcount+=1
           
    
    return product_list
print(data(["push","push","pop","push"],[5,2,5,1]))