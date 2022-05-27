function showHidePost() {
    var postForm = document.getElementById("postForm")
    var showHideButton = document.getElementById("showHidePostFormButton")
    if (postForm.style.display == "none") {
        postForm.style.display = "block"
        showHideButton.innerHTML = "Hide Form"
    } else {
        postForm.style.display = "none"
        showHideButton.innerHTML = "Write Post!"
    }
}