var catalogApp = angular.module('catalogApp', []);

catalogApp.controller('StudentListController', function ($scope) {
  $scope.students = [
    {'first_name': 'A', 'last_name': 'B'},
    {'first_name': 'C', 'last_name': 'D'},
    {'first_name': 'E', 'last_name': 'F'}
  ];
});
