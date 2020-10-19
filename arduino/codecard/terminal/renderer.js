// This file is required by the index.html file and will
// be executed in the renderer process for that window.
// All of the Node.js APIs are available in this process.

window.ELECTRON_DISABLE_SECURITY_WARNINGS = true;


const connectBtn = document.getElementById('connectBtn');
const status = document.getElementById('status');

const terminalContainer = document.getElementById('terminal-container')
const terminal = document.getElementById('term')


const SerialPort = require('serialport')
var dataBuffer = ''
var serialport = ''

var term = new Terminal({ 
  fontFamily: 'Fira Code, Iosevka, monospace',
  fontSize: 12,
  experimentalCharAtlas: 'dynamic',
  cursorBlink: true ,
  bellStyle: 'sound'
});

term.open(terminal);
Terminal.applyAddon(fit);
fit.fit(term);

var shellprompt = '\x1B[1;3;31mcodecard\x1B[0m$ ';
term.prompt = function () {
  // term.write('\r\n' + shellprompt);
  term.write(shellprompt);
};

var port;

detectBadge()

connectBtn.onclick = function () {
  if (connectBtn.innerHTML == 'Connect') {
    terminalContainer.style.display === 'block'
    port.open()
  } else if (connectBtn.innerHTML == 'Disconnect') {
    terminalContainer.style.display === 'none'
    port.close()
  } else if (connectBtn.innerHTML == 'Refresh') {
    detectBadge()
  }
}

function detectBadge(){
  disableTerminal()
  SerialPort.list((err, ports) => {
    if (err) {
      status.textContent = err.message
      return
    }
  
    for (var i = 0; i < ports.length; i++) {
      if (ports[i].comName.includes('COM') || ports[i].comName.includes('ttyUSB') || ports[i].comName.includes('wchusbserial')) {
        serialport = ports[i].comName;
        status.textContent = 'Card detected at: \'' + serialport + '\''
        connectBtn.innerHTML = 'Connect'
        connect();
        return;
      } else {
        status.textContent = 'No card detected'
        connectBtn.innerHTML = 'Refresh'
      }
    }
  })
}

function disableTerminal() {
  document.getElementsByClassName('terminal')[0].style.display = 'none'
}

function enableTerminal() {
  document.getElementsByClassName('terminal')[0].style.display = 'block'
}

function connect() {

  port = new SerialPort(serialport, {
    autoOpen: false,
    baudRate: 115200
  });

  const parsers = SerialPort.parsers;
  const parser = new parsers.Readline({
    delimiter: '\r\n'
  });

  port.pipe(parser);

  
  port.on('open', () => {
    console.log('Port open');
    term.prompt()
    term.focus()
    status.textContent = 'Connected to port ' + serialport
    connectBtn.innerHTML = 'Disconnect'
    enableTerminal()
    // port.write('help\r\n', (err) => {
    //   if (err) { return console.log('Error: ', err.message) }
    //   //console.log('message written');
    // });
  });

  port.on('close', () => {
    status.textContent = 'Disconnected from port \'' + serialport + '\''
    term.clear()
    term.write('\b \b\b \b\b \b\b \b\b \b\b \b\b \b\b \b\b \b\b \b');
    console.log('Port closed');
    connectBtn.innerHTML = 'Connect'
    disableTerminal()
  })
    
  parser.on('data', (data) => {
    if (data.includes('>>>')) {
      term.prompt()
      term.focus()
      return
    }
    term.writeln(data);
  });
    
  term.on('data', function(data) {
    if (data.indexOf('\r\n') == -1 && encodeURI(data) != '%7F'){
      dataBuffer+=data;
    }else if (encodeURI(data) === '%7F') {
      dataBuffer = dataBuffer.substring(0, dataBuffer.length - 1)
    }
  });

  term.on('paste', function (data, ev) {
    term.write(data)
  });
  
  term.on('key', function (key, ev) {
    var printable = (
      !ev.altKey && !ev.altGraphKey && !ev.ctrlKey && !ev.metaKey && !ev.spaceKey
    );
  
    if (dataBuffer.indexOf('clear') > -1 ) {
      term.clear()
      term.write('\b \b\b \b\b \b\b \b\b \b');
      dataBuffer=''
      return
    }

    if (ev.keyCode == 13 && dataBuffer.trim() != '') {
      port.write(dataBuffer)
      term.write('\r\n')
      dataBuffer = ''
    } else if (ev.keyCode == 8) {
      if (term._core.buffer.x >  10) {
        term.write('\b \b');
      }
    } else if (key == '[D') {
      if (term._core.buffer > 10) {
        term._core.buffer = term._core.buffer - 1
      }
    } else if (printable && key.trim() != '') {
      //console.log('key', key)
      term.write(key);
    } 
    // else if (key.trim() == '') {
    //   term.write('\r\n')
    //   term.prompt()
    // }

  });

}

