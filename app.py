from flask import Flask
app = Falsk(__name__)
@app.route('/')
def index():
    return "Hello world"

if __name__=="__main__":
    app.run()