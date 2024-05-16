from flask import Flask, render_template_string
import markdown

app = Flask(__name__)

@app.route('/')
def display_markdown():
    md_text = """
    **"Let's delve deeper into a topic or explore a new subject. Please provide a question or topic you'd like to discuss, and I'll be ready to provide insights, explanations, or engage in a meaningful conversation with you."**

    responses now using markdown for text.

    **prompt: display markdown tutorial walkthrough"**
    """
    html_content = markdown.markdown(md_text)
    return render_template_string(html_content)

if __name__ == '__main__':
    app.run(debug=True, port=5001)  # You can choose any other free port

