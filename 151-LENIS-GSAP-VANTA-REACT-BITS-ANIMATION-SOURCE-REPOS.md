# 151 — Four GitHub Animation/UI Libraries (Exact Instagram Source)

**Original image:** `image(20261026-172734).png`. Account `fifbuilds` says: “The most insane 3D, scroll, text & UI animation effects you've seen are free on GitHub. This truly is your new design asset library — and anyone can use them.” Hashtags include `#aitools #productdesign #webdevelopment #github #3ddesign`. **Original URL order and casing preserved below.**

| Source label | Exact original link | Independently verified actual role |
|---|---|---|
| **lenis** | http://github.com/darkroomengineering/lenis | [darkroomengineering/lenis](https://github.com/darkroomengineering/lenis): smooth-scroll library with imperative/programmatic scroll control |
| **GSAP** | http://github.com/greensock/GSAP | [greensock/GSAP](https://github.com/greensock/GSAP): JavaScript timeline/tween animation engine, ScrollTrigger ecosystem |
| **vanta** | http://github.com/tengbao/vanta | [tengbao/vanta](https://github.com/tengbao/vanta): animated 3D WebGL page backgrounds, may use three.js/p5 |
| **react-bits** | http://github.com/DavidHDev/react-bits | [DavidHDev/react-bits](https://github.com/DavidHDev/react-bits): animated components/text effects and interactive React examples |

## Implementation boundaries and how to actually use

- **Lenis**: choose only when deliberate smooth scrolling improves an app. Test native wheel/touch/trackpad, keyboard PageDown/Home/End, anchor links, browser back restoration, focus jumps, scroll locking, reduced motion and nested scrollable panels. Avoid hijacking body scroll merely for novelty.
- **GSAP**: timeline sequences, interaction feedback, staggering and transition orchestration. Revert animations/listeners on component unmount; prefer composited transforms; test motion settings and responsive/RTL variations. **The engine is distinct from the GreenSock agent skills** in [112](112-THREEJS-GSAP-DESIGN-DNA-LOTTIE-GENJUTSU-AGENT-SKILLS.md).
- **Vanta**: atmospheric backdrops such as dots, fog and topology. Runtime GPU cost, motion sickness and contrast can make full-screen decorative effects poor UX; pause offscreen/reduced-motion, cap DPR, dispose resources.
- **React Bits**: copy only individual compatible components after reviewing actual source, framework/styling conventions and licenses. Verify keyboard semantics, typing, actual data, loading placeholders and mobile performance. A carousel screenshot is not proof every offered component is “free of conditions.”
- Distinguish **source code license**, branded examples and third-party assets; read current per-package terms, dependencies and registration rules.
- **Aesthetics should support use**, not hide functionality behind parallax, autoplay motion or inaccessible hover-only flows.

### Example acceptance checklist

A real product should pass navigation and form tests with animations *disabled*, mobile throttling without dropped input, visual diff at agreed breakpoints, preferring reduced motion, correct focus restoration and zero-console-error transitions. Only then use advanced effects to add meaning.

**Source verified via connected GitHub repository existence checks. No library installed, no demo produced.**
