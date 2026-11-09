import flet as ft
from UI.view import View
from model.model import Model

'''
    CONTROLLER:
    - Funziona da intermediario tra MODELLO e VIEW
    - Gestisce la logica del flusso dell'applicazione
'''

class Controller:
    def __init__(self, view: View, model: Model):
        self._model = model
        self._view = view

        # Variabili per memorizzare le selezioni correnti
        self.biblioteca_selezionata = None
        self.genere_selezionato = None

    # POPOLA DROPDOWN
    def popola_dropdown(self):
        self._view.drop_biblioteche.options.append(ft.dropdown.Option("Nessun filtro"))
        for b in self._model.get_biblioteche():
            self._view.drop_biblioteche.options.append(ft.dropdown.Option(b.nome))

        self._view.drop_generi.options.append(ft.dropdown.Option("Nessun filtro"))
        for g in self._model.get_generi():
            self._view.drop_generi.options.append(ft.dropdown.Option(g))

        self._view.update()

    # CALLBACKS DROPDOWN
    def on_biblioteca_selezionata(self, e):
        valore = self._view.drop_biblioteche.value
        if valore == "Nessun filtro":
            self.biblioteca_selezionata = None
        else:
            self.biblioteca_selezionata = valore

    def on_genere_selezionato(self, e):
        valore = self._view.drop_generi.value
        if valore == "Nessun filtro":
            self.genere_selezionato = None
        else:
            self.genere_selezionato = valore

    # AZIONE: MOSTRA LIBRI
    def mostra_libri(self, e):
        biblioteca = self.biblioteca_selezionata
        genere = self.genere_selezionato

        libri_filtrati = self._model.get_libri_filtrati(biblioteca, genere)

        self._view.mostra_libri_in_view(libri_filtrati)

