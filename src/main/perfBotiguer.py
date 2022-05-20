import numpy as np
from producte import producte
class botiguer():
    cataleg = np.array(producte)
    def afegirProducte(self, nom, quantitatAfegida):
        if(np.where(self.cataleg.nom == nom) == []):
            nouProdicte=producte()
            nouProdicte.nom=nom
            nouProdicte.quantitat=quantitatAfegida
            np.append(nouProdicte)
        else:
            self.cataleg[np.where(self.cataleg.nom == nom)].quantitat += quantitatAfegida
    def treureProducte(self, nom, quantitatTreure):
        if (np.where(self.cataleg.nom == nom) != [] and ):
            self.cataleg[np.where(self.cataleg.nom == nom)].quantitat -= quantitatTreure
            if (self.cataleg[np.where(self.cataleg.nom == nom)].quantitat < 0):
                self.cataleg[np.where(self.cataleg.nom == nom)].quantitat = 0
        else:
            pass
    def disponibilitat(self, nom):
        if (np.where(self.cataleg.nom == nom) != []):
            return self.cataleg[np.where(self.cataleg.nom == nom)].quantitat
        else:
            pass

