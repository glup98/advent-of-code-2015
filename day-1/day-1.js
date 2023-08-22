import fs from "fs";

fs.readFile("./puzzle-input-1.txt", "utf8", (err, data) => {
  if (err) {
    console.error(err);
    return;
  }

  console.log(positionToEnterBasement(data));
});

const findFloor = function (instructions) {
  let floor = 0;

  for (let i = 0; i < instructions.length; i++) {
    if (instructions[i] === "(") {
      floor++;
    } else if (instructions[i] === ")") {
      floor--;
    }
  }

  return floor;
};

const positionToEnterBasement = function (instructions) {
  let floor = 0;

  for (let i = 0; i < instructions.length; i++) {
    if (instructions[i] === "(") {
      floor++;
    } else if (instructions[i] === ")") {
      floor--;
    }

    if (floor === -1) {
      return i + 1;
    }
  }

  return "Santa never enters the basement";
};
