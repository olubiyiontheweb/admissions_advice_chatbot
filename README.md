# admissions_advice_chatbot
An interactive chatbot that utilises published information from a university's website to chat about their courses, developed using the RASA Conversational AI framework. https://rasa.com/open-source/

#### Execute the Web scraping tool by following the steps below

> install python 3.8 (if it's not already installed)

> pip install -r .\requirements.txt

> python .\scraping_operations.py

#### Execute the Admissions chatbot by following the steps below

> python -m venv venv

> venv\scripts\activate

> pip install -r requirements.txt

> rasa train nlu

> rasa train

> rasa telemetry disable

> rasa shell nlu

> rasa run --enable-api --cors *

> rasa run actions (run this on another terminal)

> python -m http.server --directory http_webserver