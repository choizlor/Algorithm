function solution(progresses, speeds) {
  let answer = [];
  let len = progresses.length;
  let idx = 0;
  while (idx < len) {
    let st = [];
    for (let i = 0; i < progresses.length; i++) {
      if (progresses[i] < 100) {
        progresses[i] += speeds[i];
      } else {
        if (st.length === i) {
          st.push(progresses[i]);
        }
      }
    }
    for (let i = 0; i < st.length; i++) {
      progresses.shift();
      speeds.shift();
    }

    if (st.length > 0) {
      answer.push(st.length);
      idx += st.length;
    }
  }
  return answer;
}

solution([93, 30, 55], [1, 30, 5]);
