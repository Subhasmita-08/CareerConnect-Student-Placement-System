function showMessage() {

    alert(
        "Welcome to CareerConnect! Your career journey starts here."
    );

}


/* =========================
   STUDENT SEARCH
========================= */

function searchStudents() {

    let input =
        document.getElementById("studentSearch");

    let filter =
        input.value.toLowerCase();

    let table =
        document.getElementById("studentTable");

    let rows =
        table.getElementsByTagName("tbody")[0]
            .getElementsByTagName("tr");


    for (let i = 0; i < rows.length; i++) {

        let rowText =
            rows[i].textContent.toLowerCase();

        if (rowText.includes(filter)) {

            rows[i].style.display = "";

        } else {

            rows[i].style.display = "none";

        }

    }

}

function applyJob(companyName) {

    alert(
        "Application started for " +
        companyName +
        ". Application feature will be connected to the database later."
    );

}