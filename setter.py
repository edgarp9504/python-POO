class CasillaDeVotacion:
    def __init__(self, identificador, pais):
        self._identificado = identificador
        self._pais = pais
        self._region = None

    @property
    def region(self):
        return self._region

    @region.setter
    def region(self, region):
        if region in self._pais:
          self._region = region
        else:
          raise ValueError(f'La region {region} no est valida en {self._pais}')

if __name__ == '__main__':
    casilla = CasillaDeVotacion(123, ['Ciudad de Mexico', 'Morelos'])
    print(f'casilla.region={casilla.region}')
    casilla.region = 'Morelos'
    print(f'casilla.region={casilla.region}')