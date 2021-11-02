// const emailField = document.querySelector('#emailField');
// const passwordField = document.querySelector('#password');
// const repasswordField = document.querySelector('#repassword');

// emailField.addEventListener("keyup", (e) => {
//     const emailVal = e.target.value;
//     if (emailVal.length > 0) {
//         if(emailVal.includes('@') || emailVal.includes('.')){
//             // emailField.style.background='#05c46b'

//         }
//         else{
//             document.getElementById('message').style.color='#ff00ff';
//             document.getElementById('message').innerHTML='有効なメールアドレスを入力してください'
//         }
//     }
// })
// repasswordField.addEventListener("keyup", (e) => {
//     const repasswordlVal = e.target.value;
//     if (repasswordlVal==passwordField.value){
//         document.getElementById('message').style.background='#e8f0fe';
//         // document.getElementById('message').innerHTML=''
//     }else{
//         document.getElementById('message').style.color='#ff00ff';
//         document.getElementById('message').innerHTML='パスワードと同じ内容を入力してください'
//     }
// })


// const emailFeedBackArea = document.querySelector(".email_feedback_area");
// const submitBtn = document.querySelector(".btn");

// emailField.addEventListener("keyup", (e) => {
//     const emailVal = e.target.value;
  
//     // emailField.classList.remove("is_invalid");
//     // emailFeedBackArea.style.display = "none";
  
//     if (emailVal.length > 0) {
//         if(emailVal.includes('@') || emailVal.includes('.')){
//             fetch("/validate-email", {
//                 body: JSON.stringify({ email: emailVal }),
//                 method: "POST",
//             })
//                 .then((res) => res.json())
//                 .then((data) => {
//                 console.log("data", data);
//                 if (data.email_error) {
//                     submitBtn.disabled = true;
//                     // emailField.classList.add("is_invalid");
//                     emailFeedBackArea.style.display = "block";
//                     emailFeedBackArea.innerHTML = `<p>${data.email_error}</p>`;
//                 } else {
//                     submitBtn.removeAttribute("disabled");
//                 }
//             });            
//         }else{
//             emailFeedBackArea.innerHTML='有効なメールアドレスを入力してください。'

//         }
//     }
//   });