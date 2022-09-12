from pytests.pytest_fixture import *

class TestCarrinhoDeCompras:
    
    def test_deve_retornar_subtotal_dos_itens_no_carrinho(self):
        usuario = Usuario('Matheus')
        carrinho = CarrinhoDeCompras(usuario)
        celular = ItemDoCarrinho('Celular', 2100.0, 1)
        notebook = ItemDoCarrinho('Notebook', 4500.0, 1)
        caneta = ItemDoCarrinho('Caneta', 3.00, 5)

        carrinho.adiciona(celular)
        carrinho.adiciona(notebook)
        carrinho.adiciona(caneta)

        valor_esperado = 6615.0
        assert valor_esperado == carrinho.subtotal

    def test_deve_retornar_total_dos_itens_no_carrinho_quando_este_nao_tiver_desconto(self):
        usuario = Usuario('Matheus')
        carrinho = CarrinhoDeCompras(usuario)
        celular = ItemDoCarrinho('Celular', 2100.0, 1)
        notebook = ItemDoCarrinho('Notebook', 4500.0, 1)
        caneta = ItemDoCarrinho('Caneta', 3.00, 5)

        carrinho.adiciona(celular)
        carrinho.adiciona(notebook)
        carrinho.adiciona(caneta)

        valor_esperado = 6615.0
        assert valor_esperado == carrinho.total

    def test_deve_aplicar_desconto_ao_subtotal_dos_itens_no_carrinho_quando_este_nao_tiver_desconto(self):
        usuario = Usuario('Matheus')
        carrinho = CarrinhoDeCompras(usuario)
        celular = ItemDoCarrinho('Celular', 2100.0, 1)
        notebook = ItemDoCarrinho('Notebook', 4500.0, 1)
        caneta = ItemDoCarrinho('Caneta', 3.00, 5)

        carrinho.adiciona(celular)
        carrinho.adiciona(notebook)
        carrinho.adiciona(caneta)
        carrinho.aplica_desconto(500)

        valor_esperado = 6115.0
        assert valor_esperado == carrinho.total