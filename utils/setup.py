
import setuptools

install_requires = []

setuptools.setup(
    name="utils",
    version="0.1",
    packages=setuptools.find_packages(),
    install_requires=install_requires,
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'create_app = create_app:create_app',
        ],
    },
    )
