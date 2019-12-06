from sblu.xyztraj import xyz_stream, XYZParticle
from . import DATA_DIR
import numpy as np
import pytest


def test_xyz_particle():
    p = XYZParticle('0 0.0 0.0 0.0 1.0 0.0 0.0 0.0\n')
    assert p.type_ == 0
    assert np.allclose(p.t, [0, 0, 0])
    assert np.allclose(p.q, [1, 0, 0, 0])
    assert np.allclose(p.r, np.eye(3))

    p = XYZParticle('1 36.6599 -47.6586 106.5231 0.1104 0.9863 0.1046 -0.0644\n')
    r_ref = np.array([[0.96982490237103437, 0.22053928388629625, -0.10393306982829515], [0.19210207438947156, -0.95374433747699660, -0.23123263555524932], [-0.15012145668183340, 0.20428940989068534, -0.96733106289948116]])
    assert p.type_ == 1
    assert np.allclose(p.t, [36.6599, -47.6586, 106.5231])
    assert np.allclose(p.q, [0.1104, 0.9863, 0.1046, -0.0644])
    assert np.allclose(p.r, r_ref, atol=1e-3)

    with pytest.raises(Exception):
        XYZParticle('1 1 2 3 1 2 3 4 0\n')

    with pytest.raises(Exception):
        XYZParticle('2\n')


def test_xyz_stream():
    xyz_file = DATA_DIR / "xyztraj.xyz"
    xyz_file_long = DATA_DIR / "xyztraj_long.xyz"

    frames = list(
        xyz_stream(open(xyz_file))
    )

    assert len(frames) == 3
    assert frames[0].comment == 'Comment line'
    assert frames[1].comment == 'Energy: 3.000000'
    assert frames[2].comment == 'Energy: 0.000000'

    particle_1_coms = [[36.6599, -47.6586, 106.5231], [34.5694, -45.3926, 105.3711], [90.0730, -9.9783, 122.9131]]
    particle_1_rots = [[0.1104, 0.9863, 0.1046, -0.0644], [0.0663, 0.9821, 0.1604, -0.0726], [0.1182, -0.1990, -0.8218, 0.5207]]

    for frame_id, frame in enumerate(frames):
        assert len(frame.particles) == 2
        assert frame.particles[0].type_ == 0
        assert frame.particles[1].type_ == 1
        assert np.allclose(frame.particles[0].t, [-5.2180, 20.8850, 43.3590])
        assert np.allclose(frame.particles[0].q, [1.0, 0.0, 0.0, 0.0])
        assert np.allclose(frame.particles[0].r, np.eye(3))
        assert np.allclose(frame.particles[1].t, particle_1_coms[frame_id])
        assert np.allclose(frame.particles[1].q, particle_1_rots[frame_id])

    # Test longer trajectory
    frames = list(
        xyz_stream(open(xyz_file_long))
    )
    assert len(frames) == 14
