function solution(brown, yellow) {
  const num = brown + yellow;
  for (var i = 3; i <= num; i++) {
    if (num % i == 0) {
      var n = num / i;
      if ((i - 2) * (n - 2) === yellow) {
        return [n, i];
      }
    }
  }
}

console.log(solution(8, 1));
