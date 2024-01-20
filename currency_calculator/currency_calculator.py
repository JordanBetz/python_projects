class CurrencyConverter:
    currencies = {
        1: ("EUR", 1.0),
        2: ("USD", 1.09),
        3: ("JPY", 161.31)
    }
    
    def display_currencies(self):
        print("Available currencies:")
        for code, (currency, rate) in self.currencies.items():
            print(f"{code}: {currency}")
            
    def get_currency_input(self, message):
        while True:
            try:
                code = int(input(message))
                if code in self.currencies:
                    return code
                else:
                    print("Invalid currency code. Please Try again.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")
                
    def get_amount_input(self, message):
        while True:
            amount_str = input(message)
            if amount_str.replace(".", "", 1).isdigit():
                return float(amount_str)
            
    def convert_currency(self, amount, from_currency, to_currency):
        if from_currency in self.currencies and to_currency in self.currencies:
            converted_amount = amount * (self.currencies[to_currency][1] / self.currencies[from_currency][1])
            return round(converted_amount, 2)
        else:
            return None
        
    def run_converter(self):
        print("Welcome to the Currency Converter!")
        
        while True:
            self.display_currencies()
            
            from_code = self.get_currency_input("Enter the source currency (1-3): ")
            to_code = self.get_currency_input("Enter the target currency (1-3): ")
            
            if from_code == to_code:
                print("Source and target currencies are the same. No conversion needed.")
                continue
            
            if from_code not in self.currencies or to_code not in self.currencies:
                print("Invalid currency selection. Please Try again.")
                continue
            
            amount = self.get_amount_input(f"Enter the amount in {self.currencies[from_code][0]}: ")
            
            converted_amount = self.convert_currency(amount, from_code, to_code)
            
            if converted_amount is not None:
                converted_amount = round(converted_amount, 2)
                print(f"\n{amount} {self.currencies[from_code][0]} is eqivalent to {converted_amount} {self.currencies[to_code][0]}.\n")
            else:
                print("Conversation not supported between selected currencies.")
                
if __name__ == "__main__":
    converter = CurrencyConverter()
    converter.run_converter()