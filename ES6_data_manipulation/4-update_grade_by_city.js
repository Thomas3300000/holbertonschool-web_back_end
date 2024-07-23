export default function updateStudentGradeByCity(listStu, city, newGrades) {
  const cityList = listStu.filter((student) => student.location === city);

  const upStudents = cityList.map((student) => {
    const gradeStudent = newGrades.find((grade) => grade.studentId === student.id);
    const grade = gradeStudent ? gradeStudent.grade : 'N/A';
    return { ...student, grade };
  });

  return upStudents;
}
