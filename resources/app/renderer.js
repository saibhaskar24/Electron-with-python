// This file is required by the index.html file and will
// be executed in the renderer process for that window.
// No Node.js APIs are available in this process because
// `nodeIntegration` is turned off. Use `preload.js` to
// selectively enable features needed in the rendering
// process.
let {PythonShell} = require('python-shell')

function execute() {
  document.getElementById("res").innerHTML = "wait...";
  console.log(PythonShell)
  PythonShell.run('abc.py', null, function (err, results) {
    // script finished
    if (err) throw err;
    console.log( results);
    document.getElementById("res").innerHTML = "";
    for (var r in results) {
      document.getElementById('res').innerHTML += '<li>' + results[r] + '</li>';
    }
    // document.getElementById("res").innerHTML = results;
  });
}
