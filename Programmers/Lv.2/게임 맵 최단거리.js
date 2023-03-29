function solution(maps) {
  const dx = [-1, 0, 1, 0];
  const dy = [0, 1, 0, -1];
  const n = maps.length;
  const m = maps[0].length;

  let answer = 1;
  let visited = maps;
  let queue = [];

  queue.push([0, 0]);
  visited[0][0] = 0;

  while (queue.length > 0) {
    let len = queue.length

    for (let i = 0; i < len; i++) {
      let [x, y] = queue.shift();

      for (let j = 0; j < 4; j++) {
        let nx = x + dx[j];
        let ny = y + dy[j];

        if (nx >= 0 && nx < n && ny >= 0 && ny < m && visited[nx][ny] === 1) {
          if (nx == n - 1 && ny == m - 1) {
            return ++answer;
          }
          queue.push([nx, ny]);
          visited[nx][ny] = 0;
        }
      }
    }
    answer++;
  }
  return -1;
}
