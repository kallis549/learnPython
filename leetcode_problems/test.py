import collections

directions = [[1,0],[-1,0],[0,1],[0,-1]]
for dr, dc in directions:
	print("the DR in directions"+str(dr))
	print("the DC in directions"+str(dc))

def numIslands(grid) -> int:
	rows = len(grid);
	cols = len(grid[0]);
	visited = set()
	islands = 0
	q = collections.deque()

	def bfs(r,c):
		q.append((r,c))
		while q:
			row, col = q.popleft()
			for dr, dc in directions:
				r, c= row+dr, col+dc
				if(r in range(rows) and
					c in range(cols) and
					grid[r][c] == "1" and
					(r,c) not in visited):
					q.append((r,c))
					visited.add((r,c))

	print(str(rows)+"|"+str(cols))
	for r in range(rows):
		for c in range(cols):
			if grid[r][c] == "1" and (r,c) not in visited:
				bfs(r,c)
				islands += 1
	return islands
	
print(numIslands([
  ["1","1","0","1","0","1","1"],
  ["1","1","0","0","0","0","1"],
  ["0","0","0","0","0","1","1"],
  ["0","0","1","1","1","0","0"]
]))