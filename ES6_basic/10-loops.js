export default function appendToEachArrayValue(array, appendString) {
  let new_arra = [];
    for (let idx of array) {
    new_arra.push(appendString + idx);
  }

  return new_arra;
}
