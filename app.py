import re
import random
import streamlit as st

# Define tourist places only for AlUla
tourist_places = {
    "العلا": [
        " مدائن صالح - موقع أثري يعود إلى الحضارة النبطية ويعد أحد مواقع التراث العالمي لليونسكو.",
        " جبل الفيل - صخرة ضخمة على شكل فيل تُعد من أشهر معالم العلا.",
        " البلدة القديمة - تجمع تاريخي يعكس الطابع التراثي للعلا.",
        " واحة العلا - منطقة طبيعية رائعة تحيط بها أشجار النخيل.",
        " منتجع شادن - مكان مثالي للاسترخاء وسط الطبيعة الخلابة."
    ], 
    "الرياض": 
    [
        "بوليفارد رياض سيتي, وجهة ترفيهية متكاملة تضم مطاعم ومقاهي وعروض ترفيهية",
        "حديقة الملك عبدالله, حديقة جميلة تحتوي على مساحات خضراء وبحيرات ونوافير راقص ", 
        "المتحف الوطني السعودي, مكان غني بالمعلومات عن تاريخ السعودية وحضارتها", 
        "وادي حنيفة, موقع طبيعي جميل مناسب للمشي والتنزه",
        "برج المملكة, برج يضم سوقًا ومطاعم وإطلالة بانورامية على الرياض."

    ], 
    "جدة"or"جده": 
    [
        "جدة: جدة مدينة ساحلية رائعة على البحر الأحمر وتضم العديد من المعالم السياحية مثل البلد ، نادي اليخوت ، والعديد !",
        "البلد: البلد هو حي في مدينة جدة، وهو من الأحياء القديمة ذات الطابع التاريخي والثقافي العريق. يتميز هذا الحي بجوّه التقليدي الذي يعكس تاريخ مدينة جدة العميق، وهو يعد واحدًا من أشهر معالم المدينة.",
        "نافورة الملك فهد: تعد نافورة الملك فهد أطول نافورة في العالم، وتضيء سماء جدة ليلاً.",
        "الكورنيش: كورنيش جدة مثالي للاستمتاع بإطلالة البحر الأحمر، والمشي أو ركوب الدراجات.",
        "نادي اليخوت: نادي اليخوت من أفضل الأماكن للاستمتاع بمشاهد البحر الأحمر والأنشطة المائية.",
        "البروميناد: مكان رائع للتسوق والاستمتاع بالأجواء البحرية مع العديد من المطاعم والمقاهي.",
         "سيتي ووك: مركز ترفيهي يضم أنشطة ممتعة مثل العروض الحية والمطاعم.",
        "المطاعم الشهيرة: بعض المطاعم الشهيرة في جدة: مطعم النافورة، مطعم البيك، ومطعم بوقا.",
        "المعالم السياحية: تضم جدة العديد من المعالم السياحية مثل البلد ، نادي اليخوت ، نافورة الملك فهد، جدة، بير ، البروميناد، سيتي ووك، وبعض من المطاعم الشهيرة.",
    ],
    "القصيم": 
    [
        "برج الشنانة: برج الشنانة هو معلم تاريخي يقع في محافظة الرس، وهو برج مراقبة بُني قبل أكثر من 200 عام، ويعد من الشواهد التاريخية في القصيم.",
        "سوق المسوكف: سوق المسوكف هو سوق تراثي في عنيزة يعكس الطراز العمراني القديم ويضم متاجر للحرف اليدوية والمنتجات التقليدية.",
        "متحف العقيلات: متحف العقيلات في بريدة يعرض تاريخ قوافل العقيلات الذين كانوا يسافرون للتجارة بين الجزيرة العربية والشام والعراق.",
        "قرية المذنب التراثية: قرية المذنب التراثية هي قرية تاريخية تمثل الطراز المعماري القديم لمنطقة القصيم، وتضم بيوتًا طينية وأسواقًا قديمة تعكس التراث الشعبي."
    ], 
    "أبها"or "ابها": 
    [
        "ابها: أبها تتميز بمناظرها الخلابة مثل جبل السودة وحديقة أبو خيال! 🌿",
    "السودة: السودة تقع في منطقة عسير جنوب السعودية، وهي واحدة من أجمل الوجهات السياحية في المملكة. تتميز بارتفاعها الذي يصل إلى 3,015 مترًا فوق سطح البحر، مما يجعلها المكان الأبرد في المملكة. مناخها معتدل صيفًا وبارد شتاءً، لذا احرص على إحضار ملابس دافئة حتى في الصيف.",
    "حديقة ابو خيال: تقع على حافة جبال السودة، وتوفر إطلالات بانورامية رائعة على مدينة أبها. مثالية للعائلات ومحبي الهدوء، مع مساحات خضراء واسعة ومناطق للجلوس. تضم ممرات للمشي، وملعب أطفال، وكافيهات بسيطة للاستراحة. موطن للعديد من القرود البرية، لذا يُفضل الحذر عند إحضار الطعام. أفضل وقت للزيارة: الصباح الباكر أو قبل الغروب للاستمتاع بالمشهد البانورامي."
    ],
    


}

# Random greetings
greetings = ["هلا والله!", "أهلًا وسهلًا!", "مرحبا!", "يا هلا! كيف أقدر أساعدك؟", "هلا والله! وش حاب أقترح لك أماكن تزورها؟", 
             "مرحبًا! تبي تعرف عن الأماكن السياحية في المملكة العربية السعودية", "أهلًا! ودّك تعرف عن الأماكن الحلوة في اي منطقة من المذكورة فوق ؟", 
             "هلا! تبي تعرف عن الأماكن السياحية في السعودية؟"]

# Random denial responses for unrelated questions
denial_responses = [
    "أنا أجاوب عن السياحة فقط، اسألني عن الأماكن الحلوة! 😊",
    "ما أقدر أجاوب على هذا، لكن أقدر أقترح لك أماكن سياحية رائعة! 🌍",
    "خلنا بس في السياحة، وش المكان اللي تحب تعرف عنه؟ 🏝",
    "ما فهمت سؤالك، بس أقدر أساعدك في السياحة! 🤖",
    "ما عندي فكرة عن هذا، بس عندي فكرة عن الأماكن السياحية! 🏞",
    "للأسف، معلوماتي عن السياحة فقط! ودّك تسافر للعلا؟ أقدر أرشح لك أماكن حلوة ✈️",
    "أنا متخصص في السياحة، تبي تعرف عن أماكن مميزة؟"
]

# Define the NLP model responses uising regex patterns
patterns = [
    # More flexible greetings matching 

                                        #AlUla
    (r'^(مرحبا|هلا|أهلًا|اهلين|السلام عليكم|السلام)$', lambda: random.choice(greetings)),  
    
    # Thank you responses
    (r'^(شكرا|شكراً|شكرًا|مشكور|يعطيك العافية)$', lambda: "على الرحب والسعة! 😃"),  
    # This pattern now matches when "العلا" appears anywhere in the sentence along with suggestion words
    (r'(تقدر|يمكنك|ممكن|هل).*?(اقتراح|تقترح|ترشيح|تنصحني|تعطيني|ترشح).*?(العلا)', 
     lambda: "🏕 بالطبع! يمكنك زيارة:\n- " + "\n- ".join(tourist_places["العلا"])),
    # Add separate pattern to catch queries containing both "places" and "AlUla" --
    (r'(مكان|اماكن|أماكن|محلات).*?(العلا)|(العلا).*?(مكان|اماكن|أماكن|محلات)', 
     lambda: "✨ الأماكن السياحية في العلا:\n- " + "\n- ".join(tourist_places["العلا"])),
        # Detecting best places in AlUla with more flexibility
    (r'(ايش|ما هي|ماهو|ممكن تقولي|ودِّي أعرف).*?(افضل|أحسن|أروع).*?(الأماكن|الاماكن).*?(في العلا|بالعلا|العلا)', 
     lambda: "✨ الأماكن السياحية في العلا:\n- " + "\n- ".join(tourist_places["العلا"])),  
        # Matching "I want to travel to AlUla" + "suggest places"
    (r'.*(أريد|ودي|نفسي|حابب).*?(أسافر|أزور|أروح).*?(إلى العلا|للعلا|العلا).*?(مكان|أماكن|ترشيح|اقتراح|تنصحني|تعطيني)?.*?',
     lambda: "🚗 رائع! هذه بعض الأماكن التي يمكنك زيارتها في العلا:\n- " + "\n- ".join(tourist_places["العلا"])),  
    # If the user just says "العلا", assume they want tourist places
    (r'^(العلا|في العلا|بالعلا)$', 

     lambda: "✨ الأماكن السياحية في العلا:\n- " + "\n- ".join(tourist_places["العلا"])),  
                                        #ٌRiyadh
    (r'^(شكرا|شكراً|شكرًا|مشكور|يعطيك العافية)$', lambda: "على الرحب والسعة! 😃"),  
    # This pattern now matches when "الرياض" appears anywhere in the sentence along with suggestion words
    (r'(تقدر|يمكنك|ممكن|هل).*?(اقتراح|تقترح|ترشيح|تنصحني|تعطيني|ترشح).*?(الرياض)', 
     lambda: "🏙 بالطبع! يمكنك زيارة:\n- " + "\n- ".join(tourist_places["الرياض"])),
    # Add separate pattern to catch queries containing both "places" and "Riyadh" --
    (r'(مكان|اماكن|أماكن|محلات).*?(الرياض)|(الرياض).*?(مكان|اماكن|أماكن|محلات)', 
     lambda: "✨ الأماكن السياحية في الرياض:\n- " + "\n- ".join(tourist_places["الرياض"])),
        # Detecting best places in Riyadh with more flexibility
    (r'(ايش|ما هي|ماهو|ممكن تقولي|ودِّي أعرف).*?(افضل|أحسن|أروع).*?(الأماكن|الاماكن).*?(في الرياض|بالرياض|الرياض)', 
     lambda: "✨ الأماكن السياحية في الرياض:\n- " + "\n- ".join(tourist_places["الرياض"])),  
        # Matching "I want to travel to Riyadh" + "suggest places"
    (r'.*(أريد|ودي|نفسي|حابب).*?(أسافر|أزور|أروح).*?(إلى الرياض|للرياض|الرياض).*?(مكان|أماكن|ترشيح|اقتراح|تنصحني|تعطيني)?.*?',
     lambda: "🚗 رائع! هذه بعض الأماكن التي يمكنك زيارتها في الرياض:\n- " + "\n- ".join(tourist_places["الرياض"])),  
    # If the user just says "الرياض", assume they want tourist places
    (r'^(الرياض|في الرياض|بالرياض)$', 
     lambda: "✨ الأماكن السياحية في الرياض:\n- " + "\n- ".join(tourist_places["الرياض"])),  

                                        #Jeddah 
    (r'^(شكرا|شكراً|شكرًا|مشكور|يعطيك العافية)$', lambda: "على الرحب والسعة! 😃"),  
    # This pattern now matches when "جدة" appears anywhere in the sentence along with suggestion words
    (r'(تقدر|يمكنك|ممكن|هل).*?(اقتراح|تقترح|ترشيح|تنصحني|تعطيني|ترشح).*?(جدة)', 
     lambda: "🌊 بالطبع! يمكنك زيارة:\n- " + "\n- ".join(tourist_places["جدة"])),
    # Add separate pattern to catch queries containing both "places" and "Jeddah" --
    (r'(مكان|اماكن|أماكن|محلات).*?(جدة)|(جدة).*?(مكان|اماكن|أماكن|محلات)', 
     lambda: "✨ الأماكن السياحية في جدة:\n- " + "\n- ".join(tourist_places["جدة"])),
        # Detecting best places in Jeddah with more flexibility
    (r'(ايش|ما هي|ماهو|ممكن تقولي|ودِّي أعرف).*?(افضل|أحسن|أروع).*?(الأماكن|الاماكن).*?(في جدة|بجدة|جدة)', 
     lambda: "✨ الأماكن السياحية في جدة:\n- " + "\n- ".join(tourist_places["جدة"])),  
        # Matching "I want to travel to Jeddah" + "suggest places"
    (r'.*(أريد|ودي|نفسي|حابب).*?(أسافر|أزور|أروح).*?(إلى جدة|لجدة|جدة).*?(مكان|أماكن|ترشيح|اقتراح|تنصحني|تعطيني)?.*?',
     lambda: "🚢 رائع! هذه بعض الأماكن التي يمكنك زيارتها في جدة:\n- " + "\n- ".join(tourist_places["جدة"])),  
    # If the user just says "جدة", assume they want tourist places
    (r'^(جدة|في جدة|بجدة)$', 
     lambda: "✨ الأماكن السياحية في جدة:\n- " + "\n- ".join(tourist_places["جدة"])),  

                                        #َQassim 
    (r'^(شكرا|شكراً|شكرًا|مشكور|يعطيك العافية)$', lambda: "على الرحب والسعة! 😃"),  
    # This pattern now matches when "القصيم" appears anywhere in the sentence along with suggestion words
    (r'(تقدر|يمكنك|ممكن|هل).*?(اقتراح|تقترح|ترشيح|تنصحني|تعطيني|ترشح).*?(القصيم)', 
     lambda: "🌴 بالطبع! يمكنك زيارة:\n- " + "\n- ".join(tourist_places["القصيم"])),
    # Add separate pattern to catch queries containing both "places" and "Al-Qassim" --
    (r'(مكان|اماكن|أماكن|محلات).*?(القصيم)|(القصيم).*?(مكان|اماكن|أماكن|محلات)', 
     lambda: "✨ الأماكن السياحية في القصيم:\n- " + "\n- ".join(tourist_places["القصيم"])),
        # Detecting best places in Al-Qassim with more flexibility
    (r'(ايش|ما هي|ماهو|ممكن تقولي|ودِّي أعرف).*?(افضل|أحسن|أروع).*?(الأماكن|الاماكن).*?(في القصيم|بالقصيم|القصيم)', 
     lambda: "✨ الأماكن السياحية في القصيم:\n- " + "\n- ".join(tourist_places["القصيم"])),  
        # Matching "I want to travel to Al-Qassim" + "suggest places"
    (r'.*(أريد|ودي|نفسي|حابب).*?(أسافر|أزور|أروح).*?(إلى القصيم|للقصيم|القصيم).*?(مكان|أماكن|ترشيح|اقتراح|تنصحني|تعطيني)?.*?',
     lambda: "🚜 رائع! هذه بعض الأماكن التي يمكنك زيارتها في القصيم:\n- " + "\n- ".join(tourist_places["القصيم"])),  
    # If the user just says "القصيم", assume they want tourist places
    (r'^(القصيم|في القصيم|بالقصيم)$', 
     lambda: "✨ الأماكن السياحية في القصيم:\n- " + "\n- ".join(tourist_places["القصيم"])),  

                                        #Abha 
    (r'^(شكرا|شكراً|شكرًا|مشكور|يعطيك العافية)$', lambda: "على الرحب والسعة! 😃"),  
    # This pattern now matches when "أبها" or "ابها" appears anywhere in the sentence along with suggestion words
    (r'(تقدر|يمكنك|ممكن|هل).*?(اقتراح|تقترح|ترشيح|تنصحني|تعطيني|ترشح).*?(أبها|ابها)', 
    lambda: "🏔 بالطبع! يمكنك زيارة:\n- " + "\n- ".join(tourist_places["أبها"])),  
    # Add separate pattern to catch queries containing both "places" and "Abha"  
    (r'(مكان|اماكن|أماكن|محلات).*?(أبها|ابها)|(أبها|ابها).*?(مكان|اماكن|أماكن|محلات)', 
    lambda: "✨ الأماكن السياحية في أبها:\n- " + "\n- ".join(tourist_places["أبها"])),  
    # Detecting best places in Abha with more flexibility  
    (r'(ايش|ما هي|ماهو|ممكن تقولي|ودِّي أعرف).*?(افضل|أحسن|أروع).*?(الأماكن|الاماكن).*?(في أبها|بأبها|أبها|في ابها|بابها|ابها)', 
    lambda: "✨ الأماكن السياحية في أبها:\n- " + "\n- ".join(tourist_places["أبها"])),  
    # Matching "I want to travel to Abha" + "suggest places"  
    (r'.*(أريد|ودي|نفسي|حابب).*?(أسافر|أزور|أروح).*?(إلى أبها|لأبها|أبها|الى ابها|لابها|ابها).*?(مكان|أماكن|ترشيح|اقتراح|تنصحني|تعطيني)?.*?', 
    lambda: "🚗 رائع! هذه بعض الأماكن التي يمكنك زيارتها في أبها:\n- " + "\n- ".join(tourist_places["أبها"])),  
    # If the user just says "أبها" or "ابها", assume they want tourist places  
    (r'^(أبها|في أبها|بأبها|ابها|في ابها|بابها)$', 
    lambda: "✨ الأماكن السياحية في أبها:\n- " + "\n- ".join(tourist_places["أبها"])),  


    

    # If the user asks an unknown question
    (r'^(.*\?|.*؟)$', lambda: random.choice(denial_responses)),  
    
    # Default response for anything else
    (r'.*', lambda: random.choice(denial_responses))  
]

# Function to process user input using regex
def respond(user_input):
    for pattern, response_func in patterns:
        match = re.search(pattern, user_input, re.IGNORECASE)
        if match:
            print(f"Matched pattern: {pattern}")
            return response_func()
        
    print("No pattern matched")
    return random.choice(denial_responses)  # Default response if no match

def mergedchat():
    st.title("🤖 وجّهني، هو بوت للسياحة في السعودية")
    st.write("مرحبًا! كيف يمكنني مساعدتك في استكشاف المعالم السياحية في السعودية؟ حابب تعرف عن ابها, جدة, القصيم, العلا او الرياض")


    # Initialize session state for chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display chat history
    
    for role, text in st.session_state.messages:
        if role == "user":
            st.markdown(
                f"""
                <div style="background-color:#4b7196; padding:10px; border-radius:8px; margin-bottom:5px; direction:rtl; text-align:right;">
                    <span style="font-size:14px; font-weight:bold; color:white;"> أنت👤: {text}</span> 
                </div>
                """,

                unsafe_allow_html=True
            )
        else:
            
            formatted_text = text.replace("\n- ", "\n\n🔹 ")  
            st.markdown(
                f"""
                <div style="background-color:#2c3e50; padding:10px; border-radius:8px; margin-bottom:5px; direction:rtl; text-align:right;">
                    <span style="font-size:14px; font-weight:bold; color:white;">وجّهني بوت🤖: {formatted_text}</span> 
                </div>
                """,
                unsafe_allow_html=True
            )
    # Create a separate session state key for input field
    if "user_input" not in st.session_state:
        st.session_state.user_input = ""

    # Chat input field with submit button
    with st.form(key="chat_form"):
        user_input = st.text_input("✍️ اكتب سؤالك هنا:", value=st.session_state.user_input, key="input_field")
        submit_button = st.form_submit_button("إرسال")
    if st.button("🗑️ مسح المحادثة"):
        st.session_state.messages = []
        st.rerun()
    # Process input only when submit button is clicked
    if submit_button and user_input:
        # Get bot response
        bot_response = respond(user_input)
        
        # Append user message to chat history
        st.session_state.messages.append(("user", user_input))
        
        # Append bot response to chat history
        st.session_state.messages.append(("bot", bot_response))
        
        st.session_state.user_input = ""  
        

        st.rerun()

st.set_page_config(page_title="السياحة في السعودية")
page = st.sidebar.radio("انتقل إلى:", ["الرئيسية", "المحادثة", "الفريق"])

if page == "الرئيسية":
    st.title("🤖 شات بوت السياحة في السعودية!")
    st.write("شات بوت السياحة في السعودية هو مساعد ذكاء اصطناعي")
    st.write("لتوفير معلومات عن أبرز المعالم السياحية في أبها، جدة، الرياض، العلا، والقصيم ويستخدم تقنيات معالجة اللغات الطبيعية،") 
    st.write("مما يساعد المستخدمين في استكشاف المملكة بسهولة.")
    st.write("أنتقل لصفحة المحادثة للبدأ")
    st.image("https://maaal.com/wp-content/uploads/2021/02/%D8%B3%D9%8A%D8%A7%D8%AD%D8%A9-%D8%A7%D9%84%D8%B3%D8%B9%D9%88%D8%AF%D9%8A%D8%A9.jpg", use_container_width=True)


elif page == "المحادثة":
    mergedchat()

elif page == "الفريق":
    st.title("👥 فريق 3")

    team_members = [
        ("عبدالعزيز", "تطوير جزئية الشات الخاصة بالعلا"),
        ("وسن", "تطوير جزئية الشات الخاصة بجدة"),
        ("عبدالمحسن", "تطوير جزئية الشات الخاصة بالقصيم"),
        ("الهنوف", "تطوير جزئية الشات الخاصة بالرياض"),
        ("مهند", "تطوير جزئية الشات الخاصة بأبها"),
    ]

    for name, role in team_members:
        st.markdown(
            f"""
            <div style="background-color:#2c3e50; padding:10px; border-radius:8px; margin-bottom:5px;">
                <span style="font-size:14px; font-weight:bold; color:white;">المطور: {name}</span>
                <br>
                <span style="font-size:14px; color:white;">الدور: {role}</span>
            </div>
            """, 
            unsafe_allow_html=True
        )
