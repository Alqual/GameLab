/*import fetch from "node-fetch";*/
async function getData() {
  const xs = [];
  const ys = [];
  const response = await fetch('sample_.csv');
  const data = await response.text();
  const table = data.split(/\n/).slice(1);
  table.forEach(row => {
    const columns = row.split(',');
    const year = columns[0];
    xs.push(year);
    const temp = columns[1];
    ys.push(parseFloat(temp) + 14);
  })
  return { xs, ys }
}

getData();
console.log("anata!!");
