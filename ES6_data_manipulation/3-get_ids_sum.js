export default function getStudentIdsSum(students) {
  if (Object.getPrototypeOf(students) !== Array.prototype) {
    return [];
  }
  const listOfIds = students.map((student) => student.id);
  const initialValue = 0;
  const sumWithInitial = listOfIds.reduce(
    (accumulator, currentValue) => accumulator + currentValue,
    initialValue,
  );
  return sumWithInitial;
}
