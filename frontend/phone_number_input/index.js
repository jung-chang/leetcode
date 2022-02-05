const VALID_KEYS = new Set(["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]);
const MAX_LENGTH = 10;

const getFormattedPhoneNumber = (phoneNumber) => {
  let formattedPhoneNumber = "";
  for (let i = 0; i < phoneNumber.length; i++) {
    if (i === 0) {
      formattedPhoneNumber += "(";
    }
    formattedPhoneNumber += phoneNumber.charAt(i);
    if (i === 2) {
      formattedPhoneNumber += ") ";
    }
    if (i === 5) {
      formattedPhoneNumber += "-";
    }
  }
  return formattedPhoneNumber;
};

const getUnformattedPhoneNumber = (phoneNumber) => {
  let unFormattedPhoneNumber = "";
  for (let i = 0; i < phoneNumber.length; i++) {
    if (VALID_KEYS.has(phoneNumber.charAt(i))) {
      unFormattedPhoneNumber += phoneNumber.charAt(i);
    }
  }
  unFormattedPhoneNumber = unFormattedPhoneNumber.substring(0, MAX_LENGTH);
  return unFormattedPhoneNumber;
};

const isValidKey = (key) => {
  return VALID_KEYS.has(key);
};

const phoneNumberInput = document.querySelector("input.phone-number");

// Keypress captures only keys that add to input
phoneNumberInput.addEventListener("keypress", (event) => {
  if (!event.key) {
    event.preventDefault();
    return;
  }
  if (!isValidKey(event.key)) {
    event.preventDefault();
    return;
  }
  const phoneNumber = getUnformattedPhoneNumber(phoneNumberInput.value);
  if (phoneNumber.length >= MAX_LENGTH) {
    event.preventDefault();
    return;
  }
});

// Keyup captures every key
phoneNumberInput.addEventListener("keyup", (event) => {
  if (isValidKey(event.key)) {
    const phoneNumber = getUnformattedPhoneNumber(phoneNumberInput.value);
    phoneNumberInput.value = getFormattedPhoneNumber(phoneNumber);
  }
  console.log({
    key: event.key,
    value: phoneNumberInput.value,
  });
});

// Paste needs setTimeout because value is not added when it triggers.
phoneNumberInput.addEventListener("paste", () => {
  setTimeout(() => {
    const phoneNumber = getUnformattedPhoneNumber(phoneNumberInput.value);
    phoneNumberInput.value = getFormattedPhoneNumber(phoneNumber);
  }, 4);
});
