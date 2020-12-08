const fib = (n) => {
  if (n <= 2) {
    return 1;
  }
  return fib(n - 1) + fib(n - 2);
};

// Memoize version
const fib2 = (n, memo={}) => {
  if (n in memo) return memo[n];
  if(n<=2) return 1;
  memo[n] = fib2(n - 1, memo) + fib(n - 2, memo);
  return memo[n]
}
//
// console.log(fib(6));
// console.log(fib(7));
// console.log(fib(50));


console.log(fib2(6));
console.log(fib2(7));
console.log(fib2(50));
