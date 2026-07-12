from .build import build

if __name__ == "__main__":  # pragma: no cover
    day, papers, models = build()
    print(f"ai-radar: built digest for {day} ({papers} papers, {models} models)")
