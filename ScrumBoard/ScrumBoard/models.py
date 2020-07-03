from django.db import models
from django.contrib.auth.models import User
from datetime import date

# :)))))))))))))
from django.urls import reverse


#class UserMethods(User):
#    def show_boards(self):
        #per ogni board presa dal db
        #board.__str__()
#        pass

#    class Meta:
#        proxy = True


class Board(models.Model):
    """La rappresentazione di una board"""
    nome = models.CharField(max_length=50)
    #proprietario = models.ForeignKey(User, on_delete=models.CASCADE)
    #partecipanti = models.ManyToManyField(User, related_name='contributors')

    def get_absolute_url(self):
        return reverse('show-board', args=[str(self.id)])

    #def aggiungi_utente(self, utente):
    #    pass

    #def elimina_utente(self, utente):
    #    pass

    #def cambia_nome(self, nome):
    #    pass

    def num_colonne(self):
        """Restituisce il numero di colonne di questa board"""
        return Colonna.objects.filter(board=self).count()

    #def aggiungi_colonna(self, colonna):
    #    pass

    #def elimina_colonna(self, colonna):
    #    pass

    def conta_storypoints_usati(self):
        """Conta il totale dei punti storia utilizzati"""
        colonne = list(Colonna.objects.filter(board=self).order_by('pk'))
        return colonne[-1].conta_storypoints()

    def num_carte(self):
        """Conta il numero totatle di cards nella board"""
        totale = 0
        for colonna in Colonna.objects.filter(board=self):
            totale += colonna.num_carte()
        return totale

    def conta_scadute(self):
        """Conta le cards scaduta nella board"""
        count = 0
        colonne = list(Colonna.objects.filter(board=self).order_by('pk'))
        for colonna in colonne[:-1]:
            count += colonna.conta_scadute()
        return count



    #def aggiungi_card(self):
        #chiama colonna.crea_card()
    #    pass

    def Board(request, board_id):
        def get_absolute_url(self):
            return reverse('show-board', args=[str(self.id)])

    def __str__(self):
        return self.nome


class Colonna(models.Model):
    """La rappresentazione di una colonna"""
    nome = models.CharField(max_length=50)
    board = models.ForeignKey(Board, on_delete=models.CASCADE)
    is_last = models.BooleanField(default=True)

    def cambia_nome(self, nome):
        """Modifica il nome della colonna"""
        self.nome = nome

    #def crea_card(self, card):
    #    pass

    #def rimuovi_card(self, card):
    #    pass

    """ da implementare forse
    def print_lista_card(self): 
        pass
    """
    def aggiorna_ultima_colonna(self):
        pass
        #cerca la colonna is_last = true
        #cambia a false

    def num_carte(self):
        """Conta il numero totale di cards nella colonna"""
        return Card.objects.filter(colonna=self).count()

    def conta_storypoints(self):
        """Conta il numero di punti storia totali nella colonna"""
        totale = 0
        for card in Card.objects.filter(colonna=self):
            totale += Card.story_points
        return totale

    def conta_scadute(self):
        count = 0
        for card in Card.objects.filter(colonna=self):
            if (card.is_scaduta()):
                count += 1
        return count

    def __str__(self):
        return self.nome


class Card(models.Model):
    nome = models.CharField(max_length=50)
    descrizione = models.TextField()
    data_creazione = models.DateTimeField(auto_now_add=True)
    data_scadenza = models.DateField()
    story_points = models.IntegerField()
    colonna = models.ForeignKey(Colonna, on_delete="CASCADE")

    #def aggiungi_utente(self, utente): #utente tipo User
    #    pass

    #def rimuovi_utente(self, utente):
    #    pass

    def cambia_colonna(self, colonna):
        self.colonna = colonna

    def cambia_nome(self, nome):
        self.nome = nome

    def cambia_descrizione(self, descrizione):
        self.descrizione = descrizione

    def cambia_scadenza(self, scadenza):
        self.data_scadenza = scadenza

    def cambia_storypoints(self, sp):
        self.story_points = sp

    def is_scaduta(self):
        """Restituisce true se la card è scaduta"""
        colonne = list(Colonna.objects.filter(board=self.colonna.board).order_by('pk'))
        if self.colonna == colonne[-1]:
            return False

        return date.today() > self.data_scadenza

    def __str__(self):
        return self.nome
