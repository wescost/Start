def fields(map):
    count=0
    for i in range(0,len(map)):
        for j in range(0,len(map)):
            if(map[i][j]==1):
                count+=1
                area(map,i,j)
    
                return count;

def area(map,i,j):
    map[i][j]=2
    if(j-1>=0 and map[i-1][j]==1):
        area (map,i-1,j)
    if(j+1<len(map) and map[i+1][j]==1):
        area(map,i+1,j)
    if(i-1>=0 and map[i-1][j]==1):
        area(map,i-1,j)
    if(i+1<len(map) and map[i+1][j]==1):
        area(map,i+1,j)



map=[[1,1,0,0,0],
     [1,0,0,1,1],
     [0,0,0,0,0],
     [1,1,0,0,0],
     [0,0,0,0,1]]

count = fields(map)
print(count)