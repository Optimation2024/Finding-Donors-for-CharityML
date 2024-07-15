# tests/test_model.py

import pytest
from src.model import  predict


def test_predict():
    x="Kat "
    assert predict(x)=="Hello"+x
