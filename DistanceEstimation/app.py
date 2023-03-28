from flask import Flask, request,jsonify
from detect import inference

app = Flask(__name__)




print ("hello")
inference()


@app.route('/')
def hello():
    return 'Hello, World!'

# @app.route('/video_feed')
# def detect_image():    
    
    
    # detect = Detect()


    # detect.config('weights/v5lite-s.pt', 'ref/50.jpg', 0, True, False)

    # detect.detect()

    # person, plabel = detect.width_in_rf, detect.label

    # detect.config('weights/v5lite-s.pt', 'ref/dog50.jpg', 17, True, False)

    # detect.detect()

    # phone, phLabel = detect.width_in_rf, detect.label

    # print(f'{plabel}: {person} | {phLabel}: {phone}')

    # focal_person = detect.focalLength(person)
    # focal_phone = detect.focalLength(phone)

    # print(f'focal length of person: {focal_person} | focal length of phone: {focal_phone}')

    # detect.config('weights/v5lite-c.pt', 'ref/dog50.jpg', None, False, False)

    # detect.detect()

    # return results

@app.route('/api/haptics/right', methods=['GET'])
def haptics_right():
    active = request.args.get('right', type=str).lower() == 'true'
    return jsonify({"right": active})


@app.route('/api/haptics/left', methods=['GET'])
def haptics_left():
    active = request.args.get('left', type=str).lower() == 'true'
    return jsonify({"left": active})

@app.route('/api/haptics', methods=['GET'])
def haptics():
    right_active = request.args.get('right', type=str).lower() == 'true'
    left_active = request.args.get('left', type=str).lower() == 'true'

    response = {
        "right_active": right_active,
        "left_active": left_active
    }

    return jfrom flask import Flask, request,jsonify
2
from detect import inference
3
​
4
app = Flask(__name__)
5
​
6
​
7
​
8
​
9
print ("hello")
10
inference()
11
​
12
​
13
@app.route('/')
14
def hello():
15
    return 'Hello, World!'
16
​
17
# @app.route('/video_feed')
18
# def detect_image():    
19
    
20
    
21
    # detect = Detect()
22
​
23
​
24
    # detect.config('weights/v5lite-s.pt', 'ref/50.jpg', 0, True, False)
25
​
26
    # detect.detect()
27
​
28
    # person, plabel = detect.width_in_rf, detect.label
29
​
30
    # detect.config('weights/v5lite-s.pt', 'ref/dog50.jpg', 17, True, False)
31
​
32
    # detect.detect()
33
​
34
    # phone, phLabel = detect.width_in_rf, detect.label
35
​
36
    # print(f'{plabel}: {person} | {phLabel}: {phone}')
37
​
38
    # focal_person = detect.focalLength(person)
39
    # focal_phone = detect.focalLength(phone)
40
​
41
    # print(f'focal length of person: {focal_person} | focal length of phone: {focal_phone}')
42
​
43
    # detect.config('weights/v5lite-c.pt', 'ref/dog50.jpg', None, False, False)
44
​
45
    # detect.detect()sonify(response)


if __name__ == '__main__':
    app.run(debug=True) 
