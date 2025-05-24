function Summarize (...n) {
    let sum = 0
    for (let i of n){
        return sum += i
    }
    return sum
}

console.log(Summarize(1,3,5))


const Male = {
    Muscle: "5kg",
    Money: "500k Dollars"
}

const Female = {
    height: "150cm",
    weight:"60kg"
}

const person = {...Male,  ...Female}