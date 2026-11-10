# Security Scripts & Automation

A collection of cybersecurity scripts and automation tools developed to practise programming, network reconnaissance, file integrity verification and system administration.

The repository brings together practical tools written in Python, with support for additional languages as future projects are completed.

Each published project aims to include its source code, technical documentation, usage examples and supporting evidence.

## Objectives

- Develop practical programming and automation skills.
- Build reusable command-line tools for cybersecurity tasks.
- Improve understanding of networking, operating systems and security utilities.
- Apply input validation, error handling and secure coding practices.
- Document implementation, testing and observed results.
- Maintain clear and reproducible technical projects.

## Tools

### Python

| Tool | Description | Development status |
|---|---|---|
| **Nmap Reconnaissance Tool** | Automates TCP port scanning, service detection and TXT report generation using Nmap. | Completed — v1.0 |
| **File Integrity Checker** | Calculates SHA-256 file hashes and verifies file integrity against a reference hash. | Completed — v1.0 |

Both tools have been developed and documented locally. Their source code and supporting evidence are being prepared for publication.

Additional programming languages will be introduced as new tools are developed and tested.

## Project Details

### 1. Nmap Reconnaissance Tool

A Python command-line application designed to automate basic network reconnaissance using Nmap.

**Features**

- IPv4 address validation.
- Configurable TCP port selection.
- TCP Connect scanning (`-sT`).
- Service version detection (`-sV`).
- Optional TXT report generation.
- Protection against overwriting existing reports.
- Error handling for invalid input, unavailable executables and scan timeouts.

**Technologies:** Python 3, Nmap, `argparse`, `ipaddress`, `subprocess` and `pathlib`.

The tool executes Nmap through Python rather than implementing its own network scanning engine.

**Status:** v1.0 completed and tested locally. Public source code and evidence pending publication.

### 2. File Integrity Checker

A Python command-line application for calculating SHA-256 hashes and comparing them against expected reference values.

**Features**

- SHA-256 hash calculation.
- File integrity verification.
- Command-line argument handling.
- File path management.
- Error handling for file access and reading operations.

**Technologies:** Python 3, `hashlib`, `pathlib` and `argparse`.

The tool demonstrates how cryptographic hashes can help detect modifications to file contents. A matching hash does not independently establish that a file is trustworthy or free from malware.

**Status:** v1.0 completed and documented locally. Public source code and evidence pending review.

## Repository Organisation

Projects are organised by programming language, with each tool maintained in its own directory.

The initial Python tools will be published under:

- `python/nmap-reconnaissance-tool/`
- `python/file-integrity-checker/`

Each tool will have its own README, source code and supporting evidence where available.

Additional directories for Bash, PowerShell, C++ and other languages will be created when corresponding projects are ready for publication.

## Development and Validation

The tools are developed and tested in controlled or explicitly authorised environments.

Technical documentation records the intended functionality, implementation, execution instructions, observed results and known limitations.

Where applicable, screenshots demonstrate practical testing and distinguish early development stages from the final implementation.

The published code and evidence are reviewed to avoid exposing credentials, sensitive infrastructure information or unnecessary personal details.

## Security and Responsible Use

These tools are intended for educational purposes, authorised security testing and legitimate system administration.

Network reconnaissance must only be performed against systems for which the user has appropriate permission.

Generated reports may contain sensitive infrastructure details and should be handled responsibly.

The scripts are learning projects and should not be considered comprehensive security assessment tools or production-ready security solutions.

## Future Development

Planned improvements include:

- Additional Python cybersecurity utilities.
- Bash automation for Linux.
- PowerShell scripts for Windows administration and security.
- C++ projects exploring systems programming and security concepts.
- Automated testing and improved error handling.
- Additional reporting formats and reusable functionality.

New tools will be added after implementation, testing and documentation.

## References

- [Python Documentation](https://docs.python.org/3/)
- [Nmap Documentation](https://nmap.org/docs.html)
- [Python hashlib Documentation](https://docs.python.org/3/library/hashlib.html)
- [OWASP](https://owasp.org/)

---

*Part of the [Cybersecurity Portfolio](https://github.com/Abel-MV).*
