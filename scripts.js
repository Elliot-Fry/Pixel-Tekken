

let page = 'i'; 

// function switch_page() {
//     switch (page) {
//         case 'info':
//             break
//         case 'events':
//             break
//         case 'players':
//             break
//     }
// }

document.getElementById("info").onclick = () => {
    page = "i";
    // switch_page();
    // Code to display and hide elements
};

document.getElementById("events").onclick = () => {
    page = "e";
    // switch_page();
    // Code to display and hide elements
};

document.getElementById("players").onclick = () => {
    page = "p";
    // switch_page();
    // Code to display and hide elements
};

// TODO: page styling, button styling when pressed, 
//          page variable (may not be needed),
//          