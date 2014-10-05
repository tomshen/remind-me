package main

import (
    "log"
    "net/http"
    "./reminder"
)

func HomeHandler(w http.ResponseWriter, r *http.Request) {
    http.ServeFile(w, r, "./templates/index.html")
}

func RemindersHandler(w http.ResponseWriter, r *http.Request) {
    if r.Method == "POST" {
        err := reminder.NewReminder(
            r.FormValue("title"),
            r.FormValue("recipient"),
            r.FormValue("date"))
        if err != nil {
            log.Fatal(err)
        }
    } else {
        http.Error(w, "405 method not allowed", http.StatusMethodNotAllowed)
    }
}

func FaviconHandler(w http.ResponseWriter, r *http.Request) {
    http.ServeFile(w, r, "./static/favicon.ico")
}

func main() {
    // Endpoints
    http.HandleFunc("/", HomeHandler)
    http.HandleFunc("/reminders", RemindersHandler)

    // Resources
    http.HandleFunc("/favicon.ico", FaviconHandler)

    http.Handle("/static/",
        http.StripPrefix("/static/", http.FileServer(http.Dir("./dist"))))

    log.Fatal(http.ListenAndServe(":8080", nil))
}
