const crypto = require("crypto");

const mineAdventcoin = function (secretKey, numOfZeros = 5) {
  let number = 1;
  const target = "0".repeat(numOfZeros);

  while (true) {
    const data = secretKey + number.toString();
    const hash = crypto.createHash("md5").update(data).digest("hex");

    if (hash.startsWith(target)) {
      return number;
    }
    number++;
  }
};

const secretKey = "bgvyzdsv";

console.log(mineAdventcoin(secretKey, 6));
