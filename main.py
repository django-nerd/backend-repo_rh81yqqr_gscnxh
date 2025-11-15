import os
from typing import List, Optional
from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Creator Console Portfolio API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "Creator Console Portfolio API running"}

# ---------- Core Data (static for this portfolio) ----------
MAIN_MENU = [
    {"key": "frontend", "label": "Projects"},
    {"key": "uiux", "label": "Design Gallery"},
    {"key": "reviews", "label": "Website Reviews"},
    {"key": "about", "label": "About / Contact"},
]

TECH_STACK = [
    "React",
    "Next.js",
    "JavaScript",
    "Node.js",
    "GSAP",
    "Spline",
    "Sentry",
    "Google Analytics",
]

PROJECTS = {
    "React": [
        {
            "title": "Console UI Kit",
            "subtitle": "Framer Motion + Tailwind component system",
            "demo": "https://example.com/react-console-kit",
            "code": "https://github.com/example/react-console-kit"
        },
        {
            "title": "Realtime Dash",
            "subtitle": "Charts, sockets, theming",
            "demo": "https://example.com/react-realtime",
            "code": "https://github.com/example/react-realtime"
        }
    ],
    "Next.js": [
        {
            "title": "Next Commerce",
            "subtitle": "ISR, app router, Stripe",
            "demo": "https://example.com/next-commerce",
            "code": "https://github.com/example/next-commerce"
        }
    ],
    "JavaScript": [
        {
            "title": "Micro‑Interactions Lab",
            "subtitle": "Vanilla JS animations & UX patterns",
            "demo": "https://example.com/js-micro",
            "code": "https://github.com/example/js-micro"
        }
    ],
    "Node.js": [
        {
            "title": "API Boilerplate",
            "subtitle": "Express + Prisma + Auth",
            "demo": "https://example.com/node-api",
            "code": "https://github.com/example/node-api"
        }
    ],
    "GSAP": [
        {
            "title": "Motion Sequences",
            "subtitle": "Scroll & timeline choreography",
            "demo": "https://example.com/gsap-sequences",
            "code": "https://github.com/example/gsap-sequences"
        }
    ],
    "Spline": [
        {
            "title": "3D Hero Scenes",
            "subtitle": "Interactive Spline embeds",
            "demo": "https://example.com/spline-heroes",
            "code": "https://github.com/example/spline-heroes"
        }
    ],
    "Sentry": [
        {
            "title": "Observability Setup",
            "subtitle": "Error + performance monitoring",
            "demo": "https://example.com/sentry-setup",
            "code": "https://github.com/example/sentry-setup"
        }
    ],
    "Google Analytics": [
        {
            "title": "Analytics Starter",
            "subtitle": "gtag v4 + route tracking",
            "demo": "https://example.com/ga-starter",
            "code": "https://github.com/example/ga-starter"
        }
    ],
}

DESIGN_FOCUS = [
    "Modern UI / Interface",
    "UX Case Studies",
    "Web Design Inspiration",
    "Digital Design",
]

GALLERY = {
    "Modern UI / Interface": [
        {"title": "Dashboard Nova", "image": "https://images.unsplash.com/photo-1526498460520-4c246339dccb?q=80&w=1200&auto=format&fit=crop"},
        {"title": "Mobile Flow", "image": "https://images.unsplash.com/photo-1557825835-70d97c4aa78a?q=80&w=1200&auto=format&fit=crop"},
        {"title": "Dark Glass UI", "image": "https://images.unsplash.com/photo-1509099836639-18ba1795216d?q=80&w=1200&auto=format&fit=crop"}
    ],
    "UX Case Studies": [
        {"title": "Checkout Rethink", "image": "https://images.unsplash.com/photo-1515879218367-8466d910aaa4?q=80&w=1200&auto=format&fit=crop"}
    ],
    "Web Design Inspiration": [
        {"title": "Motion Gallery", "image": "https://images.unsplash.com/photo-1545235617-9465d2a55698?q=80&w=1200&auto=format&fit=crop"}
    ],
    "Digital Design": [
        {"title": "Concept Posters", "image": "https://images.unsplash.com/photo-1511765224389-37f0e77cf0eb?q=80&w=1200&auto=format&fit=crop"}
    ],
}

REVIEWS = [
    {
        "title": "2025 Trend — Minimal Motion Systems",
        "type": "article",
        "url": "https://example.com/review-trend",
        "source": "Design Journal"
    },
    {
        "title": "Landing Page UX — 5 Common Fixes",
        "type": "video",
        "url": "https://example.com/review-landing",
        "source": "YouTube"
    }
]

CONTACTS = [
    {"label": "GitHub", "url": "https://github.com/"},
    {"label": "LinkedIn", "url": "https://www.linkedin.com/"},
    {"label": "Email Me", "url": "mailto:hello@example.com"},
]

# ---------- Endpoints ----------

@app.get("/api/menu")
def get_menu():
    return {"items": MAIN_MENU}

@app.get("/api/frontend/tech")
def get_tech():
    return {"items": TECH_STACK}

@app.get("/api/projects")
def get_projects(tech: str = Query(..., description="Choose a technology key from /api/frontend/tech")):
    return {"tech": tech, "projects": PROJECTS.get(tech, [])}

@app.get("/api/design/focus")
def get_design_focus():
    return {"items": DESIGN_FOCUS}

@app.get("/api/design/gallery")
def get_gallery(focus: str = Query(..., description="Choose a focus key from /api/design/focus")):
    return {"focus": focus, "items": GALLERY.get(focus, [])}

@app.get("/api/reviews")
def get_reviews():
    return {"items": REVIEWS}

@app.get("/api/contact")
def get_contact():
    return {"items": CONTACTS}

@app.get("/test")
def test_database():
    """Connectivity probe for platform; database not required for this portfolio."""
    response = {
        "backend": "✅ Running",
        "database": "ℹ️ Not used for this app",
        "database_url": None,
        "database_name": None,
        "connection_status": "Not Required",
        "collections": []
    }
    return response


if __name__ == "__main__":
    import uvicorn
    port = int(os.getenv("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
