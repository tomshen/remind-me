package reminder

import (
    "net/mail"
    "time"
)

type Reminder struct {
    Title string
    Recipient *mail.Address
    Date time.Time
}

func NewReminder(title string, recipient string, date string) error {
    parsedRecipient, err := mail.ParseAddress(recipient)
    if err != nil {
        return err
    }
    parsedDate, err := time.Parse(time.RFC3339, date)
    if err != nil {
        return err
    }
    reminder := Reminder{
        Title: title,
        Recipient: parsedRecipient,
        Date: parsedDate,
    }
    reminder = reminder
    // TODO: write to database
    return nil
}
