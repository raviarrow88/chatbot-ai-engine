from flask import Flask, render_template, request, flash, redirect
from flask_mongoengine import MongoEngine
from flask_mongoengine.wtf import model_form



DATABASE_NAME = 'chatbot-ai'

# """
# Create database
# """
# from pymongo import Connection
# connection = Connection()
# db = connection[DATABASE_NAME]


app = Flask(__name__)
app.config['MONGODB_SETTINGS'] = {
    'db': DATABASE_NAME,
    'host': '127.0.0.1',

}
app.secret_key = 's3cr3tbot'

db = MongoEngine(app)



# models
class Project(db.Document):
    title = db.StringField(required=True)
    slug = db.StringField()
    reference = db.StringField(required=True)

    def save(self, *args, **kwargs):
        self.slug = self.title.replace('.','-').replace(',','-').replace(' ','-')
        super(Project, self).save(*args, **kwargs)


# forms
ProjectForm = model_form(Project)




# views
@app.route("/")
def hello():
    projects = Project.objects.all()
    return render_template('index.html', projects=projects)


@app.route("/add-project/", methods=['POST', 'GET'])
def add_project():
    form = ProjectForm(request.form)
    if form.validate_on_submit():
        if Project.objects.filter(title=request.form['reference']).count() >= 1:
            flash("Project with this title already exist!")
            redirect('add_project')
        project = Project(
            title =request.form['reference'],
            reference = request.form['reference']
        )
        project.save()
        flash('New entry was successfully posted')


    return render_template('add-project.html', form=form)

@app.route("/<project_slug>/submit-data/")
def submit_data(project_slug):
    project = Project.objects.get_or_404(slug=project_slug)

    return render_template('submit-data.html', project=project)

@app.route("/talk/")
def talk():
    return render_template('talk.html')



if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True, use_reloader=True)