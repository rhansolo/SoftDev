//Byteme -- Robin Han & Kenny Li
//Softdev pd8
//K28 -- Sequential Progression
//2018-12-18

var fibonacci = function(n){
    if (n < 2){
	return n;
    }
    else{
	return fibonacci(n-1) + fibonacci(n-2);
    };
};

document.getElementById('b').addEventListener("click",function(){
    console.log("added element");
    var node  = document.createElement("li");
    var text = document.createTextNode('WORD');
    node.appendChild(text);
    document.getElementById('thelist').appendChild(node);
});

document.getElementById('fb').addEventListener("click",function(e){
    console.log(f);
});

