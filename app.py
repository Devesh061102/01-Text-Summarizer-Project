from flask import Flask, render_template, request
from TextSummarizer.pipeline.prediction import PredictionPipeline
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/summarize', methods=['POST'])
def summarize():
    input_text = request.form['input_text']
    
    obj = PredictionPipeline()
    summary = obj.predict(input_text)

    word_count = len(summary.split())
    return render_template('summary.html', summary=summary,word_count=word_count)

if __name__ == '__main__':
    app.run(debug=True)
