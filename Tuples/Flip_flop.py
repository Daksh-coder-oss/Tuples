def palind(r):
    s=0
    indexes=len(r)-1
    while s<indexes:
        if r[s]!=r[indexes]:
            return False
        

        s=s+1
        indexes=indexes-1
    return True

r=(1,2,3,3,2,1)
if palind(r):
    print("Filp Flop")
else:
    print("Not a Flip Flop")
    

