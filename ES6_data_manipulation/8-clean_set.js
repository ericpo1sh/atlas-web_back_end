export default function cleanSet(set, startString) {
  let finalString = "";
  for (const word of set) {
    const stringWord = String(word);
    if (stringWord.startsWith(startString)) {
      const slicedWord = stringWord.slice(startString.length);
      finalString += (finalString.length !== 0 && slicedWord.length !== 0) ? `-${slicedWord}` : slicedWord;
    }
  }
  return finalString;
}
