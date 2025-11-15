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
    {"key": "frontend", "label": "Frontend"},
    {"key": "uiux", "label": "UI/UX Design"},
    {"key": "reviews", "label": "Website Reviews"},
    {"key": "about", "label": "About Me / Content"},
]

TECH_STACK = [
    "React",
    "Next.js",
    "TypeScript",
    "JavaScript (Vanilla)",
    "HTML / CSS",
]

PROJECTS = {
    "React": [
        {
            "title": "Project Alpha",
            "subtitle": "E‑commerce experience",
            "demo": "https://example.com/react-alpha",
            "code": "https://github.com/example/react-alpha"
        },
        {
            "title": "Project Beta",
            "subtitle": "Social app UI",
            "demo": "https://example.com/react-beta",
            "code": "https://github.com/example/react-beta"
        }
    ],
    "Next.js": [
        {
            "title": "Next Storefront",
            "subtitle": "Headless commerce",
            "demo": "https://example.com/next-store",
            "code": "https://github.com/example/next-store"
        }
    ],
    "TypeScript": [
        {
            "title": "TS Components Kit",
            "subtitle": "Accessible UI library",
            "demo": "https://example.com/ts-kit",
            "code": "https://github.com/example/ts-kit"
        }
    ],
    "JavaScript (Vanilla)": [
        {
            "title": "Micro Interactions",
            "subtitle": "Animation lab",
            "demo": "https://example.com/js-micro",
            "code": "https://github.com/example/js-micro"
        }
    ],
    "HTML / CSS": [
        {
            "title": "Fluid Layouts",
            "subtitle": "Modern responsive patterns",
            "demo": "https://example.com/css-fluid",
            "code": "https://github.com/example/css-fluid"
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
    {"label": "Dev Community", "url": "https://dev.to/"},
    {"label": "Tech Creator Profile", "url": "https://www.youtube.com/"},
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
