const range = (start, end) => new Array(end - start).fill(start).map((el, i) => start + i);

const shortMonth = [
  '1주차','2주차','3주차','4주차','5주차','6주차','7주차','8주차','9주차','10주차','11주차','12주차',
];
const monthVisitData = shortMonth.map(m => {
  return {
    'month': m,
    '출석': Math.floor(Math.random()) + 20,
    '결석': Math.floor(Math.random()) + 25,
  };
});

const campaignData = [
  {
    value: 335,
    name: 'Website'
  },
  {
    value: 310,
    name: 'Email'
  },
  {
    value: 234,
    name: 'Ads'
  },
  {
    value: 135,
    name: 'Video'
  },
  {
    value: 1548,
    name: 'Search'
  }
];
const locationData = [
  {
    value: 70,
    name: '출석'
  },
  {
    value: 5,
    name: '결석'
  },
  {
    value: 20,
    name: '지각'
  },
  {
    value: 5,
    name: '공결'
  }
];


const StackMainData = [220, 182, 191, 234, 290, 330, 310, 123, 442, 321, 90, 149, 210, 122, 133, 334, 198, 123, 125, 220];
const StackData = StackMainData.map((item, key) => {
  return {
    'label': key + 'D',
    'max': 500,
    'sales': item,
  };
});   
const SinData = range(1, 12).map(i => {
  return {
    'cate': 'Cat' + i,
    'value': ((Math.sin(i / 5) * (i / 5 - 0.1) + i / 6) * 5)
  };
});


export {
  monthVisitData,
  campaignData,
  locationData,
  StackData,
  SinData,
};