function solution(n) {
  var answer = 0;
  for (var i = 1; i <= n; i++) {
    // 약수의 개수 구하기
    if (n % i === 0 && i % 2 === 1) answer++;
  }
  return answer;
}
