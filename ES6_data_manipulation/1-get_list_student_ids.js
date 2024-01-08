export default function getListStudentsIds(list) {
  if (typeof list !== 'object') {
    return [];
  } else {
    return list.map(student => student.id);
  }
}
