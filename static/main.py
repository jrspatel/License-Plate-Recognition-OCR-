from flask import Flask, jsonify, request
from test import show_result
from shapes import give_shapes
from crop_images import Cropped_Images
app = Flask(__name__)


@app.route('/hello', methods=['GET'])
def helloworld():
	if(request.method == 'GET'):
		img_path = 'C:/Users/lenovo/PycharmProjects/license-plate/image/lice-2.jpeg'
		shapes = give_shapes(img_path)
		print("1st step done")
		print(shapes)
		Cropped_Images(shapes,img_path)
		print('second step done')

		result = show_result('C:/Users/lenovo/PycharmProjects/license-plate/cropped-image/*.*')

		print(result)
		return jsonify(result)


if __name__ == '__main__':
	app.run(debug=True)

