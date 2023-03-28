function solution(numbers, target) {
  let answer = 0;

  dfs(0, 0);

  function dfs(depth, sumV) {
    if (depth === numbers.length) {
      if (sumV === target) {
        answer++;
      }
      return;
    }
    dfs(depth + 1, sumV + numbers[depth]);
    dfs(depth + 1, sumV - numbers[depth]);
  }

  return answer;
}
