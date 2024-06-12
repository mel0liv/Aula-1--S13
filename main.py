-----------------------No main.py:

def greet(name): 

return "Hello, " + name + "!" 



if __name__ == "__main__": 

print(greet("World!"))






-----------------No .github/workflows/python-app.yml

name: Python application
on: [push]
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v2
    - name: Set up Python 3.x
      uses: actions/setup-python@v2
      with:
        python-version: '3.x'
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install flake8
    - name: Lint with flake8
      run: |
        flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics
    - name: Run script
      run: python main.py
