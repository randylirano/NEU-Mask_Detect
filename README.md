# project-mask_detect
Summary: The aim of this project is to explore the application of Artificial Intelligence (AI) in image classification. The team will build a web application using a Covid-19 facemask dataset. The dataset will have two distinct labels (with_mask vs without_mask). The model will be trained using the dataset to detect if someone entering some premises is properly using their face masks.

Follow us on Instagram: https://www.instagram.com/kati.maskdetect/

Our project website: https://kati-test.herokuapp.com/home
*****************************************************************

Project Presentation: https://docs.google.com/presentation/d/1sTcCYiBKFWlrjT4pddgZiX_TwxC-wOCFopDVOP0r5Ho/edit#slide=id.p

Our Trello task management page: https://trello.com/b/Wj24hcVg/facemask-project

Communiation plan location: project-mask_detect/docs/communiation_plan.pdf

Python model file is in the main directory: model.py

It is the main product of the Python team

Demo video link: https://www.youtube.com/watch?v=uYRLCniw4dk

A Jupyter Notebook can be found in project-mask_detect/facemask_detection_model_demo.ipynb

It serves as the file for demonstration purpose

Python test files can be found in project-mask_detect/test

Documentation files can be found in project-mask_detect/docs

Dataset files can be fount in project-mask_detect/data
*****************************************************************

### Primary customer representative:

Randy Lirano (lirano.r@northeastern.edu)

### Secondary customer representative:

Aushee Khamesra (khamesra.a@northeastern.edu)

### Scrum master:

Zihao Qiu (qiu.ziha@northeastern.edu)

### Team Member Names and IDs:

Web Development Team:

* Randy Lirano (Khoury ID: randylirano)

* Julia Rakas (Khoury ID: jrakas)

* Shruthi Raghuraman (Khoury ID: sraghuraman1)

* Jinyang Zheng (Khoury ID: pagenotfound91)

Python Development Team

* Zihao Qiu (Khoury ID: whatcat)

* Aushee Khamesra (Khoury ID: akhamesra)

* Yuqi Tao (Khoury ID: gavintao1219)

* Robert Dragomir (Khoury ID: rgdragomir)

### How to deploy locally

1. Clone our repo
`git clone `https://github.ccs.neu.edu/2021SPCS5500SB/project-mask_detect
2. Go into main repo folder
`cd project-mask_detect`
##### Start Backend

1. Install all dependencies (make sure you have pip or pip3 installed)
`pip3 install -r requirements.txt`
2. Start flask backend
`env FLASK_APP=api.py FLASK_ENV=development flask run`

##### Start Frontend

1. Open a new terminal window and navigate to project-mask_detect folder. On mac `command + t` buttons will open a new terminal window.
2. `cd frontend/face-mask-ui/`
3. Install package.json
`npm install`
4. Run angular app
`ng serve --open`
5. App should be running on http://localhost:4200/home

### How to Run Demo Notebook

1. Install Jupyter Notebook on your local machine. To install, put `pip install notebook` in your on Command Prompt (Windows)/Terminal (Mac). 
2. In Command Prompt(Windows)/Terminal(Mac), type "jupyter notebook" to launch the notebook. It should be opened in the browser. 
3. Find the location of the demo jupyter notebook, and run the cells one by one.

### How to run model.py

1. Please make sure you have Python installed on your computer, version 3.0+ is recommended. 
2. If you also have an IDE installed, you can run the py file in IDE, or you can run it on Command Prompt(Windows)/Terminal(Mac).
3. To run it on terminal, first navigate to the directory.
4. Type `python model.py` on your terminal.
5. It will execute the Python code. 
