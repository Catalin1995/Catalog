catalogApp.controller('StudentListController', function ($scope, $http) {
  $http.get("/students.json").then(function (result) {
   console.log(result);
   $scope.students = result.data;
 });
});
