from flask import Flask, render_template
import os

app = Flask(__name__)





def read_description(file_name):
    """Reads the description from a text file, or returns a default message if the file is missing."""
    file_path = os.path.join("TextForArtifacts", file_name)
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read().strip()
    return "Description not available."





@app.route('/')
def homePage():
    return render_template('homepage.html')

@app.route('/say_hi')
def say_hi():
    return render_template('artifact_template.html', 
                           artifact_title="Say Hi, You're on Camera",
                           artifact_description=read_description("SayHi.txt"),
                           image_url_1="static/images/say_hi_camera_1.jpg",
                           image_url_2="static/images/say_hi_camera_2.jpg")

@app.route('/susunu')
def susunu():
    return render_template('artifact_template.html', 
                           artifact_title="Susunu! Denpa Shōnen",
                           artifact_description=read_description("SusunuDenpaiShonen.txt"),
                           image_url_1="static/images/denpa_shonen_1.jpg",
                           image_url_2="static/images/denpa_shonen_2.jpg")

@app.route('/cctv')
def cctv():
    return render_template('artifact_template.html', 
                           artifact_title="CCTV (Closed-Circuit Television)",
                           artifact_description=read_description("CCTV.txt"),
                           image_url_1="static/images/cctv_1.jpg",
                           image_url_2="static/images/cctv_2.jpg")

@app.route('/trumanshow')
def trumanshow():
    return render_template('artifact_template.html', 
                           artifact_title="The Truman Show",
                           artifact_description=read_description("TrumanShow.txt"),
                           image_url_1="static/images/truman_show_1.jpg",
                           image_url_2="static/images/truman_show_2.jpg")

@app.route('/panopticon')
def panopticon():
    return render_template('artifact_template.html', 
                           artifact_title="Panopticon Theory & Building",
                           artifact_description=read_description("Panopticon.txt"),
                           image_url_1="static/images/panopticon_1.jpg",
                           image_url_2="static/images/panopticon_2.jpg")

@app.route('/smart_doorbells')
def smart_doorbells():
    return render_template('artifact_template.html', 
                           artifact_title="Smart Doorbells",
                           artifact_description=read_description("SmartDoorbells.txt"),
                           image_url_1="static/images/smart_doorbell_1.jpg",
                           image_url_2="static/images/smart_doorbell_2.jpg")

@app.route('/body_cams')
def body_cams():
    return render_template('artifact_template.html', 
                           artifact_title="Body Cams",
                           artifact_description=read_description("BodyCams.txt"),
                           image_url_1="static/images/body_cam_1.jpg",
                           image_url_2="static/images/body_cam_2.jpg")

@app.route('/great_firewall')
def great_firewall():
    return render_template('artifact_template.html', 
                           artifact_title="The Great Firewall of China",
                           artifact_description=read_description("GreatFirewall.txt"),
                           image_url_1="static/images/great_firewall_1.jpg",
                           image_url_2="static/images/great_firewall_2.jpg")

@app.route('/smart_city')
def smart_city():
    return render_template('artifact_template.html', 
                           artifact_title="Smart City Surveillance",
                           artifact_description=read_description("SmartCity.txt"),
                           image_url_1="static/images/smart_city_1.jpg",
                           image_url_2="static/images/smart_city_2.jpg")

@app.route('/smile_to_pay')
def smile_to_pay():
    return render_template('artifact_template.html', 
                           artifact_title="Smile to Pay Services",
                           artifact_description=read_description("SmileToPay.txt"),
                           image_url_1="static/images/smile_to_pay_1.jpg",
                           image_url_2="static/images/smile_to_pay_2.jpg")

@app.route('/big_brother')
def big_brother():
    return render_template('artifact_template.html', 
                           artifact_title="Big Brother - 1984",
                           artifact_description=read_description("BigBrother.txt"),
                           image_url_1="static/images/big_brother_1.jpg",
                           image_url_2="static/images/big_brother_2.jpg")

if __name__ == '__main__':
    app.run(debug=True)