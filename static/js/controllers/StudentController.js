catalogApp.factory('Student', function($resource){
	return $resource('/students/:id.json', {});
});

catalogApp.controller('StudentDetailsController', function ($scope, $http, $routeParams, Student) {
	$scope.stud_id = $routeParams.orderId;
	// Student.get(data)
	var url = "/students/"+$scope.stud_id+".json";
	$http.get(url).then(function (result) {
		console.log(result);
		$scope.student = result.data;
	});

	$scope.valid_modif_student = "";

	$scope.student = {};

	function validate_modif_student(student){
		if (student.first_name == ""){
			return false;
		}
		if (student.last_name == ""){
			return false;
		}
		if (student.clasa == ""){
			return false;
		}
		if (student.data_nasteri == ""){
			return false;
		}
		if (student.adresa == ""){
			return false;
		}
		if (student.alte_informati == ""){
			return false;
		}
		if (student.telefon == ""){
			return false;
		}
		if (student.cnp == ""){
			return false;
		}
		if (student.mail == ""){
			return false;
		}
		return true;
	}

	function validate_nota(nota){
		var valid = parseInt(nota)
		if (valid < 1){
			return false
		}
		else if(valid > 10){
			return false
		}
		else if(valid == ""){
			return false
		} 
		else if(valid != nota){
			return false
		}
		return true
	}

	$scope.modifica_student = function(){
		if (!validate_modif_student($scope.student)){
			$scope.valid_modif_student = "Invalid";
		}
		else{		
			idStudent = $scope.student['_id']['$oid'];
			var url = "/students/"+idStudent+".json";
			$http.patch(url, $scope.student).then(function (result){
				console.log(result);
				$scope.student = result.data;
				$scope.valid_modif_student = "Studentul a fost modificat!"
			});
		}
	}

	$scope.add_nota = function(){
		$scope.validate_absenta = "";
		$scope.validate_nota = "";
		idStud = $scope.student['_id']['$oid'];
		if (validate_nota($scope.nota) == true){
			student = create_student_modif_nota($scope.nota);
			var url = "/students/"+idStud+".json";
			$http.patch(url, student).then(function (result){
				console.log(result);
				$scope.students = result.data;
			});
			$scope.validate_nota = "Nota a fost adaugata";
			$scope.nota = "";
		}
		else{
			$scope.validate_nota = "Nota invalida";
			$scope.validate_absenta = ""
		}
	} 


	$scope.add_absenta = function(){
		$scope.validate_absenta = "";
		$scope.validate_nota = "";
		idStud = $scope.student['_id']['$oid'];
		if ($scope.absenta != ""){
			student = create_student_modif_abs($scope.absenta);
			var url = "/students/"+idStud+".json";
			$http.patch(url, student).then(function (result){
				console.log(result);
				$scope.students = result.data;
			});
			$scope.validate_absenta = "Absenta a fost adaugata";
			$scope.absenta = "";
		}
		else{
			$scope.validate_absenta = "Absenta invalida"
			$scope.validate_nota = "";
		}
	}


	$scope.delete_student_id = function(){
		id = $scope.student['_id']['$oid'];
		var data  = {id: id};
		Student.delete(data);
	}
});