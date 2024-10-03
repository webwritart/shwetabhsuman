from PIL import Image
from datetime import datetime


def log(text, category):
    today = str(datetime.today())
    if category == 'error':
        text = f"        <p style='line-height:0.1;'> {today} - <span style='color:red;'>{text}</span> </p>\n"
    elif category == 'success':
        text = f"        <p style='line-height:0.1;'> {today} - <span style='color:green;'>{text}</span> </p>\n"
    elif category == 'routine':
        text = f"        <p style='line-height:0.1;'> {today} - <span style='color:yellow;'>{text}</span> </p>\n"
    elif category == 'none':
        text = f"        <p style='line-height:0.1;'> {today} - <span style='color:white;'>{text}</span> </p>\n"
    with open("./routes/templates/manager/log.html", "r") as f:
        contents = f.readlines()
        lines = len(contents)
        index = lines - 3
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


def resize_image(img, size_f_t):
    global new_height

    if img.endswith(".jpg"):

        fixed_full_height = 800
        fixed_thumbnail_height = 200

        if size_f_t == 'f':
            new_height = fixed_full_height
        elif size_f_t == 't':
            new_height = fixed_thumbnail_height
        else:
            log("Wrong image size(f/t), miscellaneous", "error")

        try:
            image = Image.open(img)

            width = image.width
            height = image.height
            filename = image.filename
            new_filename = filename.split('.')
            extension = new_filename.pop()
            new_filename = "".join(new_filename)
            if size_f_t == 'f':
                new_filename = f"{new_filename}-f.webp"
            elif size_f_t == 't':
                new_filename = f"{new_filename}-t.webp"

            ratio = (new_height / float(height))
            new_width = int(float(width * ratio))

            image = image.resize((new_width, new_height))
            image = image.convert('RGB')
            image.save(new_filename, 'webp')

        except Exception as e:
            log("failed to open image", 'error')
    else:
        log("Not JPG format", 'error')




