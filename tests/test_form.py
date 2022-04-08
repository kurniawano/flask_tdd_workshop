import json
from tests import client
import os

def test_submit_form(client):
    # test if you can submit a form
    # you should get HTTP response 200
    # for both get and post
    pass

def test_json_file(client):
    # first remove all the existing json file
    # test if json file is created when no file present
    # load json file and see if entry is correct
    pass
  
def test_get_request(client):
    # test if you are redirected to Homepage 
    # if you try to access /your-url on GET request
    pass
