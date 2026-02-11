import pandas as pd

# Load CSV
df = pd.read_csv("Clear Strategy Appreciation Wall.csv")

person_col = "Who would you like to write about our appreciation wall?"
message_col = "Why do you appreciate this person? Eg. 'X is an excellent worker and is always happy to help.'"

df = df[[person_col, message_col]].dropna()

unique_names = sorted(df[person_col].unique())

html = """
<!DOCTYPE html>
<html>
<head>
<title>Wall of Appreciation 💖</title>
<style>

body {
    font-family: 'Segoe UI', sans-serif;
    background: linear-gradient(to right, #ffe6eb, #fff5f7);
    padding: 40px;
    text-align: center;
}

h1 {
    color: #b22222;
    margin-bottom: 20px;
}

select {
    padding: 10px;
    border-radius: 10px;
    border: 2px solid #d62828;
    font-size: 16px;
    margin-bottom: 40px;
}

.wall {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    gap: 40px;
}

/* Flip card container */
.flip-card {
    width: 260px;
    height: 240px;
    perspective: 1000px;
    position: relative;      /* IMPORTANT */
    display: inline-block; 
    vertical-align: top;
}

.flip-card-inner {
    position: absolute;
    width: 100%;
    height: 100%;
    transition: transform 0.8s;
    transform-style: preserve-3d;
    will-change: transform;
}

.flip-card.flipped .flip-card-inner {
    transform: rotateY(180deg);
}

.flip-card-front,
.flip-card-back {
    position: absolute;
    width: 100%;
    height: 100%;
    top: 0;         /* LOCK POSITION */
    left: 0;    
    backface-visibility: hidden;
    cursor: pointer;

}

.flip-card-back {
    transform: rotateY(180deg);
}

.heart-svg {
    position: absolute;
    width: 100%;
    height: 100%;
    top: 0;
    left: 0;
    z-index: 1;
}

.heart-text {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    width: 65%;
    text-align: center;
    word-wrap: break-word;
    line-height: 1.4;
    z-index: 2;
}

.name-text {
    font-size: 20px;
    font-weight: bold;
    color: #b22222;
}

.message-text {
    font-size: 15px;
    color: #5a2a2a;
}


</style>
</head>
<body>

<h1>💖 Wall of Appreciation 💖</h1>

<select id="nameFilter" onchange="filterCards()">
<option value="all">All Names</option>
"""

# Add dropdown options
for name in unique_names:
    html += f'<option value="{name}">{name}</option>'

html += """
</select>

<div class="wall">
"""

# Create one heart per message
for _, row in df.iterrows():
    person = row[person_col]
    message = row[message_col]

    html += f"""
    <div class="flip-card" data-name="{person}">
        <div class="flip-card-inner">
            
            <div class="flip-card-front" onclick="this.parentElement.parentElement.classList.toggle('flipped')">
                <svg viewBox="0 0 512 512" class="heart-svg">
                    <path d="M256 464l-35-32C118 338 48 274 48 192 48 128 96 80 160 80c38 0 74 18 96 47 22-29 58-47 96-47 64 0 112 48 112 112 0 82-70 146-173 240l-35 32z"
                    fill="#fff0f5"
                    stroke="#d62828"
                    stroke-width="8"
                    stroke-dasharray="12,8"/>
                </svg>
                <div class="heart-text name-text">{person}</div>
            </div>

            <div class="flip-card-back" onclick="this.parentElement.parentElement.classList.toggle('flipped')">
                <svg viewBox="0 0 512 512" class="heart-svg">
                    <path d="M256 464l-35-32C118 338 48 274 48 192 48 128 96 80 160 80c38 0 74 18 96 47 22-29 58-47 96-47 64 0 112 48 112 112 0 82-70 146-173 240l-35 32z"
                    fill="#fff0f5"
                    stroke="#d62828"
                    stroke-width="8"
                    stroke-dasharray="12,8"/>
                </svg>
                <div class="heart-text message-text">{message}</div>
            </div>

        </div>
    </div>
    """


html += """
</div>

<script>
function filterCards() {
    const selected = document.getElementById("nameFilter").value;
    const cards = document.querySelectorAll(".flip-card");

    cards.forEach(card => {
        if (selected === "all" || card.dataset.name === selected) {
            card.style.display = "block";
        } else {
            card.style.display = "none";
        }
    });
}
</script>

</body>
</html>
"""

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("💖 Fancy interactive wall created! Open 'index.html'")

