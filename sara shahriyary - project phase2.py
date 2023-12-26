#python3.10.6
n=int(input())
jadval=[]
jagozary=[]
sc=0
for i in range(n):
    s=input().split()
    for j in range(n):
        s[j]=int(s[j])
    jadval+=[s]
k=int(input())
for doone in range(k):
    ja=input().split()
    ja[0]=int(ja[0])
    ja[1]=int(ja[1])
    jagozary+=[ja]
#UP
def move_up(j):
    for a in range(n-1):
        for b in range(n):
            if (j[a][b]!=0 and j[a][b]!=1 and j[a][b]!=2 and j[a+1][b]==jadval[a][b]) or (j[a][b]==0):
                j[a][b]=j[a][b]+j[a+1][b]
                j[a+1][b]=0
            elif j[a][b]!=0 and j[a-1][b]!=0 and j[a][b]+j[a+1][b]==3:
                j[a][b]=3
                j[a+1][b]=0
    return j
#DOWN
def move_down(j):
    for a in range(n-1,0,-1):
        for b in range(n):
            if (j[a][b]!=0 and j[a][b]!=1 and j[a][b]!=2 and j[a-1][b]==j[a][b]) or (j[a][b]==0):
                j[a][b]=j[a][b]+j[a-1][b]
                j[a-1][b]=0
            elif j[a][b]!=0 and j[a-1][b]!=0 and j[a][b]+j[a-1][b]==3:
                j[a][b]=3
                j[a-1][b]=0
    return j
#RIGHT
def move_right(j):
    for a in range(n):
        for b in range(n-1,0,-1):
            if (j[a][b]!=0 and j[a][b]!=1 and j[a][b]!=2 and j[a][b-1]==j[a][b]) or (j[a][b]==0):
                j[a][b]=j[a][b]+j[a][b-1]
                j[a][b-1]=0
            elif j[a][b]!=0 and j[a][b-1]!=0 and j[a][b]+j[a][b-1]==3:
                j[a][b]=3
                j[a][b-1]=0
    return j
#LEFT
def move_left(j):
    for a in range(n):
        for b in range(n-1):
            if (j[a][b]!=0 and j[a][b]!=1 and j[a][b]!=2 and j[a][b+1]==j[a][b]) or (j[a][b]==0):
                j[a][b]=j[a][b]+j[a][b+1]
                j[a][b+1]=0
            elif j[a][b]!=0 and j[a][b+1]!=0 and j[a][b]+j[a][b+1]==3:
                j[a][b]=3
                j[a][b+1]=0
    return j

#EMPTY_ROW
def empty_row(table,d,ka):
    count=[]
    if table=='U':
        for a in range(n):
            if jadval[n-1][a]==0:
                count+=[a]
        replace=ka%(len(count))
        jadval[n-1][count[replace]]=d
    elif table=='D':
        for a in range(n):
            if jadval[0][a]==0:
                count+=[a]
        replace=ka%(len(count))
        jadval[0][count[replace]]=d
    return jadval

#EMPTY_COLUMN
def empty_column(table,d,ka):
    count=[]
    if table=='R':
        for a in range(n):
            if jadval[a][0]==0:
                count+=[a]
        replace=ka%(len(count))
        jadval[count[replace]][0]=d
    elif table=='L':
        for a in range(n):
            if jadval[a][n-1]==0:
                count+=[a]
        replace=ka%(len(count))
        jadval[count[replace]][n-1]=d
    return jadval

#previous
def previous(board):
    qabl=[]
    for xi in board:
        pd=[]
        for yi in xi:
            pd+=[yi]
        qabl+=[pd]
    return qabl

# partial or final
def partial_final(bo):
    for xi in bo:
        for yi in xi:
            if yi==0:
                return False
            
    for xi in range(n-1):
        for yi in range(n):
            if (bo[xi][yi]!=1 and bo[xi][yi]!=2 and bo[xi][yi]==bo[xi+1][yi]) or (bo[xi][yi]+bo[xi+1][yi]==3):
                return False
    
    for xi in range(1,n):
        for yi in range(n):
            if (bo[xi][yi]!=1 and bo[xi][yi]!=2 and bo[xi][yi]==bo[xi-1][yi]) or (bo[xi][yi]+bo[xi-1][yi]==3):
                return False
            
    for xi in range(n):
        for yi in range(n-1):
            if (bo[xi][yi]!=1 and bo[xi][yi]!=2 and bo[xi][yi]==bo[xi][yi+1]) or (bo[xi][yi]+bo[xi][yi+1]==3):
                return False
            
    for xi in range(n):
        for yi in range(1,n):
            if (bo[xi][yi]!=1 and bo[xi][yi]!=2 and bo[xi][yi]==bo[xi][yi-1]) or (bo[xi][yi]+bo[xi][yi-1]==3):
                return False

    return True

#PROCESS
y=0
harkat=''
while len(harkat)!=k and partial_final(jadval)==False:
    pre=[]
    while pre!=jadval and len(harkat)!=k and partial_final(jadval)==False:
        pre=previous(jadval)
        move_left(jadval)
        if pre!=jadval:
            empty_column('L',jagozary[y][1],jagozary[y][0])
            y+=1
            harkat+='L'

    pre=[]
    while pre!=jadval and len(harkat)!=k and partial_final(jadval)==False:
        pre=previous(jadval)
        move_down(jadval)
        if pre!=jadval:
            empty_row('D',jagozary[y][1],jagozary[y][0])
            y+=1
            harkat+='D'
        
    pre=[]
    while pre!=jadval and len(harkat)!=k and partial_final(jadval)==False:
        pre=previous(jadval)
        move_right(jadval)
        if pre!=jadval:
            empty_column('R',jagozary[y][1],jagozary[y][0])
            y+=1
            harkat+='R'

    pre=[]
    while pre!=jadval and len(harkat)!=k and partial_final(jadval)==False:
        pre=previous(jadval)
        move_up(jadval)
        if pre!=jadval:
            empty_row('U',jagozary[y][1],jagozary[y][0])
            y+=1
            harkat+='U'

#socre
def score(p):
    meghdar=p/3
    tavan=0
    while meghdar!=1:
        meghdar=meghdar/2
        tavan+=1
    return tavan

for z in jadval:
    for y in z:
        if  y!=0 and y!=1 and y!=2:
            q=score(y)
            sc+=3**(q+1)
#print
print(harkat)
for satr in jadval:
        for deraye in range(n):
            satr[deraye]=str(satr[deraye])
        print('\t'.join(satr))

for satr in jadval:
        for deraye in range(n):
            satr[deraye]=int(satr[deraye])

if partial_final(jadval)==False:
    print('The partial score is '+str(sc)+'.')
else:
    print('The final score is '+str(sc)+'.')