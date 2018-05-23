/**angular.module('AppChat').controller('MessageController', ['$http', '$log', '$scope','$routeParams', //dependency injections
//something about name being the name of the main (?)
    function($http, $log, $scope,$routeParams) {
        var thisCtrl = this; //this = object that thhtp service implements
           //makes ref to controller (?)

        this.messageList = []; //array that has messages list
        this.likeList = [];
        this.likes=0,this.dislikes=0;
        this.counter  = 2;
        this.newText = "";

        this.loadMessages = function(){

            var gID = $routeParams.gID;


            var url = "http://localhost:5000/users/groups/"+gID+"/messages";
            console.log("reqURL: " + url);

            $http.get(url).then(// success call back
                function (response){
                // The is the sucess function!
                    console.log("response: " + JSON.stringify(response));
                    thisCtrl.messageList = response.data.Messages;
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

            $log.error("Message Loaded: ", JSON.stringify(thisCtrl.messageList));
        };


        //check partsapp ui for more stuff
        //callback de exito y callback de error

        this.postMsg = function(){
            var msg = thisCtrl.newText;
            // Need to figure out who I am
            var author = "Me";
            var nextId = thisCtrl.counter++;
            var today = "5/1/2019 14:45:23"
            var likes = 0;
            var dislikes = 0;
            // Might have to rename the fields here to be inline with our schema
            thisCtrl.messageList.unshift({"mID": 533, "uID" : 423, "gID" : 2, "timestamp" :today , "content" : msg,
            "name": author, "likes": likes,"dislikes":dislikes});
            thisCtrl.newText = "";

        };




        this.loadMessages();
       // this.loadNumberOfLikes(mID);


}]);
**/
angular.module('AppChat').controller('MessageController', ['$http', '$log', '$scope', '$location', '$routeParams',
    function($http, $log, $scope, $location, $routeParams) {
        // This variable lets you access this controller
        // from within the callbacks of the $http object

        var thisCtrl = this;

        // This variable hold the information on the part
        // as read from the REST API
        var messageList = {};

        this.loadMessages = function(){
            // Get the target part id from the parameter in the url
            // using the $routerParams object
            var gid = $routeParams.gid;

            // Now create the url with the route to talk with the rest API
             var url = "http://localhost:5000/users/groups/"+gid+"/messages";
            console.log("reqURL: " + url);
            // Now issue the http request to the rest API
            $http.get(url).then(
                // Success function
                function (response) {
                    console.log("data: " + JSON.stringify(response.data));
                    // assing the part details to the variable in the controller
                    thisCtrl.partDetails = response.data.Part;
                }, //Error function
                function (response) {
                    // This is the error function
                    // If we get here, some error occurred.
                    // Verify which was the cause and show an alert.
                    var status = response.status;
                    //console.log("Error: " + reqURL);
                    //alert("Cristo");
                    if (status == 0) {
                        alert("No hay conexion a Internet");
                    }
                    else if (status == 401) {
                        alert("Su sesion expiro. Conectese de nuevo.");
                    }
                    else if (status == 403) {
                        alert("No esta autorizado a usar el sistema.");
                    }
                    else if (status == 404) {
                        alert("No se encontro la informacion solicitada.");
                    }
                    else {
                        alert("Error interno del sistema.");
                    }
                }
            );
        };

        this.loadMessages();
}]);