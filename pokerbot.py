from flask import Flask, request, render_template, jsonify

app = Flask(__name__)

class Poker:
    #create database of poker starting hands grouped by relative strength
    def __init__(self):
        self.ten = set(["aa", "kk"])
        self.nine = set(["qq", "aks", "ako"])
        self.eight = set(["jj", "1010", "aqs", "aqo"])
        self.seven = set(["99", "ajs", "ajo", "kqs"])
        self.six = set(["kqo", "a10s","a9s", "qjs", "kjs", "j10s", "88", "77", "66"])
        self.five = set([ "a8s", "qjo", "j10o", "910s",
                        "kjo", "k10s", "a10o", "k10o", "55", "44", "33", "22"])
        self.four = set(["q10s", "a9o", "q9s", "j9s", "k9s", "a7s", "a5s", "98s",
                        "a4s", "a3s", "a2s", "k8s", "k7s", "k6s", "a6s",
                        "q8s", "q7s", "j8s", "q10o", "a8o", "98s", "910o",
                        "a4s", "a3s", "a2s"])
        self.three = set(["k8s", "k7s", "k6s","a7o", "a6s", "q8s", "q7s", "j8s", "q10o", "a8o"])
        self.two = set(["k5s", "k4s", "k3s", "k2s", "q6s", "q5s", "q4s",
                        "q3s", "q2s", "j7s", "j6s", "j5s", "j4s", "j3s",
                        "j2s", "108s", "107s", "106s", "105s", "104s",
                        "103s", "102s", "75s", "53s"])

        #upper limits of bet sizes that should warrant a fold
        self.fold = {9: 50, 8: 30, 7: 20, 6: 15, 5: 10, 4: 6, 3: 2, 2: 1}

    #function that takes inputted starting hand info
    #returns a recommendation based off GTO theory
    def action(self, hand, bet, position):
        if hand in self.ten:
            return "Raise"
        if hand in self.nine:
            if bet > self.fold[9]:
                return "Fold"
            elif 20 < bet <= self.fold[9]:
                return "Call"
            else:
                return "Raise"
        if hand in self.eight:
            if bet > self.fold[8]:
                return "Fold"
            elif 15 <= bet <= self.fold[8]:
                return "Call"
            elif bet < 15:
                return "Raise"
        if hand in self.seven:
            if bet > self.fold[7]:
                return "Fold"
            elif 11 <= bet <= self.fold[7]:
                return "Call"
            elif bet < 11:
                return "Raise"
        if hand in self.six:
            if bet > self.fold[6]:
                return "Fold"
            elif 5 <= bet <= self.fold[6]:
                return "Call"
            elif bet < 5:
                return "Raise"
        if hand in self.five:
            if bet > self.fold[5]:
                return "Fold"
            elif 3 <= bet <= self.fold[5]:
                return "Call"
            elif bet < 5:
                return "Raise"
        if hand in self.four:
            if bet > self.fold[4]:
                return "Fold"
            elif 2 < bet <= self.fold[4]:
                return "Call"
            elif bet <= 2:
                return "Raise"
        if hand in self.three:
            if bet > self.fold[3]:
                return "Fold"
            elif 1 < bet <= self.fold[3]:
                return "Call"
            elif bet <=1:
                return "Raise"
        if hand in self.two:
            if bet > self.fold[2]:
                return "Fold"
            elif 0 < bet <= self.fold[2]:
                return "Call"
            elif position ==  "bb" and bet == 0:
                return "Check"
            elif (position == "b" and bet <= self.fold[2] or position == "b" and bet <= self.fold[2] or position == "sb" and bet <= self.fold[2] or position == "SB" and bet <= self.fold[2]):
                return "Call"
        else:
            if position =="bb" and bet == 0:
                return "Check"
            else:
                return "Fold"

#instance of poker class
poker = Poker()

#formats user inputted data into variables
@app.route('/', methods = ['GET','POST'])
def index():
    if request.method == 'POST':
        # extract values from the form submitted by the user
        hand = request.form['hand'].lower()
        bet = int(request.form['bet'])
        position = request.form['position'].lower()
        action = poker.action(hand, bet, position)
        return jsonify({'action': action})
    return render_template('index.html')

#returns result of action method
@app.route('/evaluate', methods=['POST'])
def evaluate():
    hand = request.form['hand'].lower()
    bet = int(request.form['bet'])
    position = request.form['position'].lower()
    action = poker.action(hand, bet, position)
    return f"Action: {action}"

if __name__ == '__main__':
    app.run(debug=False)
