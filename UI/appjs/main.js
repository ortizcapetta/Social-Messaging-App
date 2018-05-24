(function() {
//<!--declare modules which depends from ngROute from angular
//configuring navigation routes of page -->

    var app = angular.module('AppChat',['ngRoute']);
    

    app.config(['$routeProvider', '$locationProvider', function ($routeProvider, $locationProvider, $location) {
        $routeProvider.when('/login', { //first route
            templateUrl: 'pages/login.html',
            controller: 'LoginController',
            controllerAs : 'logingCtrl'

             }).when('/groups', { //detail from specific part, i can add /chat/gid or smthng
            templateUrl: 'pages/chatgroups.html',
            controller: 'GroupChatController',
            controllerAs : 'groupChatCtrl' //controlers
             }).when('/groups/:gid/messages', {
            templateUrl: 'pages/messages.html',
            controller: 'MessageController',
            controllerAs : 'msgCtrl' //controlers
            }).when('/messages/:mid', {
            templateUrl: 'pages/messagedetail.html',
            controller: 'MessageDetailsController',
            controllerAs : 'msgdtlCtrl' //controlers
             }).when('/login', {
            templateUrl: 'pages/login.html',
            controller: 'loginController',
            controllerAs : 'loginCtrl' //controlers


       /*
        }).when('/chat', { //detail from specific part, i can add /chat/gid or smthng
            templateUrl: 'pages/chat.html',
            controller: 'ChatController',
            controllerAs : 'chatCtrl' //controlers
            */



        }).otherwise({ //default routes
            redirectTo: '/groups'
        });
    }]);
})();
