catalogApp.controller('StudentDetailsController', function ($scope, $http, $routeParams) {
	$scope.stud_id = $routeParams.orderId;
	var url = "/students/"+$scope.stud_id+".json";
	$http.get(url).then(function (result) {
		console.log(result);
		$scope.student = result.data;  
		complete() 
	});

	$scope.first_name_mod = "";
	$scope.last_name_mod = "";
	$scope.clasa_mod = "";
	$scope.data_nasteri_mod = "";
	$scope.adresa_mod = "";
	$scope.alte_informati_mod = "";
	$scope.note_mod = "";
	$scope.absente_mod = "";
	$scope.valid_modif_student = "";

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

	function complete(){
		$scope.first_name_mod = $scope.student['first_name'];
		$scope.last_name_mod = $scope.student['last_name'];
		$scope.clasa_mod = $scope.student['clasa'] ;
		$scope.data_nasteri_mod = $scope.student['data_nasteri'];
		$scope.adresa_mod = $scope.student['adresa'];
		$scope.alte_informati_mod = $scope.student['alte_informati'];
		$scope.absente_mod = $scope.student['absente'];
		$scope.note_mod = $scope.student['note'];
	}

	function create_student_modif_nota(nota){
		student = {};
		student['first_name'] = $scope.first_name_mod;
		student['last_name'] = $scope.last_name_mod;
		student['clasa'] = $scope.clasa_mod;
		student['data_nasteri'] = $scope.data_nasteri_mod;
		student['adresa'] = $scope.adresa_mod;
		student['alte_informati'] = $scope.alte_informati_mod;
		$scope.note_mod.push(nota);
		student['note'] = $scope.note_mod;
		student['absente'] = $scope.absente_mod;
		return (student);
	}


	function create_student_modif_abs(absenta){
		student = {};
		student['first_name'] = $scope.first_name_mod;
		student['last_name'] = $scope.last_name_mod;
		student['clasa'] = $scope.clasa_mod;
		student['data_nasteri'] = $scope.data_nasteri_mod;
		student['adresa'] = $scope.adresa_mod;
		student['alte_informati'] = $scope.alte_informati_mod;
		student['note'] = $scope.note_mod;
		$scope.absente_mod.push(absenta);
		student['absente'] = $scope.absente_mod;
		return (student);
	}

	function create_student_to_modif(){
		student = {};
		student['first_name'] = $scope.first_name_mod;
		student['last_name'] = $scope.last_name_mod;
		student['clasa'] = $scope.clasa_mod;
		student['data_nasteri'] = $scope.data_nasteri_mod;
		student['adresa'] = $scope.adresa_mod;
		student['alte_informati'] = $scope.alte_informati_mod;
		student['note'] = $scope.note_mod;
		student['absente'] = $scope.absente_mod;
		return (student);
	}
	
	$scope.modifica_student = function(){
		var student = create_student_to_modif();
		if (!validate_modif_student(student)){
			$scope.valid_modif_student = "Invalid";
		}
		else{		
			idStudent = $scope.student['_id']['$oid'];
			var url = "/students/"+idStudent+".json";
			$http.patch(url, student).then(function (result){
				console.log(result);
				$scope.students = result.data;
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
		idStud = $scope.student['_id']['$oid'];
		var url = "/students/"+idStud+".json";
		$http.delete(url).then(function (result){
			console.log(result);
			$scope.students = result.data;
		});
	}
});