


function payIncrease(pay, increase){
    if (increase == true){
        return console.log('$' + pay * 0.25)
    }
    else {
        return console.log('$' + pay)
    }
}

payIncrease(50, 1)