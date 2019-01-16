let predef = `
import turtle

kstep1 = True

def oppgave(tur, pos, n=1, r=10):
    orig = tur.position()
    tur.pu()
    tur.goto(pos[0], pos[1]-r)
    tur.pd()
    tur.circle(r)
    tur.pu()
    tur.goto(pos[0]-r/2, pos[1]-r/2)
    tur.pd()
    tur.write(n, font=("Ariel", 16))
    tur.pu()
    tur.goto(orig)

opp = turtle.Turtle()
opp.speed(0)
opp.hideturtle()

points = [(150, 0), (0, 260), (-150, 0)]

for i, point in enumerate(points):
    oppgave(opp, point, i+1)

del opp

ivar = turtle.Turtle()
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
