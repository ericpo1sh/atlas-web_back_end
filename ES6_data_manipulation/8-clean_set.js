export default function cleanSet(set, startString) {
  const finalString = "";
  for (const word of set) {
    if (word.has(startString)) {
      word.slice(startString.length) += finalString;
      if (finalString.length % 2 !== 0 && finalString.length > 1) {
        finalString += "-";
      }
    }
  }
  return finalString;
}
