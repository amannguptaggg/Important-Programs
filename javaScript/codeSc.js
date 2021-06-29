
// "use strict";

// (function(){
//     allPara = document.querySelectorAll('p');
    
//     for (const i in allPara) {
//         allPara[i].style.color='red';
//     }
// }());

// (function(){
//     const val = 5;
//     val = 6;
// }());


// var pageTop;

// window.addEventListener('scroll',function(){
//     pageTop = window.pageYOffset;
//     if(pageTop > 500){
//         document.body.style.backgroundColor='pink';
//         alert('500px');    }
// })


// window.addEventListener('resize',function(e){
//     console.log(`the page width is ${window.innerWidth}`);
//     console.log(`the page height is ${window.innerHeight}`);
// });


// window.addEventListener('keydown',function(event){
//     console.log(`a key was pressed ${event.key} ${event.code}`);
// });



// var aVariable = 'this is outer scope';
// function testScope(){
//     aVariable = "this is local Scope can't be acced outside";
//     myLocalVariable = 'this is gloabal variable can be acced outside scope'
//     console.log(aVariable);
// }

// console.log(aVariable);
// testScope();

//this is outer scope
//this is local scope



// var btn = document.querySelector('button');
// var p0 = document.querySelector('#para0');

// var ouch = function(){
//     alert('Don\'t touch');
// }
// btn.addEventListener('click',function(event){
//    event.target.style.padding = '20px';
// });



// var myCheckBox = document.querySelector('input');

// myCheckBox.setAttribute('checked','checked');


// var myTag = document.createElement('p');
// var mytext = 'this is me here'

// myTag.innerHTML = mytext;

// var myDiv = document.querySelector('div p');
// myDiv.appendChild(myTag);

// myDiv.removeChild(myDiv.children[0]);



// var para = document.getElementsByClassName('myClass');

// for(let i =0;  i < para.length; i++){
//     para[i].style.color='blue';
//     alert(`showing para ${i}`);
// }

// for(i in para){
//     para[i].style.color='orange';
//     alert('showing para ${i}');
// }

// para[0].style.color = 'orange';


// let myHead = document.querySelectorAll('.myClass');
//  myHead[0].style.color='orange';





// var red = true;
// var blue = false;
// var green;
// var myNum = 5;
// var newNum = '5';

// var colors = ['red','green','yellow'];
// var selectedClr = 5;

// if(selectedClr == colors[1]){
//   console.log(colors)
// } else{
//   console.log('Flase value')
// }

// switch(selectedClr){
//   case '5': console.log('red');break;
//   case 'green': console.log('green');break;
//   case 'yellow': console.log('yellow');break;
//   default: console.log('no log');break
// }

// for (let index = 0; index < colors.length; index++) {
//   const element = colors[index];
//   console.log(element)
  
// }

//  colors.forEach(function(val,index,colors){
//    console.log(index)
//  })

// var mystr = "this is my string and the one of the best in internet";

// str = mystr.search('my')

// str = mystr.replace('my','Aman')
// console.log(str,"--->",mystr)

// for ( var i=0; i<10; i++ ) { console.log ( "the value of i is" +i ); }




