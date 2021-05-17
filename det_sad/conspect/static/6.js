// добавление в конспект
let title_topic = Array.from(document.querySelectorAll('.title_topic'))
let total_list = document.querySelector('#total_list')
title_topic.forEach((item, i) => {
    let div = document.createElement('div')
    div.id = item.innerHTML
    div.key = i
    div.innerHTML = `<h3 style="display: none" id='question_${i}'>${item.innerHTML}</h3>`
    div.className = 'insert'
    total_list.append(div)
})


let question = document.querySelector('#question')
question.addEventListener('focusin', fn)

function fn(e) {
    let all_insert = Array.from(document.querySelectorAll('.insert'))
    for (let i of all_insert) {
        if (i.id == e.target.name) {
            let q = document.querySelector(`#question_${i.key}`)
            q.style = 'display:block;'
            // console.log(q)
            i.append(e.target.parentNode)
        }
    }
}

//=================================================
// Удаление и возврат в контекст

let title_topic_first = Array.from(document.querySelectorAll('.questions_block'))
let section = document.querySelector('#total')
section.addEventListener('focusin', fn1)

function fn1(e) {
    let p_insert = e.target.parentNode.parentNode
    let c = p_insert.querySelectorAll('label')
    for (let i of title_topic_first) {
        if (e.target.name == i.firstChild.innerHTML) {
            if (c.length == 1) {
                e.target.parentNode.parentNode.firstChild.style = 'display:none;'
            }
            i.append(e.target.parentNode)
        }
    }
}

//=================================================

// сохранить конспект
let save_cons = document.querySelector('#save_cons')
save_cons.addEventListener('click', fn2)
let obj = {
    subjects: []
}

function fn2(e) {

    let all_themes_cons = Array.from(document.querySelectorAll('.insert'))
    for (let i of all_themes_cons) {
        let name = {name: i.firstChild.innerHTML, answers: []}
        let c = i.querySelectorAll('p')
        for (let j of c) {
            name.answers.push(j.firstChild.value)
        }
        console.log(i.querySelectorAll('p'))
        obj.subjects.push(name)
    }
    console.log(obj)
async function postData(url = '', data = {}) {
  // Default options are marked with *
    const response = await fetch(url, {
    method: 'POST', // *GET, POST, PUT, DELETE, etc.
    mode: 'cors', // no-cors, *cors, same-origin
    cache: 'no-cache', // *default, no-cache, reload, force-cache, only-if-cached
    credentials: 'same-origin', // include, *same-origin, omit
    headers: {
    'Content-Type': 'application/json'
      // 'Content-Type': 'application/x-www-form-urlencoded',
    },
    redirect: 'follow', // manual, *follow, error
    referrerPolicy: 'no-referrer', // no-referrer, *client
    body: JSON.stringify(data) // body data type must match "Content-Type" header
    });
  return await response.json(); // parses JSON response into native JavaScript objects
}

postData('http://127.0.0.1:8000/', obj)
    .then((data) => {
    console.log(data); // JSON data parsed by `response.json()` call
    });
}


//=============================================