count = 0
for i in range(1,5):
    for j in range(1,5):
        if i!=j:
            for k in range(1,5):
                if (j!=k) and (i!=k):
                    print("i,j,k:",i,j,k)
                    count+=1
print("總數：",count)

