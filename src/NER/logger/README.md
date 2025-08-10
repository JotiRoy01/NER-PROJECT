## Your last terminal command was:
```bash
python src/NER/exception/__init__.py
```
### The error is `ModuleNotFoundError: No module named 'src'`
### Solution:
In Git Bash on Windows, set the PYTHONPATH to your project root before running the script:
```bash 
export PYTHONPATH=$(pwd)
python src/NER/exception/__init__.py
```