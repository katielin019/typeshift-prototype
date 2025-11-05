const columns = document.querySelectorAll('.column');
let letters = [[]]

columns.forEach((column, index) => {
    processInput(column, index)
});

function processInput(data, idx) {
    letters[idx] = Array.from(data.children).map((child) => child.value);
    console.log(letters[idx]);
}