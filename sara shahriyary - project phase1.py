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
harkat=input()
for k in range(len(harkat)):
    s=input().split()
    s[0]=int(s[0])
    s[1]=int(s[1])
    jagozary+=[s]
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
def empty_row(t,d,k):
    count=[]
    if t=='U':
        for a in range(n):
            if jadval[n-1][a]==0:
                count+=[a]
        s=k%(len(count))
        jadval[n-1][count[s]]=d
    elif t=='D':
        for a in range(n):
            if jadval[0][a]==0:
                count+=[a]
        s=k%(len(count))
        jadval[0][count[s]]=d
    return jadval

#EMPTY_COLUMN
def empty_column(t,d,k):
    count=[]
    if t=='R':
        for a in range(n):
            if jadval[a][0]==0:
                count+=[a]
        s=k%(len(count))
        jadval[count[s]][0]=d
    elif t=='L':
        for a in range(n):
            if jadval[a][n-1]==0:
                count+=[a]
        s=k%(len(count))
        jadval[count[s]][n-1]=d
    return jadval

#previous
def previous(board):
    pre=[]
    for xi in board:
        pd=[]
        for yi in xi:
            pd+=[yi]
        pre+=[pd]
    return pre

#PROCESS
y=0
for x in range(len(harkat)):
    if harkat[x]=='U':
        pre=previous(jadval)
        jadval=move_up(jadval)
        if pre!=jadval:
            empty_row('U',jagozary[y][1],jagozary[y][0])
            y+=1

    elif harkat[x]=='D':
        pre=previous(jadval)
        jadval=move_down(jadval)
        if pre!=jadval:
            empty_row('D',jagozary[y][1],jagozary[y][0])
            y+=1

    elif harkat[x]=='R':
        pre=previous(jadval)
        jadval=move_right(jadval)
        if pre!=jadval:
            empty_column('R',jagozary[y][1],jagozary[y][0])
            y+=1

    elif harkat[x]=='L':
        pre=previous(jadval)
        jadval=move_left(jadval)
        if pre!=jadval:
            empty_column('L',jagozary[y][1],jagozary[y][0])
            y+=1
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
for satr in jadval:
        for deraye in range(n):
            satr[deraye]=str(satr[deraye])
        print('\t'.join(satr))

for satr in jadval:
        for deraye in range(n):
            satr[deraye]=int(satr[deraye])

# partial or final
def partial_final(bo):
    for xi in bo:
        for yi in xi:
            if yi==0:
                return 'The partial score is '
            
    for xi in range(n-1):
        for yi in range(n):
            if (bo[xi][yi]!=1 and bo[xi][yi]!=2 and bo[xi][yi]==bo[xi+1][yi]) or (bo[xi][yi]+bo[xi+1][yi]==3):
                return 'The partial score is '
    
    for xi in range(1,n):
        for yi in range(n):
            if (bo[xi][yi]!=1 and bo[xi][yi]!=2 and bo[xi][yi]==bo[xi-1][yi]) or (bo[xi][yi]+bo[xi-1][yi]==3):
                return 'The partial score is '
            
    for xi in range(n):
        for yi in range(n-1):
            if (bo[xi][yi]!=1 and bo[xi][yi]!=2 and bo[xi][yi]==bo[xi][yi+1]) or (bo[xi][yi]+bo[xi][yi+1]==3):
                return 'The partial score is '       
            
    for xi in range(n):
        for yi in range(1,n):
            if (bo[xi][yi]!=1 and bo[xi][yi]!=2 and bo[xi][yi]==bo[xi][yi-1]) or (bo[xi][yi]+bo[xi][yi-1]==3):
                return 'The partial score is '

    return 'The final score is '
     
print(partial_final(jadval)+str(sc)+'.')