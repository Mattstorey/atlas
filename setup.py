import io
from os.path import dirname, join
from setuptools import setup


long_description = open('README.rst').read()


def get_version(relpath):
  """Read version info from a file without importing it"""
  for line in io.open(join(dirname(__file__), relpath), encoding="cp437"):
    if "__version__" in line:
      if '"' in line:
        # __version__ = "0.9"
        return line.split('"')[1]
      elif "'" in line:
        return line.split("'")[1]


setup(
    name='pnnl-atlas',
    version=get_version("atlas/__init__.py"),
    url='https://github.com/pnnl/atlas',
    license='MIT',
    author='Joe Brown',
    author_email='joe.brown@pnnl.gov',
    description='ATLAS - a framework for assembly, annotation, and genomic binning of metagenomic and metatranscriptomic data',
    long_description=long_description,
    packages=['atlas'],
    package_data={'': [
            'atlas/Snakefile',
            'atlas/template_config.yaml',
            'atlas/rules/assemble.snakefile',
            'atlas/rules/annotate.snakefile',
            'atlas/rules/download.snakefile',
            'atlas/rules/binning.snakefile',
            'atlas/rules/gene_annotation.snakefile',
            'atlas/rules/qc.snakefile',
            'atlas/rules/binning.snakefile',
            'atlas/rules/initialize_checkm.py',
            'atlas/rules/get_fasta_of_bins.py',
            'atlas/envs/checkm.yaml',
            'atlas/envs/concoct.yaml',
            'atlas/envs/DASTool.yaml',
            'atlas/envs/dRep.yaml',
            'atlas/envs/maxbin.yaml',
            'atlas/envs/metabat.yaml',
            'atlas/envs/prokka.yaml',
            'atlas/envs/sequence_utils.yaml',
            'atlas/envs/optional_genome_binning.yaml',
            'atlas/envs/required_packages.yaml',
            'atlas/envs/report.yaml',
            'atlas/envs/eggNOG.yaml',
            'atlas/template_config.yaml',
            'atlas/report/qc_report.py',
            'atlas/report/report.css',
            'atlas/report/assembly_report.py',
            'atlas/report/bin_report.py'
                       ]},
    include_package_data=True,
    # install via conda: click, pandas, pyyaml, snakemake
    install_requires=[
        'ruamel.yaml==0.15.35'
    ],
    entry_points={
          'console_scripts': [
              'atlas = atlas.atlas:cli'
          ]
    },
    classifiers=["Topic :: Scientific/Engineering :: Bio-Informatics"],
)
