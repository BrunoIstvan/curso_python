from pytests.pytest_fixture import *
import pytest

class TestCarrinhoDeCompras:
    
    @pytest.fixture
    def usuario(self):
        return Usuario('Matheus')

    @pytest.fixture
    def carrinho(self, usuario):
        return CarrinhoDeCompras(usuario)

    @pytest.fixture
    def celular(self):
        return ItemDoCarrinho('Celular', 2100.0, 1)

    @pytest.fixture
    def notebook(self):
        return ItemDoCarrinho('Notebook', 4500.0, 1)

    @pytest.fixture
    def caneta_qtd5(self):
        return ItemDoCarrinho('Caneta', 3.00, 5)

    def test_deve_retornar_subtotal_dos_itens_no_carrinho(self, usuario, carrinho, celular, notebook, caneta_qtd5):
        
        carrinho.adiciona(celular)
        carrinho.adiciona(notebook)
        carrinho.adiciona(caneta_qtd5)

        valor_esperado = 6615.0
        assert valor_esperado == carrinho.subtotal

    def test_deve_retornar_total_dos_itens_no_carrinho_quando_este_nao_tiver_desconto(self, usuario, carrinho, celular, notebook, caneta_qtd5):
        
        carrinho.adiciona(celular)
        carrinho.adiciona(notebook)
        carrinho.adiciona(caneta_qtd5)

        valor_esperado = 6615.0
        assert valor_esperado == carrinho.total

    def test_deve_aplicar_desconto_ao_subtotal_dos_itens_no_carrinho_quando_este_nao_tiver_desconto(self, usuario, carrinho, celular, notebook, caneta_qtd5):
    
        carrinho.adiciona(celular)
        carrinho.adiciona(notebook)
        carrinho.adiciona(caneta_qtd5)
        carrinho.aplica_desconto(500)

        valor_esperado = 6115.0
        assert valor_esperado == carrinho.total
        