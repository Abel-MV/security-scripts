
import argparse
import ipaddress
import subprocess
from pathlib import Path

# Configure command-line arguments
parser = argparse.ArgumentParser(
    description="Network Reconnaissance Tool"
)

parser.add_argument(
    "target",
    help="Target IPv4 address to scan"
)

parser.add_argument(
    "-p", "--ports",
    default="22,80,443",
    help="Ports to scan (default: 22,80,443)"
)

parser.add_argument(
    "-o", "--output",
    help="Save scan results to a file inside reports/"
)

args = parser.parse_args()

# Validate the IPv4 address
try:
    target = ipaddress.IPv4Address(args.target)
except ipaddress.AddressValueError:
    parser.error("Invalid IPv4 address")

# Validate port numbers
try:
    ports = [int(port) for port in args.ports.split(",")]
    if not ports or any(port < 1 or port > 65535 for port in ports):
        raise ValueError
except ValueError:
    parser.error("Invalid ports. Use numbers between 1 and 65535.")

# Execute Nmap and handle errors
try:
    result = subprocess.run(
        [
            "nmap", "-sT", "-sV", "-Pn",
            "-p", ",".join(str(port) for port in ports),
            "--reason", str(target)
        ],
        capture_output=True,
        text=True,
        check=True,
        timeout=60
    )

except FileNotFoundError:
    parser.exit(1, "Error: Nmap is not installed.\n")

except subprocess.TimeoutExpired:
    parser.exit(1, "Error: Scan timed out.\n")

except subprocess.CalledProcessError as error:
    parser.exit(1, f"Error: Nmap failed: {error.stderr}\n")

# Display results
print("=== Network Reconnaissance Tool ===")
print(f"Target: {target}")
print(f"Ports: {args.ports}")
print(result.stdout)

# Save report if requested
if args.output:
    reports_dir = Path(__file__).resolve().parent / "reports"
    reports_dir.mkdir(exist_ok=True)

    output_name = Path(args.output).name

    if output_name != args.output or output_name in ("", ".", ".."):
        parser.error("Provide a filename without a directory path.")

    output_file = reports_dir / output_name

    try:
        with output_file.open("x", encoding="utf-8") as file:
            file.write(result.stdout)

        print(f"Report saved to: {output_file}")

    except FileExistsError:
        parser.exit(1, "Error: Report already exists. Choose another filename.\n")

    except OSError as error:
        parser.exit(1, f"Error saving report: {error}\n")
