catalogApp.factory('Student', function($resource){
	return $resource('/students/:id.json', {});
});

catalogApp.controller('StudentListController', function ($scope, $http, Student) {
	$scope.students = Student.query()
});