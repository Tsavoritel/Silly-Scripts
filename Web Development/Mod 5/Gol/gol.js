const boardElement = document.getElementById('board');

//Renders the grid to the page
function render(grid) {
    boardElement.innerHTML = '';
    boardElement.style.setProperty('--cols', grid[0].length);
    for (let r = 0; r < grid.length; r++) {
        for (let c = 0; c < grid[r].length; c++) {
            const cell = document.createElement('div');
            cell.className = grid[r][c] === 1 ? 'cell alive' : 'cell';
            boardElement.appendChild(cell);
        }
    }
}

const ROWS = 16;
const COLS = 16;
let grid;

function GenRandGrid() {
    let grid = []
    // loop from 1-10, and each turn creates a new row, then add the row to the grid
    for (let i = 0; i < ROWS; i++) {
        let row = []
        // loop from 1-10 where each turn add 0 to the row
        for (let j = 0; j < COLS; j++) {
            //gen rand float, round to int, then add to row
            cell = Math.random()
            if (cell > 0.9) {
                cell = 1
            }
            else {
                cell = 0
            }
            row.push(cell)
        }
        //add filled row to grid
        grid.push(row)
    }
    return grid;
}

/* function Click()
{
    if (grid[i].row[j] === 0)
        grid[i].row[j] = 1;
}

boardElement.onclick = Click()*/

function CheckNeighbours(r, c) {
    const rowOffSets = [-1, -1, -1, 0, 0, 1, 1, 1]
    const columnOffSets = [-1, 0, 1, -1, -1, -1, 0, 1]
    let alive = 0
    for (let i = -1; i < 2; i++) {
        for (let j = -1; j < 2; j++) {
            //console.log(r+i)
            //console.log(c+j)
            if ((0 <= r+i) && (r+i < ROWS) && (0 <= c+j) && (c+j < COLS)) {
                let neighbor = grid[r+i][c+j]
                //console.log(neighbor)
                if (neighbor === 1)
                    alive++
            }
        }
    }
}

function GenNextGen() {
    let nextGrid = []
    for (let i = 0; i < ROWS; i++) {
        let nextGenRow = []
        for (let j = 0; j < COLS; j++) {
            let cell = grid[i][j]
            let aliveNeighbors = CheckNeighbours(i, j)
            let nextCell = 0
            switch (alive) {
                case (4, 8):
                    console.log("die")
                    break;
                case 3:
                    console.log("breed")
                case (2, 3):
                    console.log("alive")
                    break;
                case (0, 1):
                    console.log("die")
                    break;
            }
        }
        nextGrid.push(nextGenRow)
    }
    grid = nextGrid
}

function step() {
    nextGrid = GenNextGen()
    render(nextGrid)
}

grid = GenRandGrid()
render(grid)

timerId = setInterval(step, 200)
