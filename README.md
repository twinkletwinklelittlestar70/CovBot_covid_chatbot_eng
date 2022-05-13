# CovBot covid chatbot

CovBot is a Q&A chatbot about covid providing functions like QA, fast diagnosis and fake news detection. This repo is the engineering part of the whole project and for algorithms and models please refer to https://github.com/twinkletwinklelittlestar70/CovBot.

# Run back-end code

The final compiled and build product of the front-end code has been placed in the static directory of the back-end. If you just want to run the system without modification, you only need to run the back-end code. 

## install python
https://www.python.org/downloads/

Best practice is to create a isolate env for the project, but it's not mandatory.

The recommended python version is 3.7.11.

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
