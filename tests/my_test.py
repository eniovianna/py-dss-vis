# -*- encoding: utf-8 -*-
"""
 Created by Ênio Viana at 15/10/2021 at 21:45:36
 Project: py-dss-vis [out, 2021]
"""
import pytest

from src.py_dss_vis.Line import Line


@pytest.fixture
def test_line_name():
    line = Line()
    assert line.name is "Line"
