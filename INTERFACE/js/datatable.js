var industry_company = {
    2: [4, [21, 22, 23, 24], [20, 21, 22, 23], "电池：", ["安全\n", "科研\n", "市场\n"], ['能量密度\n','自燃事故频率\n','循环寿命\n']],
    3: [3, [31, 32, 33], [30, 31], '电机(集成)：', ["稳定\n", "效率\n", "积累\n", '散热\n'], ['扭矩\n','能耗\n']],
    20: ['负极材料：', ],
    21: ['正极锂材料：'],
    22: ['电解液：'],
    23: ['隔膜：'],
    30: ['电子电控：'],
    31: ['五金：']
}

var weight = {
    1: {
        2: 2,
        3: 1.5,
    },
    2: {
        20: 2, 
        21: 2.5,
        22: 1.8, 
        23: 1.3
    }, 
    3: {
        30: 0.8, 
        31: 1.8
    }
}

var companies = {
    21: ["三星SDI", [211, 212, 201, 202, 221, 222, 231, 232], [90, 91, 87], 89, 'd2'],
    22: ["宁德时代", [212, 213, 203, 223, 233], [89, 87, 81], 85.5, 'ba'],
    23: ["松下电器", [214, 204, 234, 222], [85, 89, 83], 85.5, 'ba'],
    24: ["比亚迪", [224, 235, 203, 215], [87, 92, 81], 86.5, 'bb'],

    31: ["博世", [301, 311, 312, 313], [95, 92, 84], 90.5, 'de'],
    32: ["方正电机", [314, 304], [82, 88, 79], 83,'aa'],
    33: ["大洋电动机", [302, 303, 314], [88, 85, 80], 84,'b9'],

    201: ["浦项制铁", [89, 88, 85], 'cd'],
    202: ["贝特瑞（负极材料）", [85, 85, 80], 'b9'],
    203: ["凯金能源", [80, 82, 78], 'aa'],
    204: ["日立化学", [82, 78, 82], 'aa'],

    211: ["Ecopro", [90, 88, 90], 'de'],
    212: ["贝特瑞（正极材料）", [88, 88, 85], 'cd'],
    213: ["北大先行", [80, 78, 85], 'a8'],
    214: ["住友金属", [88, 76, 83], 'aa'],
    215: ["天赐材料", [73, 75, 76], '99'],
    
    
    221: ["新宙邦", [81, 80, 85], 'a8'],
    222: ["三菱化学", [88, 82, 85], 'c0'],
    223: ["江苏国泰", [83, 78, 81], 'aa'],
    224: ["杉杉电池", [88, 80, 81], 'ad'],
    

    231: ["旭化成", [82, 83, 82], 'ad'],
    232: ["东丽", [82, 82, 78], 'aa'],
    233: ["璞泰来", [78, 80, 75], '9d'],
    234: ["住友化学", [88, 85, 83], 'b7'],
    235: ["星源材质", [75, 73, 75], '9b'],
    
    301: ['EM-motive', [85, 80, 88], 'ae'],
    302: ['上汽电控', [85, 90, 85], 'bb'],
    303: ['芯长征', [80, 85, 84], 'b1'],
    304: ['汇川技术', [84, 84, 81], 'aa'],
    

    311: ['Essex', [90, 75, 80], 'c2'],
    312: ['Trelleborg Sealing', [87, 73, 78], 'b5'],
    313: ['Kennametal', [88, 80, 81], 'ae'],
    314: ['本土中小厂家', [75, 75, 75], '9a'],

}


function avgColor(color1, color2) {
    //separate each color alone (red, green, blue) from the first parameter (color1) 
    //then convert to decimal
    let color1Decimal = {
      red: parseInt(color1.slice(0, 2), 16),
      green: parseInt(color1.slice(2, 4), 16),
      blue: parseInt(color1.slice(4, 6), 16)
    }
    //separate each color alone (red, green, blue) from the second parameter (color2) 
    //then convert to decimal
    let color2Decimal = {
      red: parseInt(color2.slice(0, 2), 16),
      green: parseInt(color2.slice(2, 4), 16),
      blue: parseInt(color2.slice(4, 6), 16),
    }
    // calculate the average of each color (red, green, blue) from each parameter (color1,color2) 
    let color3Decimal = {
      red: Math.ceil((color1Decimal.red + color2Decimal.red) / 2),
      green: Math.ceil((color1Decimal.green + color2Decimal.green) / 2),
      blue: Math.ceil((color1Decimal.blue + color2Decimal.blue) / 2)
    }
    //convert the result to hexadecimal and don't forget if the result is one character
    //then convert it to uppercase
    let color3Hex = {
      red: color3Decimal.red.toString(16).padStart(2, '0').toUpperCase(),
      green: color3Decimal.green.toString(16).padStart(2, '0').toUpperCase(),
      blue: color3Decimal.blue.toString(16).padStart(2, '0').toUpperCase()
    }
    //put the colors (red, green, blue) together to have the output
    let color3 = color3Hex.red + color3Hex.green + color3Hex.blue
    return color3
  }
  console.log(avgColor("FF33CC", "3300FF"))
  // avgColor("FF33CC", "3300FF") => "991AE6"
  
  console.log(avgColor("991AE6", "FF0000"))
  // avgColor("991AE6", "FF0000") => "CC0D73"
  
  console.log(avgColor("CC0D73", "0000FF"))
  // avgColor("CC0D73", "0000FF") => "6607B9"
  