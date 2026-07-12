# -*- coding: utf-8 -*-
import os, re

ROOT = os.path.dirname(os.path.abspath(__file__))

# ---------------------------------------------------------------------------
# PRODUCT DATA
# ---------------------------------------------------------------------------
CATS = {
    "fert": {"label": "Bio-Fertilizers",      "tagclass": "tag-fert",  "cardclass": "cat-fert"},
    "pgpr": {"label": "Growth Promoters (PGPR)", "tagclass": "tag-pgpr", "cardclass": "cat-pgpr"},
    "pest": {"label": "Bio-Pesticides",        "tagclass": "tag-pest",  "cardclass": "cat-pest"},
    "kit":  {"label": "Capsule Kits",          "tagclass": "tag-kit",   "cardclass": "cat-fert"},
}

PRODUCTS = [
    # BIO-FERTILIZERS
    dict(slug="azoss", name="AZOSS", sub="Azospirillum Bacteria", cat="fert",
         img="AZOSS (Azospirillum Bacteria).png", link="https://siestogreen.com/azospirillum/",
         desc="A nitrogen-fixing bacterial capsule that colonises the root zone, improving root development and making atmospheric nitrogen available to the plant.",
         long="AZOSS delivers Azospirillum bacteria in encapsulated form, a free-living nitrogen fixer that associates closely with plant roots. Once activated in water, the culture goes to work converting atmospheric nitrogen into a form your crop can use, while also producing plant hormones that encourage stronger root branching and better water uptake. It's the capsule most farmers use as their base nitrogen program alongside NPK Grow.",
         facts={"Function": "Nitrogen fixation", "Format": "1g capsule", "Coverage": "1 capsule / acre", "Best for": "Cereals, vegetables, cash crops"}),
    dict(slug="npk-grow", name="NPK Grow", sub="Atmospheric N, Phosphate & Potassium Bacteria Consortium", cat="fert",
         img="NPK Grow (Atmospheric Nitrogen, Phosphate Solubilizing Bacteria & Potassium mobilizing bacteria).png",
         link="https://siestogreen.com/product/npk-grow/",
         desc="A three-in-one bacterial consortium that fixes nitrogen, solubilises phosphate and mobilises potassium in a single capsule.",
         long="NPK Grow combines three functional groups of beneficial bacteria in one capsule: nitrogen fixers, phosphate solubilisers, and potassium mobilisers. Rather than applying separate cultures for each macronutrient, this consortium releases all three in the soil solution at once, making it the anchor product of the Poornima Cycle Kit and a straightforward first step for anyone new to biofertilizers.",
         facts={"Function": "N-P-K availability", "Format": "1g capsule", "Coverage": "1 capsule / acre", "Pairs well with": "Zinc Grow, Mycorrhiza"}),
    dict(slug="azoto", name="AZOTO", sub="Azotobacter Bacteria", cat="fert",
         img="AZOTO (Azotobactor Bacteria).png", link="https://siestogreen.com/azotobactor/",
         desc="Free-living, non-symbiotic nitrogen fixers that also secrete growth-promoting substances to support early plant vigour.",
         long="AZOTO carries Azotobacter, a free-living soil bacterium that fixes nitrogen without needing to nodulate a host root — useful across a much wider range of crops than symbiotic fixers like Rhizobium. Beyond nitrogen, Azotobacter produces auxins and other growth substances that support faster germination and early seedling vigour.",
         facts={"Function": "Nitrogen fixation", "Format": "1g capsule", "Coverage": "1 capsule / acre", "Best for": "Cereals, oilseeds, cotton"}),
    dict(slug="aceto", name="ACETO", sub="Acetobacter / Gluconacetobacter diazotrophicus", cat="fert",
         img="ACETO (Acetobactor Bacteria).webp", link="https://siestogreen.com/acetobactor/",
         desc="An endophytic nitrogen-fixing bacterium that lives inside plant tissue, well suited to sugar-rich crops.",
         long="ACETO supplies Gluconacetobacter diazotrophicus, an endophytic bacterium that colonises the internal tissue of the plant rather than just the root surface. It's particularly effective in sugar-rich crops such as sugarcane, where it has been widely studied for its nitrogen-fixing contribution over a full crop cycle.",
         facts={"Function": "Endophytic nitrogen fixation", "Format": "1g capsule", "Coverage": "1 capsule / acre", "Best for": "Sugarcane, sweet crops"}),
    dict(slug="rhizo", name="RHIZO", sub="Rhizobium Bacteria", cat="fert",
         img="RHIZO (Rhizobium).png", link="https://siestogreen.com/product/rhizo-rhizo-nitrogen-fixing-bacteria-for-enhanced-crop-growth/",
         desc="Symbiotic nitrogen-fixing bacteria that nodulate legume roots, the classic partnership behind healthy bean and pulse crops.",
         long="RHIZO contains Rhizobium, the bacterium legumes have partnered with for millions of years. It infects root hairs and forms nodules where it fixes atmospheric nitrogen directly for the plant. For beans, peas, groundnuts and other pulses, RHIZO is typically the first capsule applied at planting.",
         facts={"Function": "Symbiotic nitrogen fixation", "Format": "1g capsule", "Coverage": "1 capsule / acre", "Best for": "Beans, peas, groundnuts, pulses"}),
    dict(slug="psb-plus", name="P.S.B. Plus", sub="Phosphate Solubilising Bacteria", cat="fert",
         img="P.S.B. Plus (Phosphate Solubizing Bacteria).png",
         link="https://siestogreen.com/product/psb-plus-boost-your-crop-growth-with-phosphate-solubilizing-bacteria/",
         desc="Converts phosphate locked up in the soil into a form roots can actually absorb — one capsule replaces up to 25kg of DAP.",
         long="Most soil phosphorus is chemically locked and unavailable to plants. P.S.B. Plus introduces phosphate-solubilising bacteria that secrete organic acids to release that phosphorus, improving root development, flowering and fruit set. As shown in our compatibility charts, one capsule solubilises phosphorus equivalent to roughly 25kg of DAP.",
         facts={"Function": "Phosphate solubilisation", "Format": "1g capsule", "Coverage": "1 capsule / acre", "Equivalent to": "≈25kg DAP per capsule"}),
    dict(slug="potash-grow", name="POTASH GROW", sub="Potassium Mobilising Bacteria", cat="fert",
         img="POTASH GROW (Potassium Mobilizing Bacteria).png", link="https://siestogreen.com/product/potash-grow/",
         desc="Mobilises bound soil potassium into plant-available form, supporting fruit quality, disease resistance and drought tolerance.",
         long="POTASH GROW carries potassium-mobilising bacteria that release potassium bound in soil minerals, an especially valuable step for fruiting and tuber crops where potassium drives sugar transport, fruit quality and stress tolerance. One capsule mobilises potassium equivalent to roughly 25kg of MOP.",
         facts={"Function": "Potassium mobilisation", "Format": "1g capsule", "Coverage": "1 capsule / acre", "Equivalent to": "≈25kg MOP per capsule"}),
    dict(slug="zinc", name="ZINC", sub="Zinc Solubilising Bacteria", cat="fert",
         img="ZINC (Zinc Solubizing Bacteria).png", link="https://siestogreen.com/zinc-solubilizing-bacteria/",
         desc="Solubilises soil zinc, a micronutrient essential for enzyme activity and healthy plant metabolism.",
         long="Zinc deficiency shows up as stunted growth and poor grain fill, yet most soil zinc sits in forms plants can't reach. ZINC introduces zinc-solubilising microorganisms that acidify the surrounding soil slightly to release usable zinc, supporting enzyme function and ion transport inside the plant.",
         facts={"Function": "Zinc solubilisation", "Format": "1g capsule", "Coverage": "1 capsule / acre", "Included in": "Poornima Cycle Kit"}),
    dict(slug="mycorrhiza", name="MYCORRHIZA", sub="Nano Power — Mycorrhizal Fungi", cat="fert",
         img="MYCORRHIZA NANO POWER.png", link="https://agroduka.ke/mycorrhiza-nano-powder/",
         desc="Beneficial root fungi that extend the plant's own root system, widening its reach for water and nutrients.",
         long="MYCORRHIZA NANO POWER introduces mycorrhizal fungi that form a symbiotic association with plant roots, effectively extending the root system's surface area many times over. This translates into better water and nutrient absorption, improved soil aggregation, and stronger tolerance to environmental stress.",
         facts={"Function": "Root symbiosis", "Format": "Nano powder", "Coverage": "100g / acre (kit rate)", "Best for": "All crop types"}),

    # PGPR
    dict(slug="humigrow", name="HUMI GROW", sub="Nano Powder — Humic Acid", cat="pgpr",
         img="HUMI GROW NANO POWDER(Humic Acid).jpeg", link="https://siestogreen.com/humigrow-nano-powder/",
         desc="A humic-acid soil conditioner that improves structure, water retention and nutrient uptake.",
         long="HUMI GROW is a concentrated humic acid powder that conditions soil rather than feeding the plant directly. It improves soil structure and aggregation, increases the soil's capacity to hold water and nutrients, and helps roots take up what's already available more efficiently.",
         facts={"Function": "Soil conditioning", "Format": "Nano powder", "Active": "Humic acid", "Included in": "Poornima Cycle Kit"}),
    dict(slug="cropforce", name="CROP FORCE", sub="Nano Powder — Bio-Zyme", cat="pgpr",
         img="CROP FORCE NANO POWDER (Bio-Zyme).png", link="https://siestogreen.com/cropforce-nano-powder/",
         desc="A biostimulant enzyme blend that improves nutrition efficiency and stress tolerance.",
         long="CROP FORCE is a bio-zyme biostimulant — a blend of natural growth agents and enzymes designed to help the plant use nutrients more efficiently, tolerate abiotic stress such as heat or drought, and express better crop quality traits.",
         facts={"Function": "Biostimulant", "Format": "Nano powder", "Active": "Bio-zyme enzyme blend", "Included in": "Poornima Cycle Kit"}),
    dict(slug="sonha-bihan", name="SONHA-BIHAN", sub="Plant & Soil Booster / Fruit Enhancer", cat="pgpr",
         img="SONHA-BIHAN(PLANT AND SOIL BOOSTER).jpeg",
         link="https://siestogreen.com/product/sonha-bihan-a-plant-soil-booster-for-improved-plant-growth-and-yield/",
         desc="A plant and soil booster aimed at improving overall vigour, flowering and fruit development.",
         long="SONHA-BIHAN is formulated to lift overall plant and soil vitality through the reproductive stage, supporting more even flowering and better fruit set and development where it matters most for final yield.",
         facts={"Function": "Growth & fruiting booster", "Format": "Capsule / powder", "Stage": "Flowering – fruiting", "Best for": "Fruiting vegetables & orchard crops"}),
    dict(slug="alp", name="ALP", sub="Chelated Multi-Micronutrient", cat="pgpr",
         img="ALP (CHELATED MULTI-MICRONUTRIENT).jpeg", link="https://siestogreen.com/product/fresh-figs-2/",
         desc="A chelated multi-micronutrient formula that corrects hidden deficiencies for balanced, even growth.",
         long="ALP supplies a chelated blend of essential micronutrients in a form plants can absorb quickly, helping correct the small, often invisible deficiencies that otherwise cap yield and quality even when the major nutrients are well supplied.",
         facts={"Function": "Micronutrient correction", "Format": "Chelated formula", "Delivery": "Foliar / soil", "Best for": "All crop types"}),

    # BIO-PESTICIDES
    dict(slug="acarida", name="ACARIDA", sub="Verticillium lecanii & Actinomycete Derivatives", cat="pest",
         img="ACARIDA (Verticillium Lecanii & Derivatives Of Actinomycets).png", link="https://siestogreen.com/acarida/",
         desc="A biological control agent effective against mites, whiteflies and aphids without synthetic residues.",
         long="ACARIDA combines the entomopathogenic fungus Verticillium lecanii with actinomycete derivatives to give broad biological control over soft-bodied pests such as mites, whiteflies and aphids, without leaving the chemical residues associated with conventional acaricides.",
         facts={"Targets": "Mites, whiteflies, aphids", "Type": "Fungal + actinomycete", "Format": "1g capsule", "Coverage": "1 capsule / acre"}),
    dict(slug="bacillus-thuringiensis", name="BACILLUS THURINGIENSIS", sub="Bt — Caterpillar & Larval Control", cat="pest",
         img="BACILLUS THURINGIENSIS.png", link="https://siestogreen.com/bacillus-thuringiensis/",
         desc="A naturally occurring soil bacterium that targets caterpillars and other larval pests while sparing beneficial insects.",
         long="Bacillus thuringiensis is one of the most widely used biological insecticides in the world. It produces proteins that are toxic specifically to the digestive systems of caterpillars and other larvae, leaving pollinators and beneficial insects unharmed.",
         facts={"Targets": "Caterpillars, larvae", "Type": "Bacterial", "Format": "1g capsule", "Coverage": "1 capsule / acre"}),
    dict(slug="traps", name="TRAPS", sub="Beauveria bassiana", cat="pest",
         img="TRAPS (BEAUVERIA BASSIANA).png", link="https://siestogreen.com/product/traps/",
         desc="An entomopathogenic fungus with broad activity against sap-sucking and soil-dwelling pests.",
         long="TRAPS delivers Beauveria bassiana, a naturally occurring fungus that infects and kills a wide range of insect pests on contact, including thrips, whiteflies and several soil-dwelling larvae, making it a useful rotation partner for resistance management.",
         facts={"Targets": "Thrips, whiteflies, soil pests", "Type": "Fungal", "Format": "1g capsule", "Coverage": "1 capsule / acre"}),
    dict(slug="life-line", name="LIFE LINE", sub="Verticillium lecanii", cat="pest",
         img="LIFE LINE (VERTICILLIUM LECANII).png", link="https://siestogreen.com/product/reversible-disc-plough-2/",
         desc="A fungal biocontrol targeting aphids, whiteflies and scale insects.",
         long="LIFE LINE is built on Verticillium lecanii, a fungus that parasitises aphids, whiteflies and scale insects. It's commonly rotated with other bio-pesticides in the range to manage sap-sucking pest pressure through the season.",
         facts={"Targets": "Aphids, whiteflies, scale", "Type": "Fungal", "Format": "1g capsule", "Coverage": "1 capsule / acre"}),
    dict(slug="indofa", name="INDOFA", sub="Trichoderma viride", cat="pest",
         img="INDOFA(TRICHODERMA VIRIDE).png", link="https://siestogreen.com/product/gaspardo-tornado-230-2/",
         desc="A root-protecting beneficial fungus that guards against soil-borne disease while boosting vigour.",
         long="INDOFA introduces Trichoderma viride, a beneficial fungus that colonises the root zone ahead of pathogens, competing with and suppressing soil-borne disease while also stimulating stronger root growth.",
         facts={"Targets": "Soil-borne pathogens", "Type": "Fungal", "Format": "1g capsule", "Coverage": "1 capsule / acre"}),
    dict(slug="pacliq", name="PACLIQ", sub="Paecilomyces lilacinus", cat="pest",
         img="PACLIQ (PAECILOMYCES LILACINUS).png", link="https://siestogreen.com/product/pacliq/",
         desc="A biological nematicide that controls root-knot nematodes without synthetic chemistry.",
         long="PACLIQ carries Paecilomyces lilacinus, a fungus that parasitises nematode eggs and juveniles in the soil, offering a biological route to controlling root-knot nematode damage that would otherwise call for synthetic nematicides.",
         facts={"Targets": "Root-knot nematodes", "Type": "Fungal", "Format": "1g capsule", "Coverage": "1 capsule / acre"}),

    # KITS
    dict(slug="poornima-cycle-kit", name="Poornima Cycle Kit", sub="Our Star Product — Full Soil Enrichment", cat="kit",
         img="POORNIMA CYCLE KIT.png", link="https://siestogreen.com/api/website/product-details/pck1acre",
         desc="A complete bio-enzyme kit combining five capsules and powders for the overall development of soil and plant.",
         long="The Poornima Cycle Kit is JSolution's flagship bundle: NPK Grow, Zinc Grow, Mycorrhiza Nano Powder, Humigrow Nano Powder and Crop Force Nano Powder, dosed together so every essential macro- and micronutrient pathway is covered in one application. It's a single solution for the overall enrichment of the soil, works across soil types and climates, and builds plant tolerance to environmental stress over time. Available in a 1-Acre pack (NPK Grow ×2, Zinc Grow ×1, Mycorrhiza 100g, Humigrow 120g, Crop Force 120g) and a 1-Hectare pack (NPK Grow ×6, Zinc Grow ×2, Mycorrhiza 200g, Humigrow 300g, Crop Force 300g).",
         facts={"Contains": "5 capsules/powders", "Pack sizes": "1 Acre & 1 Hectare", "Function": "Full soil enrichment", "Best for": "Every crop, every season"}),
    dict(slug="amavasya-plus-kit", name="Amavasya Plus Kit", sub="Lunar-Cycle Soil & Crop Kit", cat="kit",
         img="AMAVASYA PLUS KIT.jpeg", link="https://siestogreen.com/amavasya-plus-kit/",
         desc="A companion capsule kit timed to the new-moon growth cycle for sustained soil and plant health.",
         long="The Amavasya Plus Kit pairs with the Poornima Cycle Kit to give a continuous programme of biofertilizer applications through the crop cycle, keeping microbial activity and nutrient availability topped up between major growth stages.",
         facts={"Contains": "Multi-capsule kit", "Function": "Cycle maintenance", "Application": "Soil / drip", "Best for": "Ongoing soil health programs"}),
    dict(slug="ibp-soil-treatment-kit", name="IBP Soil Treatment Kit", sub="Soil Treatment Kit", cat="kit",
         img="IBP (Soil Treatment) Kit.jpeg", link="https://siestogreen.com/ibp-kit/",
         desc="A pre-planting soil treatment kit that establishes beneficial microbial populations before the crop goes in.",
         long="The IBP Soil Treatment Kit is applied ahead of planting to seed the soil with beneficial microbial populations, improving structure and disease suppression before roots are ever in the ground.",
         facts={"Contains": "Soil-treatment capsules", "Function": "Pre-planting soil prep", "Application": "Broadcast / drench", "Best for": "New plots and rotations"}),
    dict(slug="seed-treatment-kit", name="Seed Treatment Kit", sub="Seed Treatment Kit", cat="kit",
         img="SEED TREATMENT KIT.jpg", link="https://siestogreen.com/product/seed-treatment-kits/",
         desc="A seed-coating kit that gives germinating seedlings a protective, nutrient-rich microbial head start.",
         long="The Seed Treatment Kit coats seed with beneficial microbes before sowing, so germinating seedlings meet a protective, nutrient-cycling microbial community from day one, supporting faster, more even germination.",
         facts={"Contains": "Seed-coating capsules", "Function": "Germination support", "Application": "Seed coating", "Best for": "All sown crops"}),
    dict(slug="flowering-cycle-kit", name="Flowering Cycle Kit", sub="Flowering Cycle Kit", cat="kit",
         img="FLOWERING CYCLE KIT.jpg", link="https://siestogreen.com/flowering-cycle-kit/",
         desc="A flowering-stage kit formulated to support even bloom, fruit set and final yield quality.",
         long="The Flowering Cycle Kit is timed for the reproductive stage of the crop, supporting even flowering, stronger fruit set and better final quality at harvest — the stage where much of a season's yield potential is decided.",
         facts={"Contains": "Flowering-stage capsules", "Function": "Bloom & fruit-set support", "Application": "Soil / drip", "Best for": "Fruiting & flowering crops"}),
]

CERTIFICATIONS = [
    "EU.webp", "NPOP.webp", "GOI-Department of Fetrilizers.png", "NABL.png",
    "CE.webp", "KEPHIS.webp", "IISR.png", "ORGANIC.png", "ICAR.png", "IFOAM.webp",
]

CONTACT = dict(
    address="Reliable Towers, Mogotio Road, Westlands,\nP.O Box 39886-00623, Nairobi, Kenya",
    phones=["+254 114906756", "+254 112148794"],
    email="jsolutionkenya@gmail.com",
    map_iframe='<iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d249.30272662523353!2d36.80988495981679!3d-1.2664969079562498!2m3!1f0!2f0!3f0!3m2!1s0x182f1763efbdbca5%3A0xea2040773c79ea86!2sJSolution!5e0!3m2!1sen!2ske!4v1783890473602!5m2!1sen!2ske" width="600" height="450" style="border:0;" allowfullscreen loading="lazy" referrerpolicy="strict-origin-when-cross-origin"></iframe>'
)

# ---------------------------------------------------------------------------
# TEMPLATE HELPERS
# ---------------------------------------------------------------------------

def head(title, desc, root=""):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title} | JSolution Limited</title>
<meta name="description" content="{desc}">
<link rel="icon" href="{root}assets/img/jsolution-loading.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,500;9..144,600;9..144,700&family=Inter:wght@400;500;600;700;800&family=IBM+Plex+Mono:wght@400;500&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.css">
<link rel="stylesheet" href="{root}assets/css/style.css">
</head>
"""

def preloader(root=""):
    return f"""<div id="preloader"><img src="{root}assets/img/jsolution-loading.png" alt="JSolution loading"></div>"""

def ticker():
    items = [
        ('bi-telephone', 'CONTACT.PHONE'),
        ('bi-envelope', 'CONTACT.EMAIL'),
        ('bi-geo-alt', 'CONTACT.LOCATION'),
        ('bi-facebook', 'SOCIAL.FACEBOOK'),
        ('bi-instagram', 'SOCIAL.INSTAGRAM'),
        ('bi-linkedin', 'SOCIAL.LINKEDIN'),
    ]
    row = f"""
    <div class="ticker-item"><i class="bi bi-telephone"></i> {CONTACT['phones'][0]}</div>
    <div class="ticker-item"><i class="bi bi-telephone"></i> {CONTACT['phones'][1]}</div>
    <div class="ticker-item"><i class="bi bi-envelope"></i> {CONTACT['email']}</div>
    <div class="ticker-item"><i class="bi bi-geo-alt"></i> Reliable Towers, Mogotio Road, Westlands, Nairobi</div>
    <div class="ticker-item"><i class="bi bi-facebook"></i> Follow us on Facebook</div>
    <div class="ticker-item"><i class="bi bi-instagram"></i> Follow us on Instagram</div>
    <div class="ticker-item"><i class="bi bi-linkedin"></i> Connect on LinkedIn</div>
    """
    return f"""
  <div class="ticker">
    <div class="ticker-track">
      {row}
      {row}
    </div>
  </div>"""

def header(active, root=""):
    def li(href, label, key):
        cls = ' class="active"' if key == active else ''
        return f'<li><a href="{root}{href}"{cls}>{label}</a></li>'
    nav_links = "".join([
        li("index.html", "Home", "home"),
        li("about.html", "About", "about"),
        li("products.html", "Products", "products"),
        li("contact.html", "Contact", "contact"),
    ])
    return f"""
  <header class="site-header">
    <div class="container nav-row">
      <a href="{root}index.html" class="brand">
        <img src="{root}assets/img/logo copy-1.png" alt="JSolution Limited logo">
        <span>
          <span class="brand-word">JSolution</span>
          <span class="brand-tag">Biofertilizers &amp; Biopesticides</span>
        </span>
      </a>
      <nav id="navmenu" class="navmenu">
        <ul>
          {nav_links}
        </ul>
      </nav>
      <div class="nav-cta">
        <a href="{root}contact.html" class="btn btn-primary btn-sm"><i class="bi bi-cart"></i> Order Now</a>
        <button class="mobile-toggle" aria-label="Toggle menu"><i class="bi bi-list"></i></button>
      </div>
    </div>
    <div class="nav-scrim"></div>
  </header>
"""

def footer(root=""):
    prod_links = "".join(f'<li><a href="{root}products/{p["slug"]}.html">{p["name"]}</a></li>' for p in PRODUCTS[:5])
    return f"""
  <footer class="site-footer">
    <div class="container footer-top">
      <div class="footer-brand">
        <span class="brand-word display" style="font-size:1.4rem;">JSolution Limited</span>
        <p>Exclusive Kenyan distributor of Siesto Green's encapsulated organic biofertilizers and biopesticides — sustainable inputs for healthier soil and safer food.</p>
        <div class="footer-social">
          <a href="#" aria-label="Facebook"><i class="bi bi-facebook"></i></a>
          <a href="#" aria-label="Instagram"><i class="bi bi-instagram"></i></a>
          <a href="#" aria-label="LinkedIn"><i class="bi bi-linkedin"></i></a>
          <a href="#" aria-label="X"><i class="bi bi-twitter-x"></i></a>
        </div>
      </div>
      <div>
        <h4>Explore</h4>
        <ul>
          <li><a href="{root}index.html">Home</a></li>
          <li><a href="{root}about.html">About Us</a></li>
          <li><a href="{root}products.html">All Products</a></li>
          <li><a href="{root}contact.html">Contact</a></li>
        </ul>
      </div>
      <div>
        <h4>Popular Capsules</h4>
        <ul>{prod_links}</ul>
      </div>
      <div>
        <h4>Get in Touch</h4>
        <ul>
          <li><i class="bi bi-geo-alt"></i> Reliable Towers, Mogotio Road, Westlands, Nairobi</li>
          <li><i class="bi bi-telephone"></i> {CONTACT['phones'][0]}</li>
          <li><i class="bi bi-envelope"></i> {CONTACT['email']}</li>
        </ul>
      </div>
    </div>
    <div class="container footer-bottom">
      <span>&copy; 2026 JSolution Limited. All rights reserved.</span>
      <span>Exclusive distributor of Siesto Green in Kenya.</span>
    </div>
  </footer>
  <a href="#" id="scroll-top"><i class="bi bi-arrow-up"></i></a>
"""

def scripts(root=""):
    return f"""
  <script src="{root}assets/js/main.js"></script>
</body>
</html>"""

def page(title, desc, active, body, root=""):
    return head(title, desc, root) + "<body>\n" + preloader(root) + ticker() + header(active, root) + "\n<main>\n" + body + "\n</main>\n" + footer(root) + scripts(root)


def product_card(p, root=""):
    c = CATS[p["cat"]]
    return f"""
        <a href="{root}products/{p['slug']}.html" class="product-card" data-cat="{p['cat']}">
          <div class="product-thumb">
            <span class="product-tag {c['tagclass']}">{c['label']}</span>
            <img src="{root}assets/img/{p['img']}" alt="{p['name']}" loading="lazy">
          </div>
          <div class="product-body">
            <span class="sub">{p['sub']}</span>
            <h4>{p['name']}</h4>
            <span class="go-link">View details <i class="bi bi-arrow-right"></i></span>
          </div>
        </a>"""


def write(path, content):
    full = os.path.join(ROOT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8") as f:
        f.write(content)


# ---------------------------------------------------------------------------
# HOME PAGE
# ---------------------------------------------------------------------------

def build_home():
    cat_cards = f"""
        <a href="products.html#fert" class="cat-card cat-fert reveal">
          <div>
            <span class="cat-count">09 CAPSULES</span>
            <h3>Bio-Fertilizers</h3>
            <p>Nitrogen fixers, phosphate solubilisers and potassium mobilisers that feed the soil, not just the plant.</p>
          </div>
          <span class="go">Shop Bio-Fertilizers <i class="bi bi-arrow-right"></i></span>
        </a>
        <a href="products.html#pgpr" class="cat-card cat-pgpr reveal">
          <div>
            <span class="cat-count">04 FORMULAS</span>
            <h3>Growth Promoters</h3>
            <p>Biostimulants and micronutrient boosters that sharpen flowering, fruiting and stress tolerance.</p>
          </div>
          <span class="go">Shop Growth Promoters <i class="bi bi-arrow-right"></i></span>
        </a>
        <a href="products.html#pest" class="cat-card cat-pest reveal">
          <div>
            <span class="cat-count">06 CAPSULES</span>
            <h3>Bio-Pesticides</h3>
            <p>Fungal and bacterial biocontrol for mites, caterpillars, nematodes and more — no synthetic residue.</p>
          </div>
          <span class="go">Shop Bio-Pesticides <i class="bi bi-arrow-right"></i></span>
        </a>"""

    certs = "".join(f'<img src="assets/img/{c}" alt="Certification logo" loading="lazy">' for c in CERTIFICATIONS)

    body = f"""
    <section class="hero">
      <video autoplay muted loop playsinline poster="assets/img/hero-poster.jpg">
        <source src="assets/img/HERO-1.mp4" type="video/mp4">
      </video>
      <div class="container hero-inner">
        <div class="eyebrow">World's 1st Encapsulated Bio-Technology</div>
        <h1 class="h-xl">Organic capsules that rebuild Kenyan soil, one acre at a time.</h1>
        <p class="lede">JSolution Ltd. is the exclusive Kenyan distributor of Siesto Green's encapsulated organic fertilizers and pesticides — helping farmers cut chemical dependency, protect soil, air and water, and grow safer food.</p>
        <div class="hero-cta">
          <a href="products.html" class="btn btn-on-dark">Explore Products <i class="bi bi-arrow-right"></i></a>
          <a href="contact.html" class="btn btn-outline-dark">Talk to Our Team</a>
        </div>
        <div class="hero-stats">
          <div class="hero-stat"><span class="num">1 Trillion</span><span class="lbl">CFU per 1g capsule</span></div>
          <div class="hero-stat"><span class="num">1 Capsule</span><span class="lbl">Treats 1 full acre</span></div>
          <div class="hero-stat"><span class="num">25 Days</span><span class="lbl">Compost time, down from 33 months</span></div>
        </div>
      </div>
    </section>

    <section class="section">
      <div class="container split">
        <div class="split-media reveal">
          <img src="assets/img/about/who-we-are.jpg" alt="Farmer holding healthy soil and seedling">
          <div class="badge-float"><i class="bi bi-patch-check-fill" style="color:var(--dominant);font-size:1.4rem;"></i><span>Exclusive Kenyan distributor of Siesto Green</span></div>
        </div>
        <div class="reveal">
          <div class="eyebrow">Who We Are</div>
          <h2 class="h-lg">Sustainable inputs, built for the Kenyan farmer's bottom line.</h2>
          <p class="lede">At JSolution Ltd., we empower Kenyan farmers with sustainable, cost-effective alternatives to conventional fertilizers. As the exclusive distributor of Siesto Green's Encapsulated Organic Fertilizers and Pesticides, we aim to improve soil fertility, crop productivity, and promote safer food production, enhancing farmers' livelihoods and protecting the environment by mitigating soil, air, and water pollution.</p>
          <a href="about.html" class="btn btn-ghost">More About Us <i class="bi bi-arrow-right"></i></a>
        </div>
      </div>
    </section>

    <section class="section keypoints">
      <div class="container">
        <div class="section-head center">
          <div class="eyebrow">Why Farmers Switch</div>
          <h2 class="h-lg" style="color:#fff;">Three reasons the capsule beats the sack.</h2>
        </div>
        <div class="grid3">
          <div class="kp reveal">
            <span class="tag">01</span>
            <h3>Organic, better than chemical</h3>
            <p>Full microbial nutrition without the soil, air and water pollution that comes with synthetic fertilizer.</p>
          </div>
          <div class="kp reveal">
            <span class="tag">02</span>
            <h3>25-day soil transformation</h3>
            <p>Our bio-capsules cut composting time from 33 months down to 25 days.</p>
          </div>
          <div class="kp reveal">
            <span class="tag">03</span>
            <h3>Built around the capsule</h3>
            <p>Every product ships as a 1-gram capsule carrying 1 trillion CFU — easy to store, transport and apply.</p>
          </div>
        </div>
      </div>
    </section>

    <section class="section">
      <div class="container">
        <div class="section-head center">
          <div class="eyebrow">Shop By Category</div>
          <h2 class="h-lg">Everything the crop needs, in capsule form.</h2>
          <p class="lede" style="margin-inline:auto;">From nitrogen fixers to biological pest control, our full range is distributed exclusively by JSolution across Kenya.</p>
        </div>
        <div class="cat-grid">{cat_cards}</div>
      </div>
    </section>

    <section class="section section-tight" style="background:var(--cream);">
      <div class="container split">
        <div class="reveal">
          <div class="eyebrow">Star Product</div>
          <h2 class="h-lg">The Poornima Cycle Kit</h2>
          <p class="lede">A single bio-enzyme kit — NPK Grow, Zinc Grow, Mycorrhiza, Humigrow and Crop Force — dosed together for the complete development of soil and plant. Available in 1-Acre and 1-Hectare packs.</p>
          <a href="products/poornima-cycle-kit.html" class="btn btn-primary">View the Poornima Kit <i class="bi bi-arrow-right"></i></a>
        </div>
        <div class="split-media reveal">
          <img src="assets/img/POORNIMA CYCLE KIT.png" alt="Poornima Cycle Kit">
        </div>
      </div>
    </section>

    <section class="section-tight certs-strip">
      <div class="container">
        <div class="section-head center"><div class="eyebrow">Certified &amp; Trusted</div><h3 class="h-md">Backed by international organic and quality certification</h3></div>
        <div class="certs-row">{certs}</div>
      </div>
    </section>

    <section class="section">
      <div class="container">
        <div class="cta-banner reveal">
          <div>
            <div class="eyebrow" style="color:var(--lime);">Ready to switch to organic?</div>
            <h3 class="h-md">Talk to our team about the right capsule program for your farm.</h3>
          </div>
          <a href="contact.html" class="btn btn-on-dark">Get In Touch <i class="bi bi-arrow-right"></i></a>
        </div>
      </div>
    </section>
"""
    write("index.html", page("Home", "JSolution Ltd. — exclusive Kenyan distributor of Siesto Green's encapsulated organic biofertilizers and biopesticides.", "home", body))


# ---------------------------------------------------------------------------
# ABOUT PAGE
# ---------------------------------------------------------------------------

def build_about():
    steps = [
        ("Drop In", "Drop 1 capsule into 1 litre of clean water.", "bi-droplet"),
        ("Activate", "Leave for 3–4 hours until the capsule fully dissolves and bacteria activate.", "bi-hourglass-split"),
        ("Dilute", "Shake and empty into a 150–200L clean water tank for drip irrigation or drenching.", "bi-water"),
        ("Apply", "Apply across 1 acre of land using your existing irrigation system.", "bi-sprinkler"),
    ]
    steps_html = "".join(f"""
        <div class="step reveal">
          <div class="cap-icon"></div>
          <h4>{i+1:02d} · {t}</h4>
          <p style="margin-bottom:0;font-size:.92rem;color:var(--ink-soft);">{d}</p>
        </div>""" for i, (t, d, ic) in enumerate(steps))

    precautions = [
        "Never break the capsules into halves.",
        "Use chemical-free water for activation and irrigation.",
        "Use the activated solution within 12 hours through any supportive irrigation method.",
        "Never mix two different types of capsules in the same bottle for activation.",
        "Maintain a gap of at least 7 days between our product and synthetic fertilizer.",
        "Do not mix our biofertilizer with agrochemicals or synthetic fertilizers.",
        "Do not mix our biofertilizer capsules with other liquid or powder biofertilizers.",
        "Do not expose our bio-fertilizers to direct sunlight or heat.",
        "Clean sprayers and equipment before use — no chemical residue should remain.",
    ]
    prec_html = "".join(f'<li><i class="bi bi-check2-circle" style="color:var(--dominant);margin-right:.6em;"></i>{p}</li>' for p in precautions)

    certs = "".join(f'<img src="assets/img/{c}" alt="Certification logo" loading="lazy">' for c in CERTIFICATIONS)

    body = f"""
    <section class="section-tight" style="background:var(--forest-950);color:#fff;padding-top:64px;">
      <div class="container">
        <div class="eyebrow" style="color:var(--lime);">About JSolution</div>
        <h1 class="h-lg" style="color:#fff;">Exclusive distributor of Siesto Green in Kenya.</h1>
        <p class="lede" style="color:#cfe0d5;">Bringing the world's first encapsulated bio-fertilizer and bio-pesticide technology to Kenyan farms.</p>
      </div>
    </section>

    <section class="section">
      <div class="container split">
        <div class="reveal">
          <div class="eyebrow">Who We Are</div>
          <h2 class="h-lg">Soil health first, always.</h2>
          <p>At JSolution Ltd., we empower Kenyan farmers with sustainable, cost-effective alternatives to conventional fertilizers. As the exclusive distributor of Siesto Green's Encapsulated Organic Fertilizers and Pesticides, we aim to improve soil fertility, crop productivity, and promote safer food production — enhancing farmers' livelihoods while protecting the environment from soil, air and water pollution.</p>
        </div>
        <div class="split-media reveal">
          <img src="assets/img/about/soil-hands.jpg" alt="Hands holding soil and a young seedling">
        </div>
      </div>
    </section>

    <section class="section section-tight" style="background:var(--cream);">
      <div class="container" style="display:grid;grid-template-columns:1fr 1fr;gap:32px;">
        <div class="card reveal">
          <div class="icon-cap"><i class="bi bi-bullseye"></i></div>
          <h3>Our Mission</h3>
          <p>To give every Kenyan farmer an affordable, organic route to healthier soil and higher-quality crops — replacing chemical dependency with living, capsule-based microbial technology.</p>
        </div>
        <div class="card reveal">
          <div class="icon-cap"><i class="bi bi-binoculars"></i></div>
          <h3>Our Vision</h3>
          <p>A Kenyan agricultural sector where organic, encapsulated biofertilizers are the default choice — building soil that regenerates, food that's safer, and farming that's genuinely sustainable.</p>
        </div>
      </div>
    </section>

    <section class="section">
      <div class="container split">
        <div class="reveal">
          <div class="eyebrow">The Technology</div>
          <h2 class="h-lg">What is an encapsulated bio-fertilizer?</h2>
          <p>Biofertilizers are tiny capsules packed with beneficial microorganisms and essential nutrients. When added to soil, they enhance plant growth and crop yields. Our capsules represent the World's 1st Encapsulated Technology — a genuine pioneering step in agricultural input design.</p>
          <div class="pd-facts" style="grid-template-columns:1fr 1fr;">
            <div class="pd-fact"><div class="k">Weight</div><div class="v">1 gram / capsule</div></div>
            <div class="pd-fact"><div class="k">CFU count</div><div class="v">1 trillion / gram</div></div>
            <div class="pd-fact"><div class="k">Shelf life</div><div class="v">16–24 months</div></div>
            <div class="pd-fact"><div class="k">Coverage</div><div class="v">1 capsule / acre</div></div>
          </div>
        </div>
        <div class="reveal">
          <div class="card">
            <h4>Advantages of Bio Capsules</h4>
            <ul style="display:grid;grid-template-columns:1fr 1fr;gap:.6em .8em;margin-top:1em;">
              <li><i class="bi bi-check2" style="color:var(--dominant);"></i> Reduced chemical dependency</li>
              <li><i class="bi bi-check2" style="color:var(--dominant);"></i> Environmentally friendly</li>
              <li><i class="bi bi-check2" style="color:var(--dominant);"></i> High microbial content</li>
              <li><i class="bi bi-check2" style="color:var(--dominant);"></i> Easy handling &amp; transport</li>
              <li><i class="bi bi-check2" style="color:var(--dominant);"></i> Improved soil structure</li>
              <li><i class="bi bi-check2" style="color:var(--dominant);"></i> Disease suppression</li>
              <li><i class="bi bi-check2" style="color:var(--dominant);"></i> Cost-effective</li>
              <li><i class="bi bi-check2" style="color:var(--dominant);"></i> 100% organic &amp; water soluble</li>
            </ul>
          </div>
        </div>
      </div>
    </section>

    <section class="section section-tight" style="background:var(--forest-950);color:#fff;">
      <div class="container">
        <div class="section-head center"><div class="eyebrow" style="color:var(--lime);">Application</div><h2 class="h-lg" style="color:#fff;">How a capsule becomes a full acre of nutrition</h2></div>
        <div class="steps" style="--line:rgba(255,255,255,.16);">
          {steps_html}
        </div>
      </div>
    </section>

    <section class="section">
      <div class="container">
        <div class="section-head center"><div class="eyebrow">Handle With Care</div><h2 class="h-lg">Precautions for best results</h2></div>
        <div class="card" style="max-width:820px;margin-inline:auto;">
          <ul style="display:grid;gap:.9em;">{prec_html}</ul>
        </div>
      </div>
    </section>

    <section class="section-tight certs-strip">
      <div class="container">
        <div class="section-head center"><div class="eyebrow">Certifications</div><h3 class="h-md">Product, company &amp; membership certifications</h3></div>
        <div class="certs-row">{certs}</div>
      </div>
    </section>

    <section class="section">
      <div class="container">
        <div class="cta-banner reveal">
          <div>
            <div class="eyebrow" style="color:var(--lime);">See the full range</div>
            <h3 class="h-md">24 capsules and kits across fertilizers, growth promoters and pesticides.</h3>
          </div>
          <a href="products.html" class="btn btn-on-dark">Browse Products <i class="bi bi-arrow-right"></i></a>
        </div>
      </div>
    </section>
"""
    write("about.html", page("About Us", "Learn about JSolution Ltd., exclusive Kenyan distributor of Siesto Green's encapsulated organic biofertilizer technology.", "about", body))


# ---------------------------------------------------------------------------
# PRODUCTS PAGE
# ---------------------------------------------------------------------------

def build_products():
    cards = "".join(product_card(p) for p in PRODUCTS)
    filters = """
        <button class="filter-btn active" data-filter="all">All Products</button>
        <button class="filter-btn" data-filter="fert">Bio-Fertilizers</button>
        <button class="filter-btn" data-filter="pgpr">Growth Promoters</button>
        <button class="filter-btn" data-filter="pest">Bio-Pesticides</button>
        <button class="filter-btn" data-filter="kit">Capsule Kits</button>"""

    body = f"""
    <section class="section-tight" style="padding-top:56px;">
      <div class="container">
        <div class="eyebrow">Full Catalogue</div>
        <h1 class="h-lg">24 capsules, powders &amp; kits — one soil-health system.</h1>
        <p class="lede">Every product page has its own direct order form. Enter your name and phone number and our team follows up to confirm delivery.</p>
      </div>
    </section>
    <section class="section-tight">
      <div class="container">
        <div class="filter-bar">{filters}</div>
        <div class="product-grid">{cards}</div>
      </div>
    </section>
"""
    write("products.html", page("Products", "Browse JSolution's full range of encapsulated biofertilizers, growth promoters and biopesticides.", "products", body))


# ---------------------------------------------------------------------------
# CONTACT PAGE
# ---------------------------------------------------------------------------

def build_contact():
    product_options = "".join(f'<option value="{p["name"]}">{p["name"]}</option>' for p in PRODUCTS)
    body = f"""
    <section class="section-tight" style="padding-top:56px;">
      <div class="container">
        <div class="eyebrow">Get In Touch</div>
        <h1 class="h-lg">Talk to the JSolution team.</h1>
        <p class="lede">Questions about a product, bulk orders, or setting up a capsule program for your farm — we're based in Nairobi and happy to help.</p>
      </div>
    </section>

    <section class="section">
      <div class="container contact-grid">
        <div class="reveal">
          <div class="card">
            <h3>Send Us a Message</h3>
            <form class="contact-form" action="https://api.web3forms.com/submit" method="POST">
              <input type="hidden" name="access_key" value="">
              <input type="hidden" name="subject" value="New enquiry from JSolution website">
              <div class="form-row">
                <label for="c-name">Full Name</label>
                <input id="c-name" type="text" name="name" required>
              </div>
              <div class="form-row">
                <label for="c-email">Email Address</label>
                <input id="c-email" type="email" name="email" required>
              </div>
              <div class="form-row">
                <label for="c-phone">Phone Number</label>
                <input id="c-phone" type="tel" name="phone" required>
              </div>
              <div class="form-row">
                <label for="c-product">Product of Interest</label>
                <select id="c-product" name="product">
                  <option value="">General enquiry</option>
                  {product_options}
                </select>
              </div>
              <div class="form-row">
                <label for="c-message">Message</label>
                <textarea id="c-message" name="message" rows="4" required></textarea>
              </div>
              <button type="submit" class="btn btn-primary btn-block">Send Message <i class="bi bi-send"></i></button>
              <p class="form-status"></p>
            </form>
          </div>
        </div>

        <div class="reveal">
          <h3>Contact Details</h3>
          <div class="contact-method">
            <div class="icon-cap"><i class="bi bi-geo-alt"></i></div>
            <div><strong>Address</strong><p>Reliable Towers, Mogotio Road, Westlands.<br>P.O Box 39886-00623, Nairobi, Kenya.</p></div>
          </div>
          <div class="contact-method">
            <div class="icon-cap"><i class="bi bi-telephone"></i></div>
            <div><strong>Phone</strong><p>{CONTACT['phones'][0]}<br>{CONTACT['phones'][1]}</p></div>
          </div>
          <div class="contact-method">
            <div class="icon-cap"><i class="bi bi-envelope"></i></div>
            <div><strong>Email</strong><p>{CONTACT['email']}</p></div>
          </div>
          <div class="map-wrap">{CONTACT['map_iframe']}</div>
        </div>
      </div>
    </section>
"""
    write("contact.html", page("Contact", "Contact JSolution Limited — Reliable Towers, Mogotio Road, Westlands, Nairobi.", "contact", body))


# ---------------------------------------------------------------------------
# PRODUCT DETAIL PAGES
# ---------------------------------------------------------------------------

def build_product_pages():
    root = "../"
    for p in PRODUCTS:
        c = CATS[p["cat"]]
        facts_html = "".join(f'<div class="pd-fact"><div class="k">{k}</div><div class="v">{v}</div></div>' for k, v in p["facts"].items())
        related = [x for x in PRODUCTS if x["cat"] == p["cat"] and x["slug"] != p["slug"]][:4]
        if len(related) < 4:
            related += [x for x in PRODUCTS if x["slug"] != p["slug"] and x not in related][: 4 - len(related)]
        related_html = "".join(product_card(r, root=root) for r in related)

        body = f"""
    <section class="section-tight" style="padding-top:40px;">
      <div class="container">
        <div class="pd-breadcrumb"><a href="../index.html">Home</a> / <a href="../products.html">Products</a> / <a href="../products.html#{p['cat']}">{c['label']}</a> / {p['name']}</div>
        <div class="pd-wrap">
          <div class="pd-media reveal">
            <img src="../assets/img/{p['img']}" alt="{p['name']} — {p['sub']}">
          </div>
          <div class="reveal">
            <span class="product-tag {c['tagclass']}" style="position:static;display:inline-flex;margin-bottom:1em;">{c['label']}</span>
            <h1 class="h-lg mt-0">{p['name']}</h1>
            <p class="eyebrow" style="color:var(--ink-soft);text-transform:none;letter-spacing:normal;font-family:var(--font-body);font-size:1rem;">{p['sub']}</p>
            <p class="lede">{p['long']}</p>

            <div class="pd-facts">{facts_html}</div>

            <a href="{p['link']}" target="_blank" rel="noopener" class="btn btn-ghost btn-sm">Full technical spec sheet <i class="bi bi-box-arrow-up-right"></i></a>

            <div class="order-box">
              <h4>Order {p['name']}</h4>
              <p class="form-note mt-0">Enter your name and phone number — our team will call to confirm quantity and delivery.</p>
              <form class="order-form" action="https://api.web3forms.com/submit" method="POST">
                <input type="hidden" name="access_key" value="">
                <input type="hidden" name="subject" value="Order request: {p['name']}">
                <input type="hidden" name="product" value="{p['name']}">
                <div class="form-row">
                  <label for="o-name-{p['slug']}">Full Name</label>
                  <input id="o-name-{p['slug']}" type="text" name="name" required>
                </div>
                <div class="form-row">
                  <label for="o-phone-{p['slug']}">Phone Number</label>
                  <input id="o-phone-{p['slug']}" type="tel" name="phone" required>
                </div>
                <button type="submit" class="btn btn-primary btn-block">Order Now — {p['name']} <i class="bi bi-arrow-right"></i></button>
                <p class="form-status"></p>
              </form>
            </div>
          </div>
        </div>
      </div>
    </section>

    <section class="section">
      <div class="container">
        <div class="section-head"><div class="eyebrow">You May Also Need</div><h2 class="h-md">More from {c['label']}</h2></div>
        <div class="related-row">{related_html}</div>
      </div>
    </section>
"""
        write(f"products/{p['slug']}.html", page(p["name"], f"{p['name']} — {p['sub']}. Order directly from JSolution Limited, exclusive Kenyan distributor of Siesto Green.", "products", body, root=root))


if __name__ == "__main__":
    build_home()
    build_about()
    build_products()
    build_contact()
    build_product_pages()
    print("Build complete:", len(PRODUCTS), "product pages +4 core pages")
