export default function getStudentIdsSum(students) {
  if (Object.getPrototypeOf(students) !== Array.prototype) {
    return [];
  }
  return students.reduce((student) => student.id );
}
