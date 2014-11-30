from __future__ import print_function
from __future__ import division
from __future__ import absolute_import
from pyamg.testing import *

from scipy import matrix, array
from scipy.sparse import coo_matrix

from pyamg.gallery.elasticity import linear_elasticity, \
        linear_elasticity_p1, \
        q12d_local, p12d_local, p13d_local

class TestLinearElasticityP1(TestCase):
    def setUp(self):
        cases = []

        # one triangle
        V = array([[0,0],[1,0],[0,1]])
        E = array([[0,1,2]])
        cases.append( (V,E) )
        
        # two triangles
        V = array([[0,0],[1,0],[0,1],[1,1]])
        E = array([[0,1,2],[1,3,2]])
        cases.append( (V,E) )

        # one tetrahedron
        V = array([[0,0,0],[1,0,0],[0,1,0],[0,0,1]])
        E = array([[0,1,2,3]])
        cases.append( (V,E) )

        self.cases = cases


    def test_rigid_body_modes(self):
        """check that rigid body modes lie in nullspace"""

        for V,E in self.cases:
            A,B = linear_elasticity_p1(V,E)
            assert_almost_equal(A*B, 0*B)

class TestLinearElasticityGrid(TestCase):
    def test_1x1(self):
        A_expected = matrix ([[ 230769.23076923,       0.        ],
                              [      0.        ,  230769.23076923]])
        B_expected = array([[1, 0, 0],
                            [0, 1, 0]])

        A,B = linear_elasticity( (1,1), E=1e5, nu=0.3 )
        
        assert_almost_equal(A.todense(),A_expected)
        assert_almost_equal(B,B_expected)
    
    def test_1x1(self):

        data = array([ 230769.23076923,  -76923.07692308,   19230.76923077,
                       -28846.15384615,  -24038.46153846,  230769.23076923,
                        19230.76923077,  -76923.07692308,  -24038.46153846,
                       -28846.15384615,  -76923.07692308,  230769.23076923,
                       -28846.15384615,   24038.46153846,   19230.76923077,
                        19230.76923077,  230769.23076923,   24038.46153846,
                       -28846.15384615,  -76923.07692308,   19230.76923077,
                       -28846.15384615,   24038.46153846,  230769.23076923,
                       -76923.07692308,  -76923.07692308,   24038.46153846,
                       -28846.15384615,  230769.23076923,   19230.76923077,
                       -28846.15384615,  -24038.46153846,   19230.76923077,
                       -76923.07692308,  230769.23076923,  -24038.46153846,
                       -28846.15384615,  -76923.07692308,   19230.76923077,
                       230769.23076923])
        row = array([0, 2, 4, 6, 7, 1, 3, 5, 6, 7, 0, 2, 4, 5, 6, 1, 3, 4, 5, 7, 0, 2, 3, 4, 6, 1, 2, 3, 5, 7, 0, 1, 2, 4, 6, 0, 1, 3, 5, 7])
        col = array([0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7])

        A_expected = coo_matrix((data,(row,col)), shape=(8,8)).todense()
        B_expected = array([[ 1. ,  0. ,  0.5],
                            [ 0. ,  1. , -0.5],
                            [ 1. ,  0. ,  0.5],
                            [ 0. ,  1. ,  0.5],
                            [ 1. ,  0. , -0.5],
                            [ 0. ,  1. , -0.5],
                            [ 1. ,  0. , -0.5],
                            [ 0. ,  1. ,  0.5]])
        
        A,B = linear_elasticity( (2,2), E=1e5, nu=0.3 )

        assert_almost_equal(A.todense(),A_expected)
        assert_almost_equal(B,B_expected)

class TestLocalStiffnessMatrix(TestCase):
    def test_q12d_local(self):
        L = matrix([[  4,  3, -4,  3, -2, -3,  2, -3],
                    [  3,  4, -3,  2, -3, -2,  3, -4],
                    [ -4, -3,  4, -3,  2,  3, -2,  3],
                    [  3,  2, -3,  4, -3, -4,  3, -2],
                    [ -2, -3,  2, -3,  4,  3, -4,  3],
                    [ -3, -2,  3, -4,  3,  4, -3,  2],
                    [  2,  3, -2,  3, -4, -3,  4, -3],
                    [ -3, -4,  3, -2,  3,  2, -3,  4]]) / 12.0
        
        M = matrix([[  4,  1, -2, -1, -2, -1,  0,  1],
                    [  1,  4,  1,  0, -1, -2, -1, -2],
                    [ -2,  1,  4, -1,  0, -1, -2,  1],
                    [ -1,  0, -1,  4,  1, -2,  1, -2],
                    [ -2, -1,  0,  1,  4,  1, -2, -1],
                    [ -1, -2, -1, -2,  1,  4,  1,  0],
                    [  0, -1, -2,  1, -2,  1,  4, -1],
                    [  1, -2,  1, -2, -1,  0, -1,  4]]) / 4.0
        
        vertices = matrix([[ 0, 0],
                           [ 1, 0],
                           [ 1, 1],
                           [ 0, 1]])
        
        assert_almost_equal(q12d_local(vertices, 1, 0) , L)
        assert_almost_equal(q12d_local(vertices, 0, 1) , M)
        assert_almost_equal(q12d_local(vertices, 1, 1) , L + M)
        
           
        L = matrix([[ 2,  3, -2,  3, -1, -3,  1, -3],
                    [ 3,  8, -3,  4, -3, -4,  3, -8],
                    [-2, -3,  2, -3,  1,  3, -1,  3],
                    [ 3,  4, -3,  8, -3, -8,  3, -4],
                    [-1, -3,  1, -3,  2,  3, -2,  3],
                    [-3, -4,  3, -8,  3,  8, -3,  4],
                    [ 1,  3, -1,  3, -2, -3,  2, -3],
                    [-3, -8,  3, -4,  3,  4, -3,  8]]) / 12.0
        
        M = matrix([[ 4,  1,  0, -1, -2, -1, -2,  1],
                    [ 1,  6,  1,  2, -1, -3, -1, -5],
                    [ 0,  1,  4, -1, -2, -1, -2,  1],
                    [-1,  2, -1,  6,  1, -5,  1, -3],
                    [-2, -1, -2,  1,  4,  1,  0, -1],
                    [-1, -3, -1, -5,  1,  6,  1,  2],
                    [-2, -1, -2,  1,  0,  1,  4, -1],
                    [ 1, -5,  1, -3, -1,  2, -1,  6]]) / 4.0
        
        vertices = matrix([[ 0, 0],
                           [ 2, 0],
                           [ 2, 1],
                           [ 0, 1]])
        
        assert_almost_equal(q12d_local(vertices, 1, 0) , L)
        assert_almost_equal(q12d_local(vertices, 0, 1) , M)
        assert_almost_equal(q12d_local(vertices, 1, 1) , L + M)

    def test_p12d_local(self):
        L = array([[ 0.5,  0.5, -0.5,  0,   0,  -0.5], 
                   [ 0.5,  0.5, -0.5,  0,   0,  -0.5],
                   [-0.5, -0.5,  0.5,  0,   0,   0.5],
                   [ 0. ,  0. ,  0. ,  0,   0,   0. ],
                   [ 0. ,  0. ,  0. ,  0,   0,   0. ],
                   [-0.5, -0.5,  0.5,  0,   0,   0.5]])

        M = array([[ 1.5,  0.5, -1,  -0.5, -0.5,  0], 
                   [ 0.5,  1.5,  0,  -0.5, -0.5, -1],
                   [-1. ,  0. ,  1,   0. ,  0. ,  0],
                   [-0.5, -0.5,  0,   0.5,  0.5,  0],
                   [-0.5, -0.5,  0,   0.5,  0.5,  0],
                   [ 0. , -1. ,  0,   0. ,  0. ,  1]])

        V = array([[0,0],
                   [1,0],
                   [0,1]])

        assert_almost_equal(p12d_local(V, 1, 0), L)
        assert_almost_equal(p12d_local(V, 0, 1), M)
        assert_almost_equal(p12d_local(V, 1, 1), L + M)
       
        # more general test
        V = array([[0.137356377783359, 0.042667310003708],
                   [1.107483961063919, 0.109422224983395],
                   [0.169335451696327, 1.055274514490457]])
        K = array([[ 2.73065573,  1.81050544, -2.42744817, -0.43828452, -0.30320756, -1.37222092],
                   [ 1.81050544,  2.70104222, -1.43828452, -0.41203425, -0.37222092, -2.28900797],
                   [-2.42744817, -1.43828452,  2.61567379, -0.06607114, -0.18822562,  1.50435566],
                   [-0.43828452, -0.41203425, -0.06607114,  0.52563866,  0.50435566, -0.11360441],
                   [-0.30320756, -0.37222092, -0.18822562,  0.50435566,  0.49143318, -0.13213474],
                   [-1.37222092, -2.28900797,  1.50435566, -0.11360441, -0.13213474,  2.40261239]])

        assert_almost_equal(p12d_local(V, 3, 1), K)


    def test_p13d_local(self):
        L = array([[ 1,  1,  1, -1,  0,  0,  0, -1,  0,  0,  0, -1.],
                   [ 1,  1,  1, -1,  0,  0,  0, -1,  0,  0,  0, -1.],
                   [ 1,  1,  1, -1,  0,  0,  0, -1,  0,  0,  0, -1.],
                   [-1, -1, -1,  1,  0,  0,  0,  1,  0,  0,  0,  1.],
                   [ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0.],
                   [ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0.],
                   [ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0.],
                   [-1, -1, -1,  1,  0,  0,  0,  1,  0,  0,  0,  1.],
                   [ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0.],
                   [ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0.],
                   [ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0.],
                   [-1, -1, -1,  1,  0,  0,  0,  1,  0,  0,  0,  1.]]) / 6.0

        M = array([[ 4,  1,  1, -2, -1, -1, -1,  0,  0, -1,  0,  0],
                   [ 1,  4,  1,  0, -1,  0, -1, -2, -1,  0, -1,  0],
                   [ 1,  1,  4,  0,  0, -1,  0,  0, -1, -1, -1, -2],
                   [-2,  0,  0,  2,  0,  0,  0,  0,  0,  0,  0,  0],
                   [-1, -1,  0,  0,  1,  0,  1,  0,  0,  0,  0,  0],
                   [-1,  0, -1,  0,  0,  1,  0,  0,  0,  1,  0,  0],
                   [-1, -1,  0,  0,  1,  0,  1,  0,  0,  0,  0,  0],
                   [ 0, -2,  0,  0,  0,  0,  0,  2,  0,  0,  0,  0],
                   [ 0, -1, -1,  0,  0,  0,  0,  0,  1,  0,  1,  0],
                   [-1,  0, -1,  0,  0,  1,  0,  0,  0,  1,  0,  0],
                   [ 0, -1, -1,  0,  0,  0,  0,  0,  1,  0,  1,  0],
                   [ 0,  0, -2,  0,  0,  0,  0,  0,  0,  0,  0,  2]]) / 6.0

        V = array([[0,0,0],[1,0,0],[0,1,0],[0,0,1]])

        assert_almost_equal(p13d_local(V,1,0), L)
        assert_almost_equal(p13d_local(V,0,1), M)
        assert_almost_equal(p13d_local(V,1,1), L + M)

