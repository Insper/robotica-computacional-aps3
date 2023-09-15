import pytest
import cv2
from unittest.mock import patch
import numpy as np
import traceback

def run_blank_1(RodaAtividade):
    bgr = np.zeros((400,400,3), dtype=np.uint8)
    with patch('cv2.imshow'):
        try:
            bgr, D, angulo, h, f = RodaAtividade.calibration(bgr, D=80, H=12.5)
        except Exception as e:
            return {'error': e, 'traceback': traceback.format_exc().splitlines()[-2:-1]}
        
    return True
def run_ex1(RodaAtividade, fname):
    bgr = cv2.imread(fname)
    with patch('cv2.imshow'):
        bgr, D, angulo, h, f = RodaAtividade.calibration(bgr, D=80, H=12.5)
    return {'f':f,'angulo':angulo,'h':h}

def check_ex1(result):
        assert False
def test_ex1():
    from ex1 import Atividade1
    RodaAtividade = Atividade1()

    result = {
        'blank': run_blank_1(RodaAtividade),
    }
    print(result)
    check_ex1(result)