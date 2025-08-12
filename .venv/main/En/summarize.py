import argparse
from transformers import pipeline

def summarize_text(text, max_len=130, min_len=30):
    summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
    summary = summarizer(text, max_length=max_len, min_length=min_len, do_sample=False)
    return summary[0]['summary_text']

def load_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        return f.read()

def main():
    parser = argparse.ArgumentParser(description="Tiivistä muistiinpanot.")
    parser.add_argument('--file', required=True, help='Polku muistiinpanotiedostoon (.txt)')
    parser.add_argument('--style', choices=['plain', 'bullet'], default='bullet', help='Tiivistyksen tyyli')
    args = parser.parse_args()

    text = load_file(args.file)
    
    print("\n🔍 Tiivistetään muistiinpanot...\n")
    summary = summarize_text(text)

    if args.style == 'bullet':
        bullet_points = summary.split('. ')
        for point in bullet_points:
            if point.strip():
                print(f"🔹 {point.strip()}")
    else:
        print(summary)

if __name__ == "__main__":
    main()
