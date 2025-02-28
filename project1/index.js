// RANDOM PASSWORD GENERATOR
///const (Variable value = fixed cant be changed)
////let (Variable value can be change)

function generatePassword(length, includeLowercase, includeUppercase,includeNumbers,includeSymbols){

    const lowercaseChars  = "abcdefghijklmnopqrstuvwxyz";
    const uppercaseChars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    const numberChars = "0123456789";
    const symbolChars = "!@#$%^&*()_+-="

    let allowedChars = "";
    let password = "";
// ? (same like ifelse, but used to write simple conditions)
    allowedChars += includeLowercase ? lowercaseChars : "";
    allowedChars += includeUppercase ? uppercaseChars : "";
    allowedChars += includeNumbers ? numberChars : "";
    allowedChars += includeSymbols ? symbolChars : "";

   if(length <=0){
        return `(password length must be at least 1)`;
   }
//Unlike == (loose equality), ===( It compares the values exactly as they are)
   if(allowedChars.length === 0){
        return `(at lease 1 set of character need to be selected)`;
   }
   for(let i = 0; i < length; i++){
        const randomIndex = Math.floor(Math.random() * allowedChars.length);
        password += allowedChars[randomIndex];
    }
    return password;
}


const passwordLength = 12;
const includeLowercase = true;
const includeUppercase = true;
const includeNumbers = true;
const includeSymbols = true;

const password = generatePassword(passwordLength,
                                  includeLowercase,
                                  includeUppercase,
                                  includeNumbers,
                                  includeSymbols);

console.log(`Generated password: ${password}`);