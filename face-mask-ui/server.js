const cors = require('cors');
const express = require('express');
const path = require('path');
const app = express();
app.use(cors());
app.use(express.static(__dirname + '/dist/face-mask-ui'));
app.get('/*', function(req,res) {
  res.sendFile(path.join(__dirname+
                         '/dist/face-mask-ui/index.html'));});
app.listen(process.env.PORT || 8080);
