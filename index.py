
from flask import Flask 

app = Flask(__name__)

@app.route("/") 
def page_index():
    return "Главная страничка" 

print(17)
app.run(port="9999")
