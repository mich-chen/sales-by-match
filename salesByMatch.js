'use strict';

function sockMerchant(n, ar) {
    let stack = new Object();
    let pairCount = 0;

    for (let i = 0; i < n; i++) {
        if (stack.hasOwnProperty(ar[i])){
            delete stack[ar[i]]
            pairCount++
        } else {
            stack[ar[i]] = true
    }};

    return pairCount
}

function main() {
    const n = 9;

    const ar = [10, 20, 20, 10, 10, 30, 50, 10, 20];

    let result = sockMerchant(n, ar);

    return result
}

console.log(main())