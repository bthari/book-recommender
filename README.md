# book-recommender

## Installation Guide
Set up python environment:
```
pip install virtualenv
python3 -m venv env
source env/bin/ativate
```

Install Depedencies and Run Django:
```
pip install -r requirements.txt ##run when there's an update
python manage.py makemigrations ##only on first run
python manage.py migrate ##run when there's an update
python manage.py runserver
```

If theres error about `Resource stopwords not found.` stop the program and run `python3` on your terminal:
```
import nltk
nltk.download('stopwords')
```
rerun the program with `python manage.py runserver`

## User manual
#### Search by tittle:
- Click the find button on the right top
- Input your keywords
- And tadaaa!

#### Search by tittle:
Unfortunately the link isn't put yet on the web, so go to the link: `https://localhost:8000/retrieve/search-desc/`
- Input your keywords
- And you got it!
