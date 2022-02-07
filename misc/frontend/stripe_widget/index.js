class PaymentForm {
    constructor() {
        this.form = document.querySelector("form.payment")
    }

    validIdentity() {
        const formData = new FormData(this.form);
        const name = formData.get("name");
        const email = formData.get("email");
        if (!email.length || !name.length) {
            return false;
        }
        return true;
    }

    validCreditCard() {
        const formData = new FormData(this.form);
        const creditCardNumber = formData.get("credit-card-number");
        const expirationDateString = formData.get("expiration-date");
        const cvv = formData.get("cvv");
        console.log({
            creditCardNumber,
            expirationDateString,
            cvv
        })
        if (creditCardNumber.length != 10) {
            return false;
        }
        const expirationDate = Date.parse(expirationDateString);
        if (expirationDate < Date.now()) {
            return false;
        }
        if (cvv.length != 3) {
            return false;
        }
        return true;
    }

    submit(event) {
        event.preventDefault();

        if (!this.validIdentity()) {
            console.error("Invalid identity");
            return;
        }
        if (!this.validCreditCard()) {
            console.error("Invalid credit card info");
            return;
        }
        return;
    }
}


const form = new PaymentForm();
const submitForm = (event) => form.submit(event);
