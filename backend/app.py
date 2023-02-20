
from flask import Flask
import datetime
  
x = datetime.datetime.now()
  
app = Flask(__name__)
  
@app.route('/')
def get_time():
  
    return {
        'Name':"kaok", 
        "Age":"22",
        "Date":x, 
        }
  
      
if __name__ == '__main__':
    app.run(debug=True)