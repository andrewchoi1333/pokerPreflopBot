from flask import Flask, request, render_template, jsonify

pokerbot = Flask(__name__)

class Poker:
    def __init__(self):
        self.ten = set(["AA", "KK"])
        self.nine = set(["QQ", "AKs", "AKo"])
        self.eight = set(["JJ", "1010", "AQs", "AQo"])
        self.seven = set(["99", "AJs", "AJo", "KQs"])
        self.six = set(["KQo", "A10s", "QJs", "KJs", "J10s", "77", "66"])
        self.five = set(["88", "A10o", "A9s", "A8s", "QJo", "J10o", "910s", 
                         "KJo", "K10s", "K10o", "55", "44", "33", "22"])
        self.four = set(["Q10s", "Q9s", "J9s", "K9s", "A7s", "A5s", "98s", 
                         "A4s", "A3s", "A2s", "K8s", "K7s", "K6s", "A6s", 
                         "Q8s", "Q7s", "J8s", "Q10o", "A8o", "98s", "910o", 
                         "A4s", "A3s", "A2s"])
        self.three = set(["K8s", "K7s", "K6s", "A6s", "Q8s", "Q7s", "J8s", "Q10o", "A8o"])
        self.two = set(["K5s", "K4s", "K3s", "K2s", "Q6s", "Q5s", "Q4s", 
                        "Q3s", "Q2s", "J7s", "J6s", "J5s", "J4s", "J3s", 
                        "J2s", "108s", "107s", "106s", "105s", "104s", 
                        "103s", "102s", "75s", "53s"])

        self.fold = {9: 50, 8: 30, 7: 20, 6: 15, 5: 10, 4: 5, 3: 2, 2: 1}

    def action(self, hand, bet, position):
        if hand in self.ten:
            return "Raise"
        if hand in self.nine:
            if bet > self.fold[9]:
                return "Fold"
            elif 0 < bet <= self.fold[9]:
                return "Call"
            elif bet == 0:
                return "Raise"
        if hand in self.eight:
            if bet > self.fold[8]:
                return "Fold"
            elif 0 < bet <= self.fold[8]:
                return "Call"
            elif bet == 0:
                return "Raise"
        if hand in self.seven:
            if bet > self.fold[7]:
                return "Fold"
            elif 0 < bet <= self.fold[7]:
                return "Call"
            elif bet == 0:
                return "Raise"
        if hand in self.six:
            if bet > self.fold[6]:
                return "Fold"
            elif 0 < bet <= self.fold[6]:
                return "Call"
            elif bet == 0:
                return "Raise"
        if hand in self.five:
            if bet > self.fold[5]:
                return "Fold"
            elif 0 < bet <= self.fold[5]:
                return "Call"
            elif bet == 0:
                return "Raise"
        if hand in self.four:
            if bet > self.fold[4]:
                return "Fold"
            elif 0 < bet <= self.fold[4]:
                return "Call"
            elif bet == 0:
                return "Raise"
        if hand in self.three:
            if bet > self.fold[3]:
                return "Fold"
            elif 0 < bet <= self.fold[3]:
                return "Call"
            elif bet == 0:
                return "Raise"
        if hand in self.two:
            if bet > self.fold[2]:
                return "Fold"
            elif 0 < bet <= self.fold[2]:
                return "Call"
            elif position == "BB" or "bb" and bet == 0:
                return "Check"
            elif (position == "B" and bet <= self.fold[2] or position == "b" and bet <= self.fold[2] or position == "sb" and bet <= self.fold[2] or position == "SB" and bet <= self.fold[2]):
                return "Call"
        else:
            if position == (("BB" and bet == 0) or ("bb" and bet == 0)):
                return "Check"
            else:
                return "Fold"

poker = Poker()

@pokerbot.route('/', methods = ['GET','POST'])
def index():
    if request.method == 'POST':
        hand = request.form['hand']
        bet = int(request.form['bet'])
        position = request.form['position']
        action = poker.action(hand, bet, position)
        return jsonify({'action': action})
    return render_template('index.html')

@pokerbot.route('/evaluate', methods=['POST'])
def evaluate():
    hand = request.form['hand']
    bet = int(request.form['bet'])
    position = request.form['position']
    action = poker.action(hand, bet, position)
    return f"Action: {action}"

if __name__ == '__main__':
    pokerbot.run(debug=True)