# Metis covid chatbot

A Q&A chatbot about covid providing functions like sentiment analysis, fast diagnosis and fake news detection
# Run front-end code

## install node.js
https://nodejs.org/en/

## install dependencies of the project
``` bash
cd frontend

npm install
```

## Start to develop
``` bash
npm run serve
# Open http://localhost:8080 to see the UI
# This development method supports code hot update
```

## Deploy current frontend code to backend
``` bash
npm run build
# After this command, there should be a new folder `./backend/static` generated and some fe files inside.
```

## See more about Vue and Element
Vue 3.0: https://v3.vuejs.org/
ElementPlus (a Vue 3 based component library): https://element-plus.org/en-US/


# Run back-end code

## install python
https://www.python.org/downloads/

Best practice is to create a isolate env for the project, but it's not mandatory.

## install dependencies of the project
``` bash
pip install -r requirements.txt
```

## Start to develop
``` bash
export FLASK_APP=app # This command for bash. More: https://dormousehole.readthedocs.io/en/latest/quickstart.html

flask run
# Open http://127.0.0.1:5000/ to access the system with UI
```

## See more about Flask
Flask 2.0 https://flask.palletsprojects.com/en/2.0.x/