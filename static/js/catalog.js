// TODO indetare.  de ce incepe cu spatiu?
  var catalogApp = angular.module('catalogApp', ['ngRoute']);

  catalogApp.config(['$routeProvider',
    function($routeProvider) {
      $routeProvider
      .when('/students', {
        // TODO move to partials/students/list.html
        templateUrl: "partials/list.html",
        controller: "StudentListController"
      })

      .when('/modifStudent',{
        // TODO move to partials/students/update.html
        templateUrl: "partials/modifStudent.html",
        controller: "StudentListController"
      })

      // TODO move to partials/students/show.html
      .when('/student/:orderId',{
        templateUrl: 'partials/modifStudent.html',
        controller: "StudentModifController"
      })

      .when('/addStudent', {
        // TODO move to partials/students/new.html
        templateUrl: "partials/addstudent.html",
        controller: "StudentListController"
      });
    }]);

  // TODO rename to StudentController
  // TODO move to js/controllers/StudentController.js
  catalogApp.controller('StudentModifController', function ($scope, $http, $routeParams) {
    // TODO rename to studentId
    $scope.order_id = $routeParams.orderId;
    var url = "/students/"+$scope.order_id+".json";
    $http.get(url).then(function (result) {
      console.log(result);
      $scope.studentId = result.data;
    })
    $scope.message = $scope.order_id
  });

  // TODO move to js/controllers/StudentListController.js
  catalogApp.controller('StudentListController', function ($scope, $http) {
    $http.get("/students.json").then(function (result) {
     console.log(result);
     $scope.students = result.data;
   });



    $scope.array_absente = [];
    $scope.array_note = [];
    $scope.validate_absenta = "";
    $scope.validate_nota = "";
    $scope.array_absente_msg = "";
    $scope.array_note_msg = "";

    $scope.first_name_mod = ""; 
    $scope.last_name_mod = "";
    $scope.clasa_mod = "";
    $scope.data_nasteri_mod = "";
    $scope.adresa_mod = "";
    $scope.alte_informati_mod = "";
    $scope.note_mod = "";
    $scope.absente_mod = "";
    $scope.new_nota_mod = "nota";
    $scope.new_absenta_mod = "absenta";

    $scope.first_name = "";
    $scope.last_name = "";
    $scope.clasa = "";
    $scope.data_nasteri = "";
    $scope.adresa = "";
    $scope.alte_informati = "";
    $scope.note = "";
    $scope.absente = "";

    $scope.idStud = "";
    $scope.studentId = {};
    $scope.studentId['Id'] = "";
    $scope.valid_add_student = "";
    $scope.valid_modif_student = "";

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


    function complete_type_text(){
      $scope.first_name_mod = $scope.studentId['first_name'];
      $scope.last_name_mod = $scope.studentId['last_name'];
      $scope.clasa_mod = $scope.studentId['clasa'];
      $scope.data_nasteri_mod = $scope.studentId['data_nasteri'];
      $scope.adresa_mod = $scope.studentId['adresa'];
      $scope.alte_informati_mod = $scope.studentId['alte_informati'];
      $scope.note_mod = $scope.studentId['note']
      $scope.absente_mod = $scope.studentId['absente']
    }


    function remove_type_text(){
      $scope.first_name_mod = "";
      $scope.last_name_mod = "";
      $scope.clasa_mod = "";
      $scope.data_nasteri_mod = ""; 
      $scope.adresa_mod = "";
      $scope.alte_informati_mod = "";
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

    $scope.afisare_absente = function(){
      if ($scope.first_name_mod == ""){
        $scope.array_absente_msg = "Prima data alege un student!!";
        $scope.array_absente = [];
      }
      else{
        $scope.array_absente = [];
        $scope.array_absente_msg = "Absentele sunt:";
        for (i=0;i<$scope.absente_mod.length; i++){
          $scope.array_absente.push($scope.absente_mod[i]);
        } 
      }
    }

    $scope.afisare_note_by_id = function(id_student){
      for (i=0; i<$scope.students.length; i++){
        if ($scope.students[i]['_id']['$oid'] == id_student){
          $scope.array_note = [];
          $scope.array_note_msg = "Notele sunt:";
          for (j=0; j<$scope.students[i]['note'].length; j++){
            $scope.array_note.push($scope.students[i]['note'][j]);
          }
          if ($scope.array_note.length == 0){
            $scope.array_note_msg = "Acest elev nu are note!"
          }
        }
      }
    }

    $scope.afisare_absente_by_id = function(id_student){
      for (i=0; i<$scope.students.length; i++){
        if ($scope.students[i]['_id']['$oid'] == id_student){
          $scope.array_absente = [];
          $scope.array_absente_msg = "Absentele sunt:";
          for (j=0; j<$scope.students[i]['absente'].length; j++){
            $scope.array_absente.push($scope.students[i]['absente'][j]);
          }
          if ($scope.array_absente.length == 0){
            $scope.array_absente_msg = "Acest elev nu are absente!";
          }
        }
      }
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


    $scope.give_stud = function(id_student){
      var url = "/students/"+id_student+".json";
      $http.get(url).then(function (result) {
        $scope.idStud = id_student;
        console.log(result);
        $scope.studentId = result.data;
        complete_type_text()
      });
    }


    $scope.add_nota = function(){
      if ($scope.first_name_mod == ""){
        $scope.validate_nota = "Selectati un elev"
        $scope.validate_absenta = ""
      }
      else if (validate_nota($scope.nota) == true){
        student = create_student_modif_nota($scope.nota);
        var url = "/students/"+$scope.idStud+".json";
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


  //   $scope.add_absenta = function(){
  //     if ($scope.first_name_mod == ""){
  //       $scope.validate_absenta = "Selectati un elev"
  //       $scope.validate_nota = "";
  //     }
  //     else if ($scope.absenta != ""){
  //       student = create_student_modif_abs($scope.absenta);
  //       var url = "/students/"+$scope.idStud+".json";
  //       $http.patch(url, student).then(function (result){
  //         console.log(result);
  //         $scope.students = result.data;
  //       });
  //       $scope.validate_absenta = "Absenta a fost adaugata";
  //       $scope.absenta = "";
  //     }
  //     else{
  //       $scope.validate_absenta = "Absenta invalida"
  //       $scope.validate_nota = "";
  //     }
  //   }

  //   var url = "/students.json";
  //   student = create_student();

  //   $http.post("/students.json", student).then(function (result){
  //     console.log(result);
  //     $scope.students.push(result.data);
  //   });
  //   remove_all();
  // }
// }


$scope.modif_stud = function(){
  complete_type_text()
}

$scope.delete_student_id = function(id_student){
  var url = "/students/"+id_student+".json";
  $http.delete(url).then(function (result){
    console.log(result);
    $scope.students = result.data;
  });
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
  var student = create_student_to_modif();
  if (!validate_modif_student(student)){
   $scope.valid_modif_student = "Invalid";
 }
 else{
  var url = "/students/"+$scope.idStud+".json";
  $http.patch(url, student).then(function (result){
    console.log(result);
    $scope.students = result.data;
    $scope.valid_modif_student = "Studentul a fost modificat!"
  });
}
}
});
