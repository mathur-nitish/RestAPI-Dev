from flask import Flask,jsonify,request



app = Flask(__name__)

@app.route('/bfhl',methods=['GET','POST'])

def sayHi():
    if request.method == 'GET':
        return jsonify({"operation_code":1}),200
    
    if request.method == 'POST':
        data = request.json.get('data', [])
        numbers = [x for x in data if x.isdigit()]
        alphabets = [x for x in data if x.isalpha()]
        highest_alphabet = sorted(alphabets, key=lambda x: x.lower(), reverse=True)[:1]
        
        response = {
            "is_success": True,
            "user_id": "john_doe_17091999",
            "email": "john@xyz.com",
            "roll_number": "ABCD123",
            "numbers": numbers,
            "alphabets": alphabets,
            "highest_alphabet": highest_alphabet
        }       

        return jsonify(response), 200       


if __name__ == '__main__':  
   app.run()
