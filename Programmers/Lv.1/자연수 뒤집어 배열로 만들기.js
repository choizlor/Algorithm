function solution(n) {
  var answer = [];
  var lst = String(n);
  for (var i = lst.length - 1; 0 <= i; i--) {
    answer.push(parseInt(lst[i]));
  }
  return answer;
}

console.log(solution(12345));
