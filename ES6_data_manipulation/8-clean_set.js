export default function cleanSet(set, startString) {
  const finalString = "";
  for (const word of set) {
    const stringWord = String(word);
    if (stringWord.startsWith(startString)) {
      const slicedWord = stringWord.slice(startString.length);
      finalString += slicedWord;
      if (finalString.length % 2 !== 0 && finalString.length > 1) {
        finalString += "-";
      }
    }
  }
  return finalString;
}
