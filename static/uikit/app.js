// Invoke Functions Call on Document Loaded
document.addEventListener('DOMContentLoaded', function() {
    hljs.highlightAll();
});


// // let alertWrapper = document.querySelector('.alert')
// // let alertClose = document.querySelector('.alert__close')

// // if (alertWrapper) {
// //   alertClose.addEventListener('click', () =>
// //     alertWrapper.style.display = 'none'
// //   )
// // }

let alertWrapper = document.querySelectorAll('.alert');
let alertClose = document.querySelectorAll('.alert__close');

if (alertWrapper) {
    for (let i = 0; i < alertClose.length; i++) {
        alertClose[i].addEventListener('click', () => {
            alertWrapper[i].style.display = 'none'
        });
    }
}

// // Invoke Functions Call on Document Loaded
// document.addEventListener('DOMContentLoaded', function () {
//   hljs.highlightAll();
// });


// let alertWrapper = document.querySelector('.alert')
// let alertClose = document.querySelector('.alert__close')

// if (alertWrapper) {
//   alertClose.addEventListener('click', () =>
//     alertWrapper.style.display = 'none'
//   )
// }