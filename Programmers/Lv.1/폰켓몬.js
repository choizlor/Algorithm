function solution(nums) {
  let n = nums.length / 2;
  let obj = {};
  for (let i = 0; i < nums.length; i++) {
    if (obj[nums[i]] && true) {
    } else {
      obj[nums[i]] = 1;
    }
  }
  let len = 0;
  for (key in obj) {
    len++;
  }
  return n < len ? n: len
}

solution([3, 1, 2, 3]);
