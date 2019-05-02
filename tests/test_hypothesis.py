import numpy as np
import pytest

from hypothesis import given, strategies as st

from pycontest import simulation as sim2d
from pycontest import elastic_collisions as ec
from pycontest.utils import momentum, E_kin

#@pytest.mark.skip(reason="TODO")                                               
@given(mass1  = st.floats(min_value=.1, max_value=1e3),
       mass2  = st.floats(min_value=.1, max_value=1e3))
def test_energy_hypothesis(mass1, mass2):
    v1_i = .5
    v2_i = -2
    v1_f, v2_f = ec.collision_1d(v1_i, v2_i, mass1, mass2)
    E_i = E_kin([v1_i, v2_i], [mass1, mass2])
    E_f = E_kin([v1_f, v2_f], [mass1, mass2])
    np.testing.assert_allclose(E_i, E_f, atol=0, rtol=1e-9, err_msg="ENERGY")

