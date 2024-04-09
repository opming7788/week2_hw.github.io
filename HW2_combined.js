console.log("==============Task1================");
function findAndPrint(messages, current_station) {
  const greenLine = [
    "Songshan",
    "Nanjing Sanmin",
    "Taipei Arena",
    "Nanjing Fuxing",
    "Songjiang Nanjing",
    "Zhongshan",
    "Beimen",
    "Ximen",
    "Xiaonanmen",
    "Chiang Kai-shek Memorial Hall",
    "Guting",
    "Taipower Building",
    "Gongguan",
    "Wanlong",
    "Jingmei",
    "Dapinglin",
    "Qizhang",
    "Xindian City Hall",
    "Xindian",
  ];
  const greenLineModified = [
    "Songshan",
    "Nanjing Sanmin",
    "Taipei Arena",
    "Nanjing Fuxing",
    "Songjiang Nanjing",
    "Zhongshan",
    "Beimen",
    "Ximen",
    "Xiaonanmen",
    "Chiang Kai-shek Memorial Hall",
    "Guting",
    "Taipower Building",
    "Gongguan",
    "Wanlong",
    "Jingmei",
    "Dapinglin",
    "Qizhang",
    "Xindian City Hall",
    "Xindian",
    "Xiaobitan",
  ];
  let Frdlocation = {};

  for (const [friend, stationText] of Object.entries(messages)) {
    const friendstation = greenLineModified.filter((str) =>
      stationText.includes(str)
    );
    Frdlocation[friend] = friendstation[0];
  }

  let myindex = greenLine.indexOf(current_station);
  let distcollc = {};

  for (const itm of greenLine) {
    const dist = Math.abs(greenLine.indexOf(itm) - myindex);
    distcollc[itm] = dist;
  }

  distcollc["Xiaobitan"] = Math.abs(greenLine.indexOf("Qizhang") - myindex) + 1;

  let dis_of_friends = {};

  for (const [friend, frlocation] of Object.entries(Frdlocation)) {
    for (const [location, dist2] of Object.entries(distcollc)) {
      if (frlocation === location) {
        dis_of_friends[friend] = dist2;
      }
    }
  }

  const min_dist_of_friends = Math.min(...Object.values(dis_of_friends));
  let nearest_friends = [];

  for (const [key, value] of Object.entries(dis_of_friends)) {
    if (value === min_dist_of_friends) {
      nearest_friends.push(key);
    }
  }

  console.log(nearest_friends.join(" "));
}

const messages = {
  Leslie: "I'm at home near Xiaobitan station.",
  Bob: "I'm at Ximen MRT station.",
  Mary: "I have a drink near Jingmei MRT station.",
  Copper: "I just saw a concert at Taipei Arena.",
  Vivian: "I'm at Xindian station waiting for you.",
};

findAndPrint(messages, "Wanlong"); // print Mary
findAndPrint(messages, "Songshan"); // print Copper
findAndPrint(messages, "Qizhang"); // print Leslie
findAndPrint(messages, "Ximen"); // print Bob
findAndPrint(messages, "Xindian City Hall"); // print Vivian

console.log("==============Task2================");

let schedule = [];

function book(consultants, hour, duration, criteria) {
  if (schedule.length === 0) {
    consultants.forEach((consultant) => {
      let name = consultant.name; // 取得 "name" 屬性的值
      schedule.push({ [name]: [], ...consultant }); // 創建新的物件，將 "name" 屬性替換為新的鍵值對
    });
  }

  let duration_Time = [];
  for (let i = 1; i <= duration; i++) {
    duration_Time.push(hour);
    hour += 1;
  }

  let is_available = [];
  if (criteria === "price") {
    for (let consultant of schedule) {
      if (
        !consultant[Object.keys(consultant)[0]].some((time) =>
          duration_Time.includes(time)
        )
      ) {
        is_available.push(consultant);
      }
    }

    if (is_available.length === 0) {
      console.log("No Service");
      return;
    }

    let min_price_consultant = is_available.reduce((prev, curr) =>
      prev.price < curr.price ? prev : curr
    );
    let first_key = Object.keys(min_price_consultant)[0];
    console.log(first_key);

    let consultantToUpdate = schedule.find(
      (consultant) => Object.keys(consultant)[0] === first_key
    );
    if (consultantToUpdate) {
      consultantToUpdate[first_key] = [
        ...consultantToUpdate[first_key],
        ...duration_Time,
      ];
    }
  } else if (criteria === "rate") {
    for (let consultant of schedule) {
      if (
        !consultant[Object.keys(consultant)[0]].some((time) =>
          duration_Time.includes(time)
        )
      ) {
        is_available.push(consultant);
      }
    }

    if (is_available.length === 0) {
      console.log("No Service");
      return;
    }

    let max_rate_consultant = is_available.reduce((prev, curr) =>
      prev.rate > curr.rate ? prev : curr
    );
    let first_key = Object.keys(max_rate_consultant)[0];
    console.log(first_key);

    let consultantToUpdate = schedule.find(
      (consultant) => Object.keys(consultant)[0] === first_key
    );
    if (consultantToUpdate) {
      consultantToUpdate[first_key] = [
        ...consultantToUpdate[first_key],
        ...duration_Time,
      ];
    }
  }
}

const consultants = [
  { name: "John", rate: 4.5, price: 1000 },
  { name: "Bob", rate: 3, price: 1200 },
  { name: "Jenny", rate: 3.8, price: 800 },
];

book(consultants, 15, 1, "price"); // Jenny
book(consultants, 11, 2, "price"); // Jenny
book(consultants, 10, 2, "price"); // John
book(consultants, 20, 2, "rate"); // John
book(consultants, 11, 1, "rate"); // Bob
book(consultants, 11, 2, "rate"); // No Service
book(consultants, 14, 3, "price"); // John

console.log("==============Task3================");

function func(...data) {
  let mydic = {};
  for (let mytext of data) {
    let index = Math.floor(mytext.length / 2);
    mydic[mytext] = mytext[index];
  }

  let unique_values = {};
  for (let [key, value] of Object.entries(mydic)) {
    if (!(value in unique_values)) {
      unique_values[value] = key;
    } else {
      unique_values[value] = null;
    }
  }

  let unique_keys = Object.keys(unique_values).filter(
    (key) => unique_values[key] !== null
  );

  if (unique_keys.length === 0) {
    console.log("沒有");
  } else {
    for (let value of unique_keys) {
      console.log(unique_values[value]);
    }
  }
}

func("彭大牆", "陳王明雅", "吳明"); // print 彭大牆
func("郭靜雅", "王立強", "郭林靜宜", "郭立恆", "林花花"); // print 林花花
func("郭宣雅", "林靜宜", "郭宣恆", "林靜花"); // print 沒有
func("郭宣雅", "夏曼藍波安", "郭宣恆"); // print 夏曼藍波安

console.log("==============Task4================");

function getNumber(index) {
  // your code here
  let n = Math.floor((index + 1) / 3);
  n += 1;
  let mycolle = [0];
  let start = 0;
  for (let i = 0; i < n; i++) {
    for (let a = 0; a < 2; a++) {
      start += 4;
      mycolle.push(start);
    }
    start -= 1;
    mycolle.push(start);
  }
  console.log(mycolle[index]);
}
getNumber(1); // print 4
getNumber(5); // print 15
getNumber(10); // print 25
getNumber(30); // print 70

console.log("==============Task5================");

function find(spaces, stat, n) {
  let availableSeats_Dist_between_n = spaces.map((x, index) => x * stat[index]); // 將spaces和stat做內積，使用map函數遍歷兩個陣列並進行對應元素相乘
  let candidateSeats = []; // 蒐集可供搭乘的列車車廂候選
  availableSeats_Dist_between_n.forEach((itm, index) => {
    // 使用forEach函數遍歷availableSeats_Dist_between_n
    if (itm !== 0 && itm >= n) {
      // 尋找有座位的車廂且該車廂座位數大於需要搭乘的人數n
      candidateSeats.push(itm); // 蒐集可供搭乘的列車車廂候選
    }
  });
  if (candidateSeats.length !== 0) {
    // 若發現有可供搭乘的列車車廂
    console.log(
      availableSeats_Dist_between_n.indexOf(Math.min(...candidateSeats))
    ); // 印出該可供搭乘的列車車廂編號
  } else {
    // 找不到可供搭乘的列車車廂回傳-1
    console.log(-1);
  }
}

find([3, 1, 5, 4, 3, 2], [0, 1, 0, 1, 1, 1], 2); // print 5
find([1, 0, 5, 1, 3], [0, 1, 0, 1, 1], 4); // print -1
find([4, 6, 5, 8], [0, 1, 1, 1], 4); // print 2
