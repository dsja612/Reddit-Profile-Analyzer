How to run backend:

1. Run `cd backend`
2. Run `python -m venv venv`
3. Activate venv through `venv\Scripts\Activate.ps1`
4. Install dependencies from requirements.txt using `pip install -r requirements.txt`
3. `cd src` and run `uvicorn main:app --reload`