const closeModal = document.querySelector('.close-modal');
const modal = document.querySelector('.modal');

const modalBtns = [...document.getElementsByClassName('open-modal')]
const modalBody = document.getElementById('modal-body')
const startQuizBtn = document.getElementById('start-quiz-button')

const url = window.location.href

modalBtns.forEach(modalBtn=> modalBtn.addEventListener('click', ()=>{
    modal.classList.add('visible');
    // console.log( modalBtn)

    const pk = modalBtn.getAttribute('data-pk');
    const name = modalBtn.getAttribute('data-quiz');
    const numQuestions = modalBtn.getAttribute('data-questions');
    const difficulty = () => {
        const diffNum = modalBtn.getAttribute('data-difficulty');
        if(diffNum==="easy"){
            return "簡単"
        }else if(diffNum==="medium"){
            return "普通"
        }else if(diffNum==="hard"){
            return "難しい"
        }
    }
    const time = modalBtn.getAttribute('data-time');

    modalBody.innerHTML = `
        <div class="quiz-name"><b>${name}</b></div>
        <div class="text-muted">
            <ul>
                <li>難易度: <b>${difficulty()}</b></li>
                <li>問題数: <b>${numQuestions}問</b></li>
                <li>制限時間: <b>${time}分</b></li>
            </ul>
        </div>
    `

    startQuizBtn.addEventListener('click', ()=>{
        window.location.href = url + pk
    });

}))


closeModal.addEventListener('click', () => {
    modal.classList.remove('visible');
})