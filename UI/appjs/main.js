(function() {
//<!--declare modules which depends from ngROute from angular
//configuring navigation routes of page -->
    var app = angular.module('AppChat',['ngRoute']);

    app.config(['$routeProvider', '$locationProvider', function ($routeProvider, $locationProvider, $location) {
        $routeProvider.when('/login', { //first route
            templateUrl: 'pages/login.html',
            controller: 'LoginController',
            controllerAs : 'logingCtrl'
        }).when('/chat', { //detail from specific part, i can add /chat/gid or smthng
            templateUrl: 'pages/chat.html',
            controller: 'ChatController',
            controllerAs : 'chatCtrl' //controlers
        }).otherwise({ //default routes
            redirectTo: '/chat'
        });
    }]);

})();
