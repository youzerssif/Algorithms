const tableau = [1,2,3,4,5,4]
const dictionnaire = {"a":1, "b":2, "c":3}

for (const tab of tableau){
    console.log(tab)
}

for (const dict in dictionnaire){
    console.log(`${dict} : ${dictionnaire[dict]}`)
}