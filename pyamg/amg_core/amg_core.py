# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.2
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info
if version_info >= (2,6,0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_amg_core', [dirname(__file__)])
        except ImportError:
            import _amg_core
            return _amg_core
        if fp is not None:
            try:
                _mod = imp.load_module('_amg_core', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _amg_core = swig_import_helper()
    del swig_import_helper
else:
    import _amg_core
del version_info
try:
    _swig_property = property
except NameError:
    pass # Python < 2.2 doesn't have 'property'.
def _swig_setattr_nondynamic(self,class_type,name,value,static=1):
    if (name == "thisown"): return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name,None)
    if method: return method(self,value)
    if (not static):
        self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)

def _swig_setattr(self,class_type,name,value):
    return _swig_setattr_nondynamic(self,class_type,name,value,0)

def _swig_getattr(self,class_type,name):
    if (name == "thisown"): return self.this.own()
    method = class_type.__swig_getmethods__.get(name,None)
    if method: return method(self)
    raise AttributeError(name)

def _swig_repr(self):
    try: strthis = "proxy of " + self.this.__repr__()
    except: strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except AttributeError:
    class _object : pass
    _newclass = 0


F_NODE = _amg_core.F_NODE
C_NODE = _amg_core.C_NODE
U_NODE = _amg_core.U_NODE

def signof(*args):
  """
    signof(int a) -> int
    signof(float a) -> float
    signof(double a) -> double
    """
  return _amg_core.signof(*args)

def conjugate(*args):
  """
    conjugate(float const & x) -> float
    conjugate(double const & x) -> double
    conjugate(npy_cfloat_wrapper const & x) -> npy_cfloat_wrapper
    conjugate(npy_cdouble_wrapper const & x) -> npy_cdouble_wrapper
    """
  return _amg_core.conjugate(*args)

def real(*args):
  """
    real(float const & x) -> float
    real(double const & x) -> double
    real(npy_cfloat_wrapper const & x) -> float
    real(npy_cdouble_wrapper const & x) -> double
    """
  return _amg_core.real(*args)

def imag(*args):
  """
    imag(float const & x) -> float
    imag(double const & x) -> double
    imag(npy_cfloat_wrapper const & x) -> float
    imag(npy_cdouble_wrapper const & x) -> double
    """
  return _amg_core.imag(*args)

def mynorm(*args):
  """
    mynorm(float const & x) -> float
    mynorm(double const & x) -> double
    mynorm(npy_cfloat_wrapper const & x) -> float
    mynorm(npy_cdouble_wrapper const & x) -> double
    """
  return _amg_core.mynorm(*args)

def mynormsq(*args):
  """
    mynormsq(float const & x) -> float
    mynormsq(double const & x) -> double
    mynormsq(npy_cfloat_wrapper const & x) -> float
    mynormsq(npy_cdouble_wrapper const & x) -> double
    """
  return _amg_core.mynormsq(*args)

def zero_real(*args):
  """
    zero_real(float & x) -> float
    zero_real(double & x) -> double
    zero_real(npy_cfloat_wrapper & x) -> npy_cfloat_wrapper
    zero_real(npy_cdouble_wrapper & x) -> npy_cdouble_wrapper
    """
  return _amg_core.zero_real(*args)

def zero_imag(*args):
  """
    zero_imag(float & x) -> float
    zero_imag(double & x) -> double
    zero_imag(npy_cfloat_wrapper & x) -> npy_cfloat_wrapper
    zero_imag(npy_cdouble_wrapper & x) -> npy_cdouble_wrapper
    """
  return _amg_core.zero_imag(*args)

def cljp_naive_splitting(*args):
  """
    cljp_naive_splitting(int const n, int const [] Sp, int const [] Sj, int const [] Tp, int const [] Tj, 
        int [] splitting, int const colorflag)
    """
  return _amg_core.cljp_naive_splitting(*args)

def naive_aggregation(*args):
  """naive_aggregation(int const n_row, int const [] Ap, int const [] Aj, int [] x, int [] y) -> int"""
  return _amg_core.naive_aggregation(*args)

def standard_aggregation(*args):
  """standard_aggregation(int const n_row, int const [] Ap, int const [] Aj, int [] x, int [] y) -> int"""
  return _amg_core.standard_aggregation(*args)

def rs_cf_splitting(*args):
  """
    rs_cf_splitting(int const n_nodes, int const [] Sp, int const [] Sj, int const [] Tp, int const [] Tj, 
        int [] splitting)
    """
  return _amg_core.rs_cf_splitting(*args)

def rs_direct_interpolation_pass1(*args):
  """rs_direct_interpolation_pass1(int const n_nodes, int const [] Sp, int const [] Sj, int const [] splitting, int [] Bp)"""
  return _amg_core.rs_direct_interpolation_pass1(*args)

def rs_direct_interpolation_pass2(*args):
  """
    rs_direct_interpolation_pass2(int const n_nodes, int const [] Ap, int const [] Aj, float const [] Ax, int const [] Sp, 
        int const [] Sj, float const [] Sx, int const [] splitting, int const [] Bp, 
        int [] Bj, float [] Bx)
    rs_direct_interpolation_pass2(int const n_nodes, int const [] Ap, int const [] Aj, double const [] Ax, int const [] Sp, 
        int const [] Sj, double const [] Sx, int const [] splitting, int const [] Bp, 
        int [] Bj, double [] Bx)
    """
  return _amg_core.rs_direct_interpolation_pass2(*args)

def satisfy_constraints_helper(*args):
  """
    satisfy_constraints_helper(int const RowsPerBlock, int const ColsPerBlock, int const num_block_rows, int const NullDim, 
        float const [] x, float const [] y, float const [] z, int const [] Sp, 
        int const [] Sj, float [] Sx)
    satisfy_constraints_helper(int const RowsPerBlock, int const ColsPerBlock, int const num_block_rows, int const NullDim, 
        double const [] x, double const [] y, double const [] z, int const [] Sp, 
        int const [] Sj, double [] Sx)
    satisfy_constraints_helper(int const RowsPerBlock, int const ColsPerBlock, int const num_block_rows, int const NullDim, 
        npy_cfloat_wrapper const [] x, npy_cfloat_wrapper const [] y, npy_cfloat_wrapper const [] z, 
        int const [] Sp, int const [] Sj, npy_cfloat_wrapper [] Sx)
    satisfy_constraints_helper(int const RowsPerBlock, int const ColsPerBlock, int const num_block_rows, int const NullDim, 
        npy_cdouble_wrapper const [] x, npy_cdouble_wrapper const [] y, 
        npy_cdouble_wrapper const [] z, int const [] Sp, int const [] Sj, npy_cdouble_wrapper [] Sx)
    """
  return _amg_core.satisfy_constraints_helper(*args)

def calc_BtB(*args):
  """
    calc_BtB(int const NullDim, int const Nnodes, int const ColsPerBlock, float const [] b, int const BsqCols, 
        float [] x, int const [] Sp, int const [] Sj)
    calc_BtB(int const NullDim, int const Nnodes, int const ColsPerBlock, double const [] b, int const BsqCols, 
        double [] x, int const [] Sp, int const [] Sj)
    calc_BtB(int const NullDim, int const Nnodes, int const ColsPerBlock, npy_cfloat_wrapper const [] b, 
        int const BsqCols, npy_cfloat_wrapper [] x, int const [] Sp, int const [] Sj)
    calc_BtB(int const NullDim, int const Nnodes, int const ColsPerBlock, npy_cdouble_wrapper const [] b, 
        int const BsqCols, npy_cdouble_wrapper [] x, int const [] Sp, int const [] Sj)
    """
  return _amg_core.calc_BtB(*args)

def incomplete_mat_mult_bsr(*args):
  """
    incomplete_mat_mult_bsr(int const [] Ap, int const [] Aj, float const [] Ax, int const [] Bp, int const [] Bj, 
        float const [] Bx, int const [] Sp, int const [] Sj, float [] Sx, int const n_brow, 
        int const n_bcol, int const brow_A, int const bcol_A, int const bcol_B)
    incomplete_mat_mult_bsr(int const [] Ap, int const [] Aj, double const [] Ax, int const [] Bp, int const [] Bj, 
        double const [] Bx, int const [] Sp, int const [] Sj, double [] Sx, 
        int const n_brow, int const n_bcol, int const brow_A, int const bcol_A, int const bcol_B)
    incomplete_mat_mult_bsr(int const [] Ap, int const [] Aj, npy_cfloat_wrapper const [] Ax, int const [] Bp, 
        int const [] Bj, npy_cfloat_wrapper const [] Bx, int const [] Sp, int const [] Sj, 
        npy_cfloat_wrapper [] Sx, int const n_brow, int const n_bcol, int const brow_A, 
        int const bcol_A, int const bcol_B)
    incomplete_mat_mult_bsr(int const [] Ap, int const [] Aj, npy_cdouble_wrapper const [] Ax, int const [] Bp, 
        int const [] Bj, npy_cdouble_wrapper const [] Bx, int const [] Sp, int const [] Sj, 
        npy_cdouble_wrapper [] Sx, int const n_brow, int const n_bcol, 
        int const brow_A, int const bcol_A, int const bcol_B)
    """
  return _amg_core.incomplete_mat_mult_bsr(*args)

def maximum_row_value(*args):
  """
    maximum_row_value(int const n_row, float [] x, int const [] Ap, int const [] Aj, float const [] Ax)
    maximum_row_value(int const n_row, double [] x, int const [] Ap, int const [] Aj, double const [] Ax)
    maximum_row_value(int const n_row, npy_cfloat_wrapper [] x, int const [] Ap, int const [] Aj, npy_cfloat_wrapper const [] Ax)
    maximum_row_value(int const n_row, npy_cdouble_wrapper [] x, int const [] Ap, int const [] Aj, npy_cdouble_wrapper const [] Ax)
    """
  return _amg_core.maximum_row_value(*args)

def pinv_array(*args):
  """
    pinv_array(float [] Ax, int const m, int const n, char const TransA)
    pinv_array(double [] Ax, int const m, int const n, char const TransA)
    pinv_array(npy_cfloat_wrapper [] Ax, int const m, int const n, char const TransA)
    pinv_array(npy_cdouble_wrapper [] Ax, int const m, int const n, char const TransA)
    """
  return _amg_core.pinv_array(*args)

def classical_strength_of_connection(*args):
  """
    classical_strength_of_connection(int const n_row, float const theta, int const [] Ap, int const [] Aj, float const [] Ax, 
        int [] Sp, int [] Sj, float [] Sx)
    classical_strength_of_connection(int const n_row, double const theta, int const [] Ap, int const [] Aj, double const [] Ax, 
        int [] Sp, int [] Sj, double [] Sx)
    classical_strength_of_connection(int const n_row, float const theta, int const [] Ap, int const [] Aj, npy_cfloat_wrapper const [] Ax, 
        int [] Sp, int [] Sj, npy_cfloat_wrapper [] Sx)
    classical_strength_of_connection(int const n_row, double const theta, int const [] Ap, int const [] Aj, npy_cdouble_wrapper const [] Ax, 
        int [] Sp, int [] Sj, npy_cdouble_wrapper [] Sx)
    """
  return _amg_core.classical_strength_of_connection(*args)

def symmetric_strength_of_connection(*args):
  """
    symmetric_strength_of_connection(int const n_row, float const theta, int const [] Ap, int const [] Aj, float const [] Ax, 
        int [] Sp, int [] Sj, float [] Sx)
    symmetric_strength_of_connection(int const n_row, double const theta, int const [] Ap, int const [] Aj, double const [] Ax, 
        int [] Sp, int [] Sj, double [] Sx)
    symmetric_strength_of_connection(int const n_row, float const theta, int const [] Ap, int const [] Aj, npy_cfloat_wrapper const [] Ax, 
        int [] Sp, int [] Sj, npy_cfloat_wrapper [] Sx)
    symmetric_strength_of_connection(int const n_row, double const theta, int const [] Ap, int const [] Aj, npy_cdouble_wrapper const [] Ax, 
        int [] Sp, int [] Sj, npy_cdouble_wrapper [] Sx)
    """
  return _amg_core.symmetric_strength_of_connection(*args)

def evolution_strength_helper(*args):
  """
    evolution_strength_helper(float [] Sx, int const [] Sp, int const [] Sj, int const nrows, float const [] x, 
        float const [] y, float const [] b, int const BDBCols, int const NullDim, 
        float const tol)
    evolution_strength_helper(double [] Sx, int const [] Sp, int const [] Sj, int const nrows, double const [] x, 
        double const [] y, double const [] b, int const BDBCols, int const NullDim, 
        double const tol)
    evolution_strength_helper(npy_cfloat_wrapper [] Sx, int const [] Sp, int const [] Sj, int const nrows, npy_cfloat_wrapper const [] x, 
        npy_cfloat_wrapper const [] y, npy_cfloat_wrapper const [] b, 
        int const BDBCols, int const NullDim, float const tol)
    evolution_strength_helper(npy_cdouble_wrapper [] Sx, int const [] Sp, int const [] Sj, int const nrows, npy_cdouble_wrapper const [] x, 
        npy_cdouble_wrapper const [] y, npy_cdouble_wrapper const [] b, 
        int const BDBCols, int const NullDim, double const tol)
    """
  return _amg_core.evolution_strength_helper(*args)

def incomplete_mat_mult_csr(*args):
  """
    incomplete_mat_mult_csr(int const [] Ap, int const [] Aj, float const [] Ax, int const [] Bp, int const [] Bj, 
        float const [] Bx, int const [] Sp, int const [] Sj, float [] Sx, int const num_rows)
    incomplete_mat_mult_csr(int const [] Ap, int const [] Aj, double const [] Ax, int const [] Bp, int const [] Bj, 
        double const [] Bx, int const [] Sp, int const [] Sj, double [] Sx, 
        int const num_rows)
    incomplete_mat_mult_csr(int const [] Ap, int const [] Aj, npy_cfloat_wrapper const [] Ax, int const [] Bp, 
        int const [] Bj, npy_cfloat_wrapper const [] Bx, int const [] Sp, int const [] Sj, 
        npy_cfloat_wrapper [] Sx, int const num_rows)
    incomplete_mat_mult_csr(int const [] Ap, int const [] Aj, npy_cdouble_wrapper const [] Ax, int const [] Bp, 
        int const [] Bj, npy_cdouble_wrapper const [] Bx, int const [] Sp, int const [] Sj, 
        npy_cdouble_wrapper [] Sx, int const num_rows)
    """
  return _amg_core.incomplete_mat_mult_csr(*args)

def apply_distance_filter(*args):
  """
    apply_distance_filter(int const n_row, float const epsilon, int const [] Sp, int const [] Sj, float [] Sx)
    apply_distance_filter(int const n_row, double const epsilon, int const [] Sp, int const [] Sj, double [] Sx)
    """
  return _amg_core.apply_distance_filter(*args)

def apply_absolute_distance_filter(*args):
  """
    apply_absolute_distance_filter(int const n_row, float const epsilon, int const [] Sp, int const [] Sj, float [] Sx)
    apply_absolute_distance_filter(int const n_row, double const epsilon, int const [] Sp, int const [] Sj, double [] Sx)
    """
  return _amg_core.apply_absolute_distance_filter(*args)

def min_blocks(*args):
  """
    min_blocks(int const n_blocks, int const blocksize, float const [] Sx, float [] Tx)
    min_blocks(int const n_blocks, int const blocksize, double const [] Sx, double [] Tx)
    """
  return _amg_core.min_blocks(*args)

def bsr_gauss_seidel(*args):
  """
    bsr_gauss_seidel(int const [] Ap, int const [] Aj, float const [] Ax, float [] x, float const [] b, 
        int const row_start, int const row_stop, int const row_step, int const blocksize)
    bsr_gauss_seidel(int const [] Ap, int const [] Aj, double const [] Ax, double [] x, double const [] b, 
        int const row_start, int const row_stop, int const row_step, int const blocksize)
    bsr_gauss_seidel(int const [] Ap, int const [] Aj, npy_cfloat_wrapper const [] Ax, npy_cfloat_wrapper [] x, 
        npy_cfloat_wrapper const [] b, int const row_start, int const row_stop, 
        int const row_step, int const blocksize)
    bsr_gauss_seidel(int const [] Ap, int const [] Aj, npy_cdouble_wrapper const [] Ax, npy_cdouble_wrapper [] x, 
        npy_cdouble_wrapper const [] b, int const row_start, int const row_stop, 
        int const row_step, int const blocksize)
    """
  return _amg_core.bsr_gauss_seidel(*args)

def bsr_jacobi(*args):
  """
    bsr_jacobi(int const [] Ap, int const [] Aj, float const [] Ax, float [] x, float const [] b, 
        float [] temp, int const row_start, int const row_stop, int const row_step, 
        int const blocksize, float const [] omega)
    bsr_jacobi(int const [] Ap, int const [] Aj, double const [] Ax, double [] x, double const [] b, 
        double [] temp, int const row_start, int const row_stop, int const row_step, 
        int const blocksize, double const [] omega)
    bsr_jacobi(int const [] Ap, int const [] Aj, npy_cfloat_wrapper const [] Ax, npy_cfloat_wrapper [] x, 
        npy_cfloat_wrapper const [] b, npy_cfloat_wrapper [] temp, int const row_start, 
        int const row_stop, int const row_step, int const blocksize, 
        npy_cfloat_wrapper const [] omega)
    bsr_jacobi(int const [] Ap, int const [] Aj, npy_cdouble_wrapper const [] Ax, npy_cdouble_wrapper [] x, 
        npy_cdouble_wrapper const [] b, npy_cdouble_wrapper [] temp, int const row_start, 
        int const row_stop, int const row_step, int const blocksize, 
        npy_cdouble_wrapper const [] omega)
    """
  return _amg_core.bsr_jacobi(*args)

def gauss_seidel(*args):
  """
    gauss_seidel(int const [] Ap, int const [] Aj, float const [] Ax, float [] x, float const [] b, 
        int const row_start, int const row_stop, int const row_step)
    gauss_seidel(int const [] Ap, int const [] Aj, double const [] Ax, double [] x, double const [] b, 
        int const row_start, int const row_stop, int const row_step)
    gauss_seidel(int const [] Ap, int const [] Aj, npy_cfloat_wrapper const [] Ax, npy_cfloat_wrapper [] x, 
        npy_cfloat_wrapper const [] b, int const row_start, int const row_stop, 
        int const row_step)
    gauss_seidel(int const [] Ap, int const [] Aj, npy_cdouble_wrapper const [] Ax, npy_cdouble_wrapper [] x, 
        npy_cdouble_wrapper const [] b, int const row_start, int const row_stop, 
        int const row_step)
    """
  return _amg_core.gauss_seidel(*args)

def jacobi(*args):
  """
    jacobi(int const [] Ap, int const [] Aj, float const [] Ax, float [] x, float const [] b, 
        float [] temp, int const row_start, int const row_stop, int const row_step, 
        float const [] omega)
    jacobi(int const [] Ap, int const [] Aj, double const [] Ax, double [] x, double const [] b, 
        double [] temp, int const row_start, int const row_stop, int const row_step, 
        double const [] omega)
    jacobi(int const [] Ap, int const [] Aj, npy_cfloat_wrapper const [] Ax, npy_cfloat_wrapper [] x, 
        npy_cfloat_wrapper const [] b, npy_cfloat_wrapper [] temp, int const row_start, 
        int const row_stop, int const row_step, npy_cfloat_wrapper const [] omega)
    jacobi(int const [] Ap, int const [] Aj, npy_cdouble_wrapper const [] Ax, npy_cdouble_wrapper [] x, 
        npy_cdouble_wrapper const [] b, npy_cdouble_wrapper [] temp, int const row_start, 
        int const row_stop, int const row_step, npy_cdouble_wrapper const [] omega)
    """
  return _amg_core.jacobi(*args)

def block_jacobi(*args):
  """
    block_jacobi(int const [] Ap, int const [] Aj, float const [] Ax, float [] x, float const [] b, 
        float const [] Tx, float [] temp, int const row_start, int const row_stop, 
        int const row_step, float const [] omega, int const blocksize)
    block_jacobi(int const [] Ap, int const [] Aj, double const [] Ax, double [] x, double const [] b, 
        double const [] Tx, double [] temp, int const row_start, int const row_stop, 
        int const row_step, double const [] omega, int const blocksize)
    block_jacobi(int const [] Ap, int const [] Aj, npy_cfloat_wrapper const [] Ax, npy_cfloat_wrapper [] x, 
        npy_cfloat_wrapper const [] b, npy_cfloat_wrapper const [] Tx, npy_cfloat_wrapper [] temp, 
        int const row_start, int const row_stop, int const row_step, 
        npy_cfloat_wrapper const [] omega, int const blocksize)
    block_jacobi(int const [] Ap, int const [] Aj, npy_cdouble_wrapper const [] Ax, npy_cdouble_wrapper [] x, 
        npy_cdouble_wrapper const [] b, npy_cdouble_wrapper const [] Tx, 
        npy_cdouble_wrapper [] temp, int const row_start, int const row_stop, int const row_step, 
        npy_cdouble_wrapper const [] omega, int const blocksize)
    """
  return _amg_core.block_jacobi(*args)

def block_gauss_seidel(*args):
  """
    block_gauss_seidel(int const [] Ap, int const [] Aj, float const [] Ax, float [] x, float const [] b, 
        float const [] Tx, int const row_start, int const row_stop, int const row_step, 
        int const blocksize)
    block_gauss_seidel(int const [] Ap, int const [] Aj, double const [] Ax, double [] x, double const [] b, 
        double const [] Tx, int const row_start, int const row_stop, int const row_step, 
        int const blocksize)
    block_gauss_seidel(int const [] Ap, int const [] Aj, npy_cfloat_wrapper const [] Ax, npy_cfloat_wrapper [] x, 
        npy_cfloat_wrapper const [] b, npy_cfloat_wrapper const [] Tx, int const row_start, 
        int const row_stop, int const row_step, int const blocksize)
    block_gauss_seidel(int const [] Ap, int const [] Aj, npy_cdouble_wrapper const [] Ax, npy_cdouble_wrapper [] x, 
        npy_cdouble_wrapper const [] b, npy_cdouble_wrapper const [] Tx, 
        int const row_start, int const row_stop, int const row_step, int const blocksize)
    """
  return _amg_core.block_gauss_seidel(*args)

def gauss_seidel_indexed(*args):
  """
    gauss_seidel_indexed(int const [] Ap, int const [] Aj, float const [] Ax, float [] x, float const [] b, 
        int const [] Id, int const row_start, int const row_stop, int const row_step)
    gauss_seidel_indexed(int const [] Ap, int const [] Aj, double const [] Ax, double [] x, double const [] b, 
        int const [] Id, int const row_start, int const row_stop, int const row_step)
    gauss_seidel_indexed(int const [] Ap, int const [] Aj, npy_cfloat_wrapper const [] Ax, npy_cfloat_wrapper [] x, 
        npy_cfloat_wrapper const [] b, int const [] Id, int const row_start, 
        int const row_stop, int const row_step)
    gauss_seidel_indexed(int const [] Ap, int const [] Aj, npy_cdouble_wrapper const [] Ax, npy_cdouble_wrapper [] x, 
        npy_cdouble_wrapper const [] b, int const [] Id, int const row_start, 
        int const row_stop, int const row_step)
    """
  return _amg_core.gauss_seidel_indexed(*args)

def jacobi_ne(*args):
  """
    jacobi_ne(int const [] Ap, int const [] Aj, float const [] Ax, float [] x, float const [] b, 
        float const [] Tx, float [] temp, int const row_start, int const row_stop, 
        int const row_step, float const [] omega)
    jacobi_ne(int const [] Ap, int const [] Aj, double const [] Ax, double [] x, double const [] b, 
        double const [] Tx, double [] temp, int const row_start, int const row_stop, 
        int const row_step, double const [] omega)
    jacobi_ne(int const [] Ap, int const [] Aj, npy_cfloat_wrapper const [] Ax, npy_cfloat_wrapper [] x, 
        npy_cfloat_wrapper const [] b, npy_cfloat_wrapper const [] Tx, npy_cfloat_wrapper [] temp, 
        int const row_start, int const row_stop, int const row_step, 
        npy_cfloat_wrapper const [] omega)
    jacobi_ne(int const [] Ap, int const [] Aj, npy_cdouble_wrapper const [] Ax, npy_cdouble_wrapper [] x, 
        npy_cdouble_wrapper const [] b, npy_cdouble_wrapper const [] Tx, 
        npy_cdouble_wrapper [] temp, int const row_start, int const row_stop, int const row_step, 
        npy_cdouble_wrapper const [] omega)
    """
  return _amg_core.jacobi_ne(*args)

def gauss_seidel_ne(*args):
  """
    gauss_seidel_ne(int const [] Ap, int const [] Aj, float const [] Ax, float [] x, float const [] b, 
        int const row_start, int const row_stop, int const row_step, float const [] Tx, 
        float const omega)
    gauss_seidel_ne(int const [] Ap, int const [] Aj, double const [] Ax, double [] x, double const [] b, 
        int const row_start, int const row_stop, int const row_step, double const [] Tx, 
        double const omega)
    gauss_seidel_ne(int const [] Ap, int const [] Aj, npy_cfloat_wrapper const [] Ax, npy_cfloat_wrapper [] x, 
        npy_cfloat_wrapper const [] b, int const row_start, int const row_stop, 
        int const row_step, npy_cfloat_wrapper const [] Tx, float const omega)
    gauss_seidel_ne(int const [] Ap, int const [] Aj, npy_cdouble_wrapper const [] Ax, npy_cdouble_wrapper [] x, 
        npy_cdouble_wrapper const [] b, int const row_start, int const row_stop, 
        int const row_step, npy_cdouble_wrapper const [] Tx, double const omega)
    """
  return _amg_core.gauss_seidel_ne(*args)

def gauss_seidel_nr(*args):
  """
    gauss_seidel_nr(int const [] Ap, int const [] Aj, float const [] Ax, float [] x, float [] z, int const col_start, 
        int const col_stop, int const col_step, float const [] Tx, 
        float const omega)
    gauss_seidel_nr(int const [] Ap, int const [] Aj, double const [] Ax, double [] x, double [] z, int const col_start, 
        int const col_stop, int const col_step, double const [] Tx, 
        double const omega)
    gauss_seidel_nr(int const [] Ap, int const [] Aj, npy_cfloat_wrapper const [] Ax, npy_cfloat_wrapper [] x, 
        npy_cfloat_wrapper [] z, int const col_start, int const col_stop, 
        int const col_step, npy_cfloat_wrapper const [] Tx, float const omega)
    gauss_seidel_nr(int const [] Ap, int const [] Aj, npy_cdouble_wrapper const [] Ax, npy_cdouble_wrapper [] x, 
        npy_cdouble_wrapper [] z, int const col_start, int const col_stop, 
        int const col_step, npy_cdouble_wrapper const [] Tx, double const omega)
    """
  return _amg_core.gauss_seidel_nr(*args)

def overlapping_schwarz_csr(*args):
  """
    overlapping_schwarz_csr(int const [] Ap, int const [] Aj, float const [] Ax, float [] x, float const [] b, 
        float const [] Tx, int const [] Tp, int const [] Sj, int const [] Sp, int nsdomains, 
        int nrows, int row_start, int row_stop, int row_step)
    overlapping_schwarz_csr(int const [] Ap, int const [] Aj, double const [] Ax, double [] x, double const [] b, 
        double const [] Tx, int const [] Tp, int const [] Sj, int const [] Sp, 
        int nsdomains, int nrows, int row_start, int row_stop, int row_step)
    overlapping_schwarz_csr(int const [] Ap, int const [] Aj, npy_cfloat_wrapper const [] Ax, npy_cfloat_wrapper [] x, 
        npy_cfloat_wrapper const [] b, npy_cfloat_wrapper const [] Tx, int const [] Tp, 
        int const [] Sj, int const [] Sp, int nsdomains, int nrows, 
        int row_start, int row_stop, int row_step)
    overlapping_schwarz_csr(int const [] Ap, int const [] Aj, npy_cdouble_wrapper const [] Ax, npy_cdouble_wrapper [] x, 
        npy_cdouble_wrapper const [] b, npy_cdouble_wrapper const [] Tx, 
        int const [] Tp, int const [] Sj, int const [] Sp, int nsdomains, int nrows, 
        int row_start, int row_stop, int row_step)
    """
  return _amg_core.overlapping_schwarz_csr(*args)

def extract_subblocks(*args):
  """
    extract_subblocks(int const [] Ap, int const [] Aj, float const [] Ax, float [] Tx, int const [] Tp, 
        int const [] Sj, int const [] Sp, int const nsdomains, int const nrows)
    extract_subblocks(int const [] Ap, int const [] Aj, double const [] Ax, double [] Tx, int const [] Tp, 
        int const [] Sj, int const [] Sp, int const nsdomains, int const nrows)
    extract_subblocks(int const [] Ap, int const [] Aj, npy_cfloat_wrapper const [] Ax, npy_cfloat_wrapper [] Tx, 
        int const [] Tp, int const [] Sj, int const [] Sp, int const nsdomains, 
        int const nrows)
    extract_subblocks(int const [] Ap, int const [] Aj, npy_cdouble_wrapper const [] Ax, npy_cdouble_wrapper [] Tx, 
        int const [] Tp, int const [] Sj, int const [] Sp, int const nsdomains, 
        int const nrows)
    """
  return _amg_core.extract_subblocks(*args)

def apply_householders(*args):
  """
    apply_householders(float [] z, float const [] B, int const n, int const start, int const stop, int const step)
    apply_householders(double [] z, double const [] B, int const n, int const start, int const stop, int const step)
    apply_householders(npy_cfloat_wrapper [] z, npy_cfloat_wrapper const [] B, int const n, int const start, 
        int const stop, int const step)
    apply_householders(npy_cdouble_wrapper [] z, npy_cdouble_wrapper const [] B, int const n, int const start, 
        int const stop, int const step)
    """
  return _amg_core.apply_householders(*args)

def householder_hornerscheme(*args):
  """
    householder_hornerscheme(float [] z, float const [] B, float const [] y, int const n, int const start, int const stop, 
        int const step)
    householder_hornerscheme(double [] z, double const [] B, double const [] y, int const n, int const start, 
        int const stop, int const step)
    householder_hornerscheme(npy_cfloat_wrapper [] z, npy_cfloat_wrapper const [] B, npy_cfloat_wrapper const [] y, 
        int const n, int const start, int const stop, int const step)
    householder_hornerscheme(npy_cdouble_wrapper [] z, npy_cdouble_wrapper const [] B, npy_cdouble_wrapper const [] y, 
        int const n, int const start, int const stop, int const step)
    """
  return _amg_core.householder_hornerscheme(*args)

def apply_givens(*args):
  """
    apply_givens(float const [] B, float [] x, int const n, int const nrot)
    apply_givens(double const [] B, double [] x, int const n, int const nrot)
    apply_givens(npy_cfloat_wrapper const [] B, npy_cfloat_wrapper [] x, int const n, int const nrot)
    apply_givens(npy_cdouble_wrapper const [] B, npy_cdouble_wrapper [] x, int const n, int const nrot)
    """
  return _amg_core.apply_givens(*args)

def maximal_independent_set_serial(*args):
  """
    maximal_independent_set_serial(int const num_rows, int const [] Ap, int const [] Aj, int const active, int const C, 
        int const F, int [] x) -> int
    """
  return _amg_core.maximal_independent_set_serial(*args)

def maximal_independent_set_parallel(*args):
  """
    maximal_independent_set_parallel(int const num_rows, int const [] Ap, int const [] Aj, int const active, int const C, 
        int const F, int [] x, double const [] y, int const max_iters=-1) -> int
    maximal_independent_set_parallel(int const num_rows, int const [] Ap, int const [] Aj, int const active, int const C, 
        int const F, int [] x, double const [] y) -> int
    """
  return _amg_core.maximal_independent_set_parallel(*args)

def maximal_independent_set_k_parallel(*args):
  """
    maximal_independent_set_k_parallel(int const num_rows, int const [] Ap, int const [] Aj, int const k, int [] x, double const [] y, 
        int const max_iters=-1)
    maximal_independent_set_k_parallel(int const num_rows, int const [] Ap, int const [] Aj, int const k, int [] x, double const [] y)
    """
  return _amg_core.maximal_independent_set_k_parallel(*args)

def vertex_coloring_mis(*args):
  """vertex_coloring_mis(int const num_rows, int const [] Ap, int const [] Aj, int [] x) -> int"""
  return _amg_core.vertex_coloring_mis(*args)

def vertex_coloring_jones_plassmann(*args):
  """vertex_coloring_jones_plassmann(int const num_rows, int const [] Ap, int const [] Aj, int [] x, double [] y) -> int"""
  return _amg_core.vertex_coloring_jones_plassmann(*args)

def vertex_coloring_LDF(*args):
  """vertex_coloring_LDF(int const num_rows, int const [] Ap, int const [] Aj, int [] x, double const [] y) -> int"""
  return _amg_core.vertex_coloring_LDF(*args)

def breadth_first_search(*args):
  """breadth_first_search(int const [] Ap, int const [] Aj, int const seed, int [] order, int [] level)"""
  return _amg_core.breadth_first_search(*args)

def connected_components(*args):
  """connected_components(int const num_nodes, int const [] Ap, int const [] Aj, int [] components) -> int"""
  return _amg_core.connected_components(*args)

def bellman_ford(*args):
  """
    bellman_ford(int const num_rows, int const [] Ap, int const [] Aj, int const [] Ax, int [] x, 
        int [] y)
    bellman_ford(int const num_rows, int const [] Ap, int const [] Aj, float const [] Ax, float [] x, 
        int [] y)
    bellman_ford(int const num_rows, int const [] Ap, int const [] Aj, double const [] Ax, double [] x, 
        int [] y)
    """
  return _amg_core.bellman_ford(*args)

def lloyd_cluster(*args):
  """
    lloyd_cluster(int const num_rows, int const [] Ap, int const [] Aj, int const [] Ax, int const num_seeds, 
        int [] x, int [] y, int [] z)
    lloyd_cluster(int const num_rows, int const [] Ap, int const [] Aj, float const [] Ax, int const num_seeds, 
        float [] x, int [] y, int [] z)
    lloyd_cluster(int const num_rows, int const [] Ap, int const [] Aj, double const [] Ax, int const num_seeds, 
        double [] x, int [] y, int [] z)
    """
  return _amg_core.lloyd_cluster(*args)

def fit_candidates(*args):
  """
    fit_candidates(int const n_row, int const n_col, int const K1, int const K2, int const [] Ap, int const [] Ai, 
        float [] Ax, float const [] B, float [] R, float const tol)
    fit_candidates(int const n_row, int const n_col, int const K1, int const K2, int const [] Ap, int const [] Ai, 
        double [] Ax, double const [] B, double [] R, double const tol)
    fit_candidates(int const n_row, int const n_col, int const K1, int const K2, int const [] Ap, int const [] Ai, 
        npy_cfloat_wrapper [] Ax, npy_cfloat_wrapper const [] B, npy_cfloat_wrapper [] R, 
        float const tol)
    fit_candidates(int const n_row, int const n_col, int const K1, int const K2, int const [] Ap, int const [] Ai, 
        npy_cdouble_wrapper [] Ax, npy_cdouble_wrapper const [] B, npy_cdouble_wrapper [] R, 
        double const tol)
    """
  return _amg_core.fit_candidates(*args)
# This file is compatible with both classic and new-style classes.


