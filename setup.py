from setuptools import setup
from torch.utils.cpp_extension import BuildExtension, CUDAExtension

setup(
    name='inplace_abn',
    ext_modules=[
        CUDAExtension(
            'inplace_abn_cuda', [
                'inplace_abn/modules/src/inplace_abn.cpp',
                'inplace_abn/modules/src/inplace_abn_cpu.cpp',
                'inplace_abn/modules/src/inplace_abn_cuda.cu',
            ],
            extra_compile_args={
                'cxx': [],
                'nvcc': ['--expt-extended-lambda']
            })
    ],
    packages=['inplace_abn', 'inplace_abn.imagenet', 'inplace_abn.models', 'inplace_abn.modules'],
    cmdclass={'build_ext': BuildExtension})
