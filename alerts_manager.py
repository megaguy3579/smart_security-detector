def save_alerts(alerts) :
    with open("alerts.txt", "a") as file :
        for alert in alerts :
            file.write(alert + "\n")
          
