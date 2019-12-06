from typing import Iterator, List
import numpy as np


def _rot_matrix_from_quaternion(q: np.ndarray) -> np.ndarray:
    """Create rotation matrix from quaternion"""
    assert q.shape == (4, )
    m = np.zeros((3, 3), dtype=np.float)
    r, i, j, k = q
    m[0, 0] = 1 - 2 * (j**2 + k**2)
    m[1, 1] = 1 - 2 * (i**2 + k**2)
    m[2, 2] = 1 - 2 * (i**2 + j**2)
    m[0, 1] = 2 * (i*j - k*r)
    m[0, 2] = 2 * (i*k + j*r)
    m[1, 0] = 2 * (i*j + k*r)
    m[1, 2] = 2 * (j*k - i*r)
    m[2, 0] = 2 * (i*k - j*r)
    m[2, 1] = 2 * (j*k + i*r)
    return m


class XYZParticle:
    """
    A class presenting single particle from rigid-body XYZ trajectory.

    Parameters
    ----------
    line : str
        The line from XYZ file to parse.

    Attributes
    ----------
    type_ : int
        Particle type.
    t : np.ndarray
        Translation vector, array of shape (3,).
    q : np.ndarray
        Rotation quaternion, in order (w, x, y, z), array of shape (4,).
    """

    def __init__(self, line: str):
        tokens = line.split()
        self.type_ = int(tokens[0])
        tokens_f = [float(i) for i in tokens[1:]]
        assert len(tokens_f) == 7
        self.t = np.array(tokens_f[:3])
        self.q = np.array(tokens_f[3:])

    @property
    def r(self) -> np.ndarray:
        """Rotation matrix (computed)"""
        return _rot_matrix_from_quaternion(self.q)


class XYZFrame:
    """
    A class presenting single frame from rigid-body XYZ trajectory.

    Parameters
    ----------
    comment : str
        The comment from XYZ file.
    particles : list of XYZParticle
        The list of particles in this frame.
    """
    def __init__(self, comment: str, particles: List[XYZParticle]):
        self.comment = comment
        self.particles = particles


def _non_empty(x: str) -> bool:
    """Return True iff `x` contains any printable characters."""
    return len(x.strip()) > 0


def xyz_stream(file_stream: Iterator[str]) -> Iterator[XYZFrame]:
    """Iterate over frames in XYZ rigid-body file.

    Parameters
    ----------
    file_stream : iterator yielding strings
        Any way to iterate over lines of XYZ rigid-body file.

    Yields
    ------
    XYZFrame
        Single XYZ trajectory frame.

    Examples
    --------
    >>> with open('trajectory.xyz') as f_traj:
    >>>    for frame_id, frame in enumerate(xyz_stream(f_traj)):
    >>>        print('Frame #{} has {} particles.'.format(frame_id, len(frame.particles)))
    """
    # lines_good iterates over non-empty lines of file_stream
    lines_good = filter(_non_empty, file_stream)
    for line in lines_good:
        num_particles = int(line)
        comment = next(lines_good).strip()
        particles = [XYZParticle(next(lines_good)) for _ in range(num_particles)]
        yield XYZFrame(comment=comment, particles=particles)
