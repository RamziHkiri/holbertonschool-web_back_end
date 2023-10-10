export default function cleanSet(set, startString) {
  if (startString === '') return '';
  const str = [];
  set.forEach((element) => {
    if (element && element.startsWith(startString)) {
      str.push(element.replace(startString, ''));
    }
  });
  return str.join('-');
}
