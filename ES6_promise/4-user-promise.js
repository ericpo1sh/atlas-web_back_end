export default function signUpUser(firstName, lastName) {
  return new Promise((resolve) => {
    if (firstName && lastName) {
      resolve(`{ firstName: ${firstName}, lastName: ${lastName} }`);
    }
  });
}
