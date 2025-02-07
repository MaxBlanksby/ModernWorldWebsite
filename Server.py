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
    # For the homepage, we show a short excerpt from each artifact's full description.
    def excerpt(text, length=150):
        return (text[:length] + "...") if len(text) > length else text

    artifact_groups = [
        {
            "group_title": "Early Basis of Surveillance / Base Theory",
            "artifacts": [
                {
                    "title": "Panopticon",
                    "link": "/panopticon",
                    "image_url": "static/images/panopticon_1.jpg",
                    "description": excerpt(read_description("Panopticon.txt"))
                },
                {
                    "title": "Big Brother (1984)",
                    "link": "/big_brother",
                    "image_url": "static/images/big_brother_1.jpg",
                    "description": excerpt(read_description("BigBrother.txt"))
                },
                {
                    "title": "The Truman Show",
                    "link": "/trumanshow",
                    "image_url": "static/images/truman_show_1.jpg",
                    "description": excerpt(read_description("TrumanShow.txt"))
                }
            ]
        },
        {
            "group_title": "The Rise of Mass Surveillance Technologies",
            "artifacts": [
                {
                    "title": "CCTV",
                    "link": "/cctv",
                    "image_url": "static/images/cctv_1.jpg",
                    "description": excerpt(read_description("CCTV.txt"))
                },
                {
                    "title": "Body Cams",
                    "link": "/body_cams",
                    "image_url": "static/images/body_cam_1.jpg",
                    "description": excerpt(read_description("BodyCams.txt"))
                },
                {
                    "title": "Smart City Surveillance",
                    "link": "/smart_city",
                    "image_url": "static/images/smart_city_1.jpg",
                    "description": excerpt(read_description("SmartCity.txt"))
                }
            ]
        },
        {
            "group_title": "Digital & Personal Surveillance",
            "artifacts": [
                {
                    "title": "Smart Doorbells",
                    "link": "/smart_doorbells",
                    "image_url": "static/images/smart_doorbell_1.jpg",
                    "description": excerpt(read_description("SmartDoorbells.txt"))
                },
                {
                    "title": "Smile to Pay",
                    "link": "/smile_to_pay",
                    "image_url": "static/images/smile_to_pay_1.jpg",
                    "description": excerpt(read_description("SmileToPay.txt"))
                },
                {
                    "title": "The Great Firewall",
                    "link": "/great_firewall",
                    "image_url": "static/images/great_firewall_1.jpg",
                    "description": excerpt(read_description("GreatFirewall.txt"))
                }
            ]
        },
        {
            "group_title": "Surveillance in Entertainment & Reality",
            "artifacts": [
                {
                    "title": "Say Hi, You're on Camera",
                    "link": "/say_hi",
                    "image_url": "static/images/say_hi_camera_1.jpg",
                    "description": excerpt(read_description("SayHi.txt"))
                },
                {
                    "title": "Susunu! Denpa Shōnen",
                    "link": "/susunu",
                    "image_url": "static/images/denpa_shonen_1.jpg",
                    "description": excerpt(read_description("SusunuDenpaiShonen.txt"))
                },
                {
                    "title": "Coming Soon",
                    "link": "#",
                    "image_url": "static/images/coming_soon.jpg",
                    "description": "New artifact information coming soon."
                }
            ]
        }
    ]
    
    # Read transitions from text files.
    # One transition per gap between artifact groups (so for 4 groups, we expect 3 transitions).
    transition_texts = []
    for i in range(1, len(artifact_groups)):
        transition_texts.append(read_description(f"transition{i}.txt"))
    
    return render_template('homepage.html', artifact_groups=artifact_groups, transition_texts=transition_texts)

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