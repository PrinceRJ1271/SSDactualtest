// Dummy JS file for ESLint scanning

function validateInput(input) {
    const pattern = /^[a-zA-Z0-9_]+$/;
    if (!pattern.test(input)) {
        throw new Error("Invalid input detected");
    }
    return true;
}

// Example usage
try {
    validateInput("Test_123");
    console.log("Input is valid");
} catch (err) {
    console.error("Security Error:", err.message);
}
