angular.module('AppChat').controller('GroupChatController', ['$http', '$log', '$scope', '$routeParams', //dependency injections
//something about name being the name of the main (?)
    function($http, $log, $scope,$routeParams) {
        var thisCtrl = this; //this = object that thhtp service implements
           //makes ref to controller (?)

        this.groupList = []; //array that has messages list

        this.counter  = 2;
        this.newText = "";

        $scope.loadChatGroups = function(){

            //uID = $routeParams.uid
            uID = 4


            //not completely sure how to handle url in case the route is hosted somewhere else
            var url = "http://localhost:5000/users/" + uID + "/groups";
            console.log('Im inside loadChagroups');
            console.log("url: " + url);
            $http.get(url).then(// success call back
                function (response){
                // The is the sucess function!
                    console.log("response: " + JSON.stringify(response));
                    thisCtrl.groupList = response.data.Groups;
            }, // error callback
            function (response){
                // This is the error function
                var status = response.status;
                if (status == 0){
                    alert("No hay conexion a Internet");
                }
                else if (status == 401){
                    alert("Su sesion expiro. Conectese de nuevo.");
                }
                else if (status == 403){
                    alert("No esta autorizado a usar el sistema.");
                }
                else if (status == 404){
                    alert("No se encontro la informacion solicitada.");
                }
                else {
                    alert("Error interno del sistema.");
                }
            });

            $log.error("Groups Loaded: ", JSON.stringify(thisCtrl.groupList));
        };



        $scope.viewGroup = function(gID){
          console.log('Gonna view group now')

          $location.url('/users/groups/'+gID+'/messages');

        }

        this.createGrp = function(){
            //create group function

        };






        this.loadChatGroups();




}]);
