#!/usr/bin/env python3
"""Builds the six full-site pages in /full from one shared shell.
Run from the repo root:  python3 tools/build_full.py
Edit page bodies in PAGES below, then re-run."""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

TW = "https://www.twitch.tv/jaybroski"
YT = "https://www.youtube.com/channel/UCIKHN06ka6138612WOF50bg"
TT = "https://www.tiktok.com/@thejaybroski"
IG = "https://www.instagram.com/thejaybroskitv/"
XX = "https://twitter.com/TheJayBroski"
DC = "https://discord.com/invite/Ztpg7hxD7X"
MERCH = "https://streamlabs.com/thejaybroski/merch"
DEMON = "https://demon-workshop.com/?ref=jaybroski"
MONSTER = "https://www.monsterenergy.com/en-us/gaming/jaybroski/"
EMAIL = "jaybroski@bavamedia.com"

NAV = [("", "Home"), ("live/", "Live"), ("videos/", "Videos"), ("partners/", "Partners"), ("shop/", "Merch"), ("about/", "About")]

SOCIALS = f"""<nav class="socials" aria-label="Socials">
        <a href="{TW}" aria-label="Twitch"><span class="ico i-twitch"></span></a>
        <a href="{YT}" aria-label="YouTube"><span class="ico i-youtube"></span></a>
        <a href="{TT}" aria-label="TikTok"><span class="ico i-tiktok"></span></a>
        <a href="{IG}" aria-label="Instagram"><span class="ico i-instagram"></span></a>
        <a href="{XX}" aria-label="X"><span class="ico i-x"></span></a>
        <a href="{DC}" aria-label="Discord"><span class="ico i-discord"></span></a>
      </nav>"""

TICKER = """<div class="ticker" aria-hidden="true"><div class="track">
    <span>Warzone forever</span><span>GTA VI day by day</span><span>Monster Energy creator</span><span>Officer Broski on patrol</span><span>Twitch Partner</span>
    <span>Warzone forever</span><span>GTA VI day by day</span><span>Monster Energy creator</span><span>Officer Broski on patrol</span><span>Twitch Partner</span>
  </div></div>"""

CTA = f"""<section class="cta-band grit">
    <div class="wrap">
      <p class="eyebrow">Brands & business</p>
      <h2>Let's get <span class="hype-text">loud</span></h2>
      <p>Sponsored streams, YouTube integrations, launches and events with a hyped-up Call of Duty audience.</p>
      <div class="ctas"><a class="btn btn-volt" href="{{base}}partners/#inquiry">Start a campaign</a><a class="btn" href="mailto:{EMAIL}">{EMAIL}</a></div>
    </div>
  </section>"""


def vid(title, big, tag, sub="Sample title", cls=""):
    return f"""<a class="vid" href="{YT}"><div class="thumb {cls}"><span class="big">{big}</span><span class="tag">{tag}</span><span class="play"></span></div><strong>{title}</strong><small>{sub}</small></a>"""


def item(name, art, price, cls=""):
    return f"""<a class="item {cls}" href="{MERCH}"><span class="art">{art}</span><div><strong>{name}</strong><small>{price}</small></div></a>"""


SCHED = """<div class="sched">
          <div><b>Mon</b><span>About 2:30 to 8:30 PM</span></div>
          <div><b>Tue</b><span>About 2:30 to 8:30 PM</span></div>
          <div><b>Wed</b><span>About 2:30 to 9 PM</span></div>
          <div><b>Thu</b><span>About 2:30 to 8 PM</span></div>
          <div><b>Fri</b><span>About 6 to 10:30 PM</span></div>
          <div class="off"><b>Sat & Sun</b><span>Off</span></div>
        </div>"""

PARTNERS = f"""<div class="grid-3">
          <div class="partner"><span class="kind">Energy partner</span><span class="logo">Monster Energy</span><p>Part of the Monster Energy gaming roster, with Monster-backed Call of Duty streams.</p><a class="code" href="{MONSTER}">View on Monster</a></div>
          <div class="partner"><span class="kind">Gear</span><span class="logo">Demon Workshop</span><p>The custom controller Jay plays on. Grab one through his link.</p><a class="code" href="{DEMON}">ref: jaybroski</a></div>
          <div class="partner open"><span class="kind">Open slot</span><span class="logo">Your brand here</span><p>Sponsored streams, YouTube integrations and event takeovers.</p><a class="code" href="{{base}}partners/#inquiry">Start a campaign</a></div>
        </div>"""

PAGES = {
"": ("Jaybroski | Call of Duty, GTA VI and Officer Broski", f"""
  <section class="page-hero grit">
    <div class="wrap grid-2">
      <div>
        <span class="live">Live now · GTA VI</span>
        <h1>Jay<br><span class="out">broski</span></h1>
        <p class="lead">Call of Duty chaos, proximity chat crimes and a full GTA VI playthrough. Twitch Partner since 2014. Loud on purpose.</p>
        <div class="ctas">
          <a class="btn btn-twitch" href="{TW}"><span class="ico i-twitch"></span>Watch live</a>
          <a class="btn" href="{YT}"><span class="ico i-youtube"></span>Subscribe</a>
        </div>
      </div>
      <div style="transform:rotate(2deg)"><div class="thumb c" style="box-shadow:0 0 0 3px var(--volt),18px 18px 0 var(--blaze)"><span class="big" style="font-size:clamp(30px,4vw,46px)">GTA VI<br>Day 3!!!</span><span class="tag">Stream preview</span><span class="play"></span></div></div>
    </div>
  </section>
  {TICKER}
  <section class="block">
    <div class="wrap grid-4">
      <div class="stat"><strong>89K+</strong><span>Twitch followers</span></div>
      <div class="stat"><strong>4,900</strong><span>Peak live viewers</span></div>
      <div class="stat"><strong>Top 30</strong><span>English Warzone channels</span></div>
      <div class="stat"><strong>12 yrs</strong><span>On Twitch</span></div>
    </div>
  </section>
  <section class="block" style="padding-top:0">
    <div class="wrap">
      <div class="sec-head"><div><p class="eyebrow">Latest uploads</p><h2>The <span class="hype-text">clips</span></h2></div><a class="btn" href="{{base}}videos/">All videos</a></div>
      <div class="grid-3">
        {vid("Jaybroski takes over Rebirth Island", "Rebirth<br>takeover", "Warzone", "Sample title · 4,900 watching live")}
        {vid("Officer Broski pulls over the whole lobby", "Officer<br>Broski", "Proximity chat", cls="c")}
        {vid("GTA VI day 3: chat picked my crimes", "GTA VI<br>day 3", "Full gameplay", cls="b")}
      </div>
    </div>
  </section>
  <section class="block" style="padding-top:0">
    <div class="wrap grid-2" style="align-items:stretch">
      <div class="panel twitch-panel"><span class="live">Now playing</span><h3>GTA VI playthrough</h3><p>Every mission, every police chase, every bad decision chat talks him into.</p><a class="btn btn-volt" style="margin-top:18px" href="{{base}}live/">See the schedule</a></div>
      <div class="panel"><p class="eyebrow">Partners</p><h3>Monster Energy · Demon Workshop</h3><p>The brands Jay already runs with, plus room for yours.</p><a class="btn" style="margin-top:18px" href="{{base}}partners/">Partner with Jay</a></div>
    </div>
  </section>
  {CTA}
"""),

"live/": ("Live | Jaybroski", f"""
  <section class="page-hero grit">
    <div class="wrap">
      <p class="eyebrow">On stream</p>
      <h1>Pull up <span class="out">live</span></h1>
      <p class="lead">Weekday streams on Twitch. Warzone, Modern Warfare 4 and right now, a full GTA VI playthrough.</p>
      <div class="ctas"><a class="btn btn-twitch" href="{TW}"><span class="ico i-twitch"></span>twitch.tv/jaybroski</a></div>
    </div>
  </section>
  <section class="block">
    <div class="wrap grid-2" style="align-items:start">
      <div class="panel twitch-panel">
        <span class="live">Live</span>
        <div class="thumb c" style="margin-top:16px"><span class="big">Twitch player<br>goes here</span><span class="play"></span></div>
        <h3>GTA VI playthrough day 3</h3>
        <p>The live Twitch player and chat sit right here when Jay is on. When he's offline, this shows the latest VOD.</p>
      </div>
      <div>
        <p class="eyebrow">Weekly schedule</p>
        <h2 style="font-size:56px;margin:10px 0 18px">When Jay's on</h2>
        {SCHED}
        <p class="muted" style="margin-top:12px;font-size:14px">Sample times based on recent streams. Jay sets the real ones.</p>
      </div>
    </div>
  </section>
  <section class="block" style="padding-top:0">
    <div class="wrap">
      <div class="sec-head"><div><p class="eyebrow">What's on rotation</p><h2>The games</h2></div></div>
      <div class="grid-4">
        <div class="panel"><p class="eyebrow">Now</p><h3>GTA VI</h3><p>Full playthrough, one day at a time.</p></div>
        <div class="panel"><p class="eyebrow">Main</p><h3>Warzone</h3><p>Where Officer Broski was born.</p></div>
        <div class="panel"><p class="eyebrow">Also</p><h3>MW4</h3><p>Monster-backed multiplayer streams.</p></div>
        <div class="panel"><p class="eyebrow">Wildcard</p><h3>Chat's pick</h3><p>Party games and whatever chat votes for.</p></div>
      </div>
    </div>
  </section>
  {TICKER}
  {CTA}
"""),

"videos/": ("Videos | Jaybroski", f"""
  <section class="page-hero grit">
    <div class="wrap">
      <p class="eyebrow">YouTube</p>
      <h1>The <span class="out">clips</span></h1>
      <p class="lead">Full gameplays, Officer Broski moments and the best of the stream. New uploads land here automatically.</p>
      <div class="ctas"><a class="btn btn-volt" href="{YT}"><span class="ico i-youtube"></span>Subscribe on YouTube</a><a class="btn" href="{TT}"><span class="ico i-tiktok"></span>TikTok clips</a></div>
    </div>
  </section>
  <section class="block">
    <div class="wrap">
      <div class="sec-head"><div><p class="eyebrow">Latest</p><h2>Fresh drops</h2></div></div>
      <div class="grid-3">
        {vid("Jaybroski takes over Rebirth Island", "Rebirth<br>takeover", "Warzone", "Sample title · 4,900 watching live")}
        {vid("GTA VI day 3: chat picked my crimes", "GTA VI<br>day 3", "Full gameplay", cls="b")}
        {vid("GTA VI day 2: Vice City speedrun (bad)", "GTA VI<br>day 2", "Full gameplay", cls="b")}
      </div>
    </div>
  </section>
  <section class="block" style="padding-top:0">
    <div class="wrap">
      <div class="sec-head"><div><p class="eyebrow">Fan favorites</p><h2>Officer <span class="hype-text">Broski</span></h2></div></div>
      <div class="grid-3">
        {vid("Officer Broski pulls over the whole lobby", "License &amp;<br>registration", "Proximity chat", cls="c")}
        {vid("Riot shield only, no mercy", "Shield<br>only", "Warzone", cls="c")}
        {vid("Bad Boys plays, lobby panics", "Bad boys<br>bad boys", "Proximity chat", cls="c")}
      </div>
    </div>
  </section>
  <section class="block" style="padding-top:0">
    <div class="wrap">
      <div class="sec-head"><div><p class="eyebrow">Shorts</p><h2>Quick hits</h2></div></div>
      <div class="grid-4">
        {vid("lmaooooo", "lmaooo", "Top clip", "8.4K views")}
        {vid("He did NOT see me", "Not<br>today", "Short", cls="b")}
        {vid("Chat made me do it", "Chat<br>did it", "Short")}
        {vid("Rebirth 1v4", "1v4", "Short", cls="b")}
      </div>
    </div>
  </section>
  {CTA}
"""),

"partners/": ("Partners | Jaybroski", f"""
  <section class="page-hero grit">
    <div class="wrap">
      <p class="eyebrow">Brands & business</p>
      <h1>Partner <span class="out">up</span></h1>
      <p class="lead">Jay brings a live, loud Call of Duty audience that shows up every weekday. Here's who he already runs with, and how to join them.</p>
      <div class="ctas"><a class="btn btn-volt" href="#inquiry">Start a campaign</a><a class="btn" href="mailto:{EMAIL}">{EMAIL}</a></div>
    </div>
  </section>
  <section class="block">
    <div class="wrap">
      <div class="sec-head"><div><p class="eyebrow">Current partners</p><h2>The roster</h2></div></div>
      {PARTNERS}
    </div>
  </section>
  <section class="block" style="padding-top:0">
    <div class="wrap">
      <div class="sec-head"><div><p class="eyebrow">Media kit</p><h2>By the numbers</h2></div></div>
      <div class="grid-4">
        <div class="stat"><strong>89K+</strong><span>Twitch followers</span></div>
        <div class="stat"><strong>4,900</strong><span>Peak live viewers</span></div>
        <div class="stat"><strong>100+</strong><span>Hours live per month</span></div>
        <div class="stat"><strong>Top 30</strong><span>English Warzone channels</span></div>
      </div>
      <p class="muted" style="margin-top:14px;font-size:14px">Public Twitch stats, November 2026. A downloadable media kit PDF can sit here.</p>
    </div>
  </section>
  <section class="block" id="inquiry" style="padding-top:0">
    <div class="wrap grid-2" style="align-items:start">
      <div>
        <p class="eyebrow">What we can do</p>
        <h2 style="font-size:clamp(42px,7vw,84px);margin:10px 0 18px">Ways to work together</h2>
        <div class="tl">
          <div><b>Sponsored streams</b><span>Your game or product, live with chat.</span></div>
          <div><b>YouTube integrations</b><span>Ad reads and dedicated videos.</span></div>
          <div><b>Launch takeovers</b><span>Day-one streams like the Rebirth Island takeover.</span></div>
          <div><b>Events</b><span>Appearances, tournaments and creator nights.</span></div>
        </div>
      </div>
      <div class="panel" style="border-color:var(--volt)">
        <p class="eyebrow">Inquiry</p>
        <h3>Work with Jay</h3>
        <form class="form" data-mock>
          <div class="row"><label>Name<input required name="name" autocomplete="name"></label><label>Brand / company<input required name="company"></label></div>
          <label>Email<input required type="email" name="email" autocomplete="email"></label>
          <label>What are you planning?<select name="type"><option>Sponsored stream</option><option>YouTube integration</option><option>Game or product launch</option><option>Event appearance</option><option>Something else</option></select></label>
          <label>Budget range<select name="budget"><option>Let's talk</option><option>Under $1K</option><option>$1K to $5K</option><option>$5K+</option></select></label>
          <label>Details<textarea name="details" rows="3" placeholder="Dates, goals, deliverables"></textarea></label>
          <button class="btn btn-volt" type="submit">Send it</button>
        </form>
        <div class="sent" hidden><strong>Inquiry locked in</strong>Jay's team will get back to you soon.</div>
      </div>
    </div>
  </section>
"""),

"shop/": ("Merch | Jaybroski", f"""
  <section class="page-hero grit">
    <div class="wrap">
      <p class="eyebrow">Official drip</p>
      <h1>Merch <span class="out">drop</span></h1>
      <p class="lead">Rep the squad. Everything ships from Jay's official store.</p>
      <div class="ctas"><a class="btn btn-volt" href="{MERCH}">Shop the full store</a></div>
    </div>
  </section>
  {TICKER}
  <section class="block">
    <div class="wrap">
      <div class="sec-head"><div><p class="eyebrow">Featured</p><h2>The collection</h2></div></div>
      <div class="grid-4">
        {item("Broski tee", "JB", "$30")}
        {item("Squad hat", "🧢", "$28", "o")}
        {item("Hoodie", "BRO", "$55", "w")}
        {item("Officer Broski mug", "🚨", "$18", "s")}
        {item("Rebirth tee", "RB", "$30", "o")}
        {item("Sticker pack", "✦", "$8", "w")}
        {item("Mousepad", "XL", "$25")}
        {item("Beanie", "JB", "$24", "s")}
      </div>
      <p class="muted" style="margin-top:14px;font-size:14px">Sample items and prices. The real products come from Jay's Streamlabs store.</p>
    </div>
  </section>
  <section class="block" style="padding-top:0">
    <div class="wrap">
      <div class="panel grid-2" style="border-color:var(--blaze)">
        <div><p class="eyebrow">Gear Jay uses</p><h3>Demon Workshop custom controller</h3><p>The controller Jay plays on every stream. Pick one up through his link.</p></div>
        <div style="text-align:right"><a class="btn btn-volt" href="{DEMON}">Get the controller</a></div>
      </div>
    </div>
  </section>
"""),

"about/": ("About | Jaybroski", f"""
  <section class="page-hero grit">
    <div class="wrap">
      <p class="eyebrow">About</p>
      <h1>Meet <span class="out">Jay</span></h1>
      <p class="lead">"I'm funny sometimes." Twelve years on Twitch, a Warzone cop persona the internet can't get enough of, and zero volume control.</p>
    </div>
  </section>
  <div class="siren-bar"></div>
  <section class="block">
    <div class="wrap grid-2">
      <div>
        <p class="eyebrow">The story</p>
        <h2 style="font-size:clamp(42px,7vw,84px);margin:10px 0 18px">From day one to Partner</h2>
        <p style="font-size:18px">Jay started streaming on Twitch in 2014 and found his lane in Call of Duty: Warzone, where comedy, chaos and proximity chat turned random lobbies into content. That run made him a Twitch Partner and one of the most-watched English Warzone channels.</p>
        <p style="font-size:18px;margin-top:14px">Now he's bringing the same energy to GTA VI, one chaotic day at a time.</p>
        <p class="muted" style="margin-top:14px;font-size:14px">Sample bio. Jay's own story goes here.</p>
      </div>
      <div class="panel" style="aspect-ratio:4/3;display:grid;place-items:center;background-image:radial-gradient(circle at 30% 30%,rgba(255,43,74,.4),transparent 45%),radial-gradient(circle at 70% 30%,rgba(47,123,255,.4),transparent 45%)">
        <b style="font:400 clamp(60px,10vw,120px)/1 var(--display);text-transform:uppercase;transform:rotate(-6deg);text-shadow:6px 6px 0 var(--ink)">Freeze!</b>
      </div>
    </div>
  </section>
  <section class="block" style="padding-top:0">
    <div class="wrap grid-2" style="align-items:start">
      <div>
        <p class="eyebrow">Fan favorite</p>
        <h2 style="font-size:clamp(42px,7vw,84px);margin:10px 0 18px">Officer Broski</h2>
        <p style="font-size:18px">Riot shield up, proximity chat on, "Bad Boys" on the speakers. Jay's Warzone cop persona pulls over whole lobbies, and the clips travel way past Twitch.</p>
      </div>
      <div>
        <p class="eyebrow">Timeline</p>
        <div class="tl" style="margin-top:18px">
          <div><b>2014</b><span>First stream on Twitch.</span></div>
          <div><b>Warzone era</b><span>Officer Broski is born. Twitch Partner.</span></div>
          <div><b>Monster Energy</b><span>Joins the Monster gaming roster.</span></div>
          <div><b>2026</b><span>Rebirth Island takeover peaks at 4,900 live. GTA VI playthrough begins.</span></div>
        </div>
      </div>
    </div>
  </section>
  <section class="block" style="padding-top:0">
    <div class="wrap">
      <div class="sec-head"><div><p class="eyebrow">Find Jay</p><h2>Everywhere</h2></div></div>
      {SOCIALS}
    </div>
  </section>
  {CTA}
"""),
}

SHELL = """<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title}</title>
  <meta name="description" content="Jaybroski: Twitch Partner, Warzone comedian and Monster Energy creator.">
  <meta name="robots" content="noindex">
  <link rel="stylesheet" href="{assets}assets/css/base.css">
  <link rel="stylesheet" href="{assets}assets/css/full.css">
</head>
<body>
  <div class="concept-bar">Full website concept for Jaybroski, made by <a href="https://distortedbrands.com/web/">Distorted Web</a> · <a href="{assets}">see all three</a></div>
  <header class="nav">
    <div class="wrap">
      <span class="badge" aria-hidden="true">JB</span>
      <a class="name" href="{base}">Jaybroski</a>
      <button class="menu" aria-expanded="false" aria-controls="menu">Menu</button>
      <ul id="menu">
{links}
      </ul>
    </div>
  </header>
  <main>
{body}
  </main>
  <footer class="foot">
    <div class="wrap">
      <div>
        <div class="brand"><span class="badge" style="--s:42px" aria-hidden="true">JB</span>Jaybroski</div>
        <p>Call of Duty chaos and GTA VI. Stay locked in.</p>
        {socials}
      </div>
      <div><h4>Site</h4><ul>{footlinks}</ul></div>
      <div><h4>Business</h4><ul><li><a href="mailto:{email}">{email}</a></li><li><a href="{base}partners/#inquiry">Partner inquiry</a></li><li><a href="{merch}">Merch store</a></li></ul></div>
    </div>
  </footer>
  <footer class="credit">Designed by <a href="https://distortedbrands.com/web/">Distorted Web</a> · Websites that cut through.</footer>
  <script src="{assets}assets/js/modal.js"></script>
  <script>
    (function () {{
      var nav = document.querySelector(".nav"), btn = nav.querySelector(".menu");
      btn.addEventListener("click", function () {{
        var open = nav.classList.toggle("open");
        btn.setAttribute("aria-expanded", open);
      }});
    }})();
  </script>
</body>
</html>
"""

for slug, (title, body) in PAGES.items():
    depth = slug.count("/")
    base = "../" * depth            # back to /full/
    assets = "../" * (depth + 1)    # back to repo root
    links = "\n".join(
        f'        <li><a href="{base}{s}"{" aria-current=\"page\"" if s == slug else ""}>{n}</a></li>' for s, n in NAV)
    footlinks = "".join(f'<li><a href="{base}{s}">{n}</a></li>' for s, n in NAV)
    html = SHELL.format(title=title, assets=assets, base=base, links=links, body=body.replace("{base}", base),
                        socials=SOCIALS, footlinks=footlinks, email=EMAIL, merch=MERCH)
    out = ROOT / "full" / slug / "index.html"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(html)
    print("wrote", out.relative_to(ROOT))
