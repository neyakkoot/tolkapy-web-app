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

    cards_html = '<div class="grid grid-cols-1 gap-4">' # vertical stack of cards
    
    for index, each_rule in enumerate(meymayakkam_rules, start=1):
        result_value = each_rule(query)

        cards_html += f"""
        <div class="group flex items-center justify-between p-4 mb-2 bg-white/[0.03] hover:bg-white/[0.06] border-b border-slate-800/50 transition-all duration-300">
            
            <div class="flex flex-col">
                <span class="text-slate-400 text-sm font-medium tracking-tight">
                    மெய்ம்மயக்கம் {index}
                </span>
            </div>

            <div class="text-right">
                <span class="text-white text-2xl font-light tracking-wide group-hover:text-blue-400 transition-colors duration-500">
                    {result_value}
                </span>
            </div>
        </div>
        """
    
    cards_html += "</div>"

    print(cards_html)
    return jsonify({
        "status": "success",
        "message": f"You searched for: {query}",
        "data": cards_html
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
