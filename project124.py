from flask import Flask,jsonify,request

app = Flask(__name__)

data = [
    {
        "id":1,
        "Name":"Raju",
        "Contact":"9987644456",
        "done":False
    },
    {
        "id":2,
        "Name":"Rahul",
        "Contact":"987643222",
        "done":False
    }
]

@app.route("/")
def homePage():
    return("Home Page")

@app.route("/get-data")
def getData():
    return jsonify({
        "Contact":data
    })    

@app.route("/add-data",methods = ["POST"])
def addData():
    if not request.json:
        return jsonify({
            "status":"ERROR",
            "message":"Please provide the data"
        })
    contact = {
        "id":data[-1]["id"] + 1,
        "Name": request.json["Name"],
        "Contact":request.json.get("Contact",""),
        "done": False
    }    

    data.append(contact)
    return jsonify({
        "status":"SUCCESS",
        "message":"Contact successfully added"
    })

if __name__ == "__main__":
    app.run(debug=True)