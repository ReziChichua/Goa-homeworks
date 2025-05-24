//1
function solution(str){
    return str.split('').reverse().join('');
  }

//2
function points(games) {
    let total = 0;
    for (let game of games) {
      const [x, y] = game.split(':').map(Number);
      if (x > y) total += 3;
      else if (x === y) total += 1;
    }
    return total;
  }

  
//3
function addBinary(a, b) {
    return (a + b).toString(2);
  }

//4
function removeDuplicates(arr) {
    return [...new Set(arr)];
  }

  
//5
function removeUrlAnchor(url){
    return url.split('#')[0];
  }

  
//6
String.prototype.isUpperCase = function() {
    return this.toString() === this.toUpperCase();
  }
  