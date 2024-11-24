document.addEventListener("DOMContentLoaded", function() {
    const rowHeight = 41;  // Висота одного рядка в таблиці
    const rowsInput = document.getElementById("rows");

    // Функція для розрахунку кількості рядків на основі висоти екрана
    function calculateRows() {
        const screenHeight = window.innerHeight;
        const rowsPerPage = Math.floor(screenHeight / rowHeight) - 5;  // Врахування заголовка та відступів
        console.log("Calculated rows:", rowsPerPage);  // Вивести значення rows в консоль
        return rowsPerPage;
    }

    // Перевірка, чи сторінка /patients/
    if (window.location.pathname === "/patients/") {
        const urlParams = new URLSearchParams(window.location.search);
        if (!urlParams.has("rows") || urlParams.get("rows") === "") {
            // Якщо параметр rows відсутній або порожній, додаємо його і перезавантажуємо сторінку
            const rows = calculateRows();
            urlParams.set("rows", rows);
            window.location.search = urlParams.toString(); // Перезавантаження з новим параметром
        }
    }

    // Додаємо параметр rows перед надсиланням форми пошуку
    document.getElementById("searchForm").addEventListener("submit", function(event) {
        if (window.location.pathname === "/patients/") {
            const rows = calculateRows();
            const urlParams = new URLSearchParams(window.location.search);
            urlParams.set("rows", rows); // Додаємо параметр rows до форми
            window.location.search = urlParams.toString(); // Перезавантажуємо сторінку з новим параметром rows
        }
    });

    // Додаємо параметр rows тільки для посилань на сторінці /patients/, що містять ?q=
    document.querySelectorAll("a[href^='/patients/?q=']").forEach(link => {
        link.addEventListener("click", function(event) {
            const url = new URL(link.href);
            const rows = calculateRows();
            url.searchParams.set("rows", rows);  // Додаємо параметр rows
            window.location.href = url.toString();
        });
    });
});
