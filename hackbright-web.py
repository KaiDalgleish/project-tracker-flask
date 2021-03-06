from flask import Flask, request, render_template

import hackbright

app = Flask(__name__)

@app.route("/student")
def get_student():
    """Show information about a student."""

    github = request.args.get('github', 'jhacks')
    first, last, github = hackbright.get_student_by_github(github)
    projects = hackbright.get_grade_by_student(first)
    html = render_template("student_info.html",
                           first=first,
                           last=last,
                           github=github,
                           projects=projects
                           )
    return html
    
@app.route("/student-search")
def get_student_form():
    """Show form for searching for a student."""

    return render_template("student_search.html")

@app.route("/student-add")
def student_add_form():
    """Show form for adding a student."""

    return render_template("student_add.html")

@app.route("/student-added", methods=['POST'])
def student_add():
    """Add a student."""
    first_name = request.form.get('first_name')
    last_name = request.form.get('last_name')
    github = request.form.get('github')
    hackbright.make_new_student(first_name, last_name, github)
    
    html = render_template("student_info.html",
                           first=first_name,
                           last=last_name,
                           github=github)
    return html

@app.route("/project")
def show_project():
    """Show information about a project."""

    given_title = request.args.get('title')
    title, description, max_grade = hackbright.get_project_by_title(given_title)
    project_grade_list = hackbright.get_grades_by_project(given_title)
    html = render_template("project.html",
                           title=title,
                           description=description,
                           max_grade=max_grade,
                           project_grade_list=project_grade_list
                           )
    return html





if __name__ == "__main__":
    app.run(debug=True)