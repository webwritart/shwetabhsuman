from PIL import Image
from datetime import datetime


def log(text, category):
    today = str(datetime.today())
    if category == 'error':
        text = f"<p style='line-height:0.1;'> {today} - <span style='color:red;'>{text}</span> <p>\n"
    elif category == 'success':
        text = f"<p style='line-height:0.1;'> {today} - <span style='color:green;'>{text}</span> <p>\n"
    elif category == 'routine':
        text = f"<p style='line-height:0.1;'> {today} - <span style='color:yellow;'>{text}</span> <p>\n"
    elif category == 'none':
        text = f"<p style='line-height:0.1;'> {today} - <span style='color:white;'>{text}</span> <p>\n"
    with open("./routes/templates/manager/log.html", "r") as f:
        contents = f.readlines()
        lines = len(contents)
        index = lines - 4
        contents.insert(index, text)
    with open("./routes/templates/manager/log.html", "w") as f:
        contents = "".join(contents)
        f.write(contents)
        f.close()
    print("logged into log.txt successfully")


def delete_log(date):
    try:
        with open("./routes/templates/manager/log.html", "r") as f:
            contents = f.readlines()
        with open("./routes/templates/manager/log.html", "w") as f:
            for line in contents:
                if "<p" in line:
                    log_date = log_date.replace("<p style='line-height:0.1;'> ", "")
                    log_date = log_date.replace(" - <span style='color:red;'>", "")
                    log_date = log_date.replace("</span> <p>", "")
                    log_date = log_date.split(" ")
                    log_date = log_date[0]
                    if not log_date <= date:
                        f.write(line)
                else:
                    f.write(line)
        f.close()
        log("Successfully deleted log", "success")
    except Exception as e:
        log("Error in deleting log", "error")


def resize_full(img):
    if img.endswith(".jpg"):
        try:
            image = Image.open(img)
            # width, height =
        except Exception as e:
            log("failed to open image", 'error')
    else:
        log("Not JPG format", 'error')


def resize_thumbnail(image):
    image = Image.open(image)
    pass



