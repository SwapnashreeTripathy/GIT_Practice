from flask import Flask


aap = Flask(__name__)

@aap.route('/', method= ['GET'])

def helloworld():
    return "Hi there"

if __name__ == "__main__":
    aap.run(port=3000, debug=True)
