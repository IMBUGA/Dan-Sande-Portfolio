// portF.js
// Function to handle the form submission
        function showMessage(message) {
            alert(message);
        }

        document.addEventListener("DOMContentLoaded", function () {
            const greeting = document.getElementById("greeting");
            let greetings = ["Hello!", "Welcome!", "Hi, I'm Daniel!", "Nice to meet you!"];
            let index = 0;
        });
            document.addEventListener("DOMContentLoaded", function () {
                const greeting = document.getElementById("greeting");
                if (!greeting) {
                    console.error("Element with id 'greeting' not found.");
                    return;
                }
                let greetings = ["Hello!", "Welcome!", "Hi, I'm Daniel!", "Nice to meet you!"];
                let index = 0;

                setInterval(() => {
                    greeting.innerText = greetings[index];
                    index = (index + 1) % greetings.length;
                }, 3000);
            });