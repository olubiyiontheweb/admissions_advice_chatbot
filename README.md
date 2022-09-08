# admissions_advice_chatbot
An interactive chatbot that utilises published information from a university's website to chat about their courses, developed using the RASA Conversational AI framework. https://rasa.com/open-source/

#### Execute the Web scraping tool by following the steps below

> install python 3.8 (if it's not already installed)

> pip install -r .\requirements.txt

> python .\scraping_operations.py

#### Execute the Admissions chatbot by following the steps below

> python -m venv venv

> Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser (skip except you're running on windows)

> venv\scripts\activate

> pip install -r requirements.txt

> cd admissions_chatbot

> python ../web_scraping_tool/scraping_operations.py

> rasa train nlu --> rasa shell nlu (skip this line, you only need this if you plan to debug on the terminal)

> rasa train

> rasa telemetry disable (disable reporting anonymous usage)

> rasa run -m models --enable-api --cors * (run this on another terminal) or rasa nlu shell (use this for tests)

> rasa run actions (run this on another terminal)

> python -m http.server --directory ./http_webserver/ (run this on another terminal)