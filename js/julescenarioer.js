$(document).ready(function(){
    let exampleCode = function (id, tittel, text, code) {
        $(id).click(function (e) {
            window.code_editor.setValue(code);
            window.code_editor.focus(); // so that F5 works
	    $('#scenariotekst').html(tittel);
	    $('#text-scenariotekst').html(text);
	    MathJax.Hub.Typeset();
        });
    };
    
    let oppgaver = [];
    let importCode = "import turtle\n\nsp = turtle.Turtle()\n\n";
    let maler = {
    };

    oppgaver.push(
	{id: "#oppgave0",
	 tittel: "Oppgave-forslag",
	 text: "Flytt skilpadda via feltene 1 og 2. Avstanden fra utgangspunktet til 1 er 100, og fra 1 til 2 er den 200.",
	 code: "import turtle\n\nsp = turtle.Turtle()   # sp er her en forkortelse for \"skilpadde\".",
	 prepends : ""});

    for (let oppgave of oppgaver) {
	exampleCode(oppgave.id, oppgave.tittel, oppgave.text, oppgave.prepends + oppgave.code);
    }

    let workspace = Blockly.inject('blocklyDiv',
				   {toolbox: document.getElementById('toolbox')});



});

