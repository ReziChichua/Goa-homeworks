//JSON ნიშნავს JavaScript Object Notation.

//ეს არის მსუბუქი, მარტივად წასაკითხი ფორმატი, რომელიც გამოიყენება მონაცემების შესანახად და გადაცემისთვის — განსაკუთრებით სერვერსა და ვებ-აპლიკაციას შორის.


// JSON → JavaScript ობიექტი
const jsonText = '{"name":"Luka","age":25}';
const obj = JSON.parse(jsonText); // now obj.name = "Luka"

// JavaScript ობიექტი → JSON string
const jsonStr = JSON.stringify(obj);
