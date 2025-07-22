from flask import Flask, render_template_string, jsonify
import random

app = Flask(__name__)

names = ['Aarav', 'Vivaan', 'Aditya', 'Vihaan', 'Arjun', 'Sai', 'Reyansh', 'Ayaan', 'Krishna', 'Ishaan', 'Anaya', 'Siya', 'Pari', 'Avni', 'Myra', 'Aadhya', 'Anika', 'Prisha', 'Riya', 'Saanvi']

HTML = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Baby Name Pro</title>
    <script src="https://unpkg.com/tsparticles@3.3.0/tsparticles.bundle.min.js"></script>
    <audio id="puffSound" src="/static/puff.mp3" preload="auto"></audio>
    <style>
        body { font-family: 'Segoe UI', Arial, sans-serif; background: linear-gradient(120deg, #e0f7fa 0%, #f1f8e9 100%); margin: 0; padding: 0; }
        #tsparticles { position: fixed; top: 0; left: 0; width: 100vw; height: 100vh; z-index: 100; pointer-events: none; }
        .header-bar { width: 100vw; background: #1b4332; color: #fff; display: flex; align-items: center; justify-content: space-between; padding: 0 32px; height: 64px; box-shadow: 0 2px 12px #0002; position: sticky; top: 0; z-index: 200; }
        .header-title { font-size: 1.7em; font-weight: 700; letter-spacing: 1px; display: flex; align-items: center; }
        .header-title span { font-size: 1.2em; margin-right: 10px; }
        .lang-switch { background: #fff; color: #1b4332; border: none; border-radius: 5px; font-size: 1em; font-weight: 600; padding: 7px 18px; cursor: pointer; margin-left: 18px; transition: background 0.2s; }
        .lang-switch.active, .lang-switch:hover { background: #40916c; color: #fff; }
        .main-section { max-width: 540px; margin: 38px auto 30px auto; background: #fff; border-radius: 16px; box-shadow: 0 4px 24px #0002; padding: 40px 32px 32px 32px; position: relative; z-index: 2; }
        .section-title { color: #1b4332; font-size: 1.5em; margin-bottom: 0.2em; text-align: center; font-weight: 700; }
        .section-desc { color: #40916c; font-size: 1.13em; margin-bottom: 1.7em; text-align: center; }
        .step-section { display: none; }
        .step-section.active { display: block; }
        label { display: block; margin: 18px 0 6px; font-weight: 500; color: #222; }
        input, select { width: 100%; padding: 10px; border-radius: 6px; border: 1px solid #b7e4c7; font-size: 1em; background: #f8fafc; margin-bottom: 2px; }
        button { margin-top: 28px; padding: 14px 0; width: 100%; font-size: 1.15em; background: linear-gradient(90deg, #40916c 60%, #52b788 100%); color: white; border: none; border-radius: 6px; cursor: pointer; font-weight: 600; letter-spacing: 1px; transition: background 0.2s; }
        button:hover { background: linear-gradient(90deg, #1b4332 60%, #40916c 100%); }
        .result-3d { margin-top: 36px; background: rgba(255,255,255,0.95); border-radius: 16px; box-shadow: 0 2px 16px #0002; padding: 38px 18px; font-size: 1.5em; color: #2d6a4f; font-weight: 700; text-align: center; animation: popIn 1s cubic-bezier(.68,-0.55,.27,1.55); position: relative; z-index: 3; }
        @keyframes popIn { 0% { transform: scale(0.7); opacity: 0; } 100% { transform: scale(1); opacity: 1; } }
        .flower-emoji { font-size: 2.2em; margin: 0 0.2em; animation: floatFlower 1.5s infinite alternate; }
        @keyframes floatFlower { 0% { transform: translateY(0); } 100% { transform: translateY(-12px); } }
        footer { text-align: center; color: #888; font-size: 0.98em; margin-top: 30px; padding-bottom: 18px; }
        @media (max-width: 600px) { .main-section { padding: 18px 4vw; } .header-bar { padding: 0 8px; } }
    </style>
</head>
<body>
    <div id="tsparticles"></div>
    <div class="header-bar">
        <div class="header-title"><span>👶</span> Baby Name Generator</div>
        <div>
            <button class="lang-switch active" id="langHindi">हिंदी</button>
            <button class="lang-switch" id="langEnglish">English</button>
        </div>
    </div>
    <div class="main-section">
        <form id="babyForm">
            <div class="step-section active" id="step1">
                <div class="section-title" id="mainTitle">Find the Perfect Baby Name!</div>
                <div class="section-desc" id="mainDesc">A modern, interactive way to discover a meaningful name for your newborn.</div>
                <label for="parent" id="labelParent">Parent Name</label>
                <input type="text" id="parent" name="parent" placeholder="e.g. Suresh & Sunita" required>
                <label for="nationality" id="labelNationality">Nationality</label>
                <select id="nationality" name="nationality" required>
                    <option value="Indian">Indian</option>
                    <option value="Foreigner">Foreigner</option>
                </select>
                <label for="suggested" id="labelSuggested">Names you are considering for your baby</label>
                <input type="text" id="suggested" name="suggested" placeholder="e.g. Aarav, Vivaan, Emma" required>
                <button type="button" onclick="nextStep(2)" id="toKidDetail">Next</button>
            </div>
            <div class="step-section" id="step2">
                <label for="hobby" id="labelHobby">Your Hobby</label>
                <input type="text" id="hobby" name="hobby" placeholder="e.g. Singing, Reading" required>
                <label for="character" id="labelCharacter">Your Favorite Character</label>
                <input type="text" id="character" name="character" placeholder="e.g. Krishna, Harry Potter" required>
                <label for="gender" id="labelGender">Gender</label>
                <select id="gender" name="gender" required>
                    <option value="Boy">Boy</option>
                    <option value="Girl">Girl</option>
                    <option value="Other">Other</option>
                </select>
                <label for="field" id="labelField">Field you want for your child</label>
                <select id="field" name="field" required>
                    <option value="Science">Science</option>
                    <option value="Sports">Sports</option>
                    <option value="Arts">Arts</option>
                    <option value="Business">Business</option>
                    <option value="Technology">Technology</option>
                    <option value="Other">Other</option>
                </select>
                <label for="dream" id="labelDream">Your dream for your child</label>
                <input type="text" id="dream" name="dream" placeholder="e.g. Doctor, Leader, Artist" required>
                <label for="qualities" id="labelQualities">Qualities you want in your child</label>
                <input type="text" id="qualities" name="qualities" placeholder="e.g. Honest, Brave, Creative" required>
                <button type="button" onclick="nextStep(1)">Back</button>
                <button type="button" id="kidNameBtn">Reveal</button>
            </div>
            <div class="step-section" id="step3">
                <div class="result-3d" id="result" style="display:none;"></div>
                <button type="button" id="anotherNameBtn">Suggest Another Name</button>
            </div>
        </form>
        <div class="result-3d" id="result" style="display:none;"></div>
    </div>
    <footer>
        &copy; 2025 BabyNamePro | Designed with ❤️ for new parents
    </footer>
    <script>
    document.addEventListener('DOMContentLoaded', function() {
        // Language switch logic
        const langMap = {
            en: {
                mainTitle: 'Find the Perfect Baby Name!',
                mainDesc: 'A modern, interactive way to discover a meaningful name for your newborn.',
                labelParent: 'Parent Name',
                labelNationality: 'Nationality',
                labelSuggested: 'Names you are considering for your baby',
                labelHobby: 'Your Hobby',
                labelCharacter: 'Your Favorite Character',
                labelGender: 'Gender',
                labelField: 'Field you want for your child',
                labelDream: 'Your dream for your child',
                labelQualities: 'Qualities you want in your child',
                toKidDetail: 'Next',
                kidNameBtn: 'Reveal Name',
                anotherNameBtn: 'Suggest Another Name',
            },
            hi: {
                mainTitle: 'अपने बच्चे के लिए परफेक्ट नाम खोजें!',
                mainDesc: 'अपने नवजात के लिए एक अर्थपूर्ण नाम खोजने का आधुनिक, इंटरैक्टिव तरीका।',
                labelParent: 'माता-पिता का नाम',
                labelNationality: 'राष्ट्रीयता',
                labelSuggested: 'आप अपने बच्चे के लिए कौन-कौन से नाम सोच रहे हैं?',
                labelHobby: 'आपकी हॉबी',
                labelCharacter: 'आपका पसंदीदा किरदार',
                labelGender: 'लिंग',
                labelField: 'बच्चे को किस क्षेत्र में भेजना है?',
                labelDream: 'आप अपने बच्चे को क्या बनाना चाहते हैं?',
                labelQualities: 'बच्चे में कौन सी खूबियां चाहेंगे?',
                toKidDetail: 'आगे',
                kidNameBtn: 'नाम दिखाएं',
                anotherNameBtn: 'कोई दूसरा नाम',
            }
        };
        function setLang(lang) {
            const t = langMap[lang];
            document.getElementById('mainTitle').innerText = t.mainTitle;
            document.getElementById('mainDesc').innerText = t.mainDesc;
            document.getElementById('labelParent').innerText = t.labelParent;
            document.getElementById('labelNationality').innerText = t.labelNationality;
            document.getElementById('labelSuggested').innerText = t.labelSuggested;
            document.getElementById('labelHobby').innerText = t.labelHobby;
            document.getElementById('labelCharacter').innerText = t.labelCharacter;
            document.getElementById('labelGender').innerText = t.labelGender;
            document.getElementById('labelField').innerText = t.labelField;
            document.getElementById('labelDream').innerText = t.labelDream;
            document.getElementById('labelQualities').innerText = t.labelQualities;
            document.getElementById('toKidDetail').innerText = t.toKidDetail;
            document.getElementById('kidNameBtn').innerText = t.kidNameBtn;
            document.getElementById('anotherNameBtn').innerText = t.anotherNameBtn;
            document.getElementById('langHindi').classList.toggle('active', lang === 'hi');
            document.getElementById('langEnglish').classList.toggle('active', lang === 'en');
        }
        document.getElementById('langHindi').onclick = function() { setLang('hi'); };
        document.getElementById('langEnglish').onclick = function() { setLang('en'); };
        setLang('en');
        // Debug: check if tsParticles loaded
        if (typeof tsParticles === 'undefined') {
            alert('tsParticles is not loaded! Check if /static/tsparticles.bundle.min.js is present and accessible.');
            return;
        }
        // Track if tsParticles is loaded
        window.tsparticlesLoaded = false;
        // Multi-step form logic
        function nextStep(step) {
            document.getElementById('step1').classList.toggle('active', step === 1);
            document.getElementById('step2').classList.toggle('active', step === 2);
            document.getElementById('step3').classList.toggle('active', step === 3);
        }
        window.nextStep = nextStep;

        // 3D flower rain animation using tsParticles
        let flowerRainActive = false;
        let flowerRainTimeout = null;
        let flowerRainInterval = null;
        window.startFlowerRain = function(durationMs = 2000) {
            // Always destroy and reload, then add particles only after new instance is ready
            let instance = tsParticles.dom()[0];
            if (!instance) instance = tsParticles.domItem(0);
            if (instance) instance.destroy();
            tsParticles.load("tsparticles", {
                "particles": {
                    "number": { "value": 0 },
                    "shape": {
                        "type": "image",
                        "image": [
                            { "src": "/static/Phool.jpg", "width": 48, "height": 48 }
                        ]
                    },
                    "size": { "value": 32 },
                    "move": { "enable": true, "speed": 2.5, "direction": "bottom", "outModes": { "default": "out" } },
                    "opacity": { "value": 0.92 }
                },
                "interactivity": {
                    "events": { "onClick": { "enable": false }, "onHover": { "enable": false } }
                },
                "detectRetina": true
            }).then(newInstance => {
                // Add 10 flower images from just below the header
                const flowerImage = '/static/Phool.jpg';
                const manualParticles = Array.from({length: 10}, () => ({
                    position: { x: Math.random() * window.innerWidth, y: 64 },
                    size: { value: 20 },
                    shape: {
                        type: 'image',
                        options: {
                            image: [
                                { src: flowerImage, width: 32, height: 32 }
                            ]
                        }
                    }
                }));
                newInstance.particles.addManualParticles(manualParticles);
            });
        };

        tsParticles.load("tsparticles", {
            "particles": {
                "number": { "value": 0 },
                "shape": {
                    "type": "image",
                    "image": [
                        { "src": "/static/Phool.jpg", "width": 48, "height": 48 }
                    ]
                },
                "size": { "value": 32 },
                "move": { "enable": true, "speed": 2.5, "direction": "bottom", "outModes": { "default": "out" } },
                "opacity": { "value": 0.92 }
            },
            "interactivity": {
                "events": { "onClick": { "enable": false }, "onHover": { "enable": false } }
            },
            "detectRetina": true
        }).then(() => {
            // Mark tsParticles as loaded
            window.tsparticlesLoaded = true;
            // Debug: confirm image loaded
            const img = new window.Image();
            img.src = '/static/Phool.jpg';
            img.onload = () => console.log('Loaded:', img.src);
            img.onerror = () => console.error('Could not load:', img.src);
            // Step 2: Kid Name button
            document.getElementById('kidNameBtn').onclick = function() {
                const data = {
                    parent: document.getElementById('parent').value,
                    nationality: document.getElementById('nationality').value,
                    suggested: document.getElementById('suggested').value,
                    hobby: document.getElementById('hobby').value,
                    character: document.getElementById('character').value,
                    gender: document.getElementById('gender').value,
                    field: document.getElementById('field').value,
                    dream: document.getElementById('dream').value,
                    qualities: document.getElementById('qualities').value
                };
                fetch('/suggest-name', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify(data)
                })
                .then(r => r.json())
                .then(res => {
                    // Play puff sound and trigger flower rain at the same time
                    const puff = document.getElementById('puffSound');
                    try {
                        puff.currentTime = 0;
                        puff.play().catch(()=>{});
                    } catch(e) {}
                    window.startFlowerRain();
                    // Show gender and name reveal (no static flower emojis, only animation)
                    const resultDiv = document.getElementById('result');
                    resultDiv.innerHTML = `<div style='font-size:1.2em;margin-bottom:10px;'>🎉 Gender Reveal: <b>${data.gender}</b></div>${res.suggestion}`;
                    resultDiv.style.display = 'block';
                    window.scrollTo({ top: 0, behavior: 'smooth' });
                    nextStep(3);
                });
            };
            // Step 3: Koi Dusra Naam button
            document.getElementById('anotherNameBtn').onclick = function() {
                const data = {
                    parent: document.getElementById('parent').value,
                    nationality: document.getElementById('nationality').value,
                    suggested: document.getElementById('suggested').value,
                    hobby: document.getElementById('hobby').value,
                    character: document.getElementById('character').value,
                    gender: document.getElementById('gender').value,
                    field: document.getElementById('field').value,
                    dream: document.getElementById('dream').value,
                    qualities: document.getElementById('qualities').value
                };
                fetch('/suggest-name', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify(data)
                })
                .then(r => r.json())
                .then(res => {
                    // Play puff sound and trigger flower rain at the same time
                    const puff = document.getElementById('puffSound');
                    try {
                        puff.currentTime = 0;
                        puff.play().catch(()=>{});
                    } catch(e) {}
                    window.startFlowerRain();
                    // Show gender and name reveal (no static flower emojis, only animation)
                    const resultDiv = document.getElementById('result');
                    resultDiv.innerHTML = `<div style='font-size:1.2em;margin-bottom:10px;'>🎉 Gender Reveal: <b>${data.gender}</b></div>${res.suggestion}`;
                    resultDiv.style.display = 'block';
                    window.scrollTo({ top: 0, behavior: 'smooth' });
                });
            };
        });
    });
    </script>
</body>
</html>
'''


@app.route('/')
def home():
    return render_template_string(HTML)


# Suggest name based on user input
@app.route('/suggest-name', methods=['POST'])
def suggest_name():
    from flask import request
    data = request.get_json()
    parent = data.get('parent', '')
    nationality = data.get('nationality', 'Indian')
    suggested = data.get('suggested', '')
    hobby = data.get('hobby', '')
    character = data.get('character', '')
    gender = data.get('gender', '')
    field = data.get('field', '')
    dream = data.get('dream', '')
    qualities = data.get('qualities', '')


    # Name pools by gender
    indian_boy_names = ['Aarav', 'Vivaan', 'Aditya', 'Vihaan', 'Arjun', 'Sai', 'Reyansh', 'Ayaan', 'Krishna', 'Ishaan']
    indian_girl_names = ['Anaya', 'Siya', 'Pari', 'Avni', 'Myra', 'Aadhya', 'Anika', 'Prisha', 'Riya', 'Saanvi']
    foreign_boy_names = ['Liam', 'Noah', 'Mason', 'Lucas', 'Benjamin', 'Elijah', 'James', 'Logan', 'Ethan', 'Jack', 'Henry']
    foreign_girl_names = ['Emma', 'Olivia', 'Sophia', 'Mia', 'Charlotte', 'Amelia', 'Ava', 'Isabella', 'Harper']

    # User suggested names (comma separated)
    user_names = [n.strip() for n in suggested.split(',') if n.strip()]

    # Choose name pool by gender and nationality
    if nationality == 'Indian':
        if gender == 'Boy':
            pool = indian_boy_names + user_names
        elif gender == 'Girl':
            pool = indian_girl_names + user_names
        else:
            pool = indian_boy_names + indian_girl_names + user_names
    else:
        if gender == 'Boy':
            pool = foreign_boy_names + user_names
        elif gender == 'Girl':
            pool = foreign_girl_names + user_names
        else:
            pool = foreign_boy_names + foreign_girl_names + user_names

    # Enhanced logic: combine all inspirations
    vibe = (character + ' ' + field + ' ' + dream + ' ' + hobby + ' ' + qualities).lower()
    filtered = [n for n in pool if n and n.lower()[0] in vibe]
    if filtered:
        name = random.choice(filtered)
    elif pool:
        name = random.choice(pool)
    else:
        name = 'No Name Found'
    suggestion = f"Namaste {parent}! Aapke bacche ke liye sujhav hai: <span style='color:#40916c;font-size:1.3em'>{name}</span>"
    return jsonify({'suggestion': suggestion})

if __name__ == '__main__':
    app.run(debug=True)




