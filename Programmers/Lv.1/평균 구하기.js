function solution(arr) {
  var total = arr.reduce((sum, currValue) => {
    return sum + currValue;
  }, 0);
  var answer = total / arr.length
  return answer
}