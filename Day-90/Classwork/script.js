class BankAccount {
  
    #accountNumber;
    #balance;
    #pin;
  
    constructor(accountNumber, Balance, pin) {
      this.#accountNumber = accountNumber;
      this.#balance = Balance;
      this.#pin = pin;
    }


    #validatePin (pin) {
        return this.#pin === pin
    }

    #setBalance (money){
        return this.balance = money
    }


    #deposit (amount){
        return this.balance + amount
    }

    #withdraw (amount) {
        return this.balance - amount
    }
}