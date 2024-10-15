document.getElementById("download-form").addEventListener("submit", function (event) {
    event.preventDefault();

    const youtubeLink = document.getElementById("youtube-link").value;
    const statusMessage = document.getElementById("status-message");

    fetch("http://127.0.0.1:8000/download", {
        method: "POST",
        headers: {
            "Content-Type": "application/x-www-form-urlencoded",
        },
        body: new URLSearchParams({
            "link": youtubeLink,
        }),
    })
    .then(response => response.json())
    .then(data => {
        // Display success or error message
        statusMessage.textContent = data.status;
    })
    .catch((error) => {
        statusMessage.textContent = "Error downloading video.";
        console.error("Error:", error);
    });
});
