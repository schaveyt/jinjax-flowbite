from setuptools import find_namespace_packages, setup, find_packages

with open("README.md", "r") as rm:
    readme_md = rm.read()

with open("requirements.txt") as rq:
    requirements_txt = rq.read().splitlines()

setup(
    name="jinjax_flowbite",
    version="0.1.dev0",
    platforms="any",
    description="Flowbite-based JinjaX Components",
    long_description=readme_md,
    long_description_content_type="text/markdown",
    keywords="python flask jinja flowbite htmx",
    url="https://github.com/schaveyt/jinjax-flowbite",
    author="Todd Schavey",
    author_email="schaveyt@gmail.com",
    license="MIT",
    python_requires=">=3.11",
    install_requires=requirements_txt,
    packages=find_namespace_packages(where="src"),
    package_dir={"": "src"},
    package_data={
        "jinjax-flowbite.components": ["*.jinja"]
    },
    classifiers=[],
    include_package_data=True,
)

