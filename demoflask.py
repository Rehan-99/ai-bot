from flask import Flask,render_template
from flask_wtf import FlaskForm

app =Flask(__name__)
app.config['SECRET_KEY'] = "THIS IS SECRET"
class Front_End_Form(FlaskForm):
    def flipkart_url(form,url):
        if "flipkart" in url.data and lv.check(url.data):
            return True
        else:
            raise ValidationError('Enter the correct url')
    #raise validation errors
    
   
    Product_name = URLField('Enter URL :', validators=[DataRequired(message="Enter URL Please"), URL(message="Enter Valid URl Please."), flipkart_url])
    Displayed_price = StringField("Current Price of the product is : ",render_kw={'readonly':True})  
    Your_Price = IntegerField("Enter the Price, at which you want : ", validators=[InputRequired("Please enter the price.")])
    Emailsection = EmailField("Enter your email for reminders : ", validators=[InputRequired("Please enter your email address."), Email("This field requires a valid email address")])
    #submit=SubmitField("Submit")

@app.route('/form')
def form():
	return render_template("form.html")

if __name__ == '__main__':
	app.run(debug=True)
	
