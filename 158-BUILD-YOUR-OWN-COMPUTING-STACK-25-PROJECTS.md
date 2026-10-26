# 158 — “For People Who Keep Asking What to Build”: Computing Projects

**Original image:** `image(20261026-181519).png` is a static overlaid list over a person at a monitor. The header reads **“For people who keep asking what to build”**. All source items follow in their visual order. The list is not a plan to build all in one app, nor a promise they are easy to vibe-code.

## Exact 25 concepts (numbering added solely for navigation)

1. Build your own operating system
2. Build your database
3. Build your virtual machine
4. Build your web server
5. Build your own game engine
6. Build your compiler
7. Build your own programming language
8. Build your own browser
9. Build your own blockchain
10. Build your own encryption algorithm
11. Build your own CPU emulator
12. Build your own file system
13. Build your own container runtime
14. Build your own package manager
15. Build your own shell
16. Build your own window manager
17. Build your own GUI toolkit
18. Build your own text editor
19. Build your own IDE
20. Build your own version control system
21. Build your own network protocol
22. Build your own operating system kernel in assembly
23. Build your own scheduler
24. Build your own memory allocator
25. Build your own hypervisor

**Source terminology note:** “Build your database” and “Build your virtual machine” omit “own” in the visible reel. The numbering is newly added, not from video.

## Deeper-learning reference

[codecrafters-io/build-your-own-x](https://github.com/codecrafters-io/build-your-own-x) curates hands-on reimplementations of practical technologies. Other useful domain references: [SerenityOS/serenity](https://github.com/SerenityOS/serenity) as a large open learning codebase, [sqlite/sqlite](https://github.com/sqlite/sqlite), [qemu/qemu](https://github.com/qemu/qemu), [golang/go](https://github.com/golang/go) and [rust-lang/rust](https://github.com/rust-lang/rust) for code reading—not direct starter boilerplates for each tiny project.

## Build in tiers instead of attempting all at once

- **Entry:** shell, toy HTTP server, simple text editor, lexer/parser, package manager for a fixed local directory, in-memory key/value DB.
- **Intermediate:** version control subset, CPU emulator for tiny instruction set, toy file system image, garbage collector/memory allocator experiment, GUI widget toolkit.
- **Advanced:** protected virtual machine/container runtime, production-grade browser security model, reliable DB engine, compiler backend, OS kernel, hypervisor.
- **Safety/accuracy:** never present custom encryption algorithms as production cryptography. Study design via prototypes but use audited primitives for real security. Browsers, VM isolation and file systems need enormous test surfaces; do not run untrusted OS images as administrator or on real drives.

### Definition of a completed educational prototype

Readme with stated limitations, tiny documented architecture, reproducible build and tests, clear input/output behavior, error and fault injection tests, licensing, and no claim of production compatibility or security guarantees.

**Status:** all 25 ideas transcribed, linked to general source studies; nothing built.
