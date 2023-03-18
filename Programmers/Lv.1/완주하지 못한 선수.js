function solution(participant, completion) {
  let hash = [];
  participant.forEach((par) => {
    hash[par] = hash[par] ? hash[par] + 1 : 1;
  });
  completion.forEach((com) => {
    hash[com] = hash[com] - 1;
  });

  for (let key in hash) {
    if (hash[key]) return key;
  }
}

solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"]);
