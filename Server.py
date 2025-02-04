from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def homePage():
    return render_template('homepage.html')

@app.route('/say_hi')
def say_hi():
    return render_template('artifact_template.html', 
                           artifact_title="Say Hi, You're on Camera",
                           artifact_description="A common sign in public places, reminding individuals of constant surveillance. It influences behavior and self-regulation, reflecting Foucauldian discipline.",
                           image_url_1="static/images/say_hi_camera.jpg",
                           image_url_2="static/images/surveillance_sign.jpg")

@app.route('/susunu')
def susunu():
    return render_template('artifact_template.html', 
                           artifact_title="Susunu! Denpa Shōnen",
                           artifact_description="A controversial Japanese reality show where a contestant was unknowingly subjected to extreme surveillance, raising ethical concerns.",
                           image_url_1="static/images/denpa_shonen_1.jpg",
                           image_url_2="static/images/denpa_shonen_2.jpg")

@app.route('/cctv')
def cctv():
    return render_template('artifact_template.html', 
                           artifact_title="CCTV (Closed-Circuit Television)",
                           artifact_description="Used worldwide for security and surveillance, CCTV cameras shape public and private spaces, influencing behavior and crime prevention.",
                           image_url_1="static/images/cctv_1.jpg",
                           image_url_2="static/images/cctv_2.jpg")

@app.route('/trumanshow')
def trumanshow():
    return render_template('artifact_template.html', 
                           artifact_title="The Truman Show",
                           artifact_description="A fictional story reflecting real concerns about constant surveillance and the illusion of personal freedom in a controlled society.",
                           image_url_1="static/images/truman_show_1.jpg",
                           image_url_2="static/images/truman_show_2.jpg")

@app.route('/panopticon')
def panopticon():
    return render_template('artifact_template.html', 
                           artifact_title="Panopticon Theory & Building",
                           artifact_description="A prison design and social theory by Jeremy Bentham and Michel Foucault, illustrating how surveillance shapes power and self-discipline.",
                           image_url_1="static/images/panopticon_1.jpg",
                           image_url_2="static/images/panopticon_2.jpg")

@app.route('/smart_doorbells')
def smart_doorbells():
    return render_template('artifact_template.html', 
                           artifact_title="Smart Doorbells",
                           artifact_description="Devices like Ring and Nest allow homeowners to monitor their surroundings, raising privacy and data security concerns.",
                           image_url_1="static/images/smart_doorbell_1.jpg",
                           image_url_2="static/images/smart_doorbell_2.jpg")

@app.route('/body_cams')
def body_cams():
    return render_template('artifact_template.html', 
                           artifact_title="Body Cams",
                           artifact_description="Widely used in law enforcement, body cameras aim to increase transparency but also introduce surveillance and ethical dilemmas.",
                           image_url_1="static/images/body_cam_1.jpg",
                           image_url_2="static/images/body_cam_2.jpg")

@app.route('/great_firewall')
def great_firewall():
    return render_template('artifact_template.html', 
                           artifact_title="The Great Firewall of China",
                           artifact_description="A sophisticated system of censorship and surveillance, controlling internet access and restricting information flow.",
                           image_url_1="static/images/great_firewall_1.jpg",
                           image_url_2="static/images/great_firewall_2.jpg")

@app.route('/smart_city')
def smart_city():
    return render_template('artifact_template.html', 
                           artifact_title="Smart City Surveillance",
                           artifact_description="Cities worldwide use AI and big data to monitor activity, raising debates over security versus privacy.",
                           image_url_1="static/images/smart_city_1.jpg",
                           image_url_2="static/images/smart_city_2.jpg")

@app.route('/smile_to_pay')
def smile_to_pay():
    return render_template('artifact_template.html', 
                           artifact_title="Smile to Pay Services",
                           artifact_description="Facial recognition payment systems create seamless transactions but introduce concerns about biometric data privacy.",
                           image_url_1="static/images/smile_to_pay_1.jpg",
                           image_url_2="static/images/smile_to_pay_2.jpg")

@app.route('/big_brother')
def big_brother():
    return render_template('artifact_template.html', 
                           artifact_title="Big Brother - 1984",
                           artifact_description="A dystopian vision of government surveillance and control from George Orwell’s novel *1984*, eerily relevant today.",
                           image_url_1="static/images/big_brother_1.jpg",
                           image_url_2="static/images/big_brother_2.jpg")

if __name__ == '__main__':
    app.run(debug=True)
