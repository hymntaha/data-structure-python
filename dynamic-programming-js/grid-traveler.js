// Slow recursive version
const gridTraveler = (m,n)=>{
  if (m === 1 && n === 1) return 1;
  if (m === 0 || n === 0 ) return 0;
  return gridTraveler(m-1,n) + gridTraveler(m, n-1)
}

const gridTravelerMemoized = (m,n, memo={})=>{
  const key  = m + ',' + n;

  if(key in memo) return memo[key];
  if (m === 1 && n === 1) return 1;
  if (m === 0 || n === 0 ) return 0;

  memo[key] = gridTravelerMemoized(m - 1, n, memo) + gridTravelerMemoized(m, n - 1, memo);
  return memo[key];
}

console.log(gridTravelerMemoized(1,1)) // 1
console.log(gridTravelerMemoized(2,3)) // 3
console.log(gridTravelerMemoized(3,2)) // 3
console.log(gridTravelerMemoized(3,3)) // 6
console.log(gridTravelerMemoized(18,18)) // 2333606220
