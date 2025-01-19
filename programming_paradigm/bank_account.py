def __init__(self, initial_balance=0):
    """
    Initialize the BankAccount with an optional initial balance.
       :param initial_balance: float, default is 0
    """
    self.__account_balance = initial_balance


def deposit(self, amount):
    """
    Deposit the specified amount into the account.
    :param amount: float
    """
    if amount > 0:
        self.__account_balance += amount
    else:
        print("Deposit amount must be positive.")


def withdraw(self, amount):
    """
    Withdraw the specified amount from the account if sufficient funds are available.
    :param amount: float
    :return: bool, True if withdrawal is successful, False otherwise
    """
    if amount <=0:
        print("Withdrawal amount must be positive.")
        return False
    if amount <= self.__account_balance:
        self.__account_balance -= amount
        return True
    else:
        return False


def display_balance(self):
    """
    Display the current account balance in a user-friendly format.
    """
    print(f"Current Balance: ${self.__account_balance:.2f}")
  def main():
    account = BankAccount(100)
    if len(sys.argv) < 2:
        print("Usage: python main-0.py <command>:<amount>")
        print("commands: deposit, withdraw, display")
        sys.exit(1)
    command_parts = sys.argv[1].split(':')
    command = command_parts[0].lower()
    amount = None
    if len(command_parts) > 1:
        try:
            amount = float(command_parts[1])
        except ValueError:
            print("Invalid amount. Please enter a numeric value.")
            sys.exit(1)
    if command == "deposit":
        if amount is not None:
            account.deposit(amount)
            print(f"Deposited: ${amount:.2f}")
        else:
            print("Deposit command requires an amount. Usage: deposit:<amount>")
    elif command == "withdraw":
        if amount is not None:
            if account.withdraw(amount):
                print(f"Withdrew: ${amount:.2f}")
            else:
                print("Insufficient funds.")
        else:
            print("Withdraw command requires an amount. Usage: withdra:<amount>")
    elif command == "display":
        account.display_balance()
    else:
        print("Invalid command.Available commands: deposit, withdraw, display")
if __name__ == "__main__":
    main()
    
