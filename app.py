from urllib import response

from flask import Flask, make_response, render_template, request

import os
from werkzeug.utils import secure_filename

app = Flask(__name__)

UPLOAD_FOLDER = os.path.join(app.root_path, 'static', 'uploads')

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/index.html')
def index():
    return render_template('index.html')

@app.route('/resume-info')
def resume_info():
    return render_template('resume_info.html')

@app.route('/cv-info')
def cv_info():
    return render_template('cv_info.html')

@app.route('/chronological.html')
def chronological():
    return render_template('chronological.html')

@app.route('/generate/chronological', methods=['POST'])
def generate_chronological():

    data = request.form
    
    # ============================
    # PHOTO UPLOAD CODE ADD HERE
    # ============================

    photo = request.files.get('photo')

    filename = data.get("existing_photo", "")

    if photo and photo.filename != "":

        filename = secure_filename(photo.filename)

        filepath = os.path.join(
            app.config['UPLOAD_FOLDER'],
            filename
        )

        photo.save(filepath)

    # ----------------------------
    # BASIC DETAILS
    # ----------------------------
    basic = {
        "name": data.get("name"),
        "email": data.get("email"),
        "phone": data.get("phone"),
        "address": data.get("address"),
        "linkedin": data.get("linkedin"),
        "github": data.get("github"),
        "summary": data.get("summary")
    }

    # ----------------------------
    # EDUCATION
    # ----------------------------
    education = []
    for i in range(1, 10):
        if data.get(f"degree{i}"):
            education.append({
                "degree": data.get(f"degree{i}"),
                "college": data.get(f"college{i}"),
                "year": data.get(f"grad_year{i}"),
                "percentage": data.get(f"percentage{i}"),
                "duration": data.get(f"edu_duration{i}")
            })

    # ----------------------------
    # EXPERIENCE (IMPORTANT)
    # ----------------------------
    experience = []
    for i in range(1, 10):
        if data.get(f"job_title{i}"):
            experience.append({
                "job": data.get(f"job_title{i}"),
                "company": data.get(f"company{i}"),
                "duration": data.get(f"duration{i}"),
                "description": data.get(f"description{i}")
            })

    # 🔥 Reverse for latest first (Chronological style)
    experience = experience[::-1]

    # ----------------------------
    # SKILLS
    # ----------------------------
    skills = {
        "technical": data.get("skills1"),
        "soft": data.get("skills_soft1")
    }

    # ----------------------------
    # PROJECTS
    # ----------------------------
    projects = []
    for i in range(1, 10):
        if data.get(f"project{i}"):
            projects.append({
                "title": data.get(f"project{i}"),
                "desc": data.get(f"project_desc{i}"),
                "tech": data.get(f"project_tech{i}"),
                "link": data.get(f"project_link{i}")
            })

    # ----------------------------
    # CERTIFICATIONS
    # ----------------------------
    certifications = []
    for i in range(1, 10):
        if data.get(f"certification{i}"):
            certifications.append({
                "name": data.get(f"certification{i}"),
                "org": data.get(f"cert_org{i}"),
                "date": data.get(f"cert_date{i}")
            })

    # ----------------------------
    # EXTRA
    # ----------------------------
    achievements = data.get("achievements")
    hobbies = data.get("hobbies")

    return render_template('chronological_output.html',
        basic=basic,
        education=education,
        experience=experience,
        skills=skills,
        projects=projects,
        certifications=certifications,
        achievements=achievements,
        hobbies=hobbies,
        photo=filename
    )
    
@app.route('/edit/chronological', methods=['POST'])
def edit_chronological():
    data = request.form
    return render_template('chronological.html', data=data)
    

@app.route('/functional.html')
def functional():
    return render_template('functional.html')

@app.route('/generate/functional', methods=['POST'])
def generate_functional():
    
    data = request.form
    
    # ============================
    # PHOTO UPLOAD CODE ADD HERE
    # ============================

    photo = request.files.get('photo')

    filename = data.get("existing_photo", "")

    if photo and photo.filename != "":

        filename = secure_filename(photo.filename)

        filepath = os.path.join(
            app.config['UPLOAD_FOLDER'],
            filename
        )

        photo.save(filepath)


    # ===== BASIC DETAILS =====
    basic = {
        "name": data.get("name"),
        "email": data.get("email"),
        "phone": data.get("phone"),
        "address": data.get("address"),
        "linkedin": data.get("linkedin"),
        "github": data.get("github"),
        "summary": data.get("summary")
    }

    # ===== SKILLS =====
    skills = {
        "technical": data.get("skills"),
        "soft": data.get("skills_soft"),
        "problem": data.get("skills_problem")
    }

    # ===== PROJECTS =====
    projects = []
    for i in range(1, 20):
        title = data.get(f'project{i}')
        if title:
            projects.append({
                "title": title,
                "language": data.get(f'language{i}'),
                "desc": data.get(f'project_desc{i}'),
                "link": data.get(f'project_link{i}')
            })

    # ===== EDUCATION =====
    education = []
    for i in range(1, 20):
        degree = data.get(f'degree{i}')
        if degree:
            education.append({
                "degree": degree,
                "college": data.get(f'college{i}'),
                "year": data.get(f'grad_year{i}'),
                "percentage": data.get(f'percentage{i}'),
                "duration": data.get(f'edu_duration{i}')
            })

    # ===== CERTIFICATIONS =====
    certifications = []
    for i in range(1, 20):
        cert = data.get(f'certi_name{i}')
        if cert:
            certifications.append({
                "name": cert,
                "org": data.get(f'cert_org{i}'),
                "date": data.get(f'cert_date{i}')
            })

    # ===== OTHER =====
    achievements = data.get("achievements")
    hobbies = data.get("hobbies")

    return render_template('functional_output.html',
        basic=basic,
        skills=skills,
        projects=projects,
        education=education,
        certifications=certifications,
        achievements=achievements,
        hobbies=hobbies,
        photo=filename
    )

@app.route('/edit/functional', methods=['POST'])
def edit_functional():
    data = request.form
    return render_template('functional.html', data=data)


@app.route('/combinational.html')
def combination():
    return render_template('combinational.html')

@app.route('/generate/combinational', methods=['POST'])
def generate_combinational():

    data = request.form
    
    # ============================
    # PHOTO UPLOAD CODE ADD HERE
    # ============================

    photo = request.files.get('photo')

    filename = data.get("existing_photo", "")

    if photo and photo.filename != "":

        filename = secure_filename(photo.filename)

        filepath = os.path.join(
            app.config['UPLOAD_FOLDER'],
            filename
        )

        photo.save(filepath)


    # 🔹 Basic Info
    basic = {
        "name": data.get("name"),
        "email": data.get("email"),
        "phone": data.get("phone"),
        "address": data.get("address"),
        "linkedin": data.get("linkedin"),
        "github": data.get("github"),
        "summary": data.get("summary")
    }

    # 🔹 Skills
    skills = {
        "technical": data.get("skills"),
        "soft": data.get("skills_soft"),
        "problem": data.get("skills_problem")
    }

    # 🔹 Experience
    experiences = []
    for i in range(1, 10):
        job = data.get(f'job_title{i}')
        if job:
            experiences.append({
                "job": job,
                "company": data.get(f'company{i}'),
                "duration": data.get(f'duration{i}'),
                "description": data.get(f'description{i}')
            })

    # 🔹 Projects
    projects = []
    for i in range(1, 10):
        project = data.get(f'project{i}')
        if project:
            projects.append({
                "title": project,
                "language": data.get(f'language{i}'),
                "description": data.get(f'project_desc{i}'),
                "link": data.get(f'project_link{i}')
            })

    # 🔹 Education
    education = []
    for i in range(1, 10):
        degree = data.get(f'degree{i}')
        if degree:
            education.append({
                "degree": degree,
                "college": data.get(f'college{i}'),
                "year": data.get(f'grad_year{i}'),
                "percentage": data.get(f'percentage{i}'),
                "duration": data.get(f'edu_duration{i}')
            })

    # 🔹 Certifications
    certifications = []
    for i in range(1, 10):
        cert = data.get(f'certification{i}')
        if cert:
            certifications.append({
                "name": cert,
                "org": data.get(f'cert_org{i}'),
                "date": data.get(f'cert_date{i}')
            })

    return render_template('combinational_output.html',
        basic=basic,
        skills=skills,
        experiences=experiences,
        projects=projects,
        education=education,
        certifications=certifications,
        achievements=data.get("achievements"),
        hobbies=data.get("hobbies"),
        photo=filename
    )

@app.route('/edit/combinational', methods=['POST'])
def edit_combinational():
    data = request.form
    return render_template('combinational.html', data=data) 

@app.route('/freshers.html')
def freshers():
    return render_template('freshers.html')

@app.route('/generate/freshers', methods=['POST'])
def generate_fresher():
    
    data = request.form
    
    # ============================
    # PHOTO UPLOAD CODE ADD HERE
    # ============================

    photo = request.files.get('photo')

    filename = data.get("existing_photo", "")

    if photo and photo.filename != "":

        filename = secure_filename(photo.filename)

        filepath = os.path.join(
            app.config['UPLOAD_FOLDER'],
            filename
        )

        photo.save(filepath)


    # Basic Info
    basic = {
        "name": data.get("name"),
        "email": data.get("email"),
        "phone": data.get("phone"),
        "address": data.get("address"),
        "linkedin": data.get("linkedin"),
        "github": data.get("github"),
        "objective": data.get("objective")
    }

    # Education (multiple)
    education = []
    for i in range(1, 10):
        degree = data.get(f"degree{i}")
        if degree:
            education.append({
                "degree": degree,
                "college": data.get(f"college{i}"),
                "year": data.get(f"grad_year{i}"),
                "percentage": data.get(f"percentage{i}"),
                "duration": data.get(f"edu_duration{i}")
            })

    # Projects
    projects = []
    for i in range(1, 10):
        title = data.get(f"proj_title{i}")
        if title:
            projects.append({
                "title": title,
                "desc": data.get(f"proj_desc{i}"),
                "tech": data.get(f"proj_tech{i}"),
                "link": data.get(f"proj_link{i}")
            })

    # Internships
    internships = []
    for i in range(1, 10):
        title = data.get(f"intern_title{i}")
        if title:
            internships.append({
                "title": title,
                "org": data.get(f"intern_org{i}"),
                "duration": data.get(f"intern_duration{i}"),
                "desc": data.get(f"intern_desc{i}")
            })

    # Certifications
    certifications = []
    for i in range(1, 10):
        name = data.get(f"cert_name{i}")
        if name:
            certifications.append({
                "name": name,
                "org": data.get(f"cert_org{i}"),
                "date": data.get(f"cert_date{i}")
            })

    return render_template('freshers_output.html',
        basic=basic,
        education=education,
        projects=projects,
        internships=internships,
        certifications=certifications,
        technical=data.get("technical_skills"),
        soft=data.get("soft_skills"),
        achievements=data.get("ach_desc1"),
        hobbies=data.get("hobbies"),
        photo=filename
    )

@app.route('/edit/freshers', methods=['POST'])
def edit_freshers():
    data = request.form
    return render_template('freshers.html', data=data)

@app.route('/cv.html')
def cv():
    return render_template('cv.html')

@app.route('/generate/cv', methods=['POST'])
def generate_cv():
    
    data = request.form
    
    # ============================
    # PHOTO UPLOAD CODE ADD HERE
    # ============================

    photo = request.files.get('photo')

    filename = data.get("existing_photo", "")

    if photo and photo.filename != "":

        filename = secure_filename(photo.filename)

        filepath = os.path.join(
            app.config['UPLOAD_FOLDER'],
            filename
        )

        photo.save(filepath)


    # 🔹 Personal Info
    personal = {
        "name": data.get("name"),
        "email": data.get("email"),
        "phone": data.get("phone"),
        "address": data.get("address"),
        "linkedin": data.get("linkedin"),
        "github": data.get("github"),
        "objective": data.get("objective"),
    }

    # 🔹 Education
    education = []
    for i in range(1, 20):
        degree = data.get(f"degree{i}")
        if degree:
            education.append({
                "degree": degree,
                "college": data.get(f"college{i}"),
                "year": data.get(f"grad_year{i}"),
                "percentage": data.get(f"percentage{i}"),
                "duration": data.get(f"edu_duration{i}")
            })

    # 🔹 Projects
    projects = []
    for i in range(1, 20):
        project = data.get(f"project{i}")
        if project:
            projects.append({
                "title": project,
                "desc": data.get(f"project_desc{i}"),
                "tech": data.get(f"project_tech{i}"),
                "link": data.get(f"project_link{i}")
            })

    # 🔹 Experience
    experience = []
    for i in range(1, 20):
        job = data.get(f"job_title{i}")
        if job:
            experience.append({
                "job": job,
                "company": data.get(f"company{i}"),
                "duration": data.get(f"duration{i}"),
                "desc": data.get(f"description{i}")
            })

    # 🔹 Certifications
    certifications = []
    for i in range(1, 20):
        cert = data.get(f"certification{i}")
        if cert:
            certifications.append({
                "name": cert,
                "org": data.get(f"cert_org{i}"),
                "date": data.get(f"cert_date{i}")
            })

    # 🔹 Other sections
    cv_data = {
        "personal": personal,
        "education": education,
        "projects": projects,
        "experience": experience,
        "certifications": certifications,
        "research": data.get("research"),
        "publications": data.get("publications"),
        "skills": data.get("skills1"),
        "soft_skills": data.get("skills_soft1"),
        "languages": data.get("languages"),
        "awards": data.get("award1"),
        "achievements": data.get("achievement1"),
        "conferences": data.get("conferences"),
        "references": data.get("references"),
        "photo":filename
    }

    return render_template("cv_output.html", cv=cv_data)

@app.route('/edit/cv', methods=['POST'])
def edit_cv():
    data = request.form
    return render_template('cv.html', data=data)
    
import os

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 5000))
    )