
const firstName = ["Jon", "Arya", "Jamie"];
const lastName = ["Snow", "Stark", "Lannister"];
const places = ["The Wall", "Winterfell", "Kings Landing"];

const bios = [];

for(var i = 0; i < firstName.length; i++) {
    bios[i] = "My name is " + firstName[i] + " " + lastName[i] +" and I am from " + places[i];
}

console.log(bios);