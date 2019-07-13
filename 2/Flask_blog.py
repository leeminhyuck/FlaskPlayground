from flask import Flask, render_template
app = Flask(__name__)

posts = [
	{
		'author': 'Minhyuck Lee',
		'title': 'Blog Post1',
		'content': 'First post content',
		'date_posted': 'July 14, 2019'
	},
	{
		'author': 'Hojun Kim',
		'title': 'Blog Post2',
		'content': 'Second post content',
		'date_posted': 'July 15, 2019'
	}
]
	


@app.route("/")
@app.route("/home")
def home():
	return render_template('home.html', posts=posts)
	
@app.route("/about")
def about():
	return render_template('about.html', title='about')
	
if __name__=='__main__':
	app.run(debug=True)