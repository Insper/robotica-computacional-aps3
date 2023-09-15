import pytest
import cv2
from unittest.mock import patch
import numpy as np
import traceback

def run_blank_1(RodaAtividade):
    bgr = np.zeros((400,400,3), dtype=np.uint8)
    with patch('cv2.imshow'):
        try:
            bgr, point = RodaAtividade.run(bgr)
        except Exception as e:
            return {'error': e, 'traceback': traceback.format_exc().splitlines()[-2:-1]}
        
    return True
def run_ex1(RodaAtividade, fname):
    bgr = cv2.imread(fname)
    with patch('cv2.imshow'):
        bgr, point = RodaAtividade.run(bgr)
    return {'point':point}

def check_ex1(result):
        assert result['frame01']['point'][0] == pytest.approx(515., abs=20.), "Ponto de fuga em x esta fora do esperado para a imagem frame01.jpg"
        assert result['frame01']['point'][1] == pytest.approx(326., abs=20.), "Ponto de fuga em y esta fora do esperado para a imagem frame01.jpg"
        if result['blank'] is True:
            pass
        elif str(result['blank']['error']) == "list index out of range":
            assert False, "Seu codigo deve retornar -1 para D, angulo e h quando nao encontrar os circulos"
        else:
            assert False, "Ocorreu um erro inesperado ao rodar seu codigo com uma imagem em branco - {0} - {1}".format(result['blank']['traceback'], result['blank']['error'])
def test_ex1():
    from ex1 import LinhaBranca
    RodaAtividade = LinhaBranca()

    result = {
        'blank': run_blank_1(RodaAtividade),
        'frame01': run_ex1(RodaAtividade, 'img/frame01.jpg'),
    }
    print(result)
    check_ex1(result)

##############################################################################################################

def run_blank_2(RodaAtividade):
    bgr = np.zeros((400,400,3), dtype=np.uint8)
    with patch('cv2.imshow'):
        try:
            bgr, texto = RodaAtividade.run(bgr)
        except Exception as e:
            return {'error': e, 'traceback': traceback.format_exc().splitlines()[-2:-1]}
        
    return True
def run_ex2(RodaAtividade, fname):
    bgr = cv2.imread(fname)
    with patch('cv2.imshow'):
        bgr, texto = RodaAtividade.run(bgr)
    return {'texto':texto}

def check_ex2(result):
        assert result['frame01'][0] == pytest.approx(515., abs=20.), "Ponto de fuga em x esta fora do esperado para a imagem frame01.jpg"
        assert result['frame01'][1] == pytest.approx(326., abs=20.), "Ponto de fuga em y esta fora do esperado para a imagem frame01.jpg"
        if result['blank'] is True:
            pass
        elif str(result['blank']['error']) == "list index out of range":
            assert False, "Seu codigo deve retornar -1 para D, angulo e h quando nao encontrar os circulos"
        else:
            assert False, "Ocorreu um erro inesperado ao rodar seu codigo com uma imagem em branco - {0} - {1}".format(result['blank']['traceback'], result['blank']['error'])
def test_ex2():
    from ex2_ import ClassificaDominoes
    RodaAtividade = ClassificaDominoes()

    result = {
        'blank': run_blank_2(RodaAtividade),
        'domino1': run_ex2(RodaAtividade, 'img/domino.jpg'),
    }
    print(result)
    check_ex2(result)