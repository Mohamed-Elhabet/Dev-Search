// console.log('HELLO')

let loginBtn = document.getElementById('login-btn')
let logoutBtn = document.getElementById('logout-btn')
console.log(loginBtn)
console.log(logoutBtn)

let token = localStorage.getItem('token')

if(token){
  loginBtn.remove()
}else{
  logoutBtn.remove()
}

logoutBtn.addEventListener('click', (e) => {
  e.preventDefault()
  localStorage.removeItem('token')
  window.location = 'http://127.0.0.1:5500/frontend/login.html'
})

let projectsUrl = 'http://localhost:8000/api/projects/'

let getProjects = () => {
  fetch(projectsUrl)
    .then(response => response.json())
    .then(data => {
      console.log(data)
      buildProjects(data)
  })
}


let buildProjects = (projects) => {
  let projectsWrapper = document.getElementById('projects--wrapper')

  projectsWrapper.innerHTML = ''
  // console.log('projectsWrapper', projectsWrapper)
  for (let i=0; projects.length > i; i++){
    let project = projects[i]
    // console.log(project)
    let projectCard = `
      <div class="project--card">
        <img src="http://127.0.0.1:8000${project.featured_image}" />
        
        <div>
          <div class="card--header">
            <h3>${project.title}</h3>
            <strong class="vote--option" data-vote="up" data-project="${project.id}">&#43;</strong>
            <strong class="vote--option" data-vote="down" data-project="${project.id}">&#8722;</strong>
          </div>
          <i>${project.vote_ratio}% Positive feedback</i>
          <p>${project.description.substring(0,150)}</p>
        </div>
      </div>
    `

    projectsWrapper.innerHTML += projectCard 
  }

  // Add an listener
  addVoteEvents()
}

let addVoteEvents = () => {
  let voteBtns = document.getElementsByClassName('vote--option')
  // console.log('VOTE BUTTONS : ', voteBtns)
  for(let i=0; voteBtns.length > i; i++){
    voteBtns[i].addEventListener('click', (e)=> {
      // console.log('Vote was clicked : ', i)
      e.preventDefault()
      
      // what's type on vote, and what's project we're voting on 
      let vote = e.target.dataset.vote
      // let vote2 = e.target.getAttribute('data-vote')
      let project = e.target.dataset.project 
      console.log('VOTE : ', vote)
      console.log('PROJECT : ', project)
      // console.log('VOTE_2 : ', vote2)

      // let token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjc3MDc4NzQzLCJpYXQiOjE2NzY5OTIzNDMsImp0aSI6IjBjNzM2ZmE4ODg1NjRjYzBhYzkxZGEzOGM2MDU5Mjc2IiwidXNlcl9pZCI6M30.0FXGqIeTeBdYs53UmtRHulFC9MNmITXbBz01NG5-cFg'
      let token = localStorage.getItem('token')
      console.log('TOkEN : ', token)

      fetch(`http://127.0.0.1:8000/api/projects/${project}/vote/`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          Authorization: `Bearer ${token}`
        },
        body: JSON.stringify({'value': vote})
      }) 
      .then(response => response.json())
      .then(data => {
        console.log('Success : ', data) 
        getProjects()
      })   
    })
  }
}

getProjects()



