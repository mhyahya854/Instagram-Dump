# 81 — ToffeeShare: Browser-Based Peer-to-Peer File Transfer

Captured as a standalone typed website lead on 2026-10-26. The genuine public website at https://toffeeshare.net/ (historical/related https://web.toffeeshare.com/) describes an **ephemeral browser-to-browser transfer service** from the Netherlands.

## Verified product behavior (publisher claims)

- Peer-to-peer data transport with WebRTC and encrypted communication (site references DTLS 1.3); file bytes intended to flow sender→recipient without permanent cloud storage.
- A sharing link represents a **live session**, not a durable public download. Sender browser must remain open and sender machine awake/online until transfer completes.
- Website advertises no explicit file-size limit on supported browsers because it does not keep persistent storage, but **Safari has an approximate 4 GB browser limitation**, connections may time out and peer connectivity/fallback depends on network rules.
- Uploading a file to this service is not the same as storing it safely; if the sender closes the page before transfer finishes, the recipient may lose access.
- Recipient identity is only as trustworthy as link distribution; sending the link to the wrong person leaks access to that live share.
- A vendor may use servers for **signaling and NAT traversal/relay**, while still not storing file contents; do not naively promise “no servers are ever involved”.
- No local installation is normally required. It works as a browser utility, not a substitute for synchronized cloud files or backup.

## Which problems it addresses

- Handing someone a large project video/export or PDF without permanently uploading it to a cloud drive.
- Transferring original non-secret personal files between devices where both endpoints are trusted and network conditions support WebRTC.
- Minimizing long-lived public download links and third-party stored files.

## What it does not solve

- **Backup or sync:** recipients must get all bytes during the active session; no automatic multi-device version history.
- **Formal end-to-end verification:** encrypted transport is useful but vendor claims do not replace audit of browser implementation or link security.
- **Unlimited performance:** sender and recipient connection, browsers, file system and NAT affect throughput. Safari may have file size limits.
- **Revoking already downloaded files:** closing a link only blocks new/current access.
- **Self-hosted open-source clone availability:** official source repo licensing and full application source **not independently verified**. The ToffeeShare GitHub organization found publicly lists a WebRTC fork, not the whole product.

## Private transfer checklist

1. Confirm authentic domain, TLS, sender/recipient identity and intended file.
2. Consider sharing the session link through another trusted channel; don't post it in public.
3. Keep tab/device active and both endpoints powered; verify downloaded file size/checksum for valuable exports.
4. Encrypt particularly sensitive original data yourself when the threat model warrants, and share password separately.
5. Understand WebRTC may disclose network information to involved infrastructure; check privacy statements.
6. Test transfer completion on target browsers; choose another reliable method for resumable huge files, team access or persistent backups.

**Archive context:** useful for your local-first apps, original motion videos, project backups (transfer only—not backup system) and sharing assets. No files transferred during this research.

Sources https://toffeeshare.net/ ; https://web.toffeeshare.com/ . Related [72 — Self-Hosted Alternatives](72-TEN-SELF-HOSTED-PRIVACY-ALTERNATIVES-SCREENSHOTS.md), [26 — Local Tools](26-OPEN-SOURCE-ALTERNATIVES-AND-LOCAL-TOOLS.md).
