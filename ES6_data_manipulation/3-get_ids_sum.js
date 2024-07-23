export default function getStudentIdsSum(listStu) {
  return listStu.reduce((sum, student) => sum + student.id, 0);
}
