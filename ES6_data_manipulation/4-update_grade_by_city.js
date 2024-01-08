export default function updateStudentGradeByCity(students, city, newGrades) {
  if (Object.getPrototypeOf(students) !== Array.prototype) {
    return [];
  }
  return students
    .filter((student) => student.location === city)
    .map((student) => {
      const matchedGrade = newGrades.find((grade) => grade.studentId === student.id);

      return {
        ...student,
        grade: matchedGrade ? matchedGrade.grade : 'N/A',
      };
    });
}
