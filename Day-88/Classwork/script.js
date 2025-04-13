function Summarize (...n) {
    let sum = 0
    for (let i of n){
        return sum += i
    }
    return sum
}

console.log(Summarize(1,3,5,6,8))