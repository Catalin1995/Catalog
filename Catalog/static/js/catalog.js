var catalogApp = angular.module('catalogApp', []);

catalogApp.controller('StudentListController', function ($scope, $http) {
  $http.get("/students.json").then(function (result) {
  	console.log(result);
  	$scope.students = result.data;
  });

  $scope.first_name_mod = ""; 
  $scope.last_name_mod = "";
  $scope.clsa_mod = "";
  $scope.data_nasteri_mod = "";
  $scope.adresa_mod = "";
  $scope.alte_informati_mod = "";

  $scope.first_name = "";
  $scope.last_name = "";
  $scope.clasa = "";
  $scope.data_nasteri = "";
  $scope.adresa = "";
  $scope.alte_informati = "";

  $scope.idStud = "";
  $scope.studentId = {};
  $scope.studentId['Id'] = "";
  $scope.valid_add_student = ""

  function validate_id(idStud){
    if (idStud == "") {
      return false;
    }
    else {
      return true;
    }
  }

  function validate_add_student(){
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
    return true;
  }

  function complete_type_text(){
    $scope.first_name_mod = $scope.studentId['first_name'];
    $scope.last_name_mod = $scope.studentId['last_name'];
    $scope.clasa_mod = $scope.studentId['clasa'];
    $scope.data_nasteri_mod = $scope.studentId['data_nasteri'];
    $scope.adresa_mod = $scope.studentId['adresa'];
    $scope.alte_informati_mod = $scope.studentId['alte_informati'];
  }

  function remove_all(){
    $scope.first_name = "";
    $scope.last_name = "";
    $scope.clasa = "";
    $scope.data_nasteri = "";
    $scope.adresa = "";
    $scope.alte_informati = "";
    $scope.valid_add_student = "Studentul a fost adaugat";
  }

  function create_student(){
    student = {};
    student['first_name'] = $scope.first_name;
    student['last_name'] = $scope.last_name;
    student['clasa'] = $scope.clasa;
    student['data_nasteri'] = $scope.data_nasteri;
    student['adresa'] = $scope.adresa;
    student['alte_informati'] = $scope.alte_informati;
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
    return (student);
  }

  $scope.give_stud = function(){
    var valid = validate_id($scope.idStud);
    if (valid == 1) {
      var url = "/students/"+$scope.idStud+".json";
      $http.get(url).then(function (result) {
        console.log(result);
        $scope.studentId = result.data;
        complete_type_text()
      });
    }
    else{
     $scope.studentId['Id'] = "Invalid Id!!!";
   }
 }

 $scope.delete_student_id = function(){
   if (validate_id($scope.idStud)) {
    var url = "/students/"+$scope.idStud+".json";
    $http.delete(url).then(function (result){
      console.log(result);
      $scope.students = result.data;
    });
  }
  else{
   $scope.studentId['Id'] = "Invalid Id!!!";
 }
}

$scope.adauga_student = function(){

  if (!validate_add_student()) {
    $scope.valid_add_student = "Invalid";
  }
  else{
    var url = "/students.json";
    student = create_student();

    $http.post("/students.json", student).then(function (result){
      console.log(result);
      $scope.students.push(result.data);
    });
    remove_all();
  }
}


$scope.modifica_student = function(){
  if(validate_id($scope.idStud)){
    var student = create_student_to_modif();
    var url = "/students/"+$scope.idStud+".json";
    $http.patch(url, student).then(function (result){
      console.log(result);
      //$scope.students = result.data;
    });
  }
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
