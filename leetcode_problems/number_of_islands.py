#Number of Islands
#Given an m x n 2d grid map of '1's (land) and '0's (water), return the #number of islands.
#
#An island is surrounded by water and is formed by connecting adjacent lands #horizontally or vertically. You may assume all four edges of the grid are #all surrounded by water.
#
#
#
#Example 1:
#
#Input: grid = [
#  ["1","1","1","1","0"],
#  ["1","1","0","1","0"],
#  ["1","1","0","0","0"],
#  ["0","0","0","0","0"]
#]
#Output: 1
#Example 2:
#
#Input: grid = [
#  ["1","1","0","0","0"],
#  ["1","1","0","0","0"],
#  ["0","0","1","0","0"],
#  ["0","0","0","1","1"]
#]
#Output: 3

import collections

var = range(20)
print(var[12])


def numIslands(grid) -> int:
  if not grid :
    return 0

  rows = len(grid)
  cols = len(grid[0])
  visited = set()
  islands = 0
  q = collections.deque()
  
  def bfs(r,c):
    q.append((r,c))
    while q:
      row, col = q.popleft()
      directions = [[1,0],[-1,0],[0,1],[0,-1]]
      for dr, dc in directions:
        r, c = row+dr, col+dc
        if(r in range(rows) and
           c in range(cols) and
           grid[r][c] == "1" and
           (r, c) not in visited):
          q.append((r,c))
          visited.add((r,c))

  for r in range(rows):
    for c in range(cols):
      if grid[r][c]=="1" and (r,c) not in visited:
        bfs(r,c)
        islands += 1
  return islands
  

print(numIslands([
  ["1","1","0","0","0","1","1"],
  ["1","1","0","0","0","0","1"],
  ["0","0","1","0","0","1","1"],
  ["0","0","0","1","1","0","0"]
]))


#numIslands([
#  ["1","1","1","1","0"],
#  ["1","1","0","1","0"],
#  ["1","1","0","0","0"],
#  ["0","0","0","0","0"]
#])
