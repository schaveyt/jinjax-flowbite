# jinjax-flowbite <!-- omit in toc -->

HTML Component Library based on Flowbite Components and JinjaX python package

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


### 2.1. Build Python Package (Wheel)

~~~sh
.\venv\Scripts\activate
python .\setup.py bdist_wheel
~~~
