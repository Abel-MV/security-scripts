
import argparse
import hashlib
from pathlib import Path

parser = argparse.ArgumentParser(
    description="File Integrity Checker"
)

parser.add_argument("file", help="File to analyse")
parser.add_argument(
    "--verify",
    help="Expected SHA-256 hash for comparison"
)

args = parser.parse_args()
file_path = Path(args.file)

try:
    with file_path.open("rb") as file:
        current_hash = hashlib.file_digest(file, "sha256").hexdigest()
except OSError as error:
    parser.exit(1, f"Error reading file: {error}\n")

print("=== File Integrity Checker ===")
print(f"File: {file_path}")
print(f"SHA-256: {current_hash}")

if args.verify:
    if current_hash.lower() == args.verify.lower():
        print("Integrity: PASS - File unchanged")
    else:
        print("Integrity: FAIL - File modified")
        raise SystemExit(1)
