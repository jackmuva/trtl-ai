# Trtl-AI
This service is used to brainstorm ideas for email series, when inputting a website.

TrtlAI with crawl through the website map and extract all relevant data. The data will be fed into
an LLM model to help brainstorm email series ideas.

## Setting up project
* if a venv is not created: `python -m venv venv`
* `source venv/bin/activate`
* use `pip install -r requirements.txt`
* when adding new packages use `pipreqs ./ --force` to rewrite requirements.txt
* use `fastapi dev main.py` to run dev server

