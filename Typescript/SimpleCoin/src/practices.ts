console.log("hello");

interface Human {
    name: string;
    age: number;
    gender: string;
}

const person = {
    name: "psw",
    age: 26,
    gender: "male"
};

const sayHi = (person: Human): string => {
    return `${person.name}, ${person.age}, ${person.gender}`;
};

console.log(sayHi(person));

class Human2 {
    public name: string;
    private gender: string;

    constructor(name: string, gender: string) {
        this.name = name;
        this.gender = gender;
    }
}

const person2 = new Human2("psw2", "male");
console.log("person2.name :", person2.name);
// console.log("person2.gender :", person2.gender);
