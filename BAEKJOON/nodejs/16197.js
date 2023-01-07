// 16197 두 동전
const fs = require('fs');
const inputData = fs.readFileSync('./input.txt').toString().trim().split('\n');
// const inputData = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

const [N, M] = inputData[0].split(' ').map(Number);
const board = inputData.slice(1).map((item) => item.trim().split(''));
const visited = {}

const dx = [-1, 1, 0, 0];
const dy = [0, 0, -1, 1];

function coinInit() {
  const firstCoinsLoc = []
  for (let i = 0; i < N; i++) {
    for (let j = 0; j < M; j++) {
      if (board[i][j] === 'o') {
        firstCoinsLoc.push(i);
        firstCoinsLoc.push(j);
      }
    }
  }
  firstCoinsLoc.push(0)
  return [[...firstCoinsLoc]]
}

const coins = coinInit()

// 동전 위치 찾기
const bfs = () => {

  while (coins.length) {
    const [x1, y1, x2, y2, count] = coins.shift();

    if (count >= 10) {
      return -1;
    }

    for (let k = 0; k < 4; k++) {
      let nx1 = x1 + dx[k];
      let ny1 = y1 + dy[k];
      let nx2 = x2 + dx[k];
      let ny2 = y2 + dy[k];
      if(visited[[nx1, ny1, nx2, ny2]] === true) continue
      visited[[nx1, ny1, nx2, ny2]] = true

      if (0 <= nx1 && nx1 < N && 0 <= ny1 && ny1 < M && 0 <= nx2 && nx2 < N && 0 <= ny2 && ny2 < M) {
        if (board[nx1][ny1] === '#' && board[nx2][ny2] === '#') {
          continue
        }
        if (board[nx1][ny1] === '#') {
          [nx1, ny1] = [x1, y1];
        }
        if (board[nx2][ny2] === '#') {
          [nx2, ny2] = [x2, y2];
        }
        coins.push([nx1, ny1, nx2, ny2, count + 1]);
      } else if (0 <= nx1 && nx1 < N && 0 <= ny1 && ny1 < M) {        // coin2가 떨어진 경우
        return count + 1;
      } else if (0 <= nx2 && nx2 < N && 0 <= ny2 && ny2 < M) {        // coin1이 떨어진 경우
        return count + 1;
      } else {                                                        // 둘 다 떨어진 경우 무시
        continue;
      }
    } 
  }
  return -1;          // 큐가 빌 동안 리턴값이 없다면 -1 리턴
}

const ans = bfs();
console.log(ans);