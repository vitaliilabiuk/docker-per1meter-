from flask import Flask
from flask import render_template
import json
import os

app = Flask(__name__)

@app.route("/")
def landing():
    return render_template('landing.html')

@app.route("/northern-cyprus")
def northern_cyprus_page():
    with open('static/northern-cyprus/Total New_2023 const NC_pr.json', 'r') as json_file:
        json_data = json.load(json_file)
    img_directory = 'static/northern-cyprus/images/'
    img_dict = {}
    # Walk through the directory and its subdirectories
    for root, dirs, files in os.walk(img_directory):
        # Create a list of files with jpg endings in the current directory
        jpg_files = [file for file in files if file.endswith('.jpg')]
        # Add the list of jpg files to the dictionary with the directory name as the key
        img_dict[root] = jpg_files
        #app.logger.info(root)
    return render_template('northern-cyprus.html',
                           data = {'prop': json_data,
                                   'img': img_dict
                                  }
                           )

@app.route("/northern-cyprus/anal/<int:object_id>")
def object_anal_page(object_id):
    print('Loading object', object_id)
    with open('static/northern-cyprus/Total New_2023 const NC_pr.json', 'r') as json_file:
        json_data = json.load(json_file)
    
    # Search for the dictionary with the specified ID
    found_dict = next((item for item in json_data if item["ID"] == object_id), None)

    return render_template('northern-cyprus-object.html',
                           data = {'object': found_dict}
                           )

@app.route("/northern-cyprus/pics/<int:object_id>")
def object_pictures_page(object_id):
    print('Loading object', object_id)
    img_directory = 'static/northern-cyprus/images/' + str(object_id)
    # Walk through the directory
    for files in os.walk(img_directory):
        # Create a list of files with jpg endings in the current directory
        jpg_files = [file for file in files]
        app.logger.info(jpg_files[0])
    return render_template('northern-cyprus-pictures.html',
                           data = {'img': jpg_files[2],
                                   'path': jpg_files[0],
                                   'object_id': object_id
                                  }
                           )
