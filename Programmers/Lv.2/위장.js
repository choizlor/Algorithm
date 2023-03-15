function solution(clothes) {
  let answer = 1;
  let obj = {};
  for (let i = 0; i < clothes.length; i++) {
    obj[clothes[i][1]] = (obj[clothes[i][1]] || true) + 1;
  }

  for (let key in obj) {
    answer *= obj[key];
  }

  return answer - 1;
}

solution([
  ["yellow_hat", "headgear"],
  ["blue_sunglasses", "eyewear"],
  ["green_turban", "headgear"],
]);
