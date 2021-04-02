class ROIcalc():

    def __init__(self):
        self.income = []
        self.expenses = []
        self.investment = []
        self.totalincome = {}
        self.totalexpenses = {}
        self.totalinvestment = {}
        self.ROI = {}

    def prop_name(self):
        property_name = input("What name would you like to refer to this property as? ")
        self.totalincome[property_name] = 0
        self.totalexpenses[property_name] = 0
        self.totalinvestment[property_name] = 0
        self.ROI[property_name] = 0
    
    def rent_income(self):
        rent = input("How much do you charge for rent? ")
        try:
            rent = int(rent)
            self.income.append(rent)
        except:
            print(f"Halie called you stupid. Fucking idiots.")
            self.rent_income()
        
    def extra_income(self):
        extra = int(input("As this is a commercial rental, please add any additional monthly income that you expect to earn: "))
        self.income.append(extra)

    def total_income(self):
        fullincome = sum(self.income)
        for key, value in self.totalincome.items():
            if value == 0:
                self.totalincome[key] = fullincome

    def tax_exp(self):
        taxes = int(input("How much are the taxes? "))
        self.expenses.append(taxes)

    def ins_exp(self):
        insurance = int(input("How much is the insurance? "))
        self.expenses.append(insurance)
    
    def utilities_exp(self):
        water = int(input("How much is the water? "))
        self.expenses.append(water)
        garbage = int(input("How much is trash pickup? "))
        self.expenses.append(garbage)
        electric = int(input("How much is the electric? "))
        self.expenses.append(electric)
        gas = int(input("How much is the gas? "))
        self.expenses.append(gas)

    def HOA_exp(self):
        HOA = int(input("How much are the HOA fees? "))
        self.expenses.append(HOA)

    def yard_exp(self):
        yard = int(input("How much are your landscaping fees? "))
        self.expenses.append(yard)

    def vacancy_exp(self):
        vacancy = int(input("How much are you setting aside in case of a vacancy? "))
        self.expenses.append(vacancy)

    def repair_exp(self):
        repair = int(input("How much are you setting aside for repairs? "))
        self.expenses.append(repair)

    def capex_exp(self):
        capex = int(input("How much are you setting aside for capital expenditures? "))
        self.expenses.append(capex)

    def manage_exp(self):
        manage = int(input("How much are you paying for property management? "))
        self.expenses.append(manage)

    def mortgage_exp(self):
        mortgage = int(input("How much is the mortgage? "))
        self.expenses.append(mortgage)

    def down_payment(self):
        downpayment = int(input("How much was your down payment on the property? "))
        self.investment.append(downpayment)

    def closing_costs(self):
        closingcosts = int(input("How much did you pay in closing costs? "))
        self.investment.append(closingcosts)

    def reno_costs(self):
        renovations = int(input("How much did you spend on renovations? "))
        self.investment.append(renovations)

    def total_expenses(self):
        fullexpense = sum(self.expenses)
        for value in self.totalexpenses.values():
            if value == 0:
                value = fullexpense

    def total_investments(self):
        fullinvestment = sum(self.investment)
        for value in self.totalinvestment.values():
            if value == 0:
                value = fullinvestment
        

    def roi_calc(self):
        cashflow = sum(self.income) / sum(self.expenses) * 12 
        roi = cashflow / sum(self.investment) * 100
        for value in self.ROI.values():
            if value == 0:
                value = roi
        print(f"This property's ROI is: {roi}%.")
        self.income.clear()
        self.expenses.clear()
        self.investment.clear()
        
        
    def prev_property(self):
        which_prop = input("Please type your property name to view your data: ")
        if which_prop.lower() in self.ROI:
            print(self.totalincome[which_prop])
            print(self.totalexpenses[which_prop])
            print(self.totalinvestment[which_prop])
            print(self.ROI[which_prop])
        else:
            print(f"Error. Please try again.")


test = ROIcalc()

def runROI():
    print(f"Hello and welcome to our ROI calculator!")

    while True:
        response = input("Would you like to calculate your ROI or look up a previous properties values? (Please input 'Calculate' or 'Previous Property')")
        if response.lower() == 'calculate':
            test.prop_name()
            prop_type = input("Is this a 'residential' or 'commercial' property? ")
            if prop_type.lower() == 'residential':
                test.rent_income()
                test.total_income()
                test.tax_exp()
                test.ins_exp()
                test.HOA_exp()
                test.yard_exp()
                test.vacancy_exp()
                test.repair_exp()
                test.capex_exp()
                test.manage_exp()
                test.mortgage_exp()
                test.down_payment()
                test.closing_costs()
                test.reno_costs()
                test.total_expenses()
                test.total_investments()
                test.roi_calc()
            elif prop_type.lower() == 'commercial':
                test.rent_income()
                test.extra_income()
                test.total_income()
                test.tax_exp()
                test.ins_exp()
                test.utilities_exp()
                test.HOA_exp()
                test.yard_exp()
                test.vacancy_exp()
                test.repair_exp()
                test.capex_exp()
                test.manage_exp()
                test.mortgage_exp()
                test.down_payment()
                test.closing_costs()
                test.reno_costs()
                test.total_expenses()
                test.total_investments()
                test.roi_calc()
            else:
                print(f"Error. Please try again.")
        elif response.lower() == 'previous property':
            test.prev_property()
        else:
            print(f"Error. Please trya gain.")
            
runROI()