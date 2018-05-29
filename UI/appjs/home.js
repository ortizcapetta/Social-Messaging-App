
angular.module('AppChat').controller('HomeController', ['$http', '$log', '$scope', '$location','$routeParams','loggedUser',
    function($http, $log, $scope, $location,$routeParams,loggedUser) {
        var thisCtrl = this;

        this.groupList = [];
        this.loggedUser = loggedUser.getUser();


        this.jumpToGroups = function () {
            $location.url('/groups');
        };

        this.jumpToContacts = function(){
            $location.url('/contacts');

        }

}]);
