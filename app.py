from modelos.restaurante import Restaurante
from modelos.cardapio.Bebida import Bebida
from modelos.cardapio.Prato import Prato

restaurante_praca = Restaurante('praça', 'Gourmet')
bebida_suco = Bebida('Suco de Melancia', 5.0, 'grande')
prato_paozinho = Prato('Paozinho',2.00,'O melhor pão da cidade')



def main():
    print(bebida_suco)
    print(prato_paozinho)
   pass


if __name__ == '__main__':
    main()