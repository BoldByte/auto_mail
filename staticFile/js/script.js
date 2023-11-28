// Get the current year
let currentYear = new Date().getFullYear();
// Insert the current year into the footer
// document.getElementById('year').textContent = currentYear;

// $(document).ready(function() {
//     // check if the user is new or old
//     let isnewuser = false; // change this to false if the user is an old user
  
//     if (isnewuser) {
//       // display "get started" message for new users
//       let content = '<p>welcome to the investor page! get started by adding your first investor.</p>';
//       $('#content').html(content);
//     } else {
//       // display list of investors for old users
//       let investors = ['investor 1', 'investor 2', 'investor 3']; // replace with actual data
  
//       let content = '<h3>your investors:</h3><ul class="investor-list">';
//       investors.forEach(function(investor) {
//         content += '<li>' + investor + '</li>';
//       });
//       content += '</ul>';
  
//       $('#content').html(content);
//     }
  
//     // add button click event
//     $('#addbutton').click(function() {
//       // implement your logic to add a new investor here
//       console.log('add button clicked');
//     });
// });
  