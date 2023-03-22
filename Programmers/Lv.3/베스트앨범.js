function solution(genres, plays) {
  let hash = {};
  for (let i = 0; i < genres.length; i++) {
    hash[genres[i]] = hash[genres[i]] ? hash[genres[i]] + plays[i] : plays[i];
  }
  
  console.log(hash.pop)
}

solution(
  ["classic", "pop", "classic", "classic", "pop"],
  [500, 600, 150, 800, 2500]
);
