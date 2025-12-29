from flask import Flask, request, render_template, jsonify 
from tamilrulepy.meymayakkam import meymayakkam1,meymayakkam2,meymayakkam3,meymayakkam4,meymayakkam5,meymayakkam6,meymayakkam7,meymayakkam8,meymayakkam9,meymayakkam10,meymayakkam11,meymayakkam12,meymayakkam13,meymayakkam14,meymayakkam15,meymayakkam16,meymayakkam17,meymayakkam18


meymayakkam_rules = [
    meymayakkam1,
    meymayakkam2,
    meymayakkam3,
    meymayakkam4,
    meymayakkam5,
    meymayakkam6,
    meymayakkam7,
    meymayakkam8,
    meymayakkam9,
    meymayakkam10,
    meymayakkam11,
    meymayakkam12,
    meymayakkam13,
    meymayakkam14,
    meymayakkam15,
    meymayakkam16,
    meymayakkam17,
    meymayakkam18
]

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search')
def search():
    query = request.args.get('q')

    return_data = []
    
    for index,each_rule in enumerate(meymayakkam_rules):
    
        return_data.append(f"{index} ==> {each_rule(query)}")

    print(return_data)
    return jsonify({
        "status": "success",
        "message": f"You searched for: {query}",
        "data": return_data
    })


@app.route('/analyze')
def analyze():
    query = request.args.get('q')
    return f"<h1>Analysis Mode</h1><p>Analyzing data for: {query}</p>"

@app.route('/generate')
def generate():
    query = request.args.get('q')
    return f"<h1>Generation Mode</h1><p>Creating content for: {query}</p>"

if __name__ == '__main__':
    app.run(debug=True)