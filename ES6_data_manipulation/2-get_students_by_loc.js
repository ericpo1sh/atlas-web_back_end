export default function getStudentsByLocation(students, city) {
  if (Object.getPrototypeOf(students) !== Array.prototype) {
    return [];
  }
  return students.filter((loco) => loco.location === city)
}
