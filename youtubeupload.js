const { upload } = require('youtube-videos-uploader');
const credentials = { email: '', pass: '', recoveryemail: '' }

console.log(process.argv);
var myArgs = process.argv.slice(2);

const video1 = { path: myArgs[0], title: myArgs[1], description: myArgs[2] }
upload (credentials, [video1]).then(console.log)
