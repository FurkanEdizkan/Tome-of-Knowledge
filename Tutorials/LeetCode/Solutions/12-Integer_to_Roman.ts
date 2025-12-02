

function intToRoman(num: number): string {
    const values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1];
    const symbols = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"];
    
    let result = "";
    
    for (let i = 0; i < values.length; i++) {
        while (num >= values[i]) {
            result += symbols[i];
            num -= values[i];
        }
    }
    
    return result;
}


const tests: [number, string][] = [
    [3749, "MMMDCCXLIX"],
    [58, "LVIII"],
    [1994, "MCMXCIV"],
    [1, "I"],
    [3999, "MMMCMXCIX"],
];

for (const [num, expected] of tests) {
    const result = intToRoman(num);
    const status = result === expected ? "✓" : "✗";
    console.log(`${status} intToRoman(${num}) = "${result}" (expected "${expected}")`);
}