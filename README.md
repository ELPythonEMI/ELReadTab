ELReadTab
ELReadTab è un'applicazione desktop Python per la lettura e visualizzazione di file di testo strutturati, come spartiti musicali o testi di canzoni. Utilizza l'interfaccia grafica Tkinter per offrire una visualizzazione user-friendly del contenuto dei file.
Caratteristiche

Lettura di file di testo in diversi encoding (UTF-8, Latin-1, CP1252)
Visualizzazione del testo in tre pannelli separati per una facile lettura
Navigazione tra le pagine del testo con i pulsanti "Next" e "Previous"
Interfaccia grafica intuitiva con icona personalizzata

Requisiti

Python 3.x
Tkinter (solitamente incluso nelle installazioni standard di Python)

Installazione

Clona questo repository:
Copygit clone https://github.com/ELPythonEMI/ELReadTab.git

Naviga nella directory del progetto:
Copycd ELReadTab


Utilizzo

Esegui lo script Python:
Copypython elreadtab.py

L'applicazione si aprirà con una finestra grafica.
Usa i pulsanti "Load UTF-8 Text File", "Load Latin-1 Text File", o "Load CP1252 Text File" per caricare un file di testo nel formato di codifica appropriato.
Il testo verrà visualizzato in tre pannelli:

Il pannello di sinistra mostra le prime 35 righe
Il pannello inferiore mostra le successive 35 righe
Il pannello di destra mostra le ultime 33 righe


Usa i pulsanti "Next" e "Previous" per navigare attraverso il testo.

Struttura del Codice
La classe App gestisce l'interfaccia utente e la logica dell'applicazione:

__init__: Inizializza l'interfaccia utente, creando i widget e impostando il layout.
load_text_file: Gestisce il caricamento dei file di testo con l'encoding specificato.
next e prev: Gestiscono la navigazione tra le "pagine" del testo.
show_lines: Aggiorna il contenuto visualizzato nei tre pannelli di testo.

Contribuire
Sentiti libero di fork questo repository e di proporre miglioramenti attraverso pull request.
Licenza
MIT License
Autore
ELPythonEMI
