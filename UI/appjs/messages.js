angular.module('AppChat').controller('MessageController', ['$http', '$log', '$scope','$routeParams', //dependency injections
//something about name being the name of the main (?)
    function($http, $log, $scope,$routeParams) {
        var thisCtrl = this; //this = object that thhtp service implements
           //makes ref to controller (?)

        this.messageList = []; //array that has messages list
        this.likeList = [];
        this.likes=0,this.dislikes=0;
        this.counter  = 2;
        this.newText = "";
        var gID = $routeParams.gID;
        this.loadMessages = function(){
            // Get the messages from the server through the rest api o_o
            //var url = "http://localhost:5000/blahblahblah/messages chatt app;
            //there's a way to do this as a singleton tho @_@

            //not completely sure how to handle url in case the route is hosted somewhere else
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




        this.loadMessages(gID);
       // this.loadNumberOfLikes(mID);


}]);
