# Contributing

## 1. Setup Development Environment

### 1.1. Toolchain

- Install python 3.11 or newer

### 1.2. VSCode Extensions

- Pylance: `ms-python.vscode-pylance`
- Tailwind CSS Intellisense: `bradlc.vscode-tailwindcss`
- Jinja: `wholroyd.jinja`
- Jinja2 Snippet Kit: `wyattferguson.jinja2-snippet-kit`
- BetterJinja: `samuelcolvin.jinjahtml`
- Markdown All in One: `yzhang.markdown-all-in-one`
- markdownlint: `davidanson.vscode-markdownlint`

### 1.3. Python Library Dependencies

~~~sh
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
~~~


## 2.1. Publishing to PyPi

1. Install twine

    ~~~sh
    .\venv\Scripts\activate
    pip install twine # if you haven't already
    ~~~

1. Ensure you have your ~/.pypirc populated

    ~~~sh
    [pypi]
    username = __token__
    password = pypi-**********
    ~~~

1. Publish to PyPI

    ~~~sh
    py -m twine upload --repository pypi dist/* --verbose
    ~~~
