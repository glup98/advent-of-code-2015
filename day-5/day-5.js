const fs = require("fs");

const vocals = "aeiou";
const forbidden = ["ab", "cd", "pq", "xy"];
let niceStrings = 0;
let reallyNiceString = 0;

const isNiceString = function (string) {
  let vowels = 0;
  let doubleLetter = false;
  let forbiddenString = false;

  for (let i = 0; i < string.length; i++) {
    const char = string[i];

    if (vocals.includes(char)) {
      vowels++;
    }

    if (string[i + 1] === char) {
      doubleLetter = true;
    }

    if (forbidden.includes(char + string[i + 1])) {
      forbiddenString = true;
    }
  }

  return vowels >= 3 && doubleLetter && !forbiddenString;
};

const isReallyNiceString = function (string) {
  let doublePair = false;
  let repeatLetter = false;
  for (let i = 0; i < string.length; i++) {
    const pair = string[i] + string[i + 1];
    const restOfString = string.slice(i + 2);

    if (restOfString.includes(pair)) {
      doublePair = true;
    }

    if (string[i + 2] === string[i]) {
      repeatLetter = true;
    }
  }
  return doublePair && repeatLetter;
};

//Leer el archivo y ejecutar las funciones
fs.readFile("./input.txt", "utf8", (err, data) => {
  if (err) {
    console.error(err);
    return;
  }
  for (const string of data.split("\n")) {
    if (isNiceString(string)) {
      niceStrings++;
    }
    if (isReallyNiceString(string)) {
      reallyNiceString++;
    }
  }
  console.log(niceStrings);
  console.log(reallyNiceString);
});
