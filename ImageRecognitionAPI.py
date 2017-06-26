
# coding: utf-8

# In[213]:

from flask import Flask, request, redirect, url_for,make_response,jsonify, render_template
app=Flask(__name__)

from PIL import Image
from StringIO import StringIO

from keras.models import load_model
from keras.preprocessing import image
import numpy as np
import requests
import PIL
import json



#image=data.hubble_deep_field()



def predict(imageone):

    model = load_model('image_recongition_model.h5')

    #imageone = '/Users/jac812i/Documents/Imagerecognition/unknown/unknown/images?q=tbn:ANd9GcSTraBoazT_Rk9-BRdntEDaDvE2QWd2wimQuoZg4Ho-h9eFbliH.jpg'
    #img=image.load_img(imageone, target_size=(224, 224))
    img = image.img_to_array(imageone)
    red=img[:,:,0]
    green=img[:,:,1]
    blue=img[:,:,2]

    image_convert=np.array([red,green,blue])
    image_convert = np.expand_dims(image_convert, axis=0)
    preds = model.predict(image_convert)
    print (preds[0])
    listpreds = []
    for i in preds[0]:
        listpreds.append('%.5f' %i)
    print (listpreds)

    #Labels as per folder structure
    labels = ["faucet","flowerpots","hammer","thermostats"]
    pred = dict(zip(labels, listpreds))
    bestpred = labels[np.argmax(preds[0])]
    print ("probabilties for each category", pred)
    print ("Model predicted image is ", bestpred)

    # image1 = image.resize((224,224))
    #image1 = image
    #image1 = img_to_array(image1)



    #image1 = np.expand_dims(image1, axis=0)

    # pre-process the image using the appropriate function based on the
    # model that has been loaded (i.e., mean subtraction, scaling, etc.)
    #image1 = preprocess(image1)
    # classify the image
    #preds = model.predict(image1)
    #P = imagenet_utils.decode_predictions(preds)
    #for (i, (imagenetID, label, prob)) in enumerate(P[0]):
    #            print("{}. {}: {:.2f}%".format(i + 1, label, prob * 100))
    #(imagenetID, label, prob) = P[0][0]

    json_str = json.dumps(pred)

    print (json_str)

    return json_str

def read_image_from_url(url):
    response = requests.get(url, stream=True)

    img = Image.open(StringIO(response.content))
    img=img.resize((224,224), PIL.Image.ANTIALIAS).convert('RGB')
    #print img

    return img

@app.route('/api/v1/classify_image', methods=['POST'])
def classify_image():
    if 'url' in request.json:
        print("JSON request: ", request.json)
        image_url = request.json['url']
        print (image_url)
        img = read_image_from_url(image_url)
    else:
        abort(BAD_REQUEST)
    img = read_image_from_url(image_url)
    resp = predict(img)
    #return make_response(jsonify({'message': resp}), 200)
    return make_response(resp, 200)

@app.route("/", methods=['GET','POST'])
def home():
    if request.method =='POST':
        image_url = request.form.get('imageurl')
        print (image_url)
        img = read_image_from_url(image_url)
        resp = predict(img)
        #value_one = int(request.form.get('first'))
        #total = value_one + value_two
        #data = {'total': str(total)}
        return resp
    return render_template('index.html')

if __name__ == '__main__':
	app.run(debug=True,port=5432,use_reloader=True)

# In[ ]:
