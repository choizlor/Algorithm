function solution(s) {
  var st = [];
  for (var i = 0; i < s.length; i++) {
    if (s[i] === st.slice(-1)[0]) {
      st.pop();
    } else {
      st.push(s[i]);
    }
  }
  return st.length === 0 ? 1 : 0;
}

console.log(solution("baabaa"));
