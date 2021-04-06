"""
0- We can loop each position in the matrix and we can compute longest path each step.
1- Our recursive call can determine longest path in the direction
2- We can give 0 for out of bounds position or if the value in a specific direction is less than or equal to current position
3- We can give 1 if the value in a specific direction is larger than the current position
4- Once we can identify this, we can have bottom up memoization and update our cache matrix array
5- While we update the cache array, we need to get the max value of directions of each position: For instance:

Matrix [2][2] is 8 and each direction of 8 is 0,0,0,0 because each direction is either out of bounds or bigger than that direction.
So we have to calculate that via max(0,0,0,0). Once we get this max value, we need to add 1 to count current position.
The reason we want to add 1 to current position is to be able to identify if we already visited this position or not.

6- Once we calculate this max value, we also need to keep track of longest path recursively.

I tried to sketch this down on a paper, because it is really hard to explain it over docs.

We can also create directions enum to identify directions in the code base.

"""
