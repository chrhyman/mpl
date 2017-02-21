from constants import *

class Career:
    def __init__(self, name, paygrade, text):
        self.name = name
        self.paygrade = paygrade
        self.text = text

def makeCareers(): # returns a tuple of all careers as Career objects
    return (Career(ACCOUNTANT, (PAYPURPLE, PAYRED), 'Degree required.'), 
            Career(DOCTOR, (PAYYELLOW, PAYGREEN), 'Degree required.'), 
            Career(ARTIST, (PAYPURPLE, PAYRED),
'Collect $10,000 from a player who buys your art (spins a "1").'), 
            Career(ENTERTAINER, (PAYRED, PAYPURPLE), 'If two 8s, 9s, or 10s \
are spun in a row, replace your salary with the yellow Salary card, trading \
salaries if necessary.'), 
            Career(SALES, (PAYRED, PAYGREEN), 'Collect $5,000 when another \
player buys stock or insurance.'), 
            Career(COP, (PAYRED, PAYGREEN), 'Collect $10,000 from any \
opponent who speeds (spins a "10").'), 
            Career(TEACHER, (PAYRED, PAYGREEN), 'You may draw a Career card \
after all players have a job. You do not get a salary for this career but \
get the special benefits.'), 
            Career(ATHLETE, (PAYPURPLE, PAYGREEN), 'You may trade in 4 LIFE \
tiles to get the yellow Salary card, trading salaries if necessary.'), 
            Career(TECH, (PAYPURPLE, PAYGREEN), 'Any time the spinner stops \
between numbers or comes off the track, collect $50,000 to fix it.'))

class Space:
    def __init__(self, type, text=None, amount=0, to=None,
branching=False, inbranch=False, whichbranch=None):
        self.type = type
        self.text = text
        self.branching = branching # the actual space that creates the branch
        if inbranch:
            self.branch = whichbranch # if space is part of a branched path, set to 'A' or 'B'
        if self.type == START:  # space type handler
            pass
        elif self.type == STOP:
            self.stop = True
        elif self.type == FINISH:
            self.stop = True
            self.atend = True
        elif self.type == PAY:
            self.payamount = amount
            self.payto = to
        elif self.type == GET:
            self.getamount = amount
        elif self.type == LIFE:
            self.getlife = True
        elif self.type == PAYDAY:
            self.getpayday = True
        elif self.type == SPECIAL:
            pass
        else: assert False, 'Space Type Error: Invalid space type'

STANDARDBOARD = (
# Space(type, text, amt_to_pay/receive, pay_to, branching_space, isPartOfBranch, whichBranch
    Space(START, 'Borrow $100,000.', 0, None, False, True, 'a'),
    Space(GET, 'Scholarship! Collect $20,000.', 20000, None, False, True, 'a'),
    Space(PAY, 'Buy books and supplies. Pay $5,000.', 5000, BANK, False, True, 'a'),
    Space(LIFE, 'Make new friends.', 0, None, False, True, 'a'),
    Space(GET, 'Part time job. Collect $5,000.', 5000, None, False, True, 'a'),
    Space(SPECIAL, 'Study for exams. Miss next turn.', 0, None, False, True, 'a'),
    Space(LIFE, 'Study abroad.', 0, None, False, True, 'a'),
    Space(PAY, 'Spring Break! Pay $5,000.', 5000, BANK, False, True, 'a'),
    Space(LIFE, 'Dean\'s List!', 0, None, False, True, 'a'),
    Space(PAY, 'Your buddies crash your car. Pay $5,000 if not insured.', 5000, BANK, False, True, 'a'),
    Space(LIFE, 'Graduation day!', 0, None, False, True, 'a'),
    Space(SPECIAL, 'CAREER CHOICE', 0, None, False, True, 'a'),
    Space(STOP), # Note: Treats the STOP sign as a "space" that can't be landed on
    Space(START, None, 0, None, False, True, 'b'),
    Space(PAYDAY, None, 0, None, False, True, 'b'),
    Space(PAY, 'Rent apartment. Pay $5,000.', 5000, BANK, False, True, 'b'),
    Space(GET, 'Inheritance. Collect $10,000.', 10000, None, False, True, 'b'),
    Space(PAYDAY),
    Space(LIFE, 'Adopt a pet'),
    Space(SPECIAL, 'Lost! Miss next turn.'),
    Space(LIFE, 'Birthday party!'),
    Space(PAY, 'Ski accident. Pay $5,000.', 5000, DOCTOR),
    Space(GET, 'Win marathon! Collect $10,000', 10000),
    Space(LIFE, 'Visit a museum.'),
    Space(LIFE, 'Cycle to work'),
    Space(PAYDAY),
    Space(PAY, 'Car rolls away. Pay $15,000 if not insured.', 15000, BANK),
    Space(LIFE, 'GET MARRIED'),
    Space(STOP),
    Space(PAY, 'Wedding reception. Pay $10,000.', 10000, BANK),
    Space(LIFE, 'Happy honeymoon!'),
    Space(PAY, 'Upgrade computer. Pay $10,000.', 10000, SALES),
    Space(PAY, 'Car accident. Pay $10,000 if not insured.', 10000, BANK),
    Space(PAY, 'Attend high-tech seminar. Pay $10,000.', 10000, TECH),
    Space(PAY, 'Night school. Pay $20,000.', 20000, TEACHER),
    Space(PAYDAY),
    Space(PAY, 'Taxes due.', 0, ACCOUNTANT),
    Space(GET, 'Win lottery! Collect $50,000.', 50000),
    Space(LIFE, 'Visit in-laws.'),
    Space(SPECIAL, 'You may BUY A HOUSE. Draw Deed.'),
    Space(STOP),
    Space(PAYDAY),
    Space(SPECIAL, 'Lose your job. Start new career.'),
    Space(LIFE, 'Baby boy!'),
    Space(PAY, 'Furnish baby room. Pay $5,000.', 5000, SALES),
    Space(LIFE, 'Baby girl!'),
    Space(GET, 'Win talent show. Collect $10,000.', 10000),
    Space(PAYDAY),
    Space(LIFE, 'Twins!'),
    Space(PAY, '50-yard line seats at the big game. Pay $20,000.', 20000, ATHLETE),
    Space(LIFE, 'Baby girl!'),
    Space(PAY, 'Attend Hollywood movie premiere. Pay $5,000.', 5000, ENTERTAINER),
    Space(PAY, 'House flooded! Pay $40,000 if not insured.', 40000, BANK, True),
    Space(PAY, 'Family physicals. Pay $5,000.', 5000, DOCTOR, False, True, 'a'),
    Space(SPECIAL, 'Trade salary card with any player.', 0, None, False, True, 'a'),
    Space(LIFE, 'Baby boy!', 0, None, False, True, 'a'),
    Space(PAYDAY, None, 0, None, False, True, 'a'),
    Space(LIFE, 'Baby girl!', 0, None, False, True, 'a'),
    Space(PAY, 'Tree falls on house. Pay $15,000 if not insured.', 15000, BANK, False, True, 'a'),
    Space(LIFE, 'Return lost wallet.', 0, None, False, True, 'a'),
    Space(PAY, 'Buy high-definition TV. Pay $5,000.', 5000, SALES, False, True, 'b'),
    Space(SPECIAL, 'Stock market soars! Collect 1 stock.', 0, None, False, True, 'b'),
    Space(LIFE, 'Family picnic.', 0, None, False, True, 'b'),
    Space(LIFE, 'Visit Mount Rushmore.', 0, None, False, True, 'b'),
    Space(PAYDAY, None, 0, None, False, True, 'b'),
    Space(PAY, 'Car stolen! Pay $15,000 if not insured.', 15000, BANK, False, True, 'b'),
    Space(SPECIAL, 'Trade salary card with any player.'),
    Space(LIFE, 'Run for Mayor.'),
    Space(LIFE, 'Vote!'),
    Space(LIFE, 'Baby boy!'),
    Space(PAYDAY),
    Space(PAY, 'Buy luxury cruise online. Pay $25,000.', 25000, TECH),
    Space(PAY, 'Night school. Pay $20,000.', 20000, TEACHER),
    Space(LIFE, 'Learn CPR.'),
    Space(PAY, 'Art auction. Pay $20,000.', 20000, ARTIST),
    Space(PAYDAY),
    Space(LIFE, 'Volunteer at charity sports event.'),
    Space(GET, 'Win photography contest. Collect $10,000.', 10000),
    Space(SPECIAL, 'Spin again if not in the lead.'),
    Space(SPECIAL, 'Trade salary card with any player.'),
    Space(PAY, 'Taxes due.', 0, ACCOUNTANT),
    Space(PAY, 'Tennis camp. Pay $25,000.', 25000, ATHLETE),
    Space(PAY, 'Donate computer network. Pay $25,000.', 25000, TECH),
    Space(PAYDAY),
    Space(SPECIAL, 'Stock market crash. Return 1 stock.'),
    Space(SPECIAL, 'You may sell your house and buy a new one.'),
    Space(STOP),
    Space(PAY, 'Day care. Pay $5,000 per child.', 0, TEACHER),
    Space(GET, 'Write best-seller. Collect $80,000.', 80000),
    Space(LIFE, 'Adopt twins!', 0, None, True),
    Space(PAY, 'Invest in Broadway play. Pay $15,000.', 15000, ENTERTAINER, False, True, 'a'),
    Space(PAYDAY, None, 0, None, False, True, 'a'),
    Space(LIFE, 'Join health club.', 0, None, False, True, 'a'),
    Space(PAY, 'Family portrait. Pay $35,000.', 35000, ARTIST, False, True, 'a'),
    Space(SPECIAL, 'Trade salary card with any player.', 0, None, False, True, 'a'),
    Space(PAY, 'Buy sport utility vehicle. Pay $25,000.', 25000, SALES, False, True, 'a'),
    Space(GET, 'Tax refund. Collect $75,000.', 75000, None, False, True, 'a'),
    Space(PAY, 'Host Police Charity Ball. Pay $15,000.', 15000, COP, False, True, 'b'),
    Space(PAYDAY, None, 0, None, False, True, 'b'),
    Space(GET, 'Find buried treasure! Collect $80,000.', 80000, None, False, True, 'b'),
    Space(PAY, 'Taxes due.', 0, ACCOUNTANT, False, True, 'b'),
    Space(PAYDAY),
    Space(PAY, 'Donate to Art Institute. Pay $25,000.', 25000, ARTIST),
    Space(LIFE, 'Recycle'),
    Space(GET, 'TV game show winner! Collect $95,000.', 95000),
    Space(PAY, 'Summer school. Pay $5,000 per child.', 0, TEACHER),
    Space(LIFE, 'Have a Family Game Night.'),
    Space(LIFE, 'Learn sign language.'),
    Space(PAY, 'Buy lakeside cabin. Pay $90,000.', 90000, BANK),
    Space(PAYDAY),
    Space(PAY, 'Burglar! Pay $50,000 if not insured.', 50000, BANK),
    Space(GET, 'Win Nobel Prize. Collect $100,000.', 100000),
    Space(SPECIAL, 'Trade salary card with any player.'),
    Space(PAY, 'Buy home gym. Pay $30,000.', 30000, ATHLETE),
    Space(SPECIAL, 'Stock market crash. Return 1 stock.'),
    Space(PAY, 'Tornado hits house! Pay $125,000 if not insured.', 125000, BANK),
    Space(PAYDAY),
    Space(PAY, 'Life-saving operation. Pay $25,000.', 25000, DOCTOR),
    Space(PAY, 'Taxes due.', 0, ACCOUNTANT),
    Space(PAY, 'Buy sailboat. Pay $30,000.', 30000, SALES),
    Space(PAY, 'Sponsor golf tournament. Pay $35,000.', 35000, ATHLETE),
    Space(SPECIAL, 'Mid-life crisis. Start new career.'),
    Space(SPECIAL, 'Spin again if not in the lead.'),
    Space(PAYDAY),
    Space(PAY, 'Host online concert. Pay $100,000.', 100000, ENTERTAINER),
    Space(SPECIAL, 'Trade salary card with any player.'),
    Space(LIFE, 'Help the homeless.'),
    Space(SPECIAL, 'Spin again if not in the lead.'),
    Space(PAY, 'Have cosmetic surgery. Pay $100,000.', 100000, DOCTOR),
    Space(PAY, 'College. Pay $50,000 per child.', 0, TEACHER),
    Space(PAYDAY),
    Space(PAY, 'Taxes due.', 0, ACCOUNTANT),
    Space(SPECIAL, 'Spin again if not in the lead.'),
    Space(LIFE, 'Visit war memorial.'),
    Space(PAY, 'Sponsor art exhibit.', 125000, ARTIST),
    Space(LIFE, 'Grand Canyon vacation.'),
    Space(SPECIAL, 'Trade salary card with any player.'),
    Space(PAYDAY),
    Space(LIFE, 'Go fishing.'),
    Space(SPECIAL, 'Spin again if not in the lead'),
    Space(PAY, 'Hire jockey for your racehorse. Pay $65,000.', 65000, ATHLETE),
    Space(LIFE, 'Go hiking.'),
    Space(PAYDAY),
    Space(LIFE, 'Plant a tree.'),
    Space(SPECIAL, 'Spin again if not in the lead.'),
    Space(LIFE, 'Support wildlife fund.'),
    Space(PAY, 'Have website designed. Pay $45,000.', 45000, TECH),
    Space(LIFE, 'You\'re a grandparent!'),
    Space(PAYDAY),
    Space(PAY, 'Throw party for entertainment award winners. Pay $35,000.', 35000, ENTERTAINER),
    Space(PAY, 'Invest in e-commerce company. Pay $45,000.', 45000, TECH),
    Space(GET, 'Pension. Collect $20,000 times spin.', 0),
    Space(FINISH, 'RETIRE. Go to Countryside Acres or Millionaire Estates.')
)

def makeBoard(): # returns a tuple of all spaces as Space objects, in order
    return STANDARDBOARD
