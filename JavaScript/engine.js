
let stack = []

const sum = () => {
    let result = 0
    stack.forEach(elem => {
        result = result + parseInt(elem)
    });
    console.log(result) 
}
const commands = {
    "DFVR436TFDG" : console.log,
    "DGSF546D4GS" : sum
}


const fs = require('fs');
const input = []
const data = fs.readFileSync('../output.omnitrix', 'utf8');

const dataSplited = data.split(',')
const dataFinal = dataSplited.map(x => x.replaceAll("'", "").replaceAll("[", "").replaceAll("]", '').replaceAll(" ", ''))

// dataFinal.forEach(elem => {
//     if(elem == "DFVR436TFDG")
        
// });

let flag = false
let command = ''
for (i = 0; i < dataFinal.length; i++){
    if(dataFinal[i] == "SKEJ4345DFG"){
        flag = false
        commands[command](stack.toString().replaceAll(',,', ' ').replaceAll(',', ''))
        stack = []
        continue
    }

    if(dataFinal[i] == "DFVR436TFDG"){
        command = dataFinal[i]
        flag = true
        continue
    }

    if(dataFinal[i] == "DGSF546D4GS"){
        command = dataFinal[i]
        flag = true
        continue
    }
    if(flag)
        stack.push(dataFinal[i])
}
