//danfojs-main.js
const dfd = require("danfojs-node");

const arr_data = [[1, 'hello', 3.2],
            [5, 'danfojs',7.5],[3, 'javascipt',10.0]];

df = new dfd.DataFrame(arr_data)
df.ctypes.print()