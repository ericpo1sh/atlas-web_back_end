export default function uploadPhoto(fileName) {
  return new Promise((reject) => {
    if (fileName) {
      reject(Error(`${fileName} cannot be processed`));
    }
  });
}
