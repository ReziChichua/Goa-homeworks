function myForEach(array, callback) {
    for (let i = 0; i < array.length; i++) {
      callback(array[i], i, array);
    }
  }


function myMap(x, callback) {
    const result = [];
    for (let i = 0; i < x.length; i++) {
      result.push(callback(array[i], i, x));
    }
    return result;
  }