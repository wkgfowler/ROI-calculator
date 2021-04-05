from IPython.display import clear_output

class ROIcalc():

    def __init__(self):
        self.income = []
        self.expenses = []
        self.investment = []
        self.proplist = []
        self.totalincome = {}
        self.totalexpenses = {}
        self.totalinvestment = {}
        self.ROI = {}

    def prop_name(self):
        property_name = input("What name would you like to refer to this property as? ")
        if property_name in self.proplist:
            print(f"There is already a property with that name. Please try using a different name.")
            self.prop_name()
        else:
            self.proplist.append(property_name)
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
            print(f"Error. Please enter a number. ")
            self.rent_income()
            
    def extra_income(self):
        extra = input("As this is a commercial rental, please add any additional monthly income that you expect to earn: ")
        try:
            extra = int(extra)
            self.income.append(extra)
        except:
            print(f"Error. Please enter a number. ")
            self.extra_income()

    def total_income(self):
        fullincome = sum(self.income)
        for key, value in self.totalincome.items():
            if value == 0:
                self.totalincome[key] = fullincome

    def tax_exp(self):
        taxes = input("How much are the taxes? ")
        try:
            taxes = int(taxes)
            self.expenses.append(taxes)
        except:
            print(f"Error. Please enter a number. ")
            self.tax_exp()

    def ins_exp(self):
        insurance = input("How much is the insurance? ")
        try:
            insurance = int(insurance)
            self.expenses.append(insurance)
        except:
            print(f"Error. Please enter a number. ")
            self.ins_exp()

    def utilities_exp(self):
        water = input("How much is the water? ")
        try:
            water = int(water)
            self.expenses.append(water)
        except:
            print(f"Error. Please enter a number. ")
            self.utilities_exp()
        garbage = input("How much is trash pickup? ")
        try:
            garbage = int(garbage)
            self.expenses.append(garbage)
        except:
            print(f"Error. Please enter a number. ")
            self.utilities_exp()
        electric = input("How much is the electric? ")
        try:
            electric = int(electric)
            self.expenses.append(electric)
        except:
            print(f"Error. Please enter a number. ")
            self.utilities_exp()
        gas = input("How much is the gas? ")
        try:
            gas = int(gas)
            self.expenses.append(gas)
        except:
            print(f"Error. Please enter a number. ")
            self.utilities_exp()

    def HOA_exp(self):
        HOA = input("How much are the HOA fees? ")
        try:
            HOA = int(HOA)
            self.expenses.append(HOA)
        except:
            print(f"Error. Please enter a number. ")
            self.HOA_exp()

    def yard_exp(self):
        yard = input("How much are your landscaping fees? ")
        try:
            yard = int(yard)
            self.expenses.append(yard)
        except:
            print(f"Error. Please enter a number. ")
            self.yard_exp()

    def vacancy_exp(self):
        vacancy = input("How much are you setting aside in case of a vacancy? ")
        try:
            vacancy = int(vacancy)
            self.expenses.append(vacancy)
        except:
            print(f"Error. Please enter a number. ")
            self.vacancy_exp()

    def repair_exp(self):
        repair = input("How much are you setting aside for repairs? ")
        try:
            repair = int(repair)
            self.expenses.append(repair)
        except:
            print(f"Error. Please enter a number. ")
            self.repair_exp()

    def capex_exp(self):
        capex = input("How much are you setting aside for capital expenditures? ")
        try:
            capex = int(capex)
            self.expenses.append(capex)
        except:
            print(f"Error. Please enter a number. ")
            self.capex_exp()

    def manage_exp(self):
        manage = input("How much are you paying for property management? ")
        try:
            manage = int(manage)
            self.expenses.append(manage)
        except:
            print(f"Error. Please enter a number. ")
            self.manage_exp()

    def mortgage_exp(self):
        mortgage = input("How much is the mortgage? ")
        try:
            mortgage = int(mortgage)
            self.expenses.append(mortgage)
        except:
            print(f"Error. Please enter a number. ")
            self.mortgage_exp()

    def down_payment(self):
        downpayment = input("How much was your down payment on the property? ")
        try:
            downpayment = int(downpayment)
            self.investment.append(downpayment)
        except:
            print(f"Error. Please enter a number. ")
            self.down_payment()

    def closing_costs(self):
        closingcosts = input("How much did you pay in closing costs? ")
        try:
            closingcosts = int(closingcosts)
            self.investment.append(closingcosts)
        except:
            print(f"Error. Please enter a number. ")
            self.closing_costs()

    def reno_costs(self):
        renovations = input("How much did you spend on renovations? ")
        try:
            renovations = int(renovations)
            self.investment.append(renovations)
        except:
            print(f"Error. Please enter a number. ")
            self.reno_costs()

    def total_expenses(self):
        fullexpense = sum(self.expenses)
        for key, value in self.totalexpenses.items():
            if value == 0:
                self.totalexpenses[key] = fullexpense

    def total_investments(self):
        fullinvestment = sum(self.investment)
        for key, value in self.totalinvestment.items():
            if value == 0:
                self.totalinvestment[key] = fullinvestment


    def roi_calc(self):
        cashflow = ((sum(self.income)) - (sum(self.expenses))) * 12 
        roi = round(((cashflow / (sum(self.investment))) * 100), 2)
        for key, value in self.ROI.items():
            if value == 0:
                self.ROI[key] = roi
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
            self.prev_property()

    def prop_list(self):
        print(self.proplist)

test = ROIcalc()

def runROI():
    print(f"Hello and welcome to our ROI calculator!")

    while True:
        response = input("Would you like to calculate your ROI or look up a previous properties values? (Please input 'Calculate' or 'Previous Property') ")
        if response.lower() == 'calculate':
            clear_output()
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
            clear_output()
            test.prop_list()
            test.prev_property()
        else:
            print(f"Error. Please try again.")

runROI() 