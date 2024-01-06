export default function createReportObject(employeesList) {
  return {
    employees: employeesList,
    numberOfDeps() {
      return Object.keys(this.employees).length;
    },
  };
}
