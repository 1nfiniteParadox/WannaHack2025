function decryptFlag(flagArray, key) {
    let result = '';
    for (let i = 0; i < flagArray.length; i++) {
        result += String.fromCharCode(flagArray[i] ^ key.charCodeAt(i % key.length));
    }
    return result;
}

function main() {
    const flagArray = [58, 14, 0, 5, 4, 49, 12, 12, 5, 16, 40, 74, 88, 90, 55, 52, 85, 65, 43, 58, 91, 40, 81, 78, 94, 43, 49, 33, 80, 4];
    console.log('Welcome to the challenge!');
    const userInput = prompt('Enter the flag:');
    const decryptedFlag = decryptFlag(flagArray, userInput);
    if (userInput === decryptedFlag) {
        console.log('Congratulations!');
    } else {
        console.log('Wrong Flag');
    }
}

main();
