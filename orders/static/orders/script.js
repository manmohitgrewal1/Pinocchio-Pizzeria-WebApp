function clickfun(value){
  console.log("onclick working");
  var stri= ""
  for (i=0 ;i<=value.length;i++){
    if (value[i]==' '){
      break;
    }
    else{
      stri+=value[i]
    }
  }
  console.log(stri);
  try{
  var element= document.querySelector('.topping_addon')
  if (element.classList.contains('active')){
    element.classList.remove('active')
    element.classList.add('inactive')
  }
 else if (stri != 'Cheese' || stri != 'Special' ){
    
    element.classList.remove('inactive')
    element.classList.add('active') 
    
  }}
  catch{
    return
  }
}

function validation(){
  var input_btn= document.getElementById("form").elements;
  var selected_item= document.querySelector("#clicked_item_name").innerText
  if (selected_item == "Salad" || selected_item == "Pasta" || selected_item == "Subs" || selected_item == "DinnerPlatter"){
    return true
  }
  var count=0;
  for (var i=0; i< input_btn.length; i++){
    if (input_btn[i].type== 'checkbox' && input_btn[i].checked){
      count++;
    }
  }
  var form_item= document.getElementById("form").elements;
  for (var i=0; i< 8; i++){    
    if ((form_item[i].value != "small" && form_item[i].value != "large") && form_item[i].type == "radio" && form_item[i].checked){
          
          if ((form_item[i].value == "1-item SicilianPizza" || form_item[i].value == "1-item RegularPizza") && count == 1 ){
             return true 
          }
          else if ((form_item[i].value == "2-items SicilianPizza" || form_item[i].value == "2-items RegularPizza") && count == 2){
             return true
          }
          else if ((form_item[i].value == "3-items SicilianPizza" || form_item[i].value == "3-items RegularPizza") && count ==3){
             return true 
          }
          else if (form_item[i].value == "Cheese SicilianPizza" || form_item[i].value == "Cheese RegularPizza" || form_item[i].value == "Special SicilianPizza" || form_item[i].value == "Special RegularPizza"){
            return true
          }
        else{
          alert("PLEASE SELECT TOPPINGS ACCORDING TO YOUR ORDER!");
          return false
        }
        }
      } 
}

function hide_me(value){
  var element= document.querySelector('.topping_addon')
  if (element.classList.contains('active')){
    element.classList.remove('active')
    element.classList.add('inactive')
}
}

function place(){
  var status_text= document.querySelector(".show_status span");
  var button=  document.querySelector(".btn-success");
  if(status_text.innerText == "Confirmed"){
    status_text.style.color= "green";
    alert("Your order has already  been placed!");
    return
  }
  else{
  alert("Your order has been placed!");
  var rm= document.querySelectorAll("#remove_btn")
  for (var i=0; i< rm.length; i++){
  rm[i].classList.add("inactive");
  button.value="View Status"
}
var status = document.querySelector(".show_status");
status.classList.remove("inactive");
status_text.style.color= "Red";
  }
}

