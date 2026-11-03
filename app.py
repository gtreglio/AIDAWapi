# app.py
# SAI | STUDIO AI — Premium Streamlit Landing Page
#
# Run:
#   pip install streamlit
#   streamlit run app.py
#
# Place logo.png or 1.jpg in the same directory as this script.
# If both exist, logo.png takes priority.

from pathlib import Path
import base64
import mimetypes

import streamlit as st


# ---------------------------------------------------------
# PAGE CONFIGURATION
# ---------------------------------------------------------

st.set_page_config(
    page_title="SAI | Studio AI",
    page_icon="✦",
    layout="wide",
    initial_sidebar_state="collapsed",
)


# ---------------------------------------------------------
# LOAD LOCAL LOGO
# ---------------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent

LOGO_CANDIDATES = [
    BASE_DIR / "logo.png",
    BASE_DIR / "1.jpg",
    BASE_DIR / "logo.jpg",
    BASE_DIR / "logo.webp",
]

logo_data_uri = None

for logo_path in LOGO_CANDIDATES:
    if logo_path.is_file():
        mime_type = (
            mimetypes.guess_type(logo_path.name)[0]
            or "image/png"
        )

        encoded_logo = base64.b64encode(
            logo_path.read_bytes()
        ).decode("utf-8")

        logo_data_uri = (
            f"data:{mime_type};base64,{encoded_logo}"
        )
        break


# ---------------------------------------------------------
# CUSTOM CSS + FULL-PAGE HTML
# ---------------------------------------------------------

st.markdown(
    """
    <style>
    /* ---------- Streamlit reset ---------- */

    html {
        scroll-behavior: smooth;
        background: #08090c;
    }

    *,
    *::before,
    *::after {
        box-sizing: border-box;
    }

    [data-testid="stAppViewContainer"],
    [data-testid="stApp"],
    [data-testid="stHeader"],
    [data-testid="stMain"],
    [data-testid="stMainBlockContainer"],
    section.main,
    .stApp {
        background: #08090c !important;
        color: #f5f5f7;
    }

    [data-testid="stHeader"] {
        height: 0;
        min-height: 0;
        background: transparent !important;
    }

    [data-testid="stToolbar"],
    [data-testid="stDecoration"],
    #MainMenu,
    footer,
    header {
        visibility: hidden !important;
        height: 0 !important;
    }

    [data-testid="stMainBlockContainer"] {
        width: 100% !important;
        max-width: 100% !important;
        padding: 0 !important;
        margin: 0 !important;
    }

    .block-container {
        width: 100% !important;
        max-width: 100% !important;
        padding: 0 !important;
        margin: 0 !important;
    }

    .stApp {
        overflow-x: hidden;
        font-family: -apple-system, BlinkMacSystemFont,
            "SF Pro Display", "SF Pro Text", "Helvetica Neue",
            Helvetica, Arial, sans-serif;
        -webkit-font-smoothing: antialiased;
        text-rendering: optimizeLegibility;
    }

    /* ---------- Brand color system ---------- */

    :root {
        --background: #08090c;
        --surface: #101116;
        --silver: #f5f5f7;
        --muted: #9b9da8;
        --gold: #c7a77a;
        --blue: #647cff;
        --purple: #8458e9;
        --line: rgba(255, 255, 255, 0.09);
    }

    /* ---------- Global background texture ---------- */

    .sai-site {
        position: relative;
        isolation: isolate;
        min-height: 100vh;
        width: 100%;
        overflow: hidden;
        color: var(--silver);
        background:
            radial-gradient(
                ellipse at 50% 21%,
                rgba(87, 77, 110, 0.13) 0%,
                transparent 43%
            ),
            radial-gradient(
                ellipse at 4% 47%,
                rgba(38, 62, 112, 0.12) 0%,
                transparent 39%
            ),
            radial-gradient(
                ellipse at 98% 66%,
                rgba(86, 43, 139, 0.12) 0%,
                transparent 35%
            ),
            linear-gradient(
                180deg,
                #101114 0%,
                #090a0e 44%,
                #0a0b10 72%,
                #08090c 100%
            );
    }

    .sai-site::before {
        content: "";
        position: absolute;
        inset: 0;
        z-index: -1;
        pointer-events: none;
        opacity: 0.15;
        background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 180 180' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='.92' numOctaves='3' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)' opacity='.18'/%3E%3C/svg%3E");
        background-size: 180px 180px;
        mix-blend-mode: screen;
    }

    .ambient-light {
        position: absolute;
        top: 135px;
        left: 50%;
        z-index: -1;
        width: min(1000px, 100vw);
        height: 600px;
        transform: translateX(-50%);
        pointer-events: none;
        background: radial-gradient(
            ellipse,
            rgba(94, 102, 169, 0.11),
            rgba(89, 57, 130, 0.045) 40%,
            transparent 72%
        );
        filter: blur(50px);
    }

    /* ---------- Navigation ---------- */

    .sai-nav {
        position: sticky;
        top: 0;
        z-index: 100;
        display: flex;
        align-items: center;
        justify-content: space-between;
        gap: 28px;
        width: 100%;
        min-height: 74px;
        padding: 0 clamp(22px, 6.5vw, 104px);
        border-bottom: 1px solid rgba(255, 255, 255, 0.07);
        background: rgba(12, 13, 17, 0.78);
        backdrop-filter: blur(24px) saturate(150%);
        -webkit-backdrop-filter: blur(24px) saturate(150%);
    }

    .nav-brand {
        display: inline-flex;
        align-items: center;
        gap: 11px;
        flex-shrink: 0;
        color: #f6f4f0;
        text-decoration: none;
        font-size: 13px;
        font-weight: 650;
        letter-spacing: 0.2em;
        white-space: nowrap;
    }

    .brand-symbol {
        display: inline-flex;
        align-items: center;
        justify-content: center;
        width: 29px;
        height: 29px;
        border: 1px solid rgba(205, 180, 141, 0.52);
        border-radius: 9px;
        color: #e4d0ae;
        font-size: 14px;
        font-weight: 500;
        box-shadow: inset 0 0 12px rgba(195, 162, 113, 0.07);
    }

    .nav-links {
        display: flex;
        align-items: center;
        justify-content: center;
        gap: clamp(17px, 3.1vw, 43px);
        flex-wrap: wrap;
    }

    .nav-links a {
        color: #b5b5bd;
        text-decoration: none;
        font-size: 10px;
        font-weight: 600;
        letter-spacing: 0.15em;
        transition: color 180ms ease;
    }

    .nav-links a:hover {
        color: #ffffff;
    }

    .nav-signin {
        display: inline-flex;
        align-items: center;
        justify-content: center;
        min-width: 93px;
        padding: 11px 17px;
        border: 1px solid rgba(255, 255, 255, 0.2);
        border-radius: 100px;
        color: #f7f7f8 !important;
        text-decoration: none;
        font-size: 10px;
        font-weight: 650;
        letter-spacing: 0.12em;
        transition: all 200ms ease;
    }

    .nav-signin:hover {
        border-color: rgba(211, 188, 152, 0.75);
        background: rgba(211, 188, 152, 0.08);
    }

    /* ---------- Hero ---------- */

    .hero {
        position: relative;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        width: 100%;
        min-height: min(850px, calc(100svh - 74px));
        padding: 65px 24px 100px;
        text-align: center;
    }

    .hero-eyebrow {
        display: inline-flex;
        align-items: center;
        justify-content: center;
        gap: 11px;
        margin-bottom: 26px;
        color: #c9b99e;
        font-size: 10px;
        font-weight: 600;
        letter-spacing: 0.27em;
        text-transform: uppercase;
    }

    .eyebrow-line {
        display: inline-block;
        width: 23px;
        height: 1px;
        background: linear-gradient(
            90deg,
            transparent,
            #b9a17b
        );
    }

    .eyebrow-line.right {
        transform: rotate(180deg);
    }

    .hero-logo-wrap {
        position: relative;
        display: flex;
        align-items: center;
        justify-content: center;
        width: min(820px, 90vw);
        margin: 0 auto 24px;
    }

    .hero-logo-wrap::before {
        content: "";
        position: absolute;
        inset: 12% 10%;
        z-index: -1;
        border-radius: 50%;
        background: radial-gradient(
            ellipse,
            rgba(164, 146, 125, 0.13) 0%,
            rgba(83, 91, 145, 0.09) 32%,
            transparent 70%
        );
        filter: blur(45px);
    }

    .hero-logo {
        display: block;
        width: 100%;
        max-width: 820px;
        max-height: 49svh;
        object-fit: contain;
        border: 0;
        outline: none;
        border-radius: 2px;
        filter:
            drop-shadow(0 22px 32px rgba(0, 0, 0, 0.35))
            drop-shadow(0 0 30px rgba(170, 148, 113, 0.055));
    }

    .logo-placeholder {
        width: min(800px, 90vw);
        padding: 80px 20px;
        color: #f4f0e9;
        font-size: clamp(46px, 10vw, 100px);
        font-weight: 300;
        letter-spacing: 0.16em;
        text-shadow: 0 0 35px rgba(183, 156, 119, 0.15);
    }

    .hero h1 {
        max-width: 940px;
        margin: 0 auto;
        color: #f7f7f9;
        font-size: clamp(34px, 5.3vw, 68px);
        font-weight: 550;
        line-height: 1.08;
        letter-spacing: -0.055em;
    }

    .hero h1 .gradient-text {
        color: #c6c7d5;
        background: linear-gradient(
            100deg,
            #f3f3f5 0%,
            #c8c5d7 35%,
            #b4a2dc 65%,
            #e1d2bb 100%
        );
        -webkit-background-clip: text;
        background-clip: text;
        -webkit-text-fill-color: transparent;
    }

    .hero-description {
        max-width: 590px;
        margin: 23px auto 0;
        color: #a3a4af;
        font-size: clamp(14px, 1.3vw, 16px);
        font-weight: 400;
        line-height: 1.85;
        letter-spacing: 0.012em;
    }

    .hero-actions {
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 15px;
        flex-wrap: wrap;
        margin-top: 35px;
    }

    .cta-primary {
        display: inline-flex;
        align-items: center;
        justify-content: center;
        gap: 12px;
        min-height: 49px;
        padding: 0 25px;
        border: 1px solid rgba(231, 219, 197, 0.58);
        border-radius: 100px;
        background: linear-gradient(
            135deg,
            #e4d9c6 0%,
            #c7b18b 52%,
            #9c8059 100%
        );
        box-shadow:
            0 0 22px rgba(198, 165, 115, 0.12),
            inset 0 1px 0 rgba(255, 255, 255, 0.4);
        color: #111116 !important;
        text-decoration: none;
        font-size: 10px;
        font-weight: 750;
        letter-spacing: 0.14em;
        transition:
            transform 220ms ease,
            box-shadow 220ms ease,
            filter 220ms ease;
    }

    .cta-primary:hover {
        transform: translateY(-2px);
        filter: brightness(1.08);
        box-shadow:
            0 0 32px rgba(198, 165, 115, 0.22),
            0 8px 30px rgba(0, 0, 0, 0.2);
    }

    .cta-secondary {
        display: inline-flex;
        align-items: center;
        justify-content: center;
        min-height: 49px;
        padding: 0 24px;
        border: 1px solid rgba(255, 255, 255, 0.15);
        border-radius: 100px;
        background: rgba(255, 255, 255, 0.025);
        color: #e2e2e7 !important;
        text-decoration: none;
        font-size: 10px;
        font-weight: 600;
        letter-spacing: 0.13em;
        transition: background 200ms ease, border-color 200ms ease;
    }

    .cta-secondary:hover {
        border-color: rgba(255, 255, 255, 0.32);
        background: rgba(255, 255, 255, 0.06);
    }

    .cta-arrow {
        font-size: 15px;
        line-height: 1;
    }

    .hero-footnote {
        margin-top: 32px;
        color: #666873;
        font-size: 9px;
        font-weight: 550;
        letter-spacing: 0.22em;
        text-transform: uppercase;
    }

    /* ---------- Subtle separator ---------- */

    .section-divider {
        width: min(1120px, 84%);
        height: 1px;
        margin: 0 auto;
        background: linear-gradient(
            90deg,
            transparent,
            rgba(255, 255, 255, 0.13),
            rgba(191, 168, 131, 0.25),
            rgba(255, 255, 255, 0.13),
            transparent
        );
    }

    /* ---------- Brand statement ---------- */

    .statement-section {
        position: relative;
        padding: 110px 24px 105px;
        text-align: center;
        background:
            radial-gradient(
                ellipse at 50% 20%,
                rgba(89, 73, 132, 0.09),
                transparent 60%
            );
    }

    .section-label {
        margin-bottom: 23px;
        color: #b6a384;
        font-size: 10px;
        font-weight: 650;
        letter-spacing: 0.24em;
        text-transform: uppercase;
    }

    .statement-section h2 {
        max-width: 800px;
        margin: 0 auto;
        color: #f1f1f4;
        font-size: clamp(30px, 4.3vw, 53px);
        font-weight: 500;
        line-height: 1.15;
        letter-spacing: -0.045em;
    }

    .statement-section h2 span {
        color: #a4a4b3;
    }

    .statement-copy {
        max-width: 600px;
        margin: 23px auto 0;
        color: #92939f;
        font-size: 14px;
        line-height: 1.9;
    }

    /* ---------- Feature cards ---------- */

    .features-section {
        width: 100%;
        padding: 35px clamp(22px, 7vw, 110px) 120px;
    }

    .features-header {
        max-width: 680px;
        margin: 0 auto 43px;
        text-align: center;
    }

    .features-header h2 {
        margin: 0;
        color: #f4f4f6;
        font-size: clamp(26px, 3.5vw, 40px);
        font-weight: 500;
        letter-spacing: -0.04em;
    }

    .features-header p {
        margin: 15px 0 0;
        color: #8d8e9a;
        font-size: 13px;
        line-height: 1.8;
    }

    .feature-grid {
        display: grid;
        grid-template-columns: repeat(3, minmax(0, 1fr));
        gap: 18px;
        width: 100%;
        max-width: 1120px;
        margin: 0 auto;
    }

    .feature-card {
        position: relative;
        min-height: 235px;
        padding: 31px 27px;
        overflow: hidden;
        border: 1px solid rgba(255, 255, 255, 0.085);
        border-radius: 17px;
        background:
            linear-gradient(
                145deg,
                rgba(255, 255, 255, 0.045),
                rgba(255, 255, 255, 0.012) 60%,
                rgba(107, 93, 142, 0.025)
            );
        box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.025);
        transition:
            transform 250ms ease,
            border-color 250ms ease,
            background 250ms ease;
    }

    .feature-card:hover {
        transform: translateY(-4px);
        border-color: rgba(195, 171, 131, 0.27);
        background: linear-gradient(
            145deg,
            rgba(255, 255, 255, 0.065),
            rgba(255, 255, 255, 0.018)
        );
    }

    .feature-icon {
        display: flex;
        align-items: center;
        justify-content: center;
        width: 39px;
        height: 39px;
        margin-bottom: 25px;
        border: 1px solid rgba(202, 178, 140, 0.23);
        border-radius: 12px;
        background: rgba(202, 178, 140, 0.055);
        color: #d3bc97;
        font-size: 17px;
    }

    .feature-card h3 {
        margin: 0 0 12px;
        color: #ececf0;
        font-size: 17px;
        font-weight: 550;
        letter-spacing: -0.02em;
    }

    .feature-card p {
        margin: 0;
        color: #91929d;
        font-size: 12px;
        line-height: 1.85;
    }

    /* ---------- Contact section ---------- */

    .contact-section {
        position: relative;
        padding: 95px 24px 105px;
        border-top: 1px solid rgba(255, 255, 255, 0.055);
        text-align: center;
        background:
            radial-gradient(
                ellipse at 50% 100%,
                rgba(74, 73, 139, 0.12),
                transparent 65%
            );
    }

    .contact-section h2 {
        max-width: 760px;
        margin: 0 auto;
        color: #f3f3f6;
        font-size: clamp(32px, 5vw, 57px);
        font-weight: 500;
        line-height: 1.12;
        letter-spacing: -0.05em;
    }

    .contact-section p {
        max-width: 500px;
        margin: 19px auto 29px;
        color: #999aa5;
        font-size: 14px;
        line-height: 1.8;
    }

    /* ---------- Footer ---------- */

    .sai-footer {
        display: flex;
        align-items: center;
        justify-content: space-between;
        gap: 20px;
        flex-wrap: wrap;
        padding: 27px clamp(22px, 6.5vw, 104px);
        border-top: 1px solid rgba(255, 255, 255, 0.075);
        background: rgba(6, 7, 10, 0.4);
    }

    .footer-brand {
        color: #c7c4bc;
        font-size: 10px;
        font-weight: 650;
        letter-spacing: 0.2em;
    }

    .footer-copy {
        color: #696b76;
        font-size: 10px;
        letter-spacing: 0.04em;
    }

    .footer-links {
        display: flex;
        gap: 21px;
        flex-wrap: wrap;
    }

    .footer-links a {
        color: #858691;
        text-decoration: none;
        font-size: 10px;
        transition: color 180ms ease;
    }

    .footer-links a:hover {
        color: #ffffff;
    }

    /* ---------- Responsive layouts ---------- */

    @media (min-width: 1600px) {
        .hero {
            min-height: 850px;
        }

        .hero-logo-wrap {
            width: 850px;
        }
    }

    @media (max-width: 800px) {
        .sai-nav {
            min-height: 68px;
            padding: 0 22px;
            gap: 15px;
        }

        .nav-brand {
            font-size: 11px;
            letter-spacing: 0.15em;
        }

        .nav-links {
            gap: 17px;
        }

        .nav-links a {
            font-size: 9px;
        }

        .nav-links a:nth-child(3) {
            display: none;
        }

        .nav-signin {
            min-width: auto;
            padding: 10px 13px;
            font-size: 9px;
        }

        .hero {
            min-height: 760px;
            padding: 65px 22px 80px;
        }

        .hero-logo-wrap {
            width: min(680px, 94vw);
        }

        .hero-logo {
            max-height: 42svh;
        }

        .feature-grid {
            grid-template-columns: 1fr;
            max-width: 530px;
        }

        .feature-card {
            min-height: 0;
            padding: 27px;
        }

        .features-section {
            padding-bottom: 85px;
        }
    }

    @media (max-width: 480px) {
        .sai-nav {
            min-height: 64px;
            padding: 0 16px;
            gap: 10px;
        }

        .brand-symbol {
            width: 25px;
            height: 25px;
        }

        .nav-brand {
            gap: 7px;
            font-size: 10px;
            letter-spacing: 0.09em;
        }

        .nav-links {
            gap: 12px;
        }

        .nav-links a {
            font-size: 8px;
            letter-spacing: 0.08em;
        }

        .nav-links a:nth-child(2) {
            display: none;
        }

        .nav-signin {
            padding: 9px 10px;
            font-size: 8px;
            letter-spacing: 0.07em;
        }

        .hero {
            min-height: 700px;
            padding: 54px 18px 74px;
        }

        .hero-eyebrow {
            font-size: 8px;
            letter-spacing: 0.18em;
        }

        .hero-logo-wrap {
            width: 100%;
            margin-bottom: 20px;
        }

        .hero-logo {
            max-height: 35svh;
        }

        .hero-description {
            max-width: 350px;
            font-size: 13px;
        }

        .hero-actions {
            gap: 11px;
        }

        .cta-primary,
        .cta-secondary {
            min-height: 46px;
            padding: 0 18px;
            font-size: 9px;
        }

        .statement-section {
            padding: 80px 22px;
        }

        .contact-section {
            padding: 78px 22px;
        }

        .sai-footer {
            flex-direction: column;
            align-items: center;
            text-align: center;
        }
    }

    /* ---------- Reduced-motion accessibility ---------- */

    @media (prefers-reduced-motion: reduce) {
        *,
        *::before,
        *::after {
            scroll-behavior: auto !important;
            transition-duration: 0.01ms !important;
            animation-duration: 0.01ms !important;
        }
    }
    </style>
    """,
    unsafe_allow_html=True,
)


# ---------------------------------------------------------
# PAGE CONTENT
# ---------------------------------------------------------

if logo_data_uri:
    logo_html = f"""
        <img
            class="hero-logo"
            src="{logo_data_uri}"
            alt="SAI Studio AI metallic titanium and gold logo"
            fetchpriority="high"
        />
    """
else:
    logo_html = """
        <div class="logo-placeholder" role="img"
             aria-label="Studio AI logo placeholder">
            SAI
        </div>
    """


page_html = f"""
<div class="sai-site" id="home">

    <div class="ambient-light"></div>

    <!-- NAVIGATION -->

    <nav class="sai-nav" aria-label="Main navigation">

        <a class="nav-brand" href="#home" aria-label="SAI home">
            <span class="brand-symbol">✦</span>
            <span>STUDIO AI</span>
        </a>

        <div class="nav-links">
            <a href="#home">HOME</a>
            <a href="#about">ABOUT US</a>
            <a href="#contact">CONTACT US</a>
        </div>

        <a class="nav-signin" href="#contact">
            SIGN IN <span style="margin-left: 8px;">↗</span>
        </a>

    </nav>


    <!-- HERO -->

    <main>

        <section class="hero" aria-labelledby="hero-title">

            <div class="hero-eyebrow">
                <span class="eyebrow-line"></span>
                THE NEXT ERA OF CREATIVE INTELLIGENCE
                <span class="eyebrow-line right"></span>
            </div>

            <div class="hero-logo-wrap">
                {logo_html}
            </div>

            <h1 id="hero-title">
                Where technology meets
                <span class="gradient-text"> imagination.</span>
            </h1>

            <p class="hero-description">
                A new perspective on creativity, intelligence, and
                innovation. Discover a world where ambitious ideas
                become extraordinary possibilities.
            </p>

            <div class="hero-actions">
                <a class="cta-primary" href="#about">
                    EXPLORE STUDIO AI
                    <span class="cta-arrow">↗</span>
                </a>

                <a class="cta-secondary" href="#contact">
                    GET IN TOUCH
                </a>
            </div>

            <div class="hero-footnote">
                INTELLIGENCE · CREATIVITY · POSSIBILITY
            </div>

        </section>


        <div class="section-divider"></div>


        <!-- BRAND STATEMENT -->

        <section class="statement-section" id="about">

            <div class="section-label">
                A DIFFERENT KIND OF INTELLIGENCE
            </div>

            <h2>
                Built for the curious.
                <br />
                <span>Designed for what comes next.</span>
            </h2>

            <p class="statement-copy">
                We believe the future belongs to those who imagine
                beyond the ordinary. Studio AI represents a vision
                of technology that amplifies human creativity,
                simplifies complexity, and opens the door to new
                possibilities.
            </p>

        </section>


        <!-- FEATURE CARDS -->

        <section class="features-section" aria-label="Our philosophy">

            <div class="features-header">

                <div class="section-label">
                    THE STUDIO AI PHILOSOPHY
                </div>

                <h2>More than technology.</h2>

                <p>
                    A vision shaped around the things that matter:
                    powerful ideas, thoughtful design, and a more
                    creative future.
                </p>

            </div>

            <div class="feature-grid">

                <article class="feature-card">

                    <div class="feature-icon">✳</div>

                    <h3>Intelligent by design</h3>

                    <p>
                        Technology should feel intuitive, purposeful,
                        and effortless. Every interaction should bring
                        you closer to your next great idea.
                    </p>

                </article>

                <article class="feature-card">

                    <div class="feature-icon">◇</div>

                    <h3>Creativity without limits</h3>

                    <p>
                        Explore new directions, challenge convention,
                        and transform imagination into something
                        tangible and meaningful.
                    </p>

                </article>

                <article class="feature-card">

                    <div class="feature-icon">⌁</div>

                    <h3>Engineered for tomorrow</h3>

                    <p>
                        A forward-looking vision inspired by the
                        intersection of artificial intelligence,
                        refined design, and human potential.
                    </p>

                </article>

            </div>

        </section>


        <!-- CONTACT / CALL TO ACTION -->

        <section class="contact-section" id="contact">

            <div class="section-label">
                THE FUTURE IS A CREATIVE PROCESS
            </div>

            <h2>
                Your next idea
                <br />
                starts here.
            </h2>

            <p>
                Great things begin with a question, a possibility,
                or an idea that refuses to stay ordinary.
            </p>

            <a class="cta-primary" href="mailto:hello@studioai.example">
                CONNECT WITH US
                <span class="cta-arrow">↗</span>
            </a>

        </section>

    </main>


    <!-- FOOTER -->

    <footer class="sai-footer">

        <div class="footer-brand">
            SAI <span style="color: #79716a;">/</span> STUDIO AI
        </div>

        <div class="footer-copy">
            © 2026 STUDIO AI. ALL RIGHTS RESERVED.
        </div>

        <div class="footer-links">
            <a href="#home">HOME</a>
            <a href="#about">ABOUT</a>
            <a href="#contact">CONTACT</a>
        </div>

    </footer>

</div>
"""

st.markdown(page_html, unsafe_allow_html=True)
