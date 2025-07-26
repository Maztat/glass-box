import sys
from ai_client import *
from history import *
from parser import *

def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py \"What does this code do?\"")
        return
    
    message = sys.argv[1]
    files = get_files()
    print(f"\nget_files() returned {len(files)} files")
    for name in files:
        print(f" - {name} ({len(files[name])} chars)")

    results = query_ai(message, files)

    print("\n====== AI RESPONSE ======")
    if not results:
        print("No responses returned.")
    else:
        for path, response in results.items():
            print(f"\n{path}\n{response}\n")
    print(results)

if __name__ == "__main__":
    main()