const readline = require('readline');
process.stdin.setEncoding('utf-8');
const rl = readline.createInterface({input: process.stdin});
let lineNumber = 0;
let caseNumber = 0;
rl.on('line', (line) => {
    lineNumber++;
    if (lineNumber >= 3 && lineNumber % 2 === 1) {
        caseNumber++;
        const map = {};
        let hIndex = 1;
        let papersAboveHIndex = 0;
        let result = line
            .split(' ')
            .map(value => {
                if (value > hIndex) {
                    map[value] = map[value] ? map[value] + 1 : 1;
                    papersAboveHIndex += 1;
                    while (papersAboveHIndex > hIndex) {
                        hIndex += 1;
                        papersAboveHIndex -= map[hIndex] ? map[hIndex] : 0;
                    }
                }
                return hIndex;
            });
        console.log('Case #' + caseNumber + ': ' + result.join(' '));
    }
});