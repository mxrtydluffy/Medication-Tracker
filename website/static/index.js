/*
Takes medId that is being passed to the POST request
to delte the last med. Once it gets a response its going to
reload the window and refresh the page
*/

function deleteMed(medId) {
    fetch("/delete-med", {
        method: "POST",
        body: JSON.stringify({ medId: medId }),
    }).then((_res) => {
        window.location.href = "/";
    });
}