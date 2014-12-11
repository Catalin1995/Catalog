catalogApp.controller('StudentAddController', function ($scope, $http) {

	$scope.student = {};
	$scope.valid_add_student = "";

	function validate_add_student(student){
		if ($scope.first_name == ""){
			return false;
		}
		if ($scope.last_name == ""){
			return false;
		}
		if ($scope.clasa == ""){
			return false;
		}
		if ($scope.data_nasteri == ""){
			return false;
		}
		if ($scope.adresa == ""){
			return false;
		}
		if ($scope.alte_informati == ""){
			return false;
		}
		if ($scope.telefon == ""){
			return false;
		}
		if ($scope.cnp == ""){
			return false;
		}
		if ($scope.mail == ""){
			return false;
		}
		return true;
	}

	$scope.adauga_student = function(){

		if (!validate_add_student($scope.student)) {
			$scope.valid_add_student = "Invalid";
		}
		else{
			var url = "/students.json";

			$http.post("/students.json", $scope.student).then(function (result){
				console.log(result);
			});
			$scope.valid_add_student = "Studentul a fost adaugat";
			removeAll();
		}
	}
});
