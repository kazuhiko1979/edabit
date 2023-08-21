function ordinal(n) {
  return n + ([(n % 10 != 1) * (n % 10 != 2) * (n % 10 != 3) || (n % 100 == 11 || n % 100 == 12 || n % 100 == 13) ? "th" : "st", "nd", "rd"][n % 10 - 1] || "th");
}

function EPLResult(table, team) {
  var result = table.slice().sort(function(a, b) {
      return ((a[2] * 3) + (a[3] * 1) - ((b[2] * 3) + (b[3] * 1))) || (a[5] - b[5]);
  }).reverse();

  for (var i = 0; i < result.length; i++) {
      var l = result[i];
      if (l[0] == team) {
          return `${team} came ${i + 1}${ordinal(i + 1)} with ${l[2] * 3 + l[3] * 1} points and a goal difference of ${l[5]}!`;
      }
  }
}

// テスト
var table = [
	['Arsenal', 38, 14, 14, 10, 8],
	['Aston Villa', 38, 9, 8, 21, -26],
	['Bournemouth', 38, 9, 7, 22, -26],
	['Brighton', 38, 9, 14, 15, -15],
	['Burnley', 38, 15, 9, 14, -7],
	['Chelsea', 38, 20, 6, 12, 15],
	['Crystal Palace', 38, 11, 10, 17, -19],
	['Everton', 38, 13, 10, 15, -12],
	['Leicester City', 38, 18, 8, 12, 26],
	['Liverpool', 38, 32, 3, 3, 52],
	['Manchester City', 38, 26, 3, 9, 67],
	['Manchester Utd', 38, 18, 12, 8, 30],
	['Newcastle', 38, 11, 11, 16, -20],
	['Norwich', 38, 5, 6, 27, -49],
	['Sheffield Utd', 38, 14, 12, 12, 0],
	['Southampton', 38, 15, 7, 16, -9],
	['Tottenham', 38, 16, 11, 11, 14],
	['Watford', 38, 8, 10, 20, -28],
	['West Ham', 38, 10, 9, 19, -13],
	['Wolves', 38, 15, 14, 9, 11]
]

console.log(EPLResult(table, "Liverpool"));
console.log(EPLResult(table, "Manchester Utd"));
console.log(EPLResult(table, "Norwich"));
