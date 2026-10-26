# 79 — VoxelWall-Inspired Cross-Platform Audio-Reactive Desktop Wallpaper

Captured 2026-10-26. User explicitly requested “add cloning voxelwallmac for windows linus and mac”. This is a **project research brief, not a completed software clone**. Previous discussion also requested applying the established Universal-Rules constraints. Do not copy the original's protected code, scene assets, names, sounds, UI or trademarks without permission. Build an original multi-OS alternative inspired by *general features*.

## Verified product, publisher and status

Original Instagram handle: https://www.instagram.com/voxelwallmac/ .
Official commercial product: https://voxelwall.app/ ; Apple Mac App Store https://apps.apple.com/us/app/voxelwall/id6804838742 .
Public website (October 2026) describes **51 original scenes**, audio-reactive real-time GPU wallpapers, local system-audio input, Metal renderer, macOS 14.4+, energy-saver mode, preview wallpapers and paid lifetime licensing. App Store confirms **Mac-only** distribution and in-app purchases. These are dated product-publisher statements; scene count/price/compatibility may evolve.

**First-party open source:** no confirmed publicly licensed original VoxelWall repository in the research. Do not assume an Instagram demo exposes source.

## Goal for our independent version

One high-quality desktop live-wallpaper engine across **Windows, Linux and macOS** (x86-64 and ARM where build tooling allows), with:
- Abstract, original, real-time 3D/voxel scenes responding to system or microphone audio when permitted.
- Scene browser, previews, favorites, adjustable color/audio sensitivity, quality presets and FPS/battery limits.
- Start/stop, pause on battery/lock/fullscreen app, per-monitor setup where supported, static/video fallback.
- Local-first privacy: explicit audio permission, no raw sound upload, zero telemetry by default.
- Accessible compact settings UI, simple installation/uninstallation, sensible motion and brightness controls.
- Export scene stills and presets without automatically implying copyrighted VoxelWall assets.

## Cross-platform engine choices (research, not ratified)

**Preferred architecture candidate:** Rust core with wgpu (portable GPU abstraction), winit/tao for window/event management, and platform-adapter layers for actual desktop wallpaper surfaces. Rust is well aligned with existing project preferences, but native desktop integration still requires OS-specific code. Alternatives: Godot, SDL/OpenGL or Bevy if desktop wallpaper integration and pack size meet goals.

### Platform-specific technical blockers

| OS | Rendering & wallpaper integration concept | Real risk |
|---|---|---|
| Windows 10/11 | GPU scene rendered in special desktop-hosted window (e.g. WorkerW/Progman integration), per-monitor coordinates and monitor-DPI awareness | Desktop shell implementation is undocumented/fragile across Windows versions; Explorer restart and multi-monitor focus problems |
| macOS | Native desktop-level/behind-icons NSWindow strategy plus Metal/wgpu backend and ScreenCaptureKit/CoreAudio capture where permitted | App Sandbox, desktop/window layering, menu bar, lock screen and App Store restrictions; not guaranteed to replace system locked wallpaper |
| Linux X11 | Desktop/override/root-compatible window strategies with compositor tests | Multiple desktop environments and window managers have different ordering/compositing behavior |
| Linux Wayland | Compositor-specific layer-shell protocol where supported, or desktop-environment extension/plugin route | **No universal Wayland wallpaper API**; GNOME/KDE/Sway/Hyprland differ, permissions/restarts vary |

**Do not claim “write it once, guaranteed works on all laptops”**. Shared renderer plus OS adapters is the correct abstraction; test explicit OS/desktop versions before announcing support.

### Audio pipeline

Capture **system-output loopback** where OS supports and user authorizes it; fallback to user-selected microphone; provide silent/default oscillation for blocked capture. Use FFT/window smoothing, beat envelope, low/mid/high bands and subtle parameter binding to voxel scale, terrain movement and light intensity. Enforce gain/flash limits and motion accessibility. No automatic background microphone recording.

### Architecture sketch

Input (audio + theme) → permissioned capture adapter → FFT/smoothing → scene engine (Rust/wgpu) → wallpaper surface adapter (Win/mac/Linux) → quality manager (power, FPS, fullscreen, lock, multi-monitor). Configuration persists locally with schema migrations. Disable/restore host wallpaper on quit.

## Safe incremental milestones

1. **Legal/feature reference:** catalog original site's *observable* capabilities without extracting protected assets; write new design identity and acceptance tests.
2. **Renderer proof of concept:** one original stylized voxel scene in a normal resizable desktop window with manual sensitivity slider; capture FPS/CPU/GPU.
3. **Audio reactive prototype:** system audio permissions per OS, deterministic local FFT and muted mode.
4. **OS adapter:** Windows and macOS desktop windows + at least one chosen Linux compositor; safe uninstall/rollback.
5. **Performance and accessibility:** battery, fullscreen pause, monitor hotplug, sleep/resume, keyboard, reduced motion, high-contrast settings.
6. **Packaging/signing:** signed Windows installer, macOS notarization as relevant, Linux package options; pin code/dependencies/license.
7. **Original scene collection:** build a small curated set of assets from scratch before claiming VoxelWall feature parity.

### Test matrix and release gates

- Windows 11 desktop + Explorer restart; macOS supported systems + sleep/lock; Linux Ubuntu GNOME Wayland and KDE Plasma plus optional X11.
- Multi-monitor positioning, resolution/DPI, GPU availability, low-spec fallback, hotplug, microphone permission denial.
- No accidental taskbar/desktop icon obstruction; click-through behavior where appropriate; overlay/settings always accessible.
- Performance benchmark using exact FPS, GPU and watt/power evidence—not “zero performance impact.”
- Source/code audits, license manifest, reproducible signed release and rollback/uninstall verification.
- User-approved local-only defaults and all original assets independently produced.

## Not performed

No VoxelWall code obtained; no application implementation, rendering, binary installation, source cloning or platform test performed. This is a planned project, not an authorization to use unlicensed artwork or to claim pixel-perfect parity.

Related: [07 — UX Laws](07-45-UX-LAWS-ENGLISH.md), [04 — Style Library](04-DESIGN-STYLE-LIBRARY.md), [50 — Engineering Guides](50-PROGRAMMING-SYSTEM-DESIGN-GUIDES-FREE-LLM-APIS.md). Product: https://voxelwall.app/ .
