// Dummy JS file for ESLint scanning

function validateInput(input) {
  const pattern = /^[a-zA-Z0-9_]+$/;
  if (!pattern.test(input)) {
    throw new Error("Invalid input detected");
  }
  return true;
}
