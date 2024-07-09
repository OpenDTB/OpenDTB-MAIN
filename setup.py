import setuptools

setuptools.setup(
    name="OpenDTB-main",
    version="0.2.6",
    description="CASIA's digital twin brain platform",
    author="Brain Net Group",
    url="https://github.com/OpenDTB/OpenDTB-MAIN",
    license="GPL-3.0",
    install_requires=[
        "opendtb-framework @ https://github.com/OpenDTB/OpenDTB-Framework/tarball/main",
        "numba",
        "mako",
        "brainpy",
        "jaxlib",
        "matplotlib",
        "scikit-learn",
        "mne",
    ],
    packages=setuptools.find_packages(),
    include_package_data=True,
)
