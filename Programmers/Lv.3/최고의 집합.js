function solution(n, s) {
  if (n > s) return [-1];
  const num = Math.floor(s / n);
  const answer = new Array(n).fill(num);

  for (let i = 0; i < s % n; i++) {
    answer[answer.length - 1 - i]++;
  }
  
  return answer;
}
