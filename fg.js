// let n = require('synaptic');
// console.log(7556)

let weight = 0.5; // 0.5
let arr;
let sm = 0.00001 // 0.0000001
let p_i = (input) =>{
    return input*weight
}

let r_i = (output) =>{
    return output/weight
}
let corr;
function train( inp, res){
    rezz = inp * weight;
    arr = res - rezz
    // sm=1
    corr = (arr / rezz) *sm

    weight += corr
    // console.log("rezz "+ rezz);
    // console.log("corr " + corr);
    // console.log("arr "+arr);
    // console.log("sm "+sm);
    // console.log("weight "+weight);
    // console.log("-------------------------------");
    
}

i = 0;
while(true){
    i++;
    train(100,62.1371)

    // if(corr<=5){
        // console.log(corr);
        // console.log(i);
        // console.log("jkgjfgfffffffffffff");

    // }

    if(i%100000==0){
        console.log((arr > sm))
        console.log((arr < -sm))
        console.log("0000000000000000")
    }
    if(!(arr > sm || arr < -sm)){
    // console.log("arr "+arr);
    // console.log("sm "+sm);
    // console.log("sm ");

    //     console.log((arr > sm))
    //     console.log((arr < -sm))
    //     console.log(i)
    console.log("weight "+weight);

        break
    }


}
// console.log(!(arr > sm || arr < -sm))
// console.log(arr < -sm)

console.log(


    p_i(100),
    p_i(541)
// 
)
    // console.log(

        // (arr / rezz) * sm
    // );
    // console.log("rezz "+ rezz);
    // console.log("arr "+arr);
