export default function appendToEachArrayValue(array, appendString) {
  const new_Arra = [];
  for (let idx of array) {
    new_Arra.push(appendString + idx);
  }

  return new_Arra;
}
