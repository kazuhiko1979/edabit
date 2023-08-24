function secret_password(message) {
  const alphabet = 'abcdefghijklmnopqrstuvwxyz';

  if (message.length !== 9 || /[A-Z]/.test(message) || !/^[a-z]+$/.test(message)) {
    return "BANG! BANG! BANG!";
  }
  
  const divided_1 = `${alphabet.indexOf(message[0]) + 1}${message[1]}${alphabet.indexOf(message[2]) + 1}`;
  const divided_2 = message.substring(3, 6).split('').reverse().join('');
  const divided_3 = message.substring(6).split('').map(char => {
    if (char === 'z') {
        return 'a';
    } else if (char >= 'a' && char <= 'z') {
        return String.fromCharCode((char.charCodeAt(0) - 'a'.charCodeAt(0) + 1) % 26 + 'a'.charCodeAt(0));
    }
    return char;
  }).join('');

  return divided_2 + divided_3 + divided_1
  }

  // Test cases
console.log(secret_password("mubashirh"));
console.log(secret_password("mattedabi"));
console.log(secret_password("HeLen-eda"));
console.log(secret_password("pakistani"));
console.log(secret_password("airforce1"));
console.log(secret_password("airforces"));
console.log(secret_password("Airforcee"));
console.log(secret_password("pilotmuba"));
console.log(secret_password("a_rforcee"));
console.log(secret_password("iloveherh"));
console.log(secret_password("airforcess"));
console.log(secret_password("edabit"));