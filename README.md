# barhood

find bars your friends like


## Development Workflow

### Backend
lives in uppercase "Barhood" directory
* Python 3.5
* dependencies use virtual environment, "venv"
    * to activate: "source venv/bin/activate"
    * to install a new package: "pip install [package_name]"
    * to update dependencies: "pip freeze > requirements.txt"
        * required packages live in "requirements.txt"
    * to install dependencies: "pip install -r requirements.txt"
    * helpful guide: http://docs.python-guide.org/en/latest/dev/virtualenvs/

### Frontend
lives in uppercase "Public" directory
* Node 4.2.6
* dependencies in package.json file
    * install running "npm install"
    * run dev server with "npm start"
    * currently frontend app is a boilerplate hello-world courtesy of create-react-app cli

