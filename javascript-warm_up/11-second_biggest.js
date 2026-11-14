#!/usr/bin/node
if (process.argv.length <= 3) {
  console.log(0);
} else {
  let max = Number(process.argv[2]);
  let secondMax = Number(process.argv[3]);

  if (secondMax > max) {
    const temp = max;
    max = secondMax;
    secondMax = temp;
  }

  for (let i = 4; i < process.argv.length; i++) {
    const num = Number(process.argv[i]);
    if (num > max) {
      secondMax = max;
      max = num;
    } else if (num > secondMax && num < max) {
      secondMax = num;
    }
  }
  console.log(secondMax);
}
