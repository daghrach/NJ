import sys
import numpy as np
from sys import maxint

d = np.array(
        [
          [0, 34, 60, 47, 45],
          [34, 0, 56, 49, 47], 
          [60, 56, 0, 50, 48],
          [47, 49, 50, 0, 22],
          [45, 47, 48, 22, 0],
         ]
        )

# ancienne fonction 1
n = d.shape[0]
q = np.zeros((n,n))
for i in xrange(n):
    for j in xrange(n):
        if i == j:
            q[i][j] = 0
        else:
            sumI = 0
            sumJ = 0
            for k in xrange(n):
               sumI += d[i][k]
               sumJ += d[j][k]
            q[i][j] = (n-2) * d[i][j] - sumI - sumJ

# anicenne fonction 2 
minVal = maxint
for i in xrange(0,n):
    for j in xrange(i,n):
        if (q[i][j] < minVal):
            minVal = q[i][j]
            minIndex = (i,j)

# ancienne fonction 3
i = minIndex[0]
j = minIndex[1]

sumI = 0
sumJ = 0
for k in xrange(n):
    sumI += d[i][k]
    sumJ += d[j][k]

dfu = (1. / (2. * (n - 2.))) * ((n - 2.) * d[i][j] + sumI - sumJ)
dgu = (1. / (2. * (n - 2.))) * ((n - 2.) * d[i][j] - sumI + sumJ)

#ancienne fonction 4
nd = np.zeros((n-1,n-1))

# Copy over the old data to this matrix
ii = jj = 1
for i in xrange(0,n):
     if i == f or i == g:
        continue
     for j in xrange(0,n):
        if j == f or j == g:
           continue
        nd[ii][jj] = d[i][j]
        jj += 1
    ii += 1
    jj = 1
            
# Calculate the first row and column
ii = 1
for i in range (0,n):
    if i == f or i == g:
        continue
    nd[0][ii] = (d[f][i] + d[g][i] - d[f][g]) / 2.
    nd[ii][0] = (d[f][i] + d[g][i] - d[f][g]) / 2.
    ii += 1
