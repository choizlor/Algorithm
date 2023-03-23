function solution(cacheSize, cities) {
  let data = [];

  let answer = 0;
  for (let i = 0; i < cities.length; i++) {
    let lower = cities[i].toLowerCase();
    const check = data.indexOf(lower);
    if (check != -1) {
      answer += 1;
      data.splice(check, 1);
      data.push(lower);
    } else {
      answer += 5;
      if (cacheSize === 0) {
      } else if (data.length === cacheSize) {
        data.splice(0, 1);
        data.push(lower);
      } else {
        data.push(lower);
      }
    }
    // console.log(data, answer);
  }
  return answer;
}

solution(0, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA"]);
