const fs = require("fs");

// Lee el archivo y lo convierte en un array de instrucciones
const data = fs.readFileSync("./input.txt", "utf8");
const instructions = data.split("\n").filter(Boolean); // Filtra líneas vacías

let graph = {};
let memo = {};

for (let instruction of instructions) {
  const [operation, target] = instruction.split(" -> ");
  graph[target] = operation;
}

//Depth First Search
function dfs(node) {
  if (memo[node] !== undefined) {
    return memo[node];
  }

  if (/^\d+$/.test(node)) {
    console.log("soy un numero");
    return parseInt(node);
  }

  let operation = graph[node];

  if (!operation) {
    return;
  }

  let result;

  if (/^\d+$/.test(operation)) {
    result = parseInt(operation);
  } else if (operation.startsWith("NOT")) {
    let [, wire] = operation.split(" ");
    result = 65535 & ~dfs(wire);
  } else if (operation.includes("AND")) {
    let [a, , b] = operation.split(" ");
    result = dfs(a) & dfs(b);
  } else if (operation.includes("OR")) {
    let [a, , b] = operation.split(" ");
    result = dfs(a) | dfs(b);
  } else if (operation.includes("LSHIFT")) {
    let [a, , value] = operation.split(" ");
    result = dfs(a) << parseInt(value);
  } else if (operation.includes("RSHIFT")) {
    let [a, , value] = operation.split(" ");
    result = dfs(a) >> parseInt(value);
  } else {
    result = dfs(operation);
  }

  memo[node] = result;
  return result;
}

const signalToA = dfs("a");
console.log(`The signal to wire 'a' is: ${signalToA}`);
