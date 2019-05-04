let predef = `
import turtle
from turtle import Turtle
        
class KikoraTurtle(Turtle):
    def __init__(self, history = []):
        Turtle.__init__(self)
        self.fd = self.forward
    
    def _check(self, kstepsobj, r = 10):
        if self.distancesquared(kstepsobj.posarray[kstepsobj.unvisited]) < r ** 2:
            kstepsobj.visitedarray[kstepsobj.unvisited] = True
            kstepsobj.unvisited += 1
            return True
        else:
            return False

    def distancesquared(self, point):
        pos = self.position()
        return (pos[0] - point[0]) ** 2 + (pos[1] - point[1]) ** 2

    def forward(self, distance):
        self._check(ksteps)
        Turtle.forward(self, distance)

    def backward(self, distance):
        Turtle.backward(self, distance)

class TaskTurtle(Turtle):
    def __init__(self, ksteps):
        Turtle.__init__(self)
        self.speed(0)
        self.hideturtle()
        self.fd = self.forward
        self._draw_tasks(ksteps.posarray)

    def _draw_tasks(self, posarray):
        orig = self.position()
        for n, pos in enumerate(posarray):
            self._draw_task(n, pos)
        self.goto(orig)

    def _draw_task(self, n, pos, r=10):
        self.pu()
        self.goto(pos[0], pos[1]-r)
        self.pd()
        self.circle(r)
        self.pu()
        self.goto(pos[0]-r/2, pos[1]-r/2)
        self.pd()
        self.write(n, font=("Ariel", 16))
        self.pu()

class Ksteps(object):
    def __init__(self, posarray):
        self.posarray = posarray
        self.visitedarray = [False for _ in posarray]
        self.unvisited = 0  # index of first unvisited point


    def check(self, tur, n, err=1):
        """Check whether turtle is inside nth kstep area."""
        pos = tur.position()

def unvisited(steps):
    for i, step in enumerate(steps):
        if step[0]:
            return i

ksteps = Ksteps([(150, 0), (0, 260), (-150, 0)])




tasks_turtle = TaskTurtle(ksteps)
del tasks_turtle

ivar = KikoraTurtle()
ivar.showturtle()
`

function kstepscolor(num) {
    let table = document.getElementById('ksteps');
    let rows = table.getElementsByTagName('tr');
    rows[0].cells[num].style.backgroundColor = 'green';
}	

function runit() {
    var prog = window.code_editor.getValue();
    var mypre = document.getElementById("edoutput"); 
    mypre.innerHTML = ''; 
    Sk.pre = "edoutput";
    Sk.configure({output:outf, read:builtinRead}); 
    (Sk.TurtleGraphics || (Sk.TurtleGraphics = {})).target = 'mycanvas';
    Sk.canvas = 'mycanvas';
    Sk.TurtleGraphics.height = 600; Sk.TurtleGraphics.width = 800;
    var myPromise = Sk.misceval.asyncToPromise(function() {
	return Sk.importMainWithBody("<stdin>", false, predef + prog, true);
    });
    myPromise.then(function(mod) {
	let kstep1 = Sk.globals.kstep1.v;
	if (kstep1) {
	    kstepscolor(0);
	};
	if (kstep2) {
	    kstepscolor(1);
	};
	if (kstep3) {
	    kstepscolor(2);
	}

	console.log('success');
    },
		   function(err) {
		       console.log(err.toString());
		       $('#edoutput').text(err.toString());
		   });
} 

$(document).ready(function () {
    var output = $('#edoutput');
    var outf = function (text) {
        output.text(output.text() + text);
    };

    Sk.configure({output:outf, read:builtinRead});
    (Sk.TurtleGraphics || (Sk.TurtleGraphics = {})).target = 'mycanvas';
    Sk.TurtleGraphics.height = 600; Sk.TurtleGraphics.width = 800;
    var initPromise = Sk.misceval.asyncToPromise(function() {
	return Sk.importMainWithBody("<stdin>", false, predef, true);
    });
    initPromise.then(function(mod) {
	console.log('initialisert');
    },
		     function(err) {
			 console.log(err.toString());
			 $('#edoutput').text(err.toString());
		     });

    var editor = CodeMirror.fromTextArea(document.getElementById('code'), {
	// pareserfile: ["parsepython.js"],
        mode: 'python',		// 
        matchBrackets: true,
        dragDrop: false,
        styleSelectedText: false,
        showCursorWhenSelecting: true,
        lineWrapping: true,
    });

    window.code_editor = editor;
    window.outf = outf;
    window.builtinRead = builtinRead;

    $("#skulpt_run").click(function (e) { keymap["Ctrl-Enter"](editor)} );

    $("#toggledocs").click(function (e) {
        $("#quickdocs").toggle();
    });

    $('#clearoutput').click(function (e) {
        $('#edoutput').text('');
        $('#mycanvas').hide();
    });


    function builtinRead(x) {
        if (Sk.builtinFiles === undefined || Sk.builtinFiles["files"][x] === undefined)
            throw "File not found: '" + x + "'";
        return Sk.builtinFiles["files"][x];
    }
    
    editor.focus();
});
