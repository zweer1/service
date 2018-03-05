import os
from flask import Flask

app = Flask(__name__)
count = 0

def increment_counter():
    global count
    count = count + 1


# post method and increment by one for each post request
@app.route('/counter', methods=['POST'])
def post_counter():
    increment_counter() #"incremented counter by 1"
    return


# get method display the number of post requests 
@app.route('/counter', methods=['GET'])
def get_counter():
    return "POST Counter result: %d" % count


if __name__ == "__main__":
    try:
        host_name = ""
        port_number = 443
        app.run(debug=True, host=host_name, port=port_number)

    except Exception as e:
        if 'getaddrinfo failed' in e:
            print("ERROR: Please input a valid IP address or Hostname")
        else:
            print(e)
