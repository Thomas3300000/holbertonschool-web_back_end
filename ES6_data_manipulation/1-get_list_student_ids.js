export default function getListStudentIds(listStu) {
  if (!Array.isArray(listStu)) {
    return [];
  }
  return listStu.map((student) => student.id);
}
