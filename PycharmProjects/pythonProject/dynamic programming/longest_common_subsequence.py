def lcs(seq1,seq2):
    n1,n2=len(seq1),len(seq2)
    table=[[0 for x in range(n2+1)]for x in range(n1+1)]

    for i in range(n1):
        for j in range(n2):
            if seq2[j]==seq1[i]:
                table[i+1][j+1]=1+table[i][j]
            else:

                table[i + 1][j + 1]=max(table[i][j+1],table[i+1][j])
    print(table)
    return table[-1][-1]

print(lcs('naveen','srinathen'))

