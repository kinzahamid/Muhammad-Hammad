from flask import Flask, render_template_string, url_for

app = Flask(__name__)

# ============================================================
# ELITE PORTFOLIO FOR MUHAMMAD HAMMAD
# Marketing Professional | Merchandising Expert | BBA
# ============================================================
# PHOTO: Place your photo at static/hammad.jpg
#        (Change to .png in HTML_TEMPLATE if needed)
# ============================================================

CSS = """
:root {
    --navy-deep: #070b14; --navy-mid: #0a0e1a; --navy-light: #0f172a;
    --charcoal: #1e293b; --slate: #334155; --silver: #94a3b8;
    --silver-light: #cbd5e1; --white: #f8fafc; --gold: #d4af37;
    --gold-soft: #fbbf24; --gold-dim: rgba(212,175,55,0.15);
    --accent: #3b82f6; --accent-soft: rgba(59,130,246,0.15);
    --glass: rgba(15,23,42,0.7); --glass-border: rgba(255,255,255,0.08);
    --shadow: 0 25px 50px -12px rgba(0,0,0,0.5);
    --radius: 16px; --radius-sm: 8px;
    --transition: all 0.4s cubic-bezier(0.4,0,0.2,1);
    --font-heading: 'Playfair Display', serif;
    --font-body: 'Inter', sans-serif;
}
*, *::before, *::after { margin:0; padding:0; box-sizing:border-box; }
html { scroll-behavior:smooth; font-size:16px; }
body { font-family: var(--font-body); background: var(--navy-deep); color: var(--silver-light); line-height:1.6; overflow-x:hidden; -webkit-font-smoothing:antialiased; }
::selection { background:var(--gold); color:var(--navy-deep); }
.scroll-progress { position:fixed; top:0; left:0; height:3px; background: linear-gradient(90deg, var(--gold), var(--accent)); z-index:9999; width:0%; transition:width 0.1s linear; }
.particle-canvas { position:fixed; top:0; left:0; width:100%; height:100%; pointer-events:none; z-index:0; opacity:0.4; }

/* NAVIGATION */
.navbar { position:fixed; top:0; left:0; width:100%; z-index:1000; padding:1.25rem 0; transition:var(--transition); background:transparent; }
.navbar.scrolled { background:rgba(7,11,20,0.85); backdrop-filter:blur(20px); -webkit-backdrop-filter:blur(20px); border-bottom:1px solid var(--glass-border); padding:0.75rem 0; }
.nav-container { max-width:1280px; margin:0 auto; padding:0 2rem; display:flex; justify-content:space-between; align-items:center; }
.nav-logo { text-decoration:none; display:flex; align-items:center; gap:0.5rem; }
.logo-text { font-family:var(--font-heading); font-size:1.75rem; font-weight:700; color:var(--white); letter-spacing:1px; position:relative; }
.logo-text::after { content:''; position:absolute; bottom:-2px; left:0; width:100%; height:2px; background:linear-gradient(90deg, var(--gold), transparent); }
.nav-menu { display:flex; list-style:none; gap:2.5rem; align-items:center; }
.nav-link { text-decoration:none; color:var(--silver); font-size:0.875rem; font-weight:500; letter-spacing:0.5px; text-transform:uppercase; position:relative; padding:0.5rem 0; transition:var(--transition); }
.nav-link::after { content:''; position:absolute; bottom:0; left:0; width:0; height:2px; background:linear-gradient(90deg, var(--gold), var(--accent)); transition:width 0.3s ease; }
.nav-link:hover, .nav-link.active { color:var(--white); }
.nav-link:hover::after, .nav-link.active::after { width:100%; }
.hamburger { display:none; cursor:pointer; flex-direction:column; gap:5px; padding:5px; z-index:1001; }
.bar { display:block; width:25px; height:2px; background:var(--white); transition:var(--transition); border-radius:2px; }
.hamburger.active .bar:nth-child(1) { transform:rotate(45deg) translate(5px,5px); }
.hamburger.active .bar:nth-child(2) { opacity:0; }
.hamburger.active .bar:nth-child(3) { transform:rotate(-45deg) translate(5px,-5px); }

/* HERO */
.hero { min-height:100vh; display:flex; align-items:center; position:relative; overflow:hidden; padding:8rem 2rem 4rem; background:linear-gradient(135deg, var(--navy-deep) 0%, var(--navy-mid) 50%, #0d1321 100%); }
.hero-bg-elements { position:absolute; inset:0; overflow:hidden; pointer-events:none; }
.bg-grid { position:absolute; inset:0; background-image: linear-gradient(rgba(212,175,55,0.03) 1px, transparent 1px), linear-gradient(90deg, rgba(212,175,55,0.03) 1px, transparent 1px); background-size:60px 60px; animation:gridMove 20s linear infinite; }
@keyframes gridMove { 0%{transform:translate(0,0);} 100%{transform:translate(60px,60px);} }
.bg-glow { position:absolute; border-radius:50%; filter:blur(100px); opacity:0.15; animation:glowPulse 8s ease-in-out infinite; }
.bg-glow-1 { width:500px; height:500px; background:var(--gold); top:-10%; right:-5%; }
.bg-glow-2 { width:400px; height:400px; background:var(--accent); bottom:-10%; left:-5%; animation-delay:4s; }
@keyframes glowPulse { 0%,100%{transform:scale(1);opacity:0.15;} 50%{transform:scale(1.2);opacity:0.25;} }
.floating-icon { position:absolute; color:rgba(212,175,55,0.15); font-size:1.5rem; animation:floatIcon 6s ease-in-out infinite; }
@keyframes floatIcon { 0%,100%{transform:translateY(0) rotate(0deg);} 50%{transform:translateY(-20px) rotate(5deg);} }
.bg-graph { position:absolute; bottom:0; left:0; width:100%; height:40%; opacity:0.08; }
.graph-line { fill:none; stroke:var(--gold); stroke-width:2; stroke-dasharray:1000; stroke-dashoffset:1000; animation:drawLine 4s ease forwards; }
.graph-line-2 { fill:none; stroke:var(--accent); stroke-width:2; stroke-dasharray:1000; stroke-dashoffset:1000; animation:drawLine 4s ease 1s forwards; }
@keyframes drawLine { to{stroke-dashoffset:0;} }
.hero-container { max-width:1280px; margin:0 auto; width:100%; display:grid; grid-template-columns:1fr 1fr; gap:4rem; align-items:center; position:relative; z-index:1; }
.hero-badge { display:inline-flex; align-items:center; gap:0.5rem; background:var(--gold-dim); border:1px solid rgba(212,175,55,0.2); padding:0.5rem 1rem; border-radius:100px; font-size:0.8rem; font-weight:500; color:var(--gold-soft); margin-bottom:1.5rem; width:fit-content; }
.badge-dot { width:8px; height:8px; background:var(--gold); border-radius:50%; animation:pulse 2s infinite; }
@keyframes pulse { 0%,100%{opacity:1;transform:scale(1);} 50%{opacity:0.5;transform:scale(1.2);} }
.hero-title { font-family:var(--font-heading); font-size:clamp(2.5rem,6vw,5rem); font-weight:700; line-height:1.1; color:var(--white); margin-bottom:1rem; }
.title-line { display:block; background:linear-gradient(135deg, var(--white) 0%, var(--silver-light) 100%); -webkit-background-clip:text; -webkit-text-fill-color:transparent; background-clip:text; }
.hero-subtitles { display:flex; align-items:center; gap:1rem; margin-bottom:1.5rem; flex-wrap:wrap; }
.subtitle { font-size:1.1rem; font-weight:600; color:var(--gold-soft); letter-spacing:1px; text-transform:uppercase; }
.subtitle-separator { color:var(--slate); font-weight:300; }
.hero-statement { font-size:1.125rem; color:var(--silver); max-width:500px; margin-bottom:2.5rem; line-height:1.7; }
.hero-cta { display:flex; gap:1rem; flex-wrap:wrap; }

/* BUTTONS */
.btn { display:inline-flex; align-items:center; gap:0.75rem; padding:0.875rem 2rem; border-radius:var(--radius-sm); font-size:0.9rem; font-weight:600; letter-spacing:0.5px; text-decoration:none; transition:var(--transition); cursor:pointer; border:none; position:relative; overflow:hidden; }
.btn::before { content:''; position:absolute; inset:0; background:linear-gradient(90deg, transparent, rgba(255,255,255,0.1), transparent); transform:translateX(-100%); transition:transform 0.6s ease; }
.btn:hover::before { transform:translateX(100%); }
.btn-primary { background:linear-gradient(135deg, var(--gold) 0%, #c9a227 100%); color:var(--navy-deep); box-shadow:0 4px 20px rgba(212,175,55,0.3); }
.btn-primary:hover { transform:translateY(-3px); box-shadow:0 8px 30px rgba(212,175,55,0.4); }
.btn-outline { background:transparent; color:var(--white); border:1px solid var(--glass-border); backdrop-filter:blur(10px); }
.btn-outline:hover { border-color:var(--gold); background:var(--gold-dim); transform:translateY(-3px); }
.btn-whatsapp { background:linear-gradient(135deg, #25d366 0%, #128c7e 100%); color:white; box-shadow:0 4px 20px rgba(37,211,102,0.3); }
.btn-whatsapp:hover { transform:translateY(-3px); box-shadow:0 8px 30px rgba(37,211,102,0.4); }
.btn-linkedin { background:linear-gradient(135deg, #0077b5 0%, #005885 100%); color:white; box-shadow:0 4px 20px rgba(0,119,181,0.3); }
.btn-linkedin:hover { transform:translateY(-3px); box-shadow:0 8px 30px rgba(0,119,181,0.4); }
.btn-email { background:linear-gradient(135deg, var(--charcoal) 0%, var(--slate) 100%); color:var(--white); border:1px solid var(--glass-border); }
.btn-email:hover { transform:translateY(-3px); border-color:var(--accent); }

/* HERO IMAGE */
.hero-image-wrapper { display:flex; justify-content:center; align-items:center; position:relative; }
.image-container { position:relative; width:350px; height:350px; }
.orbit-ring { position:absolute; inset:-30px; border:1px dashed rgba(212,175,55,0.2); border-radius:50%; animation:orbitRotate 20s linear infinite; }
.orbit-ring::before { content:''; position:absolute; inset:-15px; border:1px solid rgba(59,130,246,0.15); border-radius:50%; animation:orbitRotate 15s linear infinite reverse; }
@keyframes orbitRotate { from{transform:rotate(0deg);} to{transform:rotate(360deg);} }
.gradient-ring { position:absolute; inset:-8px; border-radius:50%; background:linear-gradient(135deg, var(--gold), var(--accent), var(--gold)); background-size:200% 200%; animation:gradientShift 4s ease infinite; padding:3px; }
@keyframes gradientShift { 0%,100%{background-position:0% 50%;} 50%{background-position:100% 50%;} }
.photo-frame { position:relative; width:100%; height:100%; border-radius:50%; overflow:hidden; background:var(--navy-light); z-index:2; }
.profile-photo { width:100%; height:100%; object-fit:cover; object-position:center top; }
.photo-glow { position:absolute; inset:-20px; border-radius:50%; background:radial-gradient(circle, rgba(212,175,55,0.2) 0%, transparent 70%); z-index:-1; animation:glowPulse 4s ease-in-out infinite; }
.floating-label { position:absolute; background:var(--glass); backdrop-filter:blur(10px); border:1px solid var(--glass-border); padding:0.5rem 1rem; border-radius:var(--radius-sm); font-size:0.75rem; font-weight:600; color:var(--silver-light); letter-spacing:1px; text-transform:uppercase; animation:floatLabel 5s ease-in-out infinite; white-space:nowrap; z-index:3; }
.floating-label i { color:var(--gold); margin-right:0.5rem; }
@keyframes floatLabel { 0%,100%{transform:translateY(0);} 50%{transform:translateY(-15px);} }
.photo-badge { position:absolute; bottom:-10px; left:50%; transform:translateX(-50%); background:linear-gradient(135deg, var(--gold) 0%, #c9a227 100%); color:var(--navy-deep); padding:0.5rem 1.25rem; border-radius:100px; font-size:0.8rem; font-weight:700; display:flex; align-items:center; gap:0.5rem; box-shadow:0 4px 20px rgba(212,175,55,0.3); z-index:4; white-space:nowrap; }
.hero-scroll { position:absolute; bottom:2rem; left:50%; transform:translateX(-50%); z-index:2; }
.scroll-indicator { display:flex; flex-direction:column; align-items:center; gap:0.75rem; color:var(--silver); font-size:0.75rem; letter-spacing:2px; text-transform:uppercase; }
.scroll-mouse { width:24px; height:38px; border:2px solid var(--slate); border-radius:12px; display:flex; justify-content:center; padding-top:8px; }
.scroll-wheel { width:4px; height:8px; background:var(--gold); border-radius:2px; animation:scrollWheel 2s infinite; }
@keyframes scrollWheel { 0%{transform:translateY(0);opacity:1;} 100%{transform:translateY(12px);opacity:0;} }

/* SECTIONS */
.section { padding:6rem 2rem; position:relative; }
.section-container { max-width:1200px; margin:0 auto; }
.section-header { text-align:center; margin-bottom:4rem; }
.section-label { display:inline-block; font-size:0.8rem; font-weight:600; color:var(--gold); letter-spacing:3px; text-transform:uppercase; margin-bottom:1rem; }
.section-title { font-family:var(--font-heading); font-size:clamp(2rem,4vw,3rem); font-weight:700; color:var(--white); margin-bottom:1rem; }
.section-line { width:60px; height:3px; background:linear-gradient(90deg, var(--gold), var(--accent)); margin:0 auto; border-radius:2px; }

/* ABOUT */
.about { background:linear-gradient(180deg, var(--navy-deep) 0%, var(--navy-mid) 100%); }
.about-grid { display:grid; grid-template-columns:1fr 1fr; gap:4rem; align-items:start; }
.about-content { display:flex; flex-direction:column; gap:1.5rem; }
.about-text { font-size:1.05rem; color:var(--silver); line-height:1.8; }
.about-text strong { color:var(--white); font-weight:600; }
.about-interests { display:flex; flex-wrap:wrap; gap:0.75rem; margin-top:1rem; }
.interest-tag { background:var(--glass); border:1px solid var(--glass-border); padding:0.5rem 1rem; border-radius:100px; font-size:0.8rem; color:var(--silver-light); transition:var(--transition); }
.interest-tag:hover { background:var(--gold-dim); border-color:rgba(212,175,55,0.3); color:var(--gold-soft); transform:translateY(-2px); }
.stats-grid { display:grid; grid-template-columns:1fr 1fr; gap:1.5rem; }
.stat-card { background:var(--glass); border:1px solid var(--glass-border); border-radius:var(--radius); padding:2rem; text-align:center; transition:var(--transition); position:relative; overflow:hidden; }
.stat-card::before { content:''; position:absolute; top:0; left:0; width:100%; height:3px; background:linear-gradient(90deg, var(--gold), var(--accent)); transform:scaleX(0); transition:transform 0.4s ease; }
.stat-card:hover::before { transform:scaleX(1); }
.stat-card:hover { transform:translateY(-5px); border-color:rgba(212,175,55,0.2); box-shadow:var(--shadow); }
.stat-icon { font-size:1.75rem; color:var(--gold); margin-bottom:1rem; }
.stat-number { font-family:var(--font-heading); font-size:2.5rem; font-weight:700; color:var(--white); line-height:1; }
.stat-suffix { font-size:0.875rem; color:var(--gold-soft); font-weight:600; margin-top:0.25rem; }
.stat-text { font-family:var(--font-heading); font-size:1.25rem; font-weight:700; color:var(--white); }
.stat-label { font-size:0.875rem; color:var(--silver); margin-top:0.5rem; }

/* EXPERIENCE */
.experience { background:var(--navy-mid); }
.timeline { position:relative; max-width:800px; margin:0 auto; }
.timeline-line { position:absolute; left:50%; top:0; bottom:0; width:2px; background:linear-gradient(180deg, var(--gold), var(--accent)); transform:translateX(-50%); }
.timeline-item { position:relative; margin-bottom:3rem; display:flex; justify-content:center; }
.timeline-dot { position:absolute; left:50%; top:2rem; width:16px; height:16px; background:var(--gold); border:3px solid var(--navy-mid); border-radius:50%; transform:translateX(-50%); z-index:2; box-shadow:0 0 0 4px rgba(212,175,55,0.2); }
.timeline-card { width:calc(50% - 3rem); background:var(--glass); border:1px solid var(--glass-border); border-radius:var(--radius); padding:2rem; transition:var(--transition); }
.timeline-item:nth-child(odd) .timeline-card { margin-right:auto; margin-left:0; }
.timeline-item:nth-child(even) .timeline-card { margin-left:auto; margin-right:0; }
.timeline-card:hover { border-color:rgba(212,175,55,0.2); box-shadow:var(--shadow); transform:translateY(-3px); }
.timeline-header { display:flex; align-items:flex-start; gap:1rem; margin-bottom:1.5rem; }
.company-logo { width:50px; height:50px; background:linear-gradient(135deg, var(--gold) 0%, #c9a227 100%); border-radius:var(--radius-sm); display:flex; align-items:center; justify-content:center; font-size:1.25rem; color:var(--navy-deep); flex-shrink:0; }
.company-logo.medical { background:linear-gradient(135deg, var(--accent) 0%, #2563eb 100%); color:white; }
.timeline-meta h3 { font-size:1.25rem; font-weight:700; color:var(--white); margin-bottom:0.25rem; }
.timeline-role { display:block; color:var(--gold-soft); font-size:0.9rem; font-weight:600; margin-bottom:0.5rem; }
.timeline-duration { display:flex; align-items:center; gap:0.5rem; color:var(--silver); font-size:0.8rem; }
.timeline-responsibilities { list-style:none; margin-bottom:1.5rem; }
.timeline-responsibilities li { display:flex; align-items:flex-start; gap:0.75rem; margin-bottom:0.75rem; color:var(--silver); font-size:0.9rem; }
.timeline-responsibilities li i { color:var(--gold); margin-top:0.25rem; font-size:0.8rem; }
.timeline-tags { display:flex; flex-wrap:wrap; gap:0.5rem; }
.tag { background:rgba(59,130,246,0.1); border:1px solid rgba(59,130,246,0.2); color:var(--accent); padding:0.25rem 0.75rem; border-radius:100px; font-size:0.75rem; font-weight:500; }

/* EXPERTISE */
.expertise { background:linear-gradient(180deg, var(--navy-mid) 0%, var(--navy-deep) 100%); }
.expertise-grid { display:grid; grid-template-columns:repeat(4, 1fr); gap:1.5rem; }
.expertise-card { background:var(--glass); border:1px solid var(--glass-border); border-radius:var(--radius); padding:2rem; position:relative; overflow:hidden; transition:var(--transition); }
.expertise-card:hover { transform:translateY(-5px); border-color:rgba(212,175,55,0.2); box-shadow:var(--shadow); }
.expertise-glow { position:absolute; top:-50%; left:-50%; width:200%; height:200%; background:radial-gradient(circle, rgba(212,175,55,0.1) 0%, transparent 70%); opacity:0; transition:opacity 0.4s ease; }
.expertise-card:hover .expertise-glow { opacity:1; }
.expertise-icon { width:50px; height:50px; background:linear-gradient(135deg, var(--gold-dim) 0%, var(--accent-soft) 100%); border-radius:var(--radius-sm); display:flex; align-items:center; justify-content:center; font-size:1.25rem; color:var(--gold-soft); margin-bottom:1.25rem; position:relative; z-index:1; }
.expertise-card h3 { font-size:1.1rem; font-weight:700; color:var(--white); margin-bottom:0.75rem; position:relative; z-index:1; }
.expertise-card p { font-size:0.9rem; color:var(--silver); line-height:1.6; position:relative; z-index:1; }

/* EDUCATION */
.edu-timeline { position:relative; max-width:700px; margin:0 auto 4rem; }
.edu-line { position:absolute; left:2rem; top:0; bottom:0; width:2px; background:linear-gradient(180deg, var(--gold), var(--accent)); }
.edu-item { position:relative; padding-left:5rem; margin-bottom:2rem; }
.edu-dot { position:absolute; left:2rem; top:1.5rem; width:14px; height:14px; background:var(--gold); border:3px solid var(--navy-deep); border-radius:50%; transform:translateX(-50%); z-index:2; box-shadow:0 0 0 4px rgba(212,175,55,0.2); }
.edu-card { background:var(--glass); border:1px solid var(--glass-border); border-radius:var(--radius); padding:1.75rem; transition:var(--transition); position:relative; }
.edu-card:hover { border-color:rgba(212,175,55,0.2); box-shadow:var(--shadow); transform:translateX(5px); }
.edu-badge { position:absolute; top:1rem; right:1rem; background:linear-gradient(135deg, var(--gold) 0%, #c9a227 100%); color:var(--navy-deep); padding:0.25rem 0.75rem; border-radius:100px; font-size:0.7rem; font-weight:700; }
.edu-icon { width:40px; height:40px; background:linear-gradient(135deg, var(--gold-dim) 0%, var(--accent-soft) 100%); border-radius:var(--radius-sm); display:flex; align-items:center; justify-content:center; font-size:1rem; color:var(--gold-soft); margin-bottom:1rem; }
.edu-degree { font-size:1.1rem; font-weight:700; color:var(--white); margin-bottom:0.5rem; }
.edu-school { color:var(--silver); font-size:0.9rem; margin-bottom:0.25rem; }
.edu-dept { color:var(--silver); font-size:0.85rem; margin-bottom:0.5rem; }
.edu-status, .edu-duration, .edu-year { display:inline-block; background:rgba(59,130,246,0.1); border:1px solid rgba(59,130,246,0.2); color:var(--accent); padding:0.25rem 0.75rem; border-radius:100px; font-size:0.75rem; font-weight:600; }
.edu-year { background:rgba(212,175,55,0.1); border-color:rgba(212,175,55,0.2); color:var(--gold-soft); }
.languages-section { text-align:center; }
.languages-title { font-family:var(--font-heading); font-size:1.5rem; color:var(--white); margin-bottom:2rem; }
.languages-grid { display:flex; justify-content:center; gap:2rem; flex-wrap:wrap; }
.language-card { background:var(--glass); border:1px solid var(--glass-border); border-radius:var(--radius); padding:1.5rem 2rem; display:flex; align-items:center; gap:1rem; transition:var(--transition); }
.language-card:hover { transform:translateY(-3px); border-color:rgba(212,175,55,0.2); }
.lang-flag { width:40px; height:40px; background:linear-gradient(135deg, var(--gold) 0%, var(--accent) 100%); border-radius:50%; display:flex; align-items:center; justify-content:center; font-size:0.8rem; font-weight:700; color:var(--navy-deep); }
.lang-info h4 { font-size:1rem; font-weight:700; color:var(--white); }
.lang-info span { font-size:0.85rem; color:var(--silver); }
.lang-indicator { display:flex; gap:0.25rem; }
.lang-dot { width:8px; height:8px; background:var(--slate); border-radius:50%; }
.lang-dot.active { background:var(--gold); }

/* OBJECTIVE */
.objective { background:var(--navy-mid); }
.objective-card { max-width:800px; margin:0 auto; background:var(--glass); border:1px solid var(--glass-border); border-radius:var(--radius); padding:4rem 3rem; text-align:center; position:relative; transition:var(--transition); }
.objective-card:hover { border-color:rgba(212,175,55,0.2); box-shadow:var(--shadow); }
.objective-quote-icon { font-size:3rem; color:var(--gold); opacity:0.3; margin-bottom:1.5rem; }
.objective-title { font-family:var(--font-heading); font-size:2rem; color:var(--white); margin-bottom:2rem; }
.objective-text { font-size:1.15rem; color:var(--silver); line-height:1.8; font-style:italic; margin-bottom:2rem; }
.objective-signature { display:flex; align-items:center; justify-content:center; gap:1rem; }
.sig-line { width:40px; height:2px; background:var(--gold); }
.sig-name { font-family:var(--font-heading); font-size:1.1rem; color:var(--white); font-weight:600; }

/* SKILLS */
.skills { background:linear-gradient(180deg, var(--navy-deep) 0%, var(--navy-mid) 100%); }
.skills-grid { display:grid; grid-template-columns:repeat(3, 1fr); gap:2rem; }
.skill-category { background:var(--glass); border:1px solid var(--glass-border); border-radius:var(--radius); padding:2rem; transition:var(--transition); }
.skill-category:hover { transform:translateY(-5px); border-color:rgba(212,175,55,0.2); box-shadow:var(--shadow); }
.skill-cat-header { display:flex; align-items:center; gap:1rem; margin-bottom:1.5rem; }
.skill-cat-icon { width:45px; height:45px; background:linear-gradient(135deg, var(--gold-dim) 0%, var(--accent-soft) 100%); border-radius:var(--radius-sm); display:flex; align-items:center; justify-content:center; font-size:1.1rem; color:var(--gold-soft); }
.skill-cat-header h3 { font-size:1.1rem; font-weight:700; color:var(--white); }
.skill-tags { display:flex; flex-wrap:wrap; gap:0.6rem; }
.skill-tag { background:rgba(255,255,255,0.03); border:1px solid var(--glass-border); padding:0.5rem 1rem; border-radius:100px; font-size:0.8rem; color:var(--silver-light); transition:var(--transition); }
.skill-tag:hover { background:var(--gold-dim); border-color:rgba(212,175,55,0.3); color:var(--gold-soft); transform:translateY(-2px); }

/* CONTACT */
.contact { background:var(--navy-mid); }
.contact-intro { text-align:center; font-size:1.1rem; color:var(--silver); max-width:600px; margin:0 auto 3rem; }
.contact-grid { display:grid; grid-template-columns:repeat(4, 1fr); gap:1.5rem; margin-bottom:3rem; }
.contact-card { background:var(--glass); border:1px solid var(--glass-border); border-radius:var(--radius); padding:2rem; text-align:center; text-decoration:none; color:inherit; transition:var(--transition); display:flex; flex-direction:column; align-items:center; }
.contact-card:hover { transform:translateY(-5px); border-color:rgba(212,175,55,0.2); box-shadow:var(--shadow); }
.contact-icon { width:55px; height:55px; background:linear-gradient(135deg, var(--gold-dim) 0%, var(--accent-soft) 100%); border-radius:50%; display:flex; align-items:center; justify-content:center; font-size:1.25rem; color:var(--gold-soft); margin-bottom:1rem; transition:var(--transition); }
.contact-card:hover .contact-icon { background:linear-gradient(135deg, var(--gold) 0%, var(--accent) 100%); color:var(--navy-deep); }
.contact-icon.linkedin { background:rgba(0,119,181,0.1); color:#0077b5; }
.contact-card:hover .contact-icon.linkedin { background:#0077b5; color:white; }
.contact-icon.location { background:rgba(37,211,102,0.1); color:#25d366; }
.contact-card h3 { font-size:1rem; font-weight:700; color:var(--white); margin-bottom:0.5rem; }
.contact-card p { font-size:0.9rem; color:var(--silver); margin-bottom:1rem; word-break:break-word; }
.contact-action { font-size:0.8rem; font-weight:600; color:var(--gold-soft); display:flex; align-items:center; gap:0.5rem; }
.contact-cta { display:flex; justify-content:center; gap:1rem; flex-wrap:wrap; }

/* FOOTER */
.footer { background:var(--navy-deep); padding:4rem 2rem 2rem; position:relative; }
.footer-line { position:absolute; top:0; left:50%; transform:translateX(-50%); width:200px; height:2px; background:linear-gradient(90deg, transparent, var(--gold), transparent); }
.footer-container { max-width:1200px; margin:0 auto; text-align:center; }
.footer-logo { font-family:var(--font-heading); font-size:2rem; font-weight:700; color:var(--white); display:block; margin-bottom:0.5rem; }
.footer-tagline { color:var(--silver); font-size:0.9rem; margin-bottom:2rem; }
.footer-social { display:flex; justify-content:center; gap:1rem; margin-bottom:2rem; }
.social-link { width:45px; height:45px; background:var(--glass); border:1px solid var(--glass-border); border-radius:50%; display:flex; align-items:center; justify-content:center; color:var(--silver); font-size:1.1rem; text-decoration:none; transition:var(--transition); }
.social-link:hover { background:var(--gold); color:var(--navy-deep); border-color:var(--gold); transform:translateY(-3px); }
.footer-bottom { border-top:1px solid var(--glass-border); padding-top:2rem; }
.footer-bottom p { color:var(--silver); font-size:0.8rem; }

/* WHATSAPP FLOAT */
.whatsapp-float { position:fixed; bottom:2rem; right:2rem; width:60px; height:60px; background:linear-gradient(135deg, #25d366 0%, #128c7e 100%); border-radius:50%; display:flex; align-items:center; justify-content:center; color:white; font-size:1.75rem; text-decoration:none; z-index:999; box-shadow:0 4px 20px rgba(37,211,102,0.4); transition:var(--transition); }
.whatsapp-float:hover { transform:scale(1.1); box-shadow:0 6px 30px rgba(37,211,102,0.6); }
.whatsapp-pulse { position:absolute; inset:-4px; border-radius:50%; border:2px solid #25d366; animation:pulseRing 2s infinite; }
@keyframes pulseRing { 0%{transform:scale(1);opacity:1;} 100%{transform:scale(1.3);opacity:0;} }
.whatsapp-tooltip { position:absolute; right:70px; background:var(--charcoal); color:var(--white); padding:0.5rem 1rem; border-radius:var(--radius-sm); font-size:0.8rem; font-weight:600; white-space:nowrap; opacity:0; visibility:hidden; transition:var(--transition); }
.whatsapp-tooltip::after { content:''; position:absolute; right:-6px; top:50%; transform:translateY(-50%); border-width:6px 0 6px 6px; border-style:solid; border-color:transparent transparent transparent var(--charcoal); }
.whatsapp-float:hover .whatsapp-tooltip { opacity:1; visibility:visible; }

/* ============================================================ */
/*  FIX: Content visible by default (no hiding)                 */
/* ============================================================ */
.reveal-up {
    opacity: 1;
    transform: translateY(0);
    transition: opacity 0.8s ease, transform 0.8s ease;
}
/* If you want scroll animation later, you can add a class .hidden */
/* But for now, everything shows immediately */

/* RESPONSIVE */
@media (max-width: 1024px) {
    .hero-container { grid-template-columns:1fr; text-align:center; gap:3rem; }
    .hero-content { order:2; } .hero-image-wrapper { order:1; }
    .hero-statement { margin-left:auto; margin-right:auto; }
    .hero-cta { justify-content:center; }
    .about-grid { grid-template-columns:1fr; gap:3rem; }
    .expertise-grid { grid-template-columns:repeat(2, 1fr); }
    .skills-grid { grid-template-columns:1fr; }
    .contact-grid { grid-template-columns:repeat(2, 1fr); }
}
@media (max-width: 768px) {
    .nav-menu { position:fixed; top:0; right:-100%; width:70%; height:100vh; background:rgba(7,11,20,0.98); backdrop-filter:blur(20px); flex-direction:column; justify-content:center; align-items:center; gap:2rem; transition:right 0.4s ease; z-index:1000; }
    .nav-menu.active { right:0; }
    .hamburger { display:flex; }
    .image-container { width:280px; height:280px; }
    .floating-label { display:none; }
    .timeline-line { left:1rem; }
    .timeline-item { justify-content:flex-start; }
    .timeline-dot { left:1rem; }
    .timeline-card { width:calc(100% - 3rem); margin-left:3rem !important; margin-right:0 !important; }
    .expertise-grid { grid-template-columns:1fr; }
    .contact-grid { grid-template-columns:1fr; }
    .stats-grid { grid-template-columns:1fr 1fr; }
    .edu-item { padding-left:3.5rem; }
    .edu-line { left:1rem; }
    .edu-dot { left:1rem; }
    .section { padding:4rem 1.5rem; }
    .objective-card { padding:2rem 1.5rem; }
    .contact-cta { flex-direction:column; align-items:center; }
    .contact-cta .btn { width:100%; max-width:300px; justify-content:center; }
}
@media (max-width: 480px) {
    .hero { padding:7rem 1rem 3rem; }
    .hero-title { font-size:2.2rem; }
    .hero-subtitles { flex-direction:column; gap:0.5rem; }
    .subtitle-separator { display:none; }
    .image-container { width:240px; height:240px; }
    .stats-grid { grid-template-columns:1fr; }
    .btn { padding:0.75rem 1.5rem; font-size:0.85rem; }
    .whatsapp-float { width:50px; height:50px; font-size:1.5rem; bottom:1rem; right:1rem; }
    .whatsapp-tooltip { display:none; }
}
@media (prefers-reduced-motion: reduce) {
    *, *::before, *::after { animation-duration:0.01ms !important; animation-iteration-count:1 !important; transition-duration:0.01ms !important; }
    .reveal-up { opacity:1; transform:none; }
}
"""


JS = """
document.addEventListener('DOMContentLoaded', function() {
    // No need for fallback anymore - content is visible by default.
    // We keep the scroll progress and other features.

    const scrollProgress = document.getElementById('scrollProgress');
    window.addEventListener('scroll', () => {
        const scrollTop = document.documentElement.scrollTop || document.body.scrollTop;
        const scrollHeight = document.documentElement.scrollHeight - document.documentElement.clientHeight;
        const scrolled = (scrollTop / scrollHeight) * 100;
        scrollProgress.style.width = scrolled + '%';
    });

    const navbar = document.getElementById('navbar');
    window.addEventListener('scroll', () => {
        if (window.scrollY > 50) { navbar.classList.add('scrolled'); }
        else { navbar.classList.remove('scrolled'); }
    });

    const hamburger = document.getElementById('hamburger');
    const navMenu = document.getElementById('navMenu');
    hamburger.addEventListener('click', () => {
        hamburger.classList.toggle('active');
        navMenu.classList.toggle('active');
        document.body.style.overflow = navMenu.classList.contains('active') ? 'hidden' : '';
    });
    document.querySelectorAll('.nav-link').forEach(link => {
        link.addEventListener('click', () => {
            hamburger.classList.remove('active');
            navMenu.classList.remove('active');
            document.body.style.overflow = '';
        });
    });

    const sections = document.querySelectorAll('section[id]');
    const navLinks = document.querySelectorAll('.nav-link');
    window.addEventListener('scroll', () => {
        let current = '';
        sections.forEach(section => {
            const sectionTop = section.offsetTop - 100;
            if (window.scrollY >= sectionTop) { current = section.getAttribute('id'); }
        });
        navLinks.forEach(link => {
            link.classList.remove('active');
            if (link.getAttribute('data-section') === current) { link.classList.add('active'); }
        });
    });

    // Counters (remain)
    const counters = document.querySelectorAll('.stat-number[data-target]');
    const counterObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const target = parseInt(entry.target.getAttribute('data-target'));
                const suffix = entry.target.getAttribute('data-suffix') !== null ? entry.target.getAttribute('data-suffix') : '+';
                const duration = 2000;
                const step = target / (duration / 16);
                let current = 0;
                const updateCounter = () => {
                    current += step;
                    if (current < target) { entry.target.textContent = Math.floor(current); requestAnimationFrame(updateCounter); }
                    else { entry.target.textContent = target + suffix; }
                };
                updateCounter();
                counterObserver.unobserve(entry.target);
            }
        });
    }, { threshold: 0.5 });
    counters.forEach(counter => counterObserver.observe(counter));

    // Particles (remain)
    const canvas = document.getElementById('particleCanvas');
    const ctx = canvas.getContext('2d');
    let particles = [];
    let animationId;
    function resizeCanvas() { canvas.width = window.innerWidth; canvas.height = window.innerHeight; }
    resizeCanvas();
    window.addEventListener('resize', resizeCanvas);

    class Particle {
        constructor() { this.reset(); }
        reset() {
            this.x = Math.random() * canvas.width;
            this.y = Math.random() * canvas.height;
            this.size = Math.random() * 2 + 0.5;
            this.speedX = (Math.random() - 0.5) * 0.3;
            this.speedY = (Math.random() - 0.5) * 0.3;
            this.opacity = Math.random() * 0.5 + 0.1;
            this.color = Math.random() > 0.5 ? '212, 175, 55' : '59, 130, 246';
        }
        update() {
            this.x += this.speedX; this.y += this.speedY;
            if (this.x < 0 || this.x > canvas.width || this.y < 0 || this.y > canvas.height) { this.reset(); }
        }
        draw() {
            ctx.beginPath();
            ctx.arc(this.x, this.y, this.size, 0, Math.PI * 2);
            ctx.fillStyle = 'rgba(' + this.color + ', ' + this.opacity + ')';
            ctx.fill();
        }
    }

    const particleCount = window.innerWidth < 768 ? 20 : 40;
    for (let i = 0; i < particleCount; i++) { particles.push(new Particle()); }

    function animateParticles() {
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        particles.forEach(particle => { particle.update(); particle.draw(); });
        particles.forEach((a, i) => {
            particles.slice(i + 1).forEach(b => {
                const dx = a.x - b.x; const dy = a.y - b.y;
                const distance = Math.sqrt(dx * dx + dy * dy);
                if (distance < 150) {
                    ctx.beginPath(); ctx.moveTo(a.x, a.y); ctx.lineTo(b.x, b.y);
                    ctx.strokeStyle = 'rgba(212, 175, 55, ' + (0.05 * (1 - distance / 150)) + ')';
                    ctx.lineWidth = 0.5; ctx.stroke();
                }
            });
        });
        animationId = requestAnimationFrame(animateParticles);
    }

    const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    if (!prefersReducedMotion) { animateParticles(); }
    else { ctx.clearRect(0, 0, canvas.width, canvas.height); particles.forEach(particle => particle.draw()); }

    document.addEventListener('visibilitychange', () => {
        if (document.hidden) { cancelAnimationFrame(animationId); }
        else if (!prefersReducedMotion) { animateParticles(); }
    });

    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                const offset = 80;
                const targetPosition = target.getBoundingClientRect().top + window.pageYOffset - offset;
                window.scrollTo({ top: targetPosition, behavior: 'smooth' });
            }
        });
    });

    if (!prefersReducedMotion) {
        window.addEventListener('scroll', () => {
            const scrolled = window.pageYOffset;
            const parallaxElements = document.querySelectorAll('.floating-icon');
            parallaxElements.forEach((el, i) => {
                const speed = 0.1 + (i * 0.02);
                el.style.transform = 'translateY(' + (scrolled * speed) + 'px)';
            });
        });
    }

    document.querySelectorAll('.expertise-card, .skill-category, .contact-card, .stat-card').forEach(card => {
        card.addEventListener('touchstart', function() { this.classList.add('touch-active'); });
        card.addEventListener('touchend', function() { setTimeout(() => this.classList.remove('touch-active'), 300); });
    });
});
"""


HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Muhammad Hammad | Marketing Professional & BBA</title>
    <meta name="description" content="Professional portfolio of Muhammad Hammad — Marketing Professional, Merchandising Expert and BBA final-semester student based in Nawabshah, Pakistan.">
    <meta name="keywords" content="Muhammad Hammad, Marketing Professional, Merchandising Expert, BBA, Business Administration, Nawabshah, Pakistan">
    <meta name="author" content="Muhammad Hammad">
    <meta property="og:title" content="Muhammad Hammad | Marketing Professional & BBA">
    <meta property="og:description" content="Professional portfolio of Muhammad Hammad — Marketing Professional, Merchandising Expert and BBA final-semester student.">
    <meta property="og:type" content="website">
    <meta property="og:url" content="https://muhammadhammad.vercel.app">
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="Muhammad Hammad | Marketing Professional & BBA">
    <meta name="twitter:description" content="Professional portfolio of Muhammad Hammad — Marketing Professional, Merchandising Expert and BBA final-semester student.">
    <link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><text y='.9em' font-size='90'>MH</text></svg>">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=Playfair+Display:wght@400;500;600;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
    <style>
        {{ css }}
    </style>
</head>
<body>
    <div class="scroll-progress" id="scrollProgress"></div>
    <canvas id="particleCanvas" class="particle-canvas"></canvas>

    <nav class="navbar" id="navbar">
        <div class="nav-container">
            <a href="#home" class="nav-logo">
                <span class="logo-text">MH.</span>
            </a>
            <ul class="nav-menu" id="navMenu">
                <li><a href="#home" class="nav-link active" data-section="home">Home</a></li>
                <li><a href="#about" class="nav-link" data-section="about">About</a></li>
                <li><a href="#experience" class="nav-link" data-section="experience">Experience</a></li>
                <li><a href="#education" class="nav-link" data-section="education">Education</a></li>
                <li><a href="#expertise" class="nav-link" data-section="expertise">Expertise</a></li>
                <li><a href="#skills" class="nav-link" data-section="skills">Skills</a></li>
                <li><a href="#contact" class="nav-link" data-section="contact">Contact</a></li>
            </ul>
            <div class="hamburger" id="hamburger">
                <span class="bar"></span>
                <span class="bar"></span>
                <span class="bar"></span>
            </div>
        </div>
    </nav>

    <section class="hero" id="home">
        <div class="hero-bg-elements">
            <div class="bg-grid"></div>
            <div class="bg-glow bg-glow-1"></div>
            <div class="bg-glow bg-glow-2"></div>
            <div class="floating-icon" style="top:15%;left:10%;"><i class="fas fa-chart-line"></i></div>
            <div class="floating-icon" style="top:25%;right:15%;animation-delay:1s;"><i class="fas fa-briefcase"></i></div>
            <div class="floating-icon" style="bottom:30%;left:8%;animation-delay:2s;"><i class="fas fa-percentage"></i></div>
            <div class="floating-icon" style="bottom:20%;right:10%;animation-delay:3s;"><i class="fas fa-handshake"></i></div>
            <div class="floating-icon" style="top:60%;left:20%;animation-delay:1.5s;"><i class="fas fa-bullseye"></i></div>
            <div class="floating-icon" style="top:40%;right:25%;animation-delay:2.5s;"><i class="fas fa-users"></i></div>
            <svg class="bg-graph" viewBox="0 0 800 400" preserveAspectRatio="none">
                <path class="graph-line" d="M0,350 Q100,300 200,280 T400,200 T600,150 T800,80" />
                <path class="graph-line-2" d="M0,380 Q150,320 300,300 T500,220 T700,180 T800,120" />
            </svg>
        </div>

        <div class="hero-container">
            <div class="hero-content">
                <div class="hero-badge reveal-up">
                    <span class="badge-dot"></span>
                    <span>BBA Final-Semester Student</span>
                </div>
                <h1 class="hero-title reveal-up">
                    <span class="title-line">MUHAMMAD</span>
                    <span class="title-line">HAMMAD</span>
                </h1>
                <div class="hero-subtitles reveal-up">
                    <span class="subtitle">Marketing Professional</span>
                    <span class="subtitle-separator">|</span>
                    <span class="subtitle">Merchandising Expert</span>
                </div>
                <p class="hero-statement reveal-up">
                    Building business value through marketing, merchandising, customer relationships, and strategic thinking.
                </p>
                <div class="hero-cta reveal-up">
                    <a href="#experience" class="btn btn-primary">
                        <span>View My Experience</span>
                        <i class="fas fa-arrow-right"></i>
                    </a>
                    <a href="#contact" class="btn btn-outline">
                        <span>Contact Me</span>
                        <i class="fas fa-envelope"></i>
                    </a>
                </div>
            </div>

            <div class="hero-image-wrapper reveal-up">
                <div class="image-container">
                    <div class="orbit-ring"></div>
                    <div class="gradient-ring"></div>
                    <div class="photo-frame">
                        <img src="{{ url_for('static', filename='hammad.png') }}" 
                             alt="Muhammad Hammad - Marketing Professional" 
                             class="profile-photo"
                             onerror="this.style.display='none'; this.nextElementSibling.style.display='flex';">
                        <div class="profile-photo-placeholder" style="display:none;" aria-label="Muhammad Hammad professional portrait">
                            <span class="placeholder-initials">MH</span>
                        </div>
                    </div>
                    <div class="photo-glow"></div>
                </div>

                <div class="floating-label" style="top:10%;left:-20%;">
                    <i class="fas fa-bullhorn"></i> MARKETING
                </div>
                <div class="floating-label" style="top:25%;right:-25%;animation-delay:0.5s;">
                    <i class="fas fa-chart-bar"></i> BUSINESS
                </div>
                <div class="floating-label" style="bottom:25%;left:-15%;animation-delay:1s;">
                    <i class="fas fa-seedling"></i> GROWTH
                </div>
                <div class="floating-label" style="bottom:10%;right:-20%;animation-delay:1.5s;">
                    <i class="fas fa-chess"></i> STRATEGY
                </div>

                <div class="photo-badge">
                    <i class="fas fa-graduation-cap"></i>
                    <span>BBA | Marketing & Business</span>
                </div>
            </div>
        </div>

        <div class="hero-scroll">
            <div class="scroll-indicator">
                <div class="scroll-mouse">
                    <div class="scroll-wheel"></div>
                </div>
                <span>Scroll to explore</span>
            </div>
        </div>
    </section>

    <section class="section about" id="about">
        <div class="section-container">
            <div class="section-header reveal-up">
                <span class="section-label">Get To Know</span>
                <h2 class="section-title">About Me</h2>
                <div class="section-line"></div>
            </div>
            <div class="about-grid">
                <div class="about-content reveal-up">
                    <p class="about-text">
                        Muhammad Hammad is a motivated and result-oriented BBA final-semester student with approximately <strong>4 years</strong> of professional experience in marketing and merchandising and <strong>2 years</strong> of experience in the medical store industry.
                    </p>
                    <p class="about-text">
                        His expertise spans across marketing strategy, merchandising execution, sales operations, customer relationship management, and business growth initiatives. With a strong foundation in business administration and hands-on experience at <strong>Colgate-Palmolive</strong>, he brings a unique blend of academic knowledge and practical market understanding.
                    </p>
                    <div class="about-interests">
                        <span class="interest-tag">Marketing</span>
                        <span class="interest-tag">Merchandising</span>
                        <span class="interest-tag">Business Administration</span>
                        <span class="interest-tag">Sales</span>
                        <span class="interest-tag">Customer Service</span>
                        <span class="interest-tag">Finance</span>
                        <span class="interest-tag">Business Growth</span>
                        <span class="interest-tag">Data Analysis</span>
                        <span class="interest-tag">Market Research</span>
                    </div>
                </div>
                <div class="stats-grid">
                    <div class="stat-card reveal-up" data-delay="0">
                        <div class="stat-icon"><i class="fas fa-briefcase"></i></div>
                        <div class="stat-number" data-target="4">4</div>
                        <div class="stat-suffix">+ Years</div>
                        <div class="stat-label">Marketing & Merchandising</div>
                    </div>
                    <div class="stat-card reveal-up" data-delay="100">
                        <div class="stat-icon"><i class="fas fa-clinic-medical"></i></div>
                        <div class="stat-number" data-target="2">2</div>
                        <div class="stat-suffix">+ Years</div>
                        <div class="stat-label">Medical Store Experience</div>
                    </div>
                    <div class="stat-card reveal-up" data-delay="200">
                        <div class="stat-icon"><i class="fas fa-university"></i></div>
                        <div class="stat-text">BBA</div>
                        <div class="stat-label">Final Semester</div>
                    </div>
                    <div class="stat-card reveal-up" data-delay="300">
                        <div class="stat-icon"><i class="fas fa-rocket"></i></div>
                        <div class="stat-text">Business Focus</div>
                        <div class="stat-label">Marketing & Growth</div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <section class="section experience" id="experience">
        <div class="section-container">
            <div class="section-header reveal-up">
                <span class="section-label">My Journey</span>
                <h2 class="section-title">Professional Experience</h2>
                <div class="section-line"></div>
            </div>
            <div class="timeline">
                <div class="timeline-line"></div>
                <div class="timeline-item reveal-up">
                    <div class="timeline-dot"></div>
                    <div class="timeline-card">
                        <div class="timeline-header">
                            <div class="company-logo"><i class="fas fa-building"></i></div>
                            <div class="timeline-meta">
                                <h3 class="company-name">Colgate-Palmolive</h3>
                                <span class="timeline-role">Marketing & Merchandising</span>
                                <span class="timeline-duration"><i class="fas fa-calendar-alt"></i> 4 Years</span>
                            </div>
                        </div>
                        <ul class="timeline-responsibilities">
                            <li><i class="fas fa-check-circle"></i> Managed product displays and merchandising strategies to support sales growth.</li>
                            <li><i class="fas fa-check-circle"></i> Coordinated promotional campaigns to improve brand visibility.</li>
                            <li><i class="fas fa-check-circle"></i> Analyzed sales data and market trends to support marketing decisions.</li>
                            <li><i class="fas fa-check-circle"></i> Built strong relationships with retailers and distributors.</li>
                        </ul>
                        <div class="timeline-tags">
                            <span class="tag">Marketing</span>
                            <span class="tag">Merchandising</span>
                            <span class="tag">Sales Analysis</span>
                            <span class="tag">Retail</span>
                        </div>
                    </div>
                </div>
                <div class="timeline-item reveal-up">
                    <div class="timeline-dot"></div>
                    <div class="timeline-card">
                        <div class="timeline-header">
                            <div class="company-logo medical"><i class="fas fa-clinic-medical"></i></div>
                            <div class="timeline-meta">
                                <h3 class="company-name">Medical Store</h3>
                                <span class="timeline-role">Sales & Customer Service</span>
                                <span class="timeline-duration"><i class="fas fa-calendar-alt"></i> 2 Years</span>
                            </div>
                        </div>
                        <ul class="timeline-responsibilities">
                            <li><i class="fas fa-check-circle"></i> Managed day-to-day store operations and customer service.</li>
                            <li><i class="fas fa-check-circle"></i> Handled inventory, stock management, and product ordering.</li>
                            <li><i class="fas fa-check-circle"></i> Assisted customers with information regarding medicines and healthcare products.</li>
                            <li><i class="fas fa-check-circle"></i> Maintained accurate sales and purchase records.</li>
                        </ul>
                        <div class="timeline-tags">
                            <span class="tag">Sales</span>
                            <span class="tag">Customer Service</span>
                            <span class="tag">Inventory</span>
                            <span class="tag">Operations</span>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <section class="section expertise" id="expertise">
        <div class="section-container">
            <div class="section-header reveal-up">
                <span class="section-label">What I Bring</span>
                <h2 class="section-title">Business Expertise</h2>
                <div class="section-line"></div>
            </div>
            <div class="expertise-grid">
                <div class="expertise-card reveal-up">
                    <div class="expertise-glow"></div>
                    <div class="expertise-icon"><i class="fas fa-bullhorn"></i></div>
                    <h3>Marketing Strategy</h3>
                    <p>Marketing planning, brand visibility and promotional strategy.</p>
                </div>
                <div class="expertise-card reveal-up" data-delay="100">
                    <div class="expertise-glow"></div>
                    <div class="expertise-icon"><i class="fas fa-store"></i></div>
                    <h3>Merchandising</h3>
                    <p>Product presentation, retail visibility and merchandising strategy.</p>
                </div>
                <div class="expertise-card reveal-up" data-delay="200">
                    <div class="expertise-glow"></div>
                    <div class="expertise-icon"><i class="fas fa-handshake"></i></div>
                    <h3>Sales & Customer Relations</h3>
                    <p>Customer communication, relationship building and sales support.</p>
                </div>
                <div class="expertise-card reveal-up" data-delay="300">
                    <div class="expertise-glow"></div>
                    <div class="expertise-icon"><i class="fas fa-search-dollar"></i></div>
                    <h3>Market Research</h3>
                    <p>Understanding market trends, customer behavior and sales data.</p>
                </div>
                <div class="expertise-card reveal-up" data-delay="0">
                    <div class="expertise-glow"></div>
                    <div class="expertise-icon"><i class="fas fa-chart-pie"></i></div>
                    <h3>Finance</h3>
                    <p>Interest in financial understanding and business growth.</p>
                </div>
                <div class="expertise-card reveal-up" data-delay="100">
                    <div class="expertise-glow"></div>
                    <div class="expertise-icon"><i class="fas fa-users-cog"></i></div>
                    <h3>Human Resources</h3>
                    <p>Communication, teamwork, coordination and organizational understanding.</p>
                </div>
                <div class="expertise-card reveal-up" data-delay="200">
                    <div class="expertise-glow"></div>
                    <div class="expertise-icon"><i class="fas fa-cogs"></i></div>
                    <h3>Business Administration</h3>
                    <p>Business operations, management and organizational practices.</p>
                </div>
                <div class="expertise-card reveal-up" data-delay="300">
                    <div class="expertise-glow"></div>
                    <div class="expertise-icon"><i class="fas fa-boxes"></i></div>
                    <h3>Inventory Management</h3>
                    <p>Stock management, product ordering and operational coordination.</p>
                </div>
            </div>
        </div>
    </section>

    <section class="section education" id="education">
        <div class="section-container">
            <div class="section-header reveal-up">
                <span class="section-label">Academic Background</span>
                <h2 class="section-title">Education</h2>
                <div class="section-line"></div>
            </div>
            <div class="edu-timeline">
                <div class="edu-line"></div>
                <div class="edu-item reveal-up">
                    <div class="edu-dot"></div>
                    <div class="edu-card">
                        <div class="edu-badge current">In Progress</div>
                        <div class="edu-icon"><i class="fas fa-university"></i></div>
                        <h3 class="edu-degree">BBA — Bachelor of Business Administration</h3>
                        <p class="edu-school">Shahid Benazir Bhutto University</p>
                        <p class="edu-dept">BBA Department</p>
                        <span class="edu-status">Final Semester</span>
                    </div>
                </div>
                <div class="edu-item reveal-up">
                    <div class="edu-dot"></div>
                    <div class="edu-card">
                        <div class="edu-icon"><i class="fas fa-laptop-code"></i></div>
                        <h3 class="edu-degree">Software Technology Diploma</h3>
                        <p class="edu-school">Government Habib Technical College, Nawabshah</p>
                        <span class="edu-duration">3 Years</span>
                    </div>
                </div>
                <div class="edu-item reveal-up">
                    <div class="edu-dot"></div>
                    <div class="edu-card">
                        <div class="edu-icon"><i class="fas fa-certificate"></i></div>
                        <h3 class="edu-degree">D.I.T. — Diploma in Information Technology</h3>
                        <p class="edu-school">6-Month Computer Course</p>
                        <span class="edu-duration">CNIC-Certified</span>
                    </div>
                </div>
                <div class="edu-item reveal-up">
                    <div class="edu-dot"></div>
                    <div class="edu-card">
                        <div class="edu-icon"><i class="fas fa-school"></i></div>
                        <h3 class="edu-degree">Intermediate</h3>
                        <p class="edu-school">Jam Sahib College, Nawabshah</p>
                        <span class="edu-year">2022</span>
                    </div>
                </div>
                <div class="edu-item reveal-up">
                    <div class="edu-dot"></div>
                    <div class="edu-card">
                        <div class="edu-icon"><i class="fas fa-book"></i></div>
                        <h3 class="edu-degree">Matriculation</h3>
                        <p class="edu-school">Noor Eastern College, Nawabshah</p>
                        <span class="edu-year">2020</span>
                    </div>
                </div>
            </div>
            <div class="languages-section reveal-up">
                <h3 class="languages-title">Languages</h3>
                <div class="languages-grid">
                    <div class="language-card">
                        <div class="lang-flag">EN</div>
                        <div class="lang-info"><h4>English</h4><span>Fluent</span></div>
                        <div class="lang-indicator"><div class="lang-dot active"></div><div class="lang-dot active"></div><div class="lang-dot active"></div><div class="lang-dot active"></div></div>
                    </div>
                    <div class="language-card">
                        <div class="lang-flag">UR</div>
                        <div class="lang-info"><h4>Urdu</h4><span>Fluent</span></div>
                        <div class="lang-indicator"><div class="lang-dot active"></div><div class="lang-dot active"></div><div class="lang-dot active"></div><div class="lang-dot active"></div></div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <section class="section objective" id="objective">
        <div class="section-container">
            <div class="objective-card reveal-up">
                <div class="objective-quote-icon"><i class="fas fa-quote-left"></i></div>
                <h2 class="objective-title">Career Objective</h2>
                <blockquote class="objective-text">
                    Motivated and result-oriented BBA student with professional experience in marketing, merchandising, sales, customer service, and business operations, seeking opportunities to contribute to organizational growth through effective communication, business understanding, strategic thinking, and professional execution.
                </blockquote>
                <div class="objective-signature">
                    <span class="sig-line"></span>
                    <span class="sig-name">Muhammad Hammad</span>
                </div>
            </div>
        </div>
    </section>

    <section class="section skills" id="skills">
        <div class="section-container">
            <div class="section-header reveal-up">
                <span class="section-label">My Toolkit</span>
                <h2 class="section-title">Skills & Competencies</h2>
                <div class="section-line"></div>
            </div>
            <div class="skills-grid">
                <div class="skill-category reveal-up">
                    <div class="skill-cat-header">
                        <div class="skill-cat-icon"><i class="fas fa-bullhorn"></i></div>
                        <h3>Marketing & Business</h3>
                    </div>
                    <div class="skill-tags">
                        <span class="skill-tag">Marketing Strategy</span>
                        <span class="skill-tag">Merchandising</span>
                        <span class="skill-tag">Market Research</span>
                        <span class="skill-tag">Sales Support</span>
                        <span class="skill-tag">Business Growth</span>
                        <span class="skill-tag">Customer Relationship Management</span>
                    </div>
                </div>
                <div class="skill-category reveal-up" data-delay="100">
                    <div class="skill-cat-header">
                        <div class="skill-cat-icon"><i class="fas fa-tasks"></i></div>
                        <h3>Management & Operations</h3>
                    </div>
                    <div class="skill-tags">
                        <span class="skill-tag">Inventory Management</span>
                        <span class="skill-tag">Stock Management</span>
                        <span class="skill-tag">Product Ordering</span>
                        <span class="skill-tag">Record Keeping</span>
                        <span class="skill-tag">Team Coordination</span>
                        <span class="skill-tag">Communication</span>
                    </div>
                </div>
                <div class="skill-category reveal-up" data-delay="200">
                    <div class="skill-cat-header">
                        <div class="skill-cat-icon"><i class="fas fa-laptop"></i></div>
                        <h3>Technical / Computer Skills</h3>
                    </div>
                    <div class="skill-tags">
                        <span class="skill-tag">MS Word</span>
                        <span class="skill-tag">MS Excel</span>
                        <span class="skill-tag">MS PowerPoint</span>
                        <span class="skill-tag">Internet Research</span>
                        <span class="skill-tag">Basic IT Skills</span>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <section class="section contact" id="contact">
        <div class="section-container">
            <div class="section-header reveal-up">
                <span class="section-label">Get In Touch</span>
                <h2 class="section-title">Let's Connect</h2>
                <div class="section-line"></div>
            </div>
            <p class="contact-intro reveal-up">
                Interested in working together, discussing an opportunity, or connecting professionally? Get in touch.
            </p>
            <div class="contact-grid">
                <a href="tel:03033517039" class="contact-card reveal-up">
                    <div class="contact-icon"><i class="fas fa-phone-alt"></i></div>
                    <h3>Phone</h3>
                    <p>03033517039</p>
                    <span class="contact-action">Call Now <i class="fas fa-arrow-right"></i></span>
                </a>
                <a href="mailto:hammadjattgill@gmail.com" class="contact-card reveal-up" data-delay="100">
                    <div class="contact-icon"><i class="fas fa-envelope"></i></div>
                    <h3>Email</h3>
                    <p>hammadjattgill@gmail.com</p>
                    <span class="contact-action">Send Email <i class="fas fa-arrow-right"></i></span>
                </a>
                <a href="https://www.linkedin.com/in/muhammad-hammad-28856636b/" target="_blank" rel="noopener noreferrer" class="contact-card reveal-up" data-delay="200">
                    <div class="contact-icon linkedin"><i class="fab fa-linkedin-in"></i></div>
                    <h3>LinkedIn</h3>
                    <p>Connect on LinkedIn</p>
                    <span class="contact-action">View Profile <i class="fas fa-arrow-right"></i></span>
                </a>
                <div class="contact-card reveal-up" data-delay="300">
                    <div class="contact-icon location"><i class="fas fa-map-marker-alt"></i></div>
                    <h3>Location</h3>
                    <p>Nawabshah, Pakistan</p>
                    <span class="contact-action">Available for Remote</span>
                </div>
            </div>
            <div class="contact-cta reveal-up">
                <a href="https://wa.me/923033517039?text=Hello%20Muhammad%20Hammad%2C%20I%20visited%20your%20portfolio%20and%20would%20like%20to%20connect%20with%20you." target="_blank" rel="noopener noreferrer" class="btn btn-whatsapp">
                    <i class="fab fa-whatsapp"></i><span>Chat on WhatsApp</span>
                </a>
                <a href="https://www.linkedin.com/in/muhammad-hammad-28856636b/" target="_blank" rel="noopener noreferrer" class="btn btn-linkedin">
                    <i class="fab fa-linkedin"></i><span>Connect on LinkedIn</span>
                </a>
                <a href="mailto:hammadjattgill@gmail.com" class="btn btn-email">
                    <i class="fas fa-envelope"></i><span>Email Me</span>
                </a>
            </div>
        </div>
    </section>

    <footer class="footer">
        <div class="footer-line"></div>
        <div class="footer-container">
            <div class="footer-brand">
                <span class="footer-logo">MH.</span>
                <p class="footer-tagline">Marketing Professional | Merchandising Expert | BBA</p>
            </div>
            <div class="footer-social">
                <a href="https://wa.me/923033517039" target="_blank" rel="noopener noreferrer" aria-label="WhatsApp" class="social-link"><i class="fab fa-whatsapp"></i></a>
                <a href="https://www.linkedin.com/in/muhammad-hammad-28856636b/" target="_blank" rel="noopener noreferrer" aria-label="LinkedIn" class="social-link"><i class="fab fa-linkedin-in"></i></a>
                <a href="mailto:hammadjattgill@gmail.com" aria-label="Email" class="social-link"><i class="fas fa-envelope"></i></a>
            </div>
            <div class="footer-bottom">
                <p>&copy; 2026 Muhammad Hammad. All Rights Reserved.</p>
            </div>
        </div>
    </footer>

    <a href="https://wa.me/923033517039?text=Hello%20Muhammad%20Hammad%2C%20I%20visited%20your%20portfolio%20and%20would%20like%20to%20connect%20with%20you." target="_blank" rel="noopener noreferrer" class="whatsapp-float" aria-label="Chat with Muhammad Hammad on WhatsApp">
        <div class="whatsapp-pulse"></div>
        <i class="fab fa-whatsapp"></i>
        <span class="whatsapp-tooltip">Chat with Muhammad Hammad</span>
    </a>

    <script>
        {{ js }}
    </script>
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(HTML_TEMPLATE, css=CSS, js=JS)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)