class PaymentForm {
    constructor() {
        this.form = document.querySelector("form.payment")
    }

    validEmail() {
        const formData = new FormData(this.form);
        const email = formData.get("email");
        if (!email.length) {
            return false;
        }
        console.log(...formData);
        return true;
    }

    validCreditCard() {
        const formData = new FormData(this.form);
        const creditCardNumber = formData.get("email");
        const expirationDate = formData.get("expiration-date");
        const cvv = formData.get("cvv");

        return true;
    }

    submit(event) {
        event.preventDefault();
        console.log({event})
        if (!this.validEmail()) {
            console.error("Invalid email");
            return;
        }
        return;
    }
}


const form = new PaymentForm();
const submitForm = (event) => form.submit(event);
