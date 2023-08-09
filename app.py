from flask import Flask, request, jsonify, render_template
app = Flask(__name__)


class MyOperations:
    """Class for handling operations
    """
    def __init__(self, num1=None, num2=None) -> None:
        """Constructor for operations
        
        :param num1: Number 1
        :type num1: Int
        :param num2: Number 2
        :type num2: Int
        :return : None
        """
        self._num1 = num1
        self._num2 = num2
    
    @property
    def num1(self):
        """Getter for num1
        
        :return : Number 1
        :rtype : Int
        """
        return self._num1
    
    @property
    def num2(self):
        """Getter for num2
        
        :return : Number 2
        :rtype : Int
        """
        return self._num2

    @num1.setter
    def num1(self, val):
        """Setter for num1
        
        :param val: Number 1
        :type val: Int
        :retturn : None
        """
        self._num1 = val

    @num2.setter
    def num2(self, val):
        """Setter for num2
        
        :param val: Number 2
        :type val: Int
        :retturn : None
        """
        self._num2 = val
    
    def add(self):
        """Add two numbers
        """
        return self.num1 + self.num2
    
    def subt(self):
        """Subtract two numbers
        """
        return self.num1 - self.num2
    
    def mul(self):
        """Multiply two numbers
        """
        return self.num1 * self.num2
    
    def div(self):
        """ Divide two numbers
        """
        return self.num1 / self.num2
    

@app.route("/")
def home():
    # logger.debug("home loaded")
    return render_template("index.html")

@app.route('/<string:operation>', methods=['GET'])
def calculate(operation):
    # logger.debug("operation started")
    num1 = float(request.args.get('num1', 0))
    # logger.debug("got 1st number")
    num2 = float(request.args.get('num2', 0))
    # logger.debug("got 2nd number")
    op_obj = MyOperations(num1,num2)
    if operation == 'add':
        # logger.debug("addition performed")
        result = op_obj.add()
    elif operation == 'subtract':
        # logger.debug("subtraction performed")
        result = op_obj.subt()
    elif operation == 'multiply':
        # logger.debug("multiplication performed")
        result = op_obj.mul()
    elif operation == 'divide':
        # logger.debug("division performed")
        result = op_obj.div()

    return jsonify({"result": result})

if __name__ == '__main__':
    app.run(debug=False,host="0.0.0.0")
