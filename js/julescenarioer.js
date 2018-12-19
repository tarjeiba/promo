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
    
    let rudolfs = [];
    let importCode = "import turtle\n\nrudolf = turtle.Turtle()\n\n";
    let maler = {
	kvadrat: "def kvadrat(n):\n    for _ in range(4):\n        rudolf.forward(n)\n        rudolf.right(90)\n\n",
	stjerne: "def stjerne(n):\n    for _ in range(5):\n        rudolf.forward(n)\n        rudolf.right(144)\n\n",
    };

    rudolfs.push(
	{id: "#rudolf0",
	 tittel: "Møt Rudolf",
	 text: "Skilpadda Rudolf opprettes ved å skrive <code>rudolf = turtle.Turtle()</code>, etter først å ha gjort verden klar for skilpadder à la Rudolf ved å skrive <code>import turtle</code>. La oss prøve det, for deretter å fortelle Rudolf at han skal gå 50 framover, før han skal snu seg 30° mot høyre, atter gå 30 framover, snu seg 150° mot venstre og gå 20 framover.",
	 code: "for c in ['red', 'green', 'yellow', 'blue']:\n    rudolf.color(c)\n    rudolf.forward(75)\n    rudolf.left(90)\n",
	 prepends: importCode});

    rudolfs.push(
	{id: "#rudolf1",
	 tittel: "Rudolf tuller det til",
	 text: "Det hender Rudolf tuller ting til. At beina stokker seg. At han går på trynet. At ordene ikke vil ut.",
	 code: "rudolf.write(\"Naa naermer det seg jul.\"  # Her tuller det seg til for Rudolf",
	 prepends: importCode});

    rudolfs.push(
	{id: "#rudolf2",
	 tittel: "Rudolf går",
	 text: "Rudolf er flink til å gå <code>forward</code> og å svinge til <code>right</code> eller <code>venstre</code>.",
	 code: "rudolf.forward(30)\nrudolf.right(90)\nrudolf.forward(100)",
	 prepends: importCode});

    rudolfs.push(
	{id: "#rudolf3",
	 tittel: "Rudolf bytter blyant",
	 text: "Rudolf er glad i farger.",
	 code: "rudolf.color('red')\nrudolf.fd(100)",
	 prepends: importCode});

    rudolfs.push(
	{id: "#rudolf4",
	 tittel: "Rudolf fargelegger",
	 text: "Rudolf er glad i å bruke farger. Han fargelegger kun innenfor linjene. Du er en ryddig type, Rudolf.",
	 code: "rudolf.fillcolor('yellow')\nrudolf.begin_fill()\nkvadrat(100)\nrudolf.end_fill()",
	 prepends: importCode + maler.kvadrat});

    rudolfs.push(
	{id: "#rudolf5",
	 tittel: "Rudolf er utålmodig",
	 text: "Rudolf er ikke glad i å gjenta seg sjøl. Dersom Rudolf har lært seg å gå i en firkant, ønsker han å kunne si til seg sjøl \"gå en firkant, Rudolf\". Du er en effektiv fyr, Rudolf.",
	 code: "kvadrat(100)",
	 prepends: importCode + maler.kvadrat});

    rudolfs.push(
	{id: "#rudolf6",
	 tittel: "Rudolf ... stjerna vår",
	 text: "Rudolf er, som seg hør og bør, glad i jula. Rudolf er derfor også glad i stjerner. Logikk. Du er en logiker, Rudolf.",
	 code:"stjerne(100)",
	 prepends: importCode + maler.stjerne});
	 
    rudolfs.push(
	{id: "#rudolf7",
	 tittel: "Rudolf fargelegger fem stjerner",
	 text: "Rudolf innser at han nå har alle verktøyene som skal til for å begynne å fylle himmelen med stjerner. Han kan bruke <code>for</code>-løkker for å repetere, og å tegne stjerner som han nettopp gjorde. En himmel full av stjerner, Rudolf.",
	 code: "",
	 prepends: importCode});

    rudolfs.push(
	{id: "#rudolf8",
	 tittel: "Rudolf ser ikke skogen for bare trær",
	 text: "Nå har Rudolf gått i firkanter, i trekanter, i stjerner. Rudolf har fargelagt. Rudolf har sett på stjernene. Rudolf er sliten. Rudolf innser at han med litt kreativitet, et ord Rudolf er redd for, kan lage seg et grantre han kan sove under. Dette fortjener du, Rudolf.",
	 code: "def juletre(n):\n    \"\"\"Lager et n høyt juletre, bestående av tre grønne trekanter og en brun base.\"\"\"\n    # Koden din går her\n",
	 prepends: importCode});

    rudolfs.push(
	{id: "#rudolf9",
	 tittel: "Rudolf tar kontroll",
	 text: "Rudolf har følt seg overarbeidet i det siste. «Gjør dette først, så dette, så dette.» Aldri får Rudolf beskjed om «Ta deg en lur, Rudolf». Rudolf gidder ikke mer. Fra nå av gjør Rudolf som han sjøl vil. God jul, Rudolf!",
	 code: "wn = turtle.Screen()\n\nrudolf.fd(50)\n\nwn.onclick(rudolf.goto)\nwn.listen()",
	 prepends: importCode});

    for (let rudolf of rudolfs) {
	exampleCode(rudolf.id, rudolf.tittel, rudolf.text, rudolf.prepends + rudolf.code);
    }
});

