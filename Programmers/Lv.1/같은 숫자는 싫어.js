function solution(arr) {
  let st = [];
  for (let i = 0; i < arr.length; i++) {
    if (st.slice(-1)[0] !== arr[i]) {
      st.push(arr[i]);
    }
  }
  return st;
}

solution([1, 1, 3, 3, 0, 1, 1]);
