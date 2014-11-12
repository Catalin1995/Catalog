var catalogApp = angular.module('catalogApp', []);

catalogApp.controller('StudentListController', function ($scope, $http) {
  $http.get("/students.json").then(function (result) {
  	console.log(result);
  	$scope.students = result.data;
  });

  $scope.idStud = 1;
  $scope.studentId = "asd";
  $scope.give_stud = function(){
  	var url = "/students/"+$scope.idStud+".json";
	$http.get(url).then(function (result) {
  	console.log(result);
  	$scope.studentId = result.data;
  });
}
  
  //$scope.studentId = $scope.give_stud();
  //$scope.aux = 1;
  //$scope.first_name = "Last name";
  //$scope.last_name  = "First name";

  //$http.post('/students.json', first_name, last_name).then(function(result) {
  //	console.log(result);
  //	$scope.student = result.data;
  //});
});
