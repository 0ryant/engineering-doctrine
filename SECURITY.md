# Security

This repository is **documentation, examples, and small helper scripts** for engineering doctrine. It is not a runtime service, dependency manifest for production systems, or secret store.

## What belongs here

Report security issues that affect **this repository** or **consumers of its content** in a way you believe should be fixed or disclosed first in private, for example:

- Accidental committed secrets, credentials, or private URLs (also rotate affected credentials if live).
- **Malicious or unsafe** script content in `scripts/` (if the script could harm someone who runs it with typical inputs).
- A documented practice that, if followed literally, would **systematically** weaken security in a way maintainers can correct (open an issue; use private reporting only if public discussion would make harm worse, e.g. a reliable exploit path).

## What to use public issues for

Use normal issues and pull requests for:

- Typos, broken links, or editorial problems.
- Suggestions to strengthen security-related **principle** text in `doctrine/` (those changes are still reviewed carefully, but are usually not sensitive).

## How to report privately

- Use **GitHub private vulnerability reporting**: open the repository's **Security** tab and choose **Report a vulnerability**.
- If you cannot use private reporting, open a public issue that says only that you have a security report and asks a maintainer to contact you. Do not include details, live secrets, exploits against third-party systems, or PII.

## What to expect

- A human acknowledgment for reports that are in scope, when maintainers are available.
- No guaranteed SLA. This is a volunteer-style open project unless stated otherwise in [GOVERNANCE.md](GOVERNANCE.md).
- Coordinated disclosure: maintainers will aim to **fix** accidental leaks or clear documentation bugs before a public write-up, when practical. Purely documentation disagreements are handled in the open.

## License note

Licensing and redistribution terms are in [LICENSE](LICENSE) and [README.md](README.md). Security reporting is separate from copyright or patent questions.
