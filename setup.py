from setuptools import setup, find_packages

setup(
        name = "oldies",
        packages = find_packages(),
        namespace_packages=["oldies"],
        zip_safe = False,
        entry_points = {"gui_scripts": ["oldies-apahida-ui = oldies.entrypoint.main:main"]}
)

