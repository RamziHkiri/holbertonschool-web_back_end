export default function appendToEachArrayValue(array, appendString) {
  const New_Arra = [];
  for (const idx of array) {
    New_Arra.push(appendString + idx);
  }

  return New_Arra;
}
