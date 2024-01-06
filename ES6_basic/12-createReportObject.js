export default function createReportObject(employeesList) {
  return {
    allEmployees: employeesList,
    numberOfDeps() {
      return Object.keys(thisallEmployees).length;
    },
  };
}
