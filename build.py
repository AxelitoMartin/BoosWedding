"""Generate the per-language pages (en/, fr/, zh/) from one template.

Edit the text in STRINGS below, then run:  python3 build.py
"""

from html import escape
from pathlib import Path

ROOT = Path(__file__).parent

# Venue: coordinates from the Google Maps pin (GCJ-02, the system Chinese map apps use)
VENUE_ZH = "白家大院（北门）"
VENUE_ADDRESS_ZH = "北京市海淀区苏州街15号"
MAP_LINKS = {
    "google": ("Google Maps", "Google 地图", "https://www.google.com/maps/place/Baijia+Restaurant+%EF%BC%88North+Gate%EF%BC%89/@39.980939,116.304395,17z/data=!3m1!4b1!4m6!3m5!1s0x35f0514887b8b481:0x45f1b1ca78a98e57!8m2!3d39.980939!4d116.304395!16s%2Fg%2F11cm1jnj1l"),
    "apple": ("Apple Maps", "Apple 地图", "https://maps.apple.com/?q=%E7%99%BD%E5%AE%B6%E5%A4%A7%E9%99%A2%EF%BC%88%E5%8C%97%E9%97%A8%EF%BC%89&ll=39.980939,116.304395"),
    "amap": ("Amap (高德地图)", "高德地图", "https://uri.amap.com/marker?position=116.304395,39.980939&name=%E7%99%BD%E5%AE%B6%E5%A4%A7%E9%99%A2%EF%BC%88%E5%8C%97%E9%97%A8%EF%BC%89&coordinate=gaode&callnative=1"),
    "baidu": ("Baidu Maps (百度地图)", "百度地图", "https://api.map.baidu.com/marker?location=39.980939,116.304395&coord_type=gcj02&title=%E7%99%BD%E5%AE%B6%E5%A4%A7%E9%99%A2%EF%BC%88%E5%8C%97%E9%97%A8%EF%BC%89&content=%E5%8C%97%E4%BA%AC%E5%B8%82%E6%B5%B7%E6%B7%80%E5%8C%BA%E8%8B%8F%E5%B7%9E%E8%A1%9715%E5%8F%B7&output=html&src=webapp.booswedding.site"),
}

# Who guests contact in the "AI agent" section, per language: (label, shown value, link or None)
AXEL = [
    ("Email", "axel.steph.martin@gmail.com", "mailto:axel.steph.martin@gmail.com"),
    ("WhatsApp", "+1 (734) 780-9938", "https://wa.me/17347809938"),
]
CLAUDIA = [
    ("电子邮箱", "claudia.j.shi@gmail.com", "mailto:claudia.j.shi@gmail.com"),
    ("微信号", "claudiaisawesome", None),  # WeChat has no web link; the button copies the ID
]
CONTACTS = {"en": AXEL, "fr": AXEL, "zh": CLAUDIA}


def contact_button(label, value, link, copied=""):
    inner = (f'\n            <span class="contact-label">{escape(label)}</span>'
             f'\n            <span class="contact-value">{escape(value)}</span>\n          ')
    if link is None:
        return f'          <button type="button" class="contact-btn" data-copy="{escape(value)}" data-copied="{escape(copied)}">{inner}</button>'
    target = ' target="_blank" rel="noopener"' if link.startswith("http") else ""
    return f'          <a class="contact-btn" href="{link}"{target}>{inner}</a>'

LANGS = [("en", "English"), ("fr", "Français"), ("zh", "中文")]

STRINGS = {
    "en": {
        "html_lang": "en",
        "title": "Claudia & Axel · 4 September 2027 · Beijing",
        "nav_details": "Details",
        "nav_rsvp": "RSVP",
        "date_html": "Sept 4<sup>th</sup> 2027",
        "place": "Beijing, China",
        "scroll": "Scroll",
        "nav_story": "Our story",
        "story_title": "Our story",
        "story": [
            "We may have been married a year ago by an overly enthusiastic New York City Hall employee whose break we cut short, but somehow that was not quite enough for us.",
            "Since then, a lot has changed. Claudia became a green card holder and a fierce entrepreneur, determined to escape the permanent underclass of our future AI overlords. Axel, meanwhile, became a doctor (of philosophy, not the kind who can actually help you) and now pursues an academic career in cancer research, blissfully oblivious to his wife's worries.",
            "Somehow, all of this has made us ready to celebrate properly with all of you whom we hold dear. We hope you will join us for a quintessential Qing-style wedding, with horses, music, yellow silk and imperial drama galore!",
        ],
        "details_title": "We're getting married",
        "details_lead": "We would love for you to celebrate with us in Beijing. A formal invitation with the full programme will follow.",
        "when": "When",
        "when_value": "Saturday 4 September 2027",
        "where": "Where",
        "where_value": "Beijing, China",
        "venue": "Venue",
        "venue_value": "Baijia Dayuan",
        "days": "days", "hours": "hours", "minutes": "minutes",
        "rsvp_title": "Will you celebrate with us",
        "rsvp_lead": "We are finalising our guest list, so please let us know by 1 February 2027.",
        "first_name": "First name", "last_name": "Last name",
        "email": "Email", "address": "Postal address (for the formal invitation)",
        "availability": "Availability",
        "accept": "Joyfully accept", "decline": "Regretfully decline",
        "guests": "Number of guests (including you)",
        "dietary": "Special dietary requirements",
        "diet_options": [("none", "None"), ("pescatarian", "Pescatarian"), ("vegetarian", "Vegetarian"), ("vegan", "Vegan"), ("gluten", "Gluten free"),
                         ("dairy", "Dairy free"), ("nuts", "Nut allergy"), ("halal", "Halal"), ("other", "Other (please specify below)")],
        "lodging": "I am travelling from abroad and would like help with accommodation",
        "diet_choose": "Please select",
        "diet_other": "Other allergies or notes",
        "message": "A message for us (optional)",
        "submit": "Send",
        "thanks_title": "Thank you",
        "thanks_body": "Your answer has been received. Formal details to follow.",
        "error": "Oops, something went wrong while sending. Please try again.",
        "nav_travel": "Travel",
        "guide_title": "Travelling to China",
        "guide_lead": "A few useful links for guests coming from abroad. Rules change often, so please check them again a few weeks before you travel.",
        "guide_groups": [["Visas", [["Visa-free entry and 240-hour transit rules", "https://en.nia.gov.cn/", "National Immigration Administration"], ["Apply for a Chinese visa", "https://www.visaforchina.cn/", "Chinese Visa Application Service Center"], ["Chinese Embassy in the United States", "https://us.china-embassy.gov.cn/eng/", "Visas for US residents"], ["Chinese Embassy in France", "https://fr.china-embassy.gov.cn/fra/", "Visas for residents of France"]]], ["Apps and payments", [["How to pay in Beijing", "https://english.beijing.gov.cn/specials/paymentservices/howtopaybeijing/", "Official guide from the Beijing government"], ["Video guides: Alipay and WeChat Pay", "https://english.beijing.gov.cn/specials/paymentservices/guidevideos/", "Linking a foreign card, step by step"], ["Alipay", "https://global.alipay.com/", "Pay almost everywhere with your own Visa or Mastercard"], ["WeChat", "https://www.wechat.com/", "Messaging and WeChat Pay"], ["DiDi", "https://www.didiglobal.com/", "Taxis and rides, available in English inside Alipay"]]]],
        "guide_tip": "Good to know: Google, WhatsApp and Instagram do not work in mainland China on local Wi-Fi. Use your home SIM's roaming data or set up a VPN before you leave.",
        "ask_title": "Ask our new AI agent anything!",
        "ask_sub": "(It's just Axel...)",
        "ask_body": "Visas, travel, outfits or anything else on your mind: our cutting-edge assistant answers every message personally. Response times may vary depending on how many experiments are running.",
        "venue_title": "The venue",
        "venue_desc": "A Qing dynasty garden dating back to the reign of Emperor Kangxi, now a restaurant serving imperial cuisine. The perfect setting for a Qing-style celebration.",
        "venue_address": "15 Suzhou Street, Haidian District, Beijing",
        "venue_taxi": "For your taxi driver",
        "venue_metro": "Metro Line 10, Suzhoujie station, then about a 500 m walk.",
        "maps_note": "Google Maps does not work in mainland China without a VPN. Apple Maps and Amap work everywhere.",
        "maps_order": ["google", "apple", "amap", "baidu"],
        "footer": "4 September 2027 · Beijing",
    },
    "fr": {
        "html_lang": "fr",
        "title": "Claudia & Axel · 4 septembre 2027 · Pékin",
        "nav_details": "Infos",
        "nav_rsvp": "Réponse",
        "date_html": "4 septembre 2027",
        "place": "Pékin, Chine",
        "scroll": "Défiler",
        "nav_story": "Notre histoire",
        "story_title": "Notre histoire",
        "story": [
            "Nous avons beau avoir été mariés il y a un an par un employé de la mairie de New York un peu trop enthousiaste, dont nous avons écourté la pause, cela ne nous a, étrangement, pas suffi.",
            "Depuis, beaucoup de choses ont changé. Claudia est devenue titulaire d'une green card et entrepreneuse acharnée, bien décidée à échapper à la sous-classe permanente de nos futurs maîtres IA. Axel, de son côté, est devenu docteur (le genre avec une thèse, pas celui qui peut réellement vous soigner) et poursuit une carrière universitaire dans la recherche sur le cancer, dans une ignorance bienheureuse des inquiétudes de sa femme.",
            "Allez savoir pourquoi, tout cela nous a rendus prêts à célébrer comme il se doit avec vous tous qui nous êtes chers. Nous espérons que vous nous rejoindrez pour un mariage dans la plus pure tradition Qing, où chevaux, musique, soie jaune et drames impériaux seront au rendez-vous !",
        ],
        "details_title": "Nous nous marions",
        "details_lead": "Nous serions ravis de célébrer ce jour avec vous à Pékin. Une invitation officielle avec le programme complet suivra.",
        "when": "Quand",
        "when_value": "Samedi 4 septembre 2027",
        "where": "Où",
        "where_value": "Pékin, Chine",
        "venue": "Lieu",
        "venue_value": "Baijia Dayuan",
        "days": "jours", "hours": "heures", "minutes": "minutes",
        "rsvp_title": "Serez-vous des nôtres",
        "rsvp_lead": "Nous finalisons la liste des invités, merci de nous répondre avant le 1er février 2027.",
        "first_name": "Prénom", "last_name": "Nom",
        "email": "E-mail", "address": "Adresse postale (pour l'invitation officielle)",
        "availability": "Disponibilité",
        "accept": "Avec joie", "decline": "À regret, je ne pourrai pas venir",
        "guests": "Nombre de personnes (vous compris)",
        "dietary": "Régime alimentaire particulier",
        "diet_options": [("none", "Aucun"), ("pescatarian", "Pescétarien"), ("vegetarian", "Végétarien"), ("vegan", "Végan"), ("gluten", "Sans gluten"),
                         ("dairy", "Sans lactose"), ("nuts", "Allergie aux fruits à coque"), ("halal", "Halal"), ("other", "Autre (à préciser ci-dessous)")],
        "lodging": "Je viens de l'étranger et j'aimerais de l'aide pour l'hébergement",
        "diet_choose": "Choisir",
        "diet_other": "Autres allergies ou remarques",
        "message": "Un petit mot pour nous (facultatif)",
        "submit": "Envoyer",
        "thanks_title": "Merci",
        "thanks_body": "Votre réponse a bien été reçue. Les détails suivront.",
        "error": "Oups, l'envoi a échoué. Merci de réessayer.",
        "nav_travel": "Voyage",
        "guide_title": "Venir en Chine",
        "guide_lead": "Quelques liens utiles pour les invités venant de l'étranger. Les règles changent souvent, pensez à les vérifier quelques semaines avant votre départ.",
        "guide_groups": [["Visas", [["Exemption de visa et transit de 240 heures", "https://en.nia.gov.cn/", "Administration nationale de l'immigration (en anglais)"], ["Demander un visa chinois", "https://www.visaforchina.cn/", "Centre de demande de visa pour la Chine"], ["Ambassade de Chine en France", "https://fr.china-embassy.gov.cn/fra/", "Visas pour les résidents en France"], ["Ambassade de Chine aux États-Unis", "https://us.china-embassy.gov.cn/eng/", "Visas pour les résidents américains"]]], ["Applications et paiements", [["Comment payer à Pékin", "https://english.beijing.gov.cn/specials/paymentservices/howtopaybeijing/", "Guide officiel de la ville de Pékin (en anglais)"], ["Tutoriels vidéo : Alipay et WeChat Pay", "https://english.beijing.gov.cn/specials/paymentservices/guidevideos/", "Associer une carte étrangère, étape par étape"], ["Alipay", "https://global.alipay.com/", "Payez presque partout avec votre carte Visa ou Mastercard"], ["WeChat", "https://www.wechat.com/", "Messagerie et WeChat Pay"], ["DiDi", "https://www.didiglobal.com/", "Taxis et VTC, disponible en anglais dans Alipay"]]]],
        "guide_tip": "Bon à savoir : Google, WhatsApp et Instagram ne fonctionnent pas en Chine continentale sur le Wi-Fi local. Utilisez les données en itinérance de votre forfait ou installez un VPN avant de partir.",
        "ask_title": "Posez toutes vos questions à notre nouvel agent IA !",
        "ask_sub": "(C'est juste Axel...)",
        "ask_body": "Visa, voyage, tenue ou toute autre question : notre assistant dernier cri répond personnellement à chaque message. Le délai de réponse peut varier selon le nombre d'expériences en cours.",
        "venue_title": "Le lieu",
        "venue_desc": "Un jardin de la dynastie Qing datant du règne de l'empereur Kangxi, aujourd'hui un restaurant de cuisine impériale. Le cadre idéal pour une fête façon Qing.",
        "venue_address": "15 rue Suzhou, district de Haidian, Pékin",
        "venue_taxi": "Pour votre chauffeur de taxi",
        "venue_metro": "Métro ligne 10, station Suzhoujie, puis environ 500 m à pied.",
        "maps_note": "Google Maps ne fonctionne pas en Chine continentale sans VPN. Apple Plans et Amap fonctionnent partout.",
        "maps_order": ["google", "apple", "amap", "baidu"],
        "footer": "4 septembre 2027 · Pékin",
    },
    "zh": {
        "html_lang": "zh-Hans",
        "title": "Claudia & Axel · 2027年9月4日 · 北京",
        "nav_details": "婚礼信息",
        "nav_rsvp": "回复出席",
        "date_html": "2027年9月4日",
        "place": "中国 · 北京",
        "scroll": "向下滑动",
        "nav_story": "我们的故事",
        "story_title": "我们的故事",
        "story": [
            "我们虽然一年前就已经在纽约市政厅，由一位热情过头的工作人员（我们还打断了人家的休息时间）证婚，但不知怎的，总觉得还不够尽兴。",
            "这期间发生了很多变化。Claudia 拿到了绿卡，还成了一名拼劲十足的创业者，誓要逃离未来 AI 霸主统治下的“永久底层”；而 Axel 成了博士，在癌症研究领域追求学术事业，对老婆的种种忧虑浑然不觉，乐在其中。",
            "也许正因如此，我们终于准备好和所有珍爱的亲朋好友们好好庆祝一番。诚邀您参加一场原汁原味的清朝风格婚礼：骏马、鼓乐、明黄丝绸，还有满满的宫廷大戏！",
        ],
        "details_title": "我们要结婚啦",
        "details_lead": "诚挚邀请您来北京与我们共同见证这一天。正式请柬及详细流程将随后寄出。",
        "when": "时间",
        "when_value": "2027年9月4日（星期六）",
        "where": "地点",
        "where_value": "中国北京",
        "venue": "场地",
        "venue_value": "白家大院",
        "days": "天", "hours": "小时", "minutes": "分钟",
        "rsvp_title": "期待您的光临",
        "rsvp_lead": "我们正在确认宾客名单，请于2027年2月1日前回复。",
        "first_name": "名", "last_name": "姓",
        "email": "电子邮箱", "address": "邮寄地址（用于寄送正式请柬）",
        "availability": "能否出席",
        "accept": "欣然赴约", "decline": "遗憾缺席",
        "guests": "出席人数（含您本人）",
        "dietary": "饮食禁忌",
        "diet_options": [("none", "无"), ("pescatarian", "鱼素（可吃海鲜）"), ("vegetarian", "素食"), ("vegan", "纯素"), ("gluten", "无麸质"),
                         ("dairy", "乳制品过敏"), ("nuts", "坚果过敏"), ("halal", "清真"), ("other", "其他（请在下方注明）")],
        "lodging": "我从海外前来，希望获得住宿安排方面的帮助",
        "diet_choose": "请选择",
        "diet_other": "其他过敏或备注",
        "message": "给我们的留言（选填）",
        "submit": "提交",
        "thanks_title": "谢谢",
        "thanks_body": "我们已收到您的回复，详细信息将随后通知。",
        "error": "抱歉，提交失败，请稍后再试。",
        "nav_travel": "出行指南",
        "guide_title": "海外来宾出行指南",
        "guide_lead": "以下链接供从海外前来的宾客参考。相关政策时有变化，请在出发前几周再次确认。",
        "guide_groups": [["签证", [["免签入境及240小时过境免签政策", "https://www.nia.gov.cn/", "国家移民管理局"], ["申请中国签证", "https://www.visaforchina.cn/", "中国签证申请服务中心"], ["中国驻美国大使馆", "https://us.china-embassy.gov.cn/eng/", "在美居民签证信息（英文）"], ["中国驻法国大使馆", "https://fr.china-embassy.gov.cn/fra/", "在法居民签证信息（法文）"]]], ["应用与支付", [["北京支付指南", "https://english.beijing.gov.cn/specials/paymentservices/howtopaybeijing/", "北京市政府官方指南（英文）"], ["视频教程：支付宝与微信支付", "https://english.beijing.gov.cn/specials/paymentservices/guidevideos/", "绑定境外银行卡的步骤（英文）"], ["支付宝", "https://global.alipay.com/", "可绑定 Visa 或万事达卡，几乎随处可用"], ["微信", "https://www.wechat.com/", "聊天与微信支付"], ["滴滴出行", "https://www.didiglobal.com/", "打车出行，支付宝内也可直接使用"]]]],
        "guide_tip": "温馨提示：在中国大陆使用本地 Wi-Fi 时无法访问 Google、WhatsApp 和 Instagram。建议使用国际漫游数据，或在出发前准备好 VPN。",
        "ask_title": "有任何问题，尽管问我们全新的 AI 助手！",
        "ask_sub": "（其实就是 Claudia……）",
        "ask_body": "签证、出行、穿搭，或者任何其他问题：我们最先进的“智能助手”会亲自回复每一条消息。回复速度视她手头的创业项目有多忙而定。",
        "copied": "微信号已复制",
        "venue_title": "婚礼场地",
        "venue_desc": "始建于康熙年间的清代王府园林，如今是一家以宫廷菜闻名的餐厅。用来举办一场清朝风格的婚礼，再合适不过了。",
        "venue_address": "北京市海淀区苏州街15号",
        "venue_taxi": "",
        "venue_metro": "地铁10号线苏州街站，步行约500米。",
        "maps_note": "",
        "maps_order": ["amap", "baidu", "apple", "google"],
        "footer": "2027年9月4日 · 北京",
    },
}

FONTS = (
    "https://fonts.googleapis.com/css2?family=Bodoni+Moda:opsz@6..96"
    "&family=Mrs+Saint+Delafield&family=Open+Sans:wght@400;600"
    "{extra}&display=swap"
)

TEMPLATE = """<!doctype html>
<html lang="{html_lang}">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title}</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="{fonts}" rel="stylesheet">
  <link rel="stylesheet" href="../assets/style.css?v=7">
{alternates}
</head>
<body>
  <header class="hero">
    <div class="topbar">
      <nav>
        <a href="#story">{nav_story}</a>
        <a href="#details">{nav_details}</a>
        <a href="#rsvp">{nav_rsvp}</a>
        <a href="#travel">{nav_travel}</a>
      </nav>
      <nav class="langs" aria-label="Language">
{lang_links}
      </nav>
    </div>
    <div class="hero-text">
      <p class="names">Claudia &amp; Axel</p>
      <p class="date">{date_html}</p>
      <p class="place">{place}</p>
    </div>
    <a class="scroll-cue" href="#story">{scroll} ↓</a>
  </header>

  <section id="story">
    <div class="wrap">
      <div class="story-card">
        <div class="seal" aria-hidden="true">囍</div>
        <h2>{story_title}</h2>
        <div class="story">
{story}
        </div>
      </div>
    </div>
  </section>

  <section id="details">
    <div class="wrap">
      <h2>{details_title}</h2>
      <p class="lead">{details_lead}</p>
      <div class="details">
        <div class="detail"><div class="label">{when}</div><div class="value">{when_value}</div></div>
        <div class="detail"><div class="label">{where}</div><div class="value">{where_value}</div></div>
        <div class="detail"><div class="label">{venue}</div><div class="value">{venue_value}</div></div>
      </div>
      <div class="venue">
        <h3>{venue_title}</h3>
        <p class="venue-name">{venue_name_html}</p>
        <p>{venue_desc}</p>
        <p class="venue-address">{venue_address}</p>
{venue_taxi_html}
        <p class="venue-metro">{venue_metro}</p>
        <div class="map-links">
{map_links}
        </div>
{maps_note_html}
      </div>
      <div class="countdown" data-countdown>
        <div><strong data-days>–</strong><span>{days}</span></div>
        <div><strong data-hours>–</strong><span>{hours}</span></div>
        <div><strong data-minutes>–</strong><span>{minutes}</span></div>
      </div>
    </div>
  </section>

  <div class="photo">
    <img src="../assets/save-the-date.jpg" alt="Claudia &amp; Axel, Beijing, 4 September 2027" loading="lazy">
  </div>

  <section id="rsvp">
    <div class="wrap">
      <h2>{rsvp_title}</h2>
      <p class="lead">{rsvp_lead}</p>

      <form class="rsvp">
        <div class="row">
          <label class="field">{first_name}<input type="text" name="firstName" autocomplete="given-name" required maxlength="100"></label>
          <label class="field">{last_name}<input type="text" name="lastName" autocomplete="family-name" required maxlength="100"></label>
        </div>
        <label class="field">{email}<input type="email" name="email" autocomplete="email" required maxlength="200"></label>
        <label class="field">{address}<input type="text" name="address" autocomplete="street-address" maxlength="300"></label>

        <fieldset>
          <legend>{availability}</legend>
          <div class="options">
            <label><input type="radio" name="attending" value="yes" required> {accept}</label>
            <label><input type="radio" name="attending" value="no"> {decline}</label>
          </div>
        </fieldset>

        <label class="field">{guests}
          <input type="number" name="guests" min="1" max="10" value="1">
        </label>

        <label class="field">{dietary}
          <select name="dietary">
            <option value="" disabled selected>{diet_choose}</option>
{diet_options}
          </select>
        </label>
        <label class="field">{diet_other}<input type="text" name="dietaryOther" maxlength="300"></label>
        <label class="check"><input type="checkbox" name="lodging" value="yes"> {lodging}</label>

        <label class="field">{message}<textarea name="message" rows="3" maxlength="1000"></textarea></label>

        <button type="submit">{submit}</button>
      </form>

      <div class="form-msg" data-success hidden>
        <h3>{thanks_title}</h3>
        <p>{thanks_body}</p>
      </div>
      <div class="form-msg error" data-error hidden><p>{error}</p></div>
    </div>
  </section>

  <section id="travel">
    <div class="wrap wide">
      <h2>{guide_title}</h2>
      <p class="lead">{guide_lead}</p>
      <div class="guide">
{guide_groups}
      </div>
      <p class="tip">{guide_tip}</p>
    </div>
  </section>

  <section id="ask">
    <div class="wrap">
      <div class="ask-card">
        <h2>{ask_title}</h2>
        <p class="ask-sub">{ask_sub}</p>
        <p>{ask_body}</p>
        <div class="contact">
{contact_buttons}
        </div>
      </div>
    </div>
  </section>

  <footer>
    <div class="monogram">C &amp; A</div>
    <p>{footer}</p>
  </footer>

  <script src="../assets/site.js?v=7"></script>
</body>
</html>
"""


def build(code: str) -> str:
    s = {k: v for k, v in STRINGS[code].items()}
    # Plain-text values are escaped; date_html intentionally contains markup.
    out = {k: (escape(v) if isinstance(v, str) and k != "date_html" else v) for k, v in s.items()}
    out["title"] = escape(s["title"])
    out["fonts"] = FONTS.format(extra="&family=Noto+Serif+SC:wght@400;600" if code == "zh" else "")
    out["lang_links"] = "\n".join(
        f'        <a href="../{c}/" hreflang="{STRINGS[c]["html_lang"]}"'
        + (' aria-current="page"' if c == code else "")
        + f">{label}</a>"
        for c, label in LANGS
    )
    out["alternates"] = "\n".join(
        f'  <link rel="alternate" hreflang="{STRINGS[c]["html_lang"]}" href="../{c}/">' for c, _ in LANGS
    )
    out["diet_options"] = "\n".join(
        f'            <option value="{v}">{escape(t)}</option>' for v, t in s["diet_options"]
    )
    out["story"] = "\n".join(f"          <p>{escape(p)}</p>" for p in s["story"])
    out["guide_groups"] = "\n".join(
        f'        <div class="guide-group">\n          <h3>{escape(title)}</h3>\n          <ul>\n'
        + "\n".join(
            f'            <li><a href="{url}" target="_blank" rel="noopener">{escape(label)}</a>'
            f'<span>{escape(note)}</span></li>'
            for label, url, note in links
        )
        + "\n          </ul>\n        </div>"
        for title, links in s["guide_groups"]
    )
    zh = code == "zh"
    out["venue_taxi_html"] = "" if zh else (
        f'        <p class="venue-taxi"><span>{escape(s["venue_taxi"])}</span>'
        f'<strong lang="zh-Hans">{VENUE_ADDRESS_ZH} {VENUE_ZH}</strong></p>'
    )
    out["venue_name_html"] = VENUE_ZH if zh else f'{out["venue_value"]} · <span lang="zh-Hans">{VENUE_ZH}</span>'
    out["map_links"] = "\n".join(
        f'          <a href="{escape(MAP_LINKS[k][2])}" target="_blank" rel="noopener">{escape(MAP_LINKS[k][1 if zh else 0])}</a>'
        for k in s["maps_order"]
    )
    out["maps_note_html"] = f'        <p class="maps-note">{escape(s["maps_note"])}</p>' if s["maps_note"] else ""
    out["contact_buttons"] = "\n".join(contact_button(*c, copied=s.get("copied", "")) for c in CONTACTS[code])
    return TEMPLATE.format(**out)


if __name__ == "__main__":
    for code, _ in LANGS:
        path = ROOT / code / "index.html"
        path.parent.mkdir(exist_ok=True)
        path.write_text(build(code), encoding="utf-8")
        print("wrote", path.relative_to(ROOT))
