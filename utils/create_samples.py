from reportlab.pdfgen import canvas
import os

def create_pdf(filename, content):
    path = os.path.join("data/resumes", filename)
    c = canvas.Canvas(path)
    text_obj = c.beginText(50, 800)
    text_obj.setFont("Helvetica", 10)
    
    for line in content.split('\n'):
        text_obj.textLine(line)
        
    c.drawText(text_obj)
    c.save()
    print(f"Created {path}")

# Sample 1: Python Developer
python_dev = """
John Doe
Python Backend Developer

Skills: Python, Django, Flask, SQL, Docker, AWS, Git, REST APIs
Experience:
- Senior Developer at TechCorp (3 years)
- Built scalable microservices using Django and PostgreSQL.
- Optimized database queries, reducing latency by 40%.
- Deployed applications on AWS using Docker containers.

Education: B.S. in Computer Science
"""

# Sample 2: Data Scientist
data_scientist = """
Jane Smith
Data Scientist

Skills: Python, Machine Learning, Deep Learning, NLP, Pandas, NumPy, Scikit-Learn, TensorFlow, SQL
Experience:
- Data Scientist at AI Labs (2 years)
- Developed predictive models for customer churn using Random Forest and XGBoost.
- Implemented NLP pipelines for sentiment analysis on social media data.
- Visualized complex datasets using Tableau and Matplotlib.

Education: M.S. in Data Science
"""

# Sample 3: Web Developer (Frontend focus)
web_dev = """
Alice Johnson
Frontend Developer

Skills: JavaScript, React, Angular, HTML, CSS, Git, Webpack
Experience:
- Frontend Engineer at WebWorks (2 years)
- Built responsive user interfaces using React and Redux.
- Collaborated with UI/UX designers to implement pixel-perfect designs.
- Improved web performance and SEO metrics.

Education: B.A. in Web Design
"""

if __name__ == "__main__":
    if not os.path.exists("data/resumes"):
        os.makedirs("data/resumes")
    
    create_pdf("python_dev_resume.pdf", python_dev)
    create_pdf("data_scientist_resume.pdf", data_scientist)
    create_pdf("web_dev_resume.pdf", web_dev)
