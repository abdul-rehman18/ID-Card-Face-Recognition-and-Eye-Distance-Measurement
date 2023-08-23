# Import necessary libraries
import os
import seaborn as sns
import matplotlib.pyplot as plt
from eyeDist import EyeDistance
from werkzeug.utils import secure_filename
from image_processing import process_and_compare
from sklearn.metrics import confusion_matrix, f1_score, accuracy_score
from flask import Flask, render_template, request, redirect, url_for,flash


# Initialize the Flask framework
app = Flask(__name__)
app.secret_key = '12345'
app.config['UPLOAD_FOLDER'] = 'static/images'
ALLOWED_EXTENSIONS = {'jpg', 'jpeg', 'png'}

# Check if a given filename has an allowed extension
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Lists to store true labels and predicted labels
true = [] 
pred = []

# Process and compare images for similarity
similarity_score,match=process_and_compare('static/images/id1.jpg','static/images/f1.jpg')
true.append(1 if match else 0)
pred.append(1 if similarity_score<0.63 else 0)

similarity_score,match=process_and_compare('static/images/id1.jpg','static/images/f2.jpg')
true.append(1 if match else 0)
pred.append(1 if similarity_score<0.63 else 0)

similarity_score,match=process_and_compare('static/images/id3.jpg','static/images/f3.jpg')
true.append(1 if match else 0)
pred.append(1 if similarity_score<0.63 else 0)

similarity_score,match=process_and_compare('static/images/id4.jpg','static/images/f4.jpg')
true.append(1 if match else 0)
pred.append(1 if similarity_score<0.63 else 0)

similarity_score,match=process_and_compare('static/images/id5.jpg','static/images/f5.jpg')
true.append(1 if match else 0)
pred.append(1 if similarity_score<0.63 else 0)

similarity_score,match=process_and_compare('static/images/id6.jpg','static/images/f6.jpg')
true.append(1 if match else 0)
pred.append(1 if similarity_score<0.63 else 0)

similarity_score,match=process_and_compare('static/images/id3.jpg','static/images/f1.jpg')
true.append(1 if match else 0)
pred.append(1 if similarity_score<0.63 else 0)

similarity_score,match=process_and_compare('static/images/id6.jpg','static/images/f3.jpg')
true.append(1 if match else 0)
pred.append(1 if similarity_score<0.63 else 0)

similarity_score,match=process_and_compare('static/images/id4.jpg','static/images/f5.jpg')
true.append(1 if match else 0)
pred.append(1 if similarity_score<0.63 else 0)

similarity_score,match=process_and_compare('static/images/id5.jpg','static/images/f2.jpg')
true.append(1 if match else 0)
pred.append(1 if similarity_score<0.63 else 0)

# Calculate the F1 score using true and predicted labels
f1 = f1_score(true, pred)

# Calculate the accuracy using true and predicted labels
accuracy = accuracy_score(true, pred)

# Generate a confusion matrix using true and predicted labels
mat = confusion_matrix(true, pred)

# Create a heatmap visualization of the confusion matrix
sns.heatmap(mat.T, square = True, annot=True, fmt = "d",xticklabels=['match','not match'],yticklabels=['match','not match'])
plt.xlabel("true labels")
plt.ylabel("predicted label")
plt.show()

# Initialize empty lists to store true labels and predicted labels
true_labels=[]
predicted_labels=[]


@app.route('/', methods=['GET', 'POST'])
def index():
    # Handle POST requests when the form is submitted	
    if request.method == 'POST':
	# Check if 'id_card' and 'person_image' files are present in the request
        if 'id_card' not in request.files or 'person_image' not in request.files:
            flash('No file part')
            return redirect(request.url)
        
    # Global variables to store uploaded files
    global file1 ,file2
    file1 = request.files['id_card']
    file2 = request.files['person_image']
	
	# Check if any of the uploaded files is empty
    if file1.filename == '' or file2.filename == '':
        flash('No selected file')
        return redirect(request.url)
        
    # Check if both files have allowed extensions
    if file1 and allowed_file(file1.filename) and file2 and allowed_file(file2.filename):
	    # Securely generate filenames for uploaded files
        filename1 = secure_filename(file1.filename)
        filename2 = secure_filename(file2.filename)

	    # Paths to save uploaded files
        file1_path = os.path.join(app.config['UPLOAD_FOLDER'], filename1)
        file2_path = os.path.join(app.config['UPLOAD_FOLDER'], filename2)
	    
	    # Save the uploaded files
        file1.save(file1_path)
        file2.save(file2_path)

        # Process and compare uploaded images
        similarity_score, match = process_and_compare(file1_path, file2_path)
            
	    # Generate URLs for image paths
        id_card_image_url = url_for('static', filename=f'images/{secure_filename(file1.filename)}')
        person_image_url = url_for('static', filename=f'images/{secure_filename(file2.filename)}')
        conf_matrix_url = url_for('static',filename=f'images/confusion_matrix.png')
            
        # Calculate and store eye distance metrics
        distance_mm,distance_px,conv_fact,ref = EyeDistance(file2_path)

        # Render the result template with the provided data
        return render_template('result.html', similarity_score=similarity_score, match=match,
                               distance_mm=distance_mm, distance_px=distance_px, conv_fact=conv_fact,
                               ref=ref, id_card_image_url=id_card_image_url, person_image_url=person_image_url,conf_matrix_url=conf_matrix_url, f1=f1, accuracy=accuracy)

    # Render the index template when there's a GET request	   
    return render_template('index.html')


# Run the Flask framework if this script is being executed directly
if __name__ == '__main__':
    # Start the app in debug mode
    app.run(debug=True)

    
