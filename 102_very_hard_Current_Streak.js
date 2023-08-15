
function totalDaysBetweenDates(date1, date2) {
  const oneDay = 24 * 60 * 60 * 1000;
  const diffInDays = Math.abs(moment(date2).diff(moment(date1), 'days'));
  return diffInDays
}

function current_streak(today, lst) {
  const result = lst.slice(0, -1).map((_, i) => totalDaysBetweenDates(lst[i]['date'], lst[i+1]['date']));

  let start = 1;
  result.forEach(diff => {
    start = diff === 1 ? start + 1 : 1;
  });

  return lst.length > 0 && totalDaysBetweenDates(today, lst.slice(-1)[0]['date']) === 0 ? start : 0;

}

console.log(current_streak("1985-03-19", [
  {
    "date": "1985-03-19"
  }
]))

console.log(current_streak("2019-09-23", [
  {
    "date": "2019-09-18"
  },
  {
    "date": "2019-09-19"
  },
  {
    "date": "2019-09-21"
  },
  {
    "date": "2019-09-22"
  },
  {
    "date": "2019-09-23"
  }
]))

console.log(current_streak("2019-09-30", [
  {
    "date": "2019-09-18"
  },
  {
    "date": "2019-09-19"
  },
  {
    "date": "2019-09-20"
  },
  {
    "date": "2019-09-26"
  },
  {
    "date": "2019-09-27"
  },
  {
    "date": "2019-09-30"
  }
]))

console.log(current_streak("2019-09-23", [
  {
    "date": "2019-09-18"
  },
  {
    "date": "2019-09-19"
  },
  {
    "date": "2019-09-20"
  },
  {
    "date": "2019-09-21"
  },
  {
    "date": "2019-09-22"
  },
  {
    "date": "2019-09-23"
  }
]))

console.log(current_streak("2019-09-23", [
  {
    "date": "2019-06-25"
  },
  {
    "date": "2019-06-28"
  },
  {
    "date": "2019-07-02"
  },
  {
    "date": "2019-07-07"
  },
  {
    "date": "2019-07-09"
  },
  {
    "date": "2019-07-12"
  },
  {
    "date": "2019-07-13"
  },
  {
    "date": "2019-07-14"
  },
  {
    "date": "2019-07-15"
  },
  {
    "date": "2019-07-16"
  },
  {
    "date": "2019-07-17"
  },
  {
    "date": "2019-07-25"
  },
  {
    "date": "2019-07-26"
  },
  {
    "date": "2019-07-29"
  },
  {
    "date": "2019-07-31"
  },
  {
    "date": "2019-08-03"
  },
  {
    "date": "2019-08-06"
  },
  {
    "date": "2019-08-07"
  },
  {
    "date": "2019-08-09"
  },
  {
    "date": "2019-08-12"
  },
  {
    "date": "2019-08-13"
  },
  {
    "date": "2019-08-14"
  },
  {
    "date": "2019-08-16"
  },
  {
    "date": "2019-08-17"
  },
  {
    "date": "2019-08-21"
  },
  {
    "date": "2019-08-22"
  },
  {
    "date": "2019-08-23"
  },
  {
    "date": "2019-08-24"
  },
  {
    "date": "2019-08-25"
  },
  {
    "date": "2019-08-26"
  },
  {
    "date": "2019-08-27"
  },
  {
    "date": "2019-08-28"
  },
  {
    "date": "2019-08-29"
  },
  {
    "date": "2019-08-30"
  },
  {
    "date": "2019-09-02"
  },
  {
    "date": "2019-09-03"
  },
  {
    "date": "2019-09-04"
  },
  {
    "date": "2019-09-05"
  },
  {
    "date": "2019-09-06"
  },
  {
    "date": "2019-09-08"
  },
  {
    "date": "2019-09-11"
  },
  {
    "date": "2019-09-12"
  },
  {
    "date": "2019-09-13"
  },
  {
    "date": "2019-09-15"
  },
  {
    "date": "2019-09-16"
  },
  {
    "date": "2019-09-17"
  },
  {
    "date": "2019-09-18"
  },
  {
    "date": "2019-09-20"
  },
  {
    "date": "2019-09-22"
  },
  {
    "date": "2019-09-23"
  }
]))

console.log(current_streak("2019-09-25", [
  {
    "date": "2019-09-16"
  },
  {
    "date": "2019-09-17"
  },
  {
    "date": "2019-09-21"
  },
  {
    "date": "2019-09-22"
  },
  {
    "date": "2019-09-23"
  }
]))

console.log(current_streak("2019-09-16", []))