document.addEventListener("DOMContentLoaded", function () {
    const dropArea = document.getElementById("drop-area");
    const fileInput = document.getElementById("file-input");
    const form = document.getElementById("upload-form");
    const previewArea = document.getElementById("preview-area");
    const previewImg = document.getElementById("preview-img");
    const resultText = document.getElementById("result-text");

    dropArea.addEventListener("dragover", (e) => {
        e.preventDefault();
        dropArea.style.borderColor = "#3498db";
    });

    dropArea.addEventListener("dragleave", (e) => {
        e.preventDefault();
        dropArea.style.borderColor = "#b2bec3";
    });

    dropArea.addEventListener("drop", (e) => {
        e.preventDefault();
        dropArea.style.borderColor = "#b2bec3";
        const files = e.dataTransfer.files;
        if (files.length > 0) {
            uploadFile(files[0]);
        }
    });

    fileInput.addEventListener("change", function () {
        if (this.files.length > 0) {
            uploadFile(this.files[0]);
        }
    });

    function uploadFile(file) {
        const formData = new FormData(form);
        formData.set("image", file);

        fetch("/upload-image/", {
            method: "POST",
            headers: { "X-CSRFToken": getCSRFToken() },
            body: formData,
        })
            .then((response) => response.json())
            .then((data) => {
                previewImg.src = data.image_url;
                previewArea.style.display = "block";
                resultText.innerText = `Prediction: ${data.result}`;
            })
            .catch((error) => {
                resultText.innerText = "Error: " + error;
            });
    }

    function getCSRFToken() {
        return document.querySelector("[name=csrfmiddlewaretoken]").value;
    }
});
