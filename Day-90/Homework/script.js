class Thermostat {
   
    #temperature;
    #minTemp;
    #maxTemp;
    #mode;
  
    
    constructor(minTemp, maxTemp, initialTemp, mode = "off") {
      this.#minTemp = minTemp;
      this.#maxTemp = maxTemp;
      this.#mode = mode;
  
      if (initialTemp < minTemp || initialTemp > maxTemp) {
        throw new Error(`Initial temperature must be between ${minTemp} and ${maxTemp}.`);
      }
      this.#temperature = initialTemp;
    }
  
  
    #setTemperature(value) {
      if (value < this.#minTemp) {
        this.#temperature = this.#minTemp;
      } else if (value > this.#maxTemp) {
        this.#temperature = this.#maxTemp;
      } else {
        this.#temperature = value;
      }
    }
  
   
    adjustTemperature(value) {
      this.#setTemperature(value);
      console.log(`Temperature adjusted to ${this.#temperature}°`);
    }
  
  
    changeMode(mode) {
      const validModes = ["cool", "heat", "off"];
      if (!validModes.includes(mode)) {
        throw new Error(`Invalid mode. Valid modes are: ${validModes.join(", ")}.`);
      }
      this.#mode = mode;
      console.log(`Mode changed to ${this.#mode}`);
    }
  
   
    getCurrentTemperature() {
      return this.#temperature;
    }
  }



  class SecureNote {
   
    #content;
    #pin;
  
 
    constructor(content, pin) {
      this.#content = content;
      this.#pin = pin;
    }
  
   
    #validatePin(inputPin) {
      return inputPin === this.#pin;
    }
  
   
    updateContent(newContent, pin) {
      if (this.#validatePin(pin)) {
        this.#content = newContent;
        console.log("Content updated successfully.");
      } else {
        console.log("Access denied: Incorrect PIN.");
      }
    }
  
   
    getContent(pin) {
      if (this.#validatePin(pin)) {
        return this.#content;
      } else {
        return "Access denied: Incorrect PIN.";
      }
    }
  }