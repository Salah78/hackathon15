from saagieapi import SaagieApi
from flask import Flask, render_template
import json
import numpy as np


app = Flask(__name__)

# Api Connection
saagieapi = SaagieApi.easy_connect(url_saagie_platform="https://demo-workspace.a4.saagie.io/projects/platform/2/",
    user="ESTIAM_G15_bigue.diaw",
    password="Admin-1234")

# road project defined
@app.route("/get-project")
def projet():
    project = saagieapi.projects.list()
   
    return(project)


# Feature copy/past    
@app.route("/copy-paste")
def projet2():
    saagieapi = SaagieApi.easy_connect(url_saagie_platform="https://demo-workspace.a4.saagie.io/projects/platform/2/",
    user="ESTIAM_G15_bigue.diaw",
    password="Admin-1234")
    
    get_list = saagieapi.projects.list()
    print(get_list["projects"])
    projet_name = get_list["projects"]
    list_project = [d['name'] for d in projet_name]
    print(list_project)
    description_value = [d['description'] for d in projet_name]
    print(description_value)
    name_project = list_project[0]
    description = description_value[0]
    id_project = saagieapi.projects.get_id(name_project)
    print(id_project)
    project_info = saagieapi.projects.get_info(id_project)
    print(project_info)
    project_dict = saagieapi.projects.create(name="copy" + " " + name_project,
                                      group="estiam_g15_hackaton",
                                      role='Manager',
                                      description=description)
    
    return(get_list)

@app.route("/backup")
def project3():
    #function recover/backup
    get_list = saagieapi.projects.list()
    projet_name = get_list["projects"]
    list_project = [d['name'] for d in projet_name]
    description_value = [d['description'] for d in projet_name]
    name_project = list_project[0]
    description = description_value[0]
    id_project = saagieapi.projects.get_id(name_project)
    project_info = saagieapi.projects.get_info(id_project)
    # Save
    np.save("recovery"+ name_project, project_info)
    # Load
    read_dictionary = np.load("recovery"+ name_project,allow_pickle='TRUE').item()

    return(get_list)

# @app.route("/reqid")
# def project4():
#     get_list = saagieapi.projects.list()
#     projet_name = get_list["projects"]
#     list_project = [d['name'] for d in projet_name]
#     name_project = list_project[0]
#     id_project = saagieapi.projects.get_id(name_project)
#     return(id_project)

# Function tree structure of project contains
@app.route("/audit")
def index():
    get_list = saagieapi.projects.list()
    print(get_list["projects"])
    projet_name = get_list["projects"]
    list_project = [d['name'] for d in projet_name]
    print(list_project)
    name_project = list_project[0]
    name_project1 = list_project[1]

    id_project = saagieapi.projects.get_id(name_project)
    print(id_project)
    project_info = saagieapi.projects.get_info(id_project)
    print(project_info)
    projectName1 = name_project
    projectName2 = name_project1

    req1 = saagieapi.projects.get_info("435ca92e-c2e6-45a0-a851-61dfb86f74c8")
    data1 = json.dumps(req1)
    req2 = saagieapi.projects.get_info("1fc6f5e5-001d-4722-86e0-6dcfd23fe479")
    data2 = json.dumps(req2)
    return render_template('index.html', data1=data1, data2=data2, projectName1=projectName1, projectName2=projectName2)





























if __name__ == "__main__":
    app.run(debug=True)
    print("api start !")