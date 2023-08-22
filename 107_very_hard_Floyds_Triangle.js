function floyd(up_to, n_row) {
  const input_list = [];

  const count = up_to ? up_to : n_row;

  for (let countVal = count; countVal > 0; countVal--) {
    const x = Math.floor(countVal * (countVal + 1) / 2);
    const sublist = [];
    for (let i = x; i > x - countVal; i--) {
      sublist.push(i);
    }
    input_list.push(sublist);
  }

  const output_list = input_list.map(sublist => [...sublist].sort((a, b) => a - b));


  if (up_to) {
    const index_containing_target = output_list.findIndex(sublist => sublist.includes(up_to));
    return output_list.slice(0, index_containing_target + 1);
  } else {
    return output_list;
  }
}

// 使用例
console.log(floyd(up_to=1));
console.log(floyd(up_to=2));
console.log(floyd(up_to=7));
console.log(floyd(up_to=9));
console.log(floyd(up_to=15));
console.log(floyd(up_to=50));

console.log(floyd(n_row=1));
console.log(floyd(n_row=2));
console.log(floyd(n_row=5));
console.log(floyd(n_row=6));
console.log(floyd(n_row=11));



