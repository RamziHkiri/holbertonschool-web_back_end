export default function createEmployeesObject(departmentName, employees, number = 11) {
  const obj = { [departmentName] : employees, number }

  return obj;
}
