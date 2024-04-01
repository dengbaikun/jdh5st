function decodeString(encodedString) {
    const base64Chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789+/";
    let decodedString = "";
    for (let i = 0, bitGroup = 0, bitCount = 0, currentChar; currentChar = encodedString.charAt(i++);) {
        if (currentChar !== '=') {
            bitGroup = (bitGroup << 6) | base64Chars.indexOf(currentChar);
            if ((bitCount += 6) >= 8) {
                decodedString += String.fromCharCode((bitGroup >> (bitCount -= 8)) & 0xFF);
            }
        }
    }
    return decodedString;
}
function findString(index) {
    const keyArray = ["mZyZnLDHD2LhBW", "rNLlAwe", "AfHAvK0", "mtr6zLPWwuS", "Dxfswhu", "mJjPvufXuuu", "mZm3ofvfzg51DG", "mJGZmtj3y1Dur3O", "mxvJDdzKmgPOCq", "mJeXmtu1mJnVy1LsA3i", "ntG0mtqXmfbPtMvbDq", "nZG3ody2AfrMyKrU", "nde2ntvPCvbnz1K", "ve5psKi", "mtaXnJaYr1jPBxLm", "C1rKDM0", "mtjPte5Wqvi", "mZG4ChPmB2Di"];
    let adjustedIndex = index - 327;
    let keyString = keyArray[adjustedIndex];
    return decodeString(keyString);
}

function selectRandomCharacters(sourceString, count) {
    let result = '';
    let remainingCharacters = [...sourceString]; // 将字符串转换为字符数组以便操作

    for (let i = 0; i < count && remainingCharacters.length > 0; i++) {
        let randomIndex = Math.floor(Math.random() * remainingCharacters.length);
        result += remainingCharacters[randomIndex];
        remainingCharacters.splice(randomIndex, 1); // 从数组中移除已选字符
    }

    return result;
}
// 将随机数的范围扩大到0到10，包括0但不包括10 实现向下取整
function g() {
    return 10 * Math.random() | 0
}


function removeCharacters(source, charsToRemove) {
    const pattern = new RegExp(`[${charsToRemove}]`, 'g');
    return source.replace(pattern, "");
}

function m(options) {
    let length = options.size;
    const characters = options.num;
    let result = "";

    while (length--) {
        let randomIndex = Math.floor(Math.random() * characters.length);
        result += characters[randomIndex];
    }

    return result;
}

// function genFingerPrint() {
//     var r = findString(335), n = selectRandomCharacters(r, 4), o = g(), i = removeCharacters(r, n)
//         ,a = ((m({
//         size: o, num: i
//     }) + n + m({
//         size: ((12 - o)) - 1, num: i
//     })) + o).split(""), u = a.slice(0, 8), h = a.slice(8), p = [];
//     for (; u.length > 0;) {
//         p.push((35 - parseInt(u.pop(), 36)).toString(36))
//     }
//     return (p.concat(h)).join("")
//
// }

function genFingerPrint() {
    // 获取基础字符串
    let baseString = findString(335);
    // 从基础字符串中选择4个随机字符
    let randomCharacters = selectRandomCharacters(baseString, 4);
    // 从基础字符串中移除这些随机选择的字符
    let baseStringWithoutRandom = removeCharacters(baseString, randomCharacters);
    // 将随机数的范围扩大到0到10，包括0但不包括10 实现向下取整
    let o = g();
    // 使用修改后的字符串生成新的随机字符串
    let generatedString1 = m({ size: o, num: baseStringWithoutRandom });
    // 再次生成字符串，长度根据之前的数值动态调整
    let generatedString2 = m({ size: 12 - o - 1, num: baseStringWithoutRandom });
    // 组合所有生成的字符串，并转换为字符数组
    let combinedString = (generatedString1 + randomCharacters + generatedString2 + o).split("");
    // 分离数组的前8个字符和剩余的部分
    let firstPart = combinedString.slice(0, 8);
    let secondPart = combinedString.slice(8);
    // 将第一部分的每个字符转换并反转，使用 reduceRight 实现
    let transformedFirstPart = firstPart.reduceRight((accumulator, character) =>
        accumulator + (35 - parseInt(character, 36)).toString(36), "");
    // 合并转换后的第一部分和第二部分，生成最终的字符串
    return transformedFirstPart + secondPart.join("");
}


console.info(genFingerPrint())