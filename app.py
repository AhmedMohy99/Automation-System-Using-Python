from flask import Flask, render_template, request, jsonify
import os

app = Flask(__name__)

# Ensure templates folder path is correct for Vercel
base_dir = os.path.dirname(os.path.abspath(__file__))
app.template_folder = os.path.join(base_dir, 'templates')

@app.route('/')
def index():
    return render_template('automation_ui.html')

@app.route('/run-automation', methods=['POST'])
def run_auto():
    topic = request.json.get('topic')
    # Link to the automation logic here
    # In a real scenario, you'd call the generate_marketing_bundle function
    return jsonify({
        "status": "success",
        "message": f"Automation started for {topic}. Check the vault!",
        "preview": "Blog: How to scale... IG: 🚀 Ready to grow? #Marketing"
    })

if __name__ == '__main__':
    app.run(debug=True)
