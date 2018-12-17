function runit() {
    var prog = window.code_editor.getValue(); 
    var mypre = document.getElementById("edoutput"); 
    mypre.innerHTML = ''; 
    Sk.pre = "edoutput";
    Sk.configure({output:outf, read:builtinRead}); 
    (Sk.TurtleGraphics || (Sk.TurtleGraphics = {})).target = 'mycanvas';
    Sk.TurtleGraphics.height = 600; Sk.TurtleGraphics.width = 800;
    var myPromise = Sk.misceval.asyncToPromise(function() {
	return Sk.importMainWithBody("<stdin>", false, prog, true);
    });
    myPromise.then(function(mod) {
	console.log('success');
    },
		   function(err) {
		       console.log(err.toString());
		       $('#edoutput').text(err.toString());
		   });
} 

$(document).ready(function () { // Dette er en jquery-funksjon -- sjekk den ut
    var output = $('#edoutput');
    var outf = function (text) {
        output.text(output.text() + text);
    };

    var keymap = {
        "Ctrl-Enter" : function (editor) {
            Sk.configure({output: outf, read: builtinRead});
            Sk.canvas = "mycanvas";
            if (editor.getValue().indexOf('turtle') > -1 ) {
                $('#mycanvas').show();
            }
            Sk.pre = "edoutput";
            (Sk.TurtleGraphics || (Sk.TurtleGraphics = {})).target = 'mycanvas';
            try {
                Sk.misceval.asyncToPromise(function() {
                    return Sk.importMainWithBody("<stdin>",false,editor.getValue(),true);
                });
            } catch(e) {
                outf(e.toString() + "\n")
            }
        },
        "Shift-Enter": function (editor) {
            Sk.configure({output: outf, read: builtinRead});
            Sk.canvas = "mycanvas";
            Sk.pre = "edoutput";
            if (editor.getValue().indexOf('turtle') > -1 ) {
                $('#mycanvas').show()
            }
            try {
                Sk.misceval.asyncToPromise(function() {
                    return Sk.importMainWithBody("<stdin>",false,editor.getValue(),true);
                });
            } catch(e) {
                outf(e.toString() + "\n")
            }
        }
    }

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
