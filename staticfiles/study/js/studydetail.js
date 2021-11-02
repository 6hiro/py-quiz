const like = document.getElementById('like')

const postId = like.getAttribute('data-postid');
console.log(postId)

const csrf = document.getElementsByName('csrfmiddlewaretoken')

const likePost = () => {
    const res = fetch(`like/${postId}`,
        {
            method: 'POST', 
            body: JSON.stringify({}),
            headers: { 
                "X-CSRFToken": csrf[0].value,
                "Content-Type": "application/json; charset=utf-8" 
            }
        }
    )
    .then(res => {
        res.json();
    })
    .then(result => {
        console.log(result)
        if(result.result==='like'){

        }else if(result.result==='unlike'){

        }
    })
    .catch((e) =>{
        console.log(e)
    });

}
// like.onClick =  ()=>{
//     console.log("################")
//     // likepost();
// };
like.addEventListener('click', e=>{
    console.log("################");
    likePost();
})