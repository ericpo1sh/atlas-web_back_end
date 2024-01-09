export default function handleResponseFromAPI(promise) {
  return new Promise((resolve, reject) => {
    if (resolve) {
      resolve({ status: 200, body: 'Success' })
      console.log('Got a response from the API')
    }
    if (reject) {
      reject(Error);
    }
  });
}
