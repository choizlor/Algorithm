const changeTime = (time) => {
  let [hour, minute] = time.split(":");
  return parseInt(hour) * 60 + parseInt(minute);
};

function solution(book_time) {
  let time = [];

  book_time.sort().forEach((time) => {
    const start = changeTime(time[0]);
    const end = changeTime(time[1]) + 10;

    if (time.length === 0) {
      time.push(end);
    } else {
      time.sort();
      let check = true;
      for (let i = 0; i < time.length; i++) {
        if (start >= answer[i]) {
          answer[i] = end;
          check = false;
          break;
        }
      }
      if (check) answer.push(end);
    }
  });
  return time.length;
}

solution([
  ["15:00", "17:00"],
  ["16:40", "18:20"],
  ["14:20", "15:20"],
  ["14:10", "19:20"],
  ["18:20", "21:20"],
]);
