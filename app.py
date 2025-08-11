from flask import Flask, render_template, request
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
 
import numpy as np
 
 
app = Flask(__name__)

 



verbose_name =['A+','A-','AB+','AB-','B+','B-','O+','O-']
 
 
blood_group = load_model('blood_group.h5')
blood = load_model('blood.h5')

 

def predict_label(img_path):
	test_image = image.load_img(img_path, target_size=(224,224))
	test_image = image.img_to_array(test_image)/255.0
	test_image = test_image.reshape(1, 224,224,3)

	predict_x=blood_group.predict(test_image) 
	classes_x=np.argmax(predict_x,axis=1)
	
	return  verbose_name[classes_x[0]] 

def predict_labels(img_path):
	test_image = image.load_img(img_path, target_size=(224,224))
	test_image = image.img_to_array(test_image)/255.0
	test_image = test_image.reshape(1, 224,224,3)

	predict_x=blood.predict(test_image) 
	classes_x=np.argmax(predict_x,axis=1)
	
	return  verbose_name[classes_x[0]]  

@app.route("/")
@app.route("/first")
def first():
	return render_template('first.html')
    
@app.route("/login")
def login():
	return render_template('login.html')   
    
@app.route("/index", methods=['GET', 'POST'])
def index():
	return render_template("index.html")


 

@app.route("/submit", methods = ['GET', 'POST'])
def submit():
	predict_result = None
	img_path = None
 
	if request.method == 'POST':
		img = request.files['my_image']
	 
	    # predict_result = "Prediction: Success" 
		img_path = "static/tests/" + img.filename	
		img.save(img_path)
		#plt.imshow(img)

		 

		predict_result = predict_label(img_path)
		 
			 
		 
 			  
	return render_template("prediction.html", prediction = predict_result, img_path = img_path)

@app.route("/indexs", methods=['GET', 'POST'])
def indexs():
	return render_template("indexs.html")


 

@app.route("/submits", methods = ['GET', 'POST'])
def submits():
	predict_result = None
	img_path = None
	
	if request.method == 'POST':
		img = request.files['my_image']
	 
	    # predict_result = "Prediction: Success" 
		img_path = "static/tests/" + img.filename	
		img.save(img_path)
		#plt.imshow(img)

		 

		predict_result = predict_labels(img_path)
		 
			 
		 
 			  
	return render_template("predictions.html", prediction = predict_result, img_path = img_path)
@app.route("/chart")
def chart():
	return render_template('chart.html') 
@app.route("/performance")
def performance():
	return render_template('performance.html')  	
@app.route("/charts")
def charts():
	return render_template('charts.html') 
@app.route("/performances")
def performances():
	return render_template('performances.html')  

	

	
if __name__ =='__main__':
	app.run(debug = True)


	

	


