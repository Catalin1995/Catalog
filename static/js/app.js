var catalogApp = angular.module('catalogApp', ['ngRoute', 'ngResource']);

catalogApp.config(['$routeProvider',
  function($routeProvider) {
    $routeProvider
    .when('/students', {
      templateUrl: "partials/students/list.html",
      controller: "StudentListController"
    })

    .when('/students/:orderId',{
      templateUrl: 'partials/students/show.html',
      controller: "StudentDetailsController"
    })

    .when('/new', {
      templateUrl: "partials/students/new.html",
      controller: "StudentAddController" 
    });
  }]);
