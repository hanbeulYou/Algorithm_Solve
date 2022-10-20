let fs = require('fs');
let input = fs.readFileSync('/dev/stdin').toString().split(' ');
let N = Number(input);

function findQueens(n) {
	let arrQueen = new Array(n);
	dfs(n, 0, arrQueen);
	return answer;
}

function isValid(n, now, array) {
	for(let i=1; i<=now; i++){
		if(array[now]==array[now-i]) return false;
		if(array[now]-i==array[now-i]) return false;
		if(array[now]+i==array[now-i]) return false;
	}
	return true;
}

function dfs(n, now, array) {
	if(now >= n) {
		answer += 1;
		// console.log(array);
		return;
	}
	for(let i=0; i<n; i++) {
		array[now] = i;
		if(isValid(n, now, array)) {
			dfs(n, now+1, array);
		}
	}
}

let answer = 0;
console.log(findQueens(N)) // 2