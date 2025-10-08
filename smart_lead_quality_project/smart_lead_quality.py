import pandas as pd

data = {
    "Company Name": ["TechVerse", "AI Labs", "Foodiez", "MarketBoost", "HealthSync"],
    "Email": ["info@techverse.com", "contact@ailabs.io", "support@foodiez.net", "hello@marketboost.ai", "team@healthsync.org"],
    "Website": ["https://techverse.com", "https://ailabs.io", "https://foodiez.net", "https://marketboost.ai", "https://healthsync.org"]
}

df = pd.DataFrame(data)

keywords = ["tech", "ai", "market", "data", "digital", "cloud", "analytics"]

def score_lead(row):
    score = 0
    domain = row["Website"].lower()
    email = row["Email"]
    
    if any(k in domain for k in keywords):
        score += 50
    
    if "@" in email and "." in email.split("@")[-1]:
        score += 30
        
    if domain.endswith(".com") or domain.endswith(".io"):
        score += 20
    
    return min(score, 100)

df["Lead Score"] = df.apply(score_lead, axis=1)
df = df.sort_values(by="Lead Score", ascending=False)

df.to_csv("smart_lead_quality.csv", index=False)
print("✅ Lead quality report saved as smart_lead_quality.csv")
