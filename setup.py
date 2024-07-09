import setuptools

setuptools.setup(
    name="OpenDTB-main",
    version="0.2.6",
    description="CASIA's digital twin brain platform",
    author="ZJB Group",
    url="https://github.com/ZJBGroup/ZJB-Main",
    license="GPL-3.0",
    install_requires=[
        "zjb-framework @ https://github.com/ZJBGroup/ZJB-Framework/tarball/main",
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
