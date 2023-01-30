from flask import Flask
from rdkit import Chem

app = Flask(__name__)

@app.route('/')
def hello_world():
    return Chem.MolToMolBlock(Chem.MolFromSmiles('C1CCC1'))
    #return 'Hello, World!'
