// let n = require('synaptic');
// console.log(7556)

let weight = 0.5;
let arr;
let sm = 0.0000001
let p_i = (input) =>{
    return input*weight
}

let r_i = (output) =>{
    return output*weight
}

function train( inp, res){
    rezz = inp * weight;
    arr = res - rezz
    let corr = (arr / rezz) *sm
    weight += corr
}

i = 0;
while(true){
    i++;
    train(100,62.1371)
    // if(i==20000){
        // break;
    // }
    if(!(arr > sm || arr < -sm)){
        break
    }
}
console.log(


    p_i(100),
    p_i(541)

)