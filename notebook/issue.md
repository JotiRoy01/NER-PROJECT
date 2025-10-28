## Problem with the pip
* ModuleNotFoundError: No module named 'pip'
Explanation:
Your Python environment is missing pip, so you cannot install the datasets package.
1. Reactivate your virtual environment (if using one)
```bash
source env_NER/Scripts/activate
```
2. Reinstall pip in your environment:
```bash
python -m ensurepip --upgrade
```
3. Upgrade pip (optional but recommended):
```bash
python -m pip install --upgrade pip
```
