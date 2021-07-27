function CodelandUsernameValidation(strParam){
    // code goes here
    
    const pattern = "^(?=[a-zA-Z0-9._]{4,25}$)[^_.].*[^_.]$";
    const result = pattern.test(strParam);
    
    if (result){
        return true;
    }else{
        return false;
    }
}



// keep this function call here 
const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});


console.log(CodelandUsernameValidation(rl.question()));