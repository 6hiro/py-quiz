const url = window.location.href
const quizBox = document.getElementById('quiz-box')
const scoreBox = document.getElementById('score-box')
const resultBox = document.getElementById('result-box')
const timerBox = document.getElementById('timer-box')

const activateTimer = (time) => {
    if (time.toString().length < 2) {
        timerBox.innerHTML = `<b>0${time}:00</b>`
    } else {
        timerBox.innerHTML = `<b>${time}:00</b>`
    }

    let minutes = time - 1
    let seconds = 60
    let displaySeconds
    let displayMinutes

    const timer = setInterval(()=>{
        seconds --
        if (seconds < 0) {
            seconds = 59
            minutes --
        }
        if (minutes.toString().length < 2) {
            displayMinutes = '0'+minutes
        } else {
            displayMinutes = minutes
        }
        if(seconds.toString().length < 2) {
            displaySeconds = '0' + seconds
        } else {
            displaySeconds = seconds
        }
        if (minutes === 0 && seconds === 0) {
            timerBox.innerHTML = "<b>00:00</b>"
            setTimeout(()=>{
                clearInterval(timer)
                alert('Time over')
                sendData()
            }, 500)
        }

        timerBox.innerHTML = `<b>${displayMinutes}:${displaySeconds}</b>`
    }, 1000)
}
const getQuestions = async() => {
    const res =  await fetch(`${url}data/`)
    const result = await res.json();
    const data = await result.data;

    data.forEach(el => {
        // console.log(el)
        for (const [question, answers] of Object.entries(el)){
            quizBox.innerHTML += `
                <hr>
                <div class="question">
                    <b>${question}</b>
                </div>
            `
            answers.forEach(answer=>{
                quizBox.innerHTML += `
                    <div>
                        <input 
                            type="radio" 
                            class="answer" 
                            id="${question}-${answer}" 
                            name="${question}" 
                            value="${answer}"
                        >
                        <label for="${question}">${answer}</label>
                    </div>
                `
            })
        }
    });
    activateTimer(result.time)
};
getQuestions();

const quizForm = document.getElementById('quiz-form')
const csrf = document.getElementsByName('csrfmiddlewaretoken')
const sendData = () => {
    const elements = [...document.getElementsByClassName('answer')];
    const data = {};
    // console.log(csrf[0].value)
    // data['csrfmiddlewaretoken'] = csrf[0].value
    elements.forEach(el=>{
        if (el.checked) {
            data[el.name] = el.value;
        } else {
            if (!data[el.name]) {
                data[el.name] = null;
            }
        }
    });
    // console.log(data)
   
    const res =  fetch(`${url}save/`, 
        {
            method: 'POST', 
            body: JSON.stringify(data),
            headers: { 
                "X-CSRFToken": csrf[0].value,
                "Content-Type": "application/json" 
            }
        })
        .then(res => {
            res.json();
        })
        .then(result => {
            // console.log(result)
            result.data.forEach(res=>{
                // console.log(res)
                resultBox.innerHTML += `
                    <hr/>
                    <div class="question">問題：${res.question}</div>
                    <div class="answer">解答：${res.answer} 正解：${res.correct_answer}</div>
                `
            });

        })

    // result.data.forEach(res=>{
    //     console.log(res)
    //     // if(res.correct==="correct"){
    //     //     const correct = "正解" 
    //     // }else if(res.correct==="incorrect"){
    //     //     const correct = "不正解"
    //     // }else if(res.correct==="none"){
    //     //     const　correct = "解答なし"
    //     // }
    //     resultBox.innerHTML += `
    //         <hr/>
    //         <div>問題：${res.question}</div>
    //         <div>解答：${res.answer} 正解：${res.correct_answer}</div>
    //     `
    // }); 

}

quizForm.addEventListener('submit', e=>{
    e.preventDefault();
    console.log("#############")
    sendData();
    // quizForm.style.visibility='hidden';
});
