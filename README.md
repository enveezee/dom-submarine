# DOM Submarine ⚓

**A tactical DOM parsing framework inspired by naval doctrine and submarine operations.**

---

## Mission Overview

DOM Submarine is not just a parser—it's a vessel. A hunter-class tactical system designed to infiltrate the hostile waters of modern web applications, detect semantic targets, and extract meaningful content with precision. This framework draws heavily from the operational discipline of the United States Navy, adapting its crew structure, terminology, and mission-critical mindset to the digital battlespace.

---

## Why Naval Doctrine?

Modern web environments are volatile, complex, and often adversarial. Parsing them requires more than brute force—it demands **discipline**, **modularity**, and **strategic thinking**. The U.S. Navy has spent decades refining protocols for operating in extreme conditions, managing specialized crews, and executing high-stakes missions. These principles translate seamlessly to software architecture:

- **Chain of Command** → Clear module responsibility
- **Redundancy & Resilience** → Modular fallback systems
- **Environmental Conditioning** → DOM volatility handling
- **Mission-Critical Thinking** → Strategic parsing, not just scraping

Whether you're parsing a Shadow DOM or managing memory under load, you're facing the same challenges submariners do: limited visibility, hostile terrain, and the need for precision under pressure.

The universality of disciplined systems thinking can be applied in cross-domain operational doctrine, and as such we draw upon the experience and expertise of the US Military's Office of the Chief of Naval Operations (OPNAV) and their published instructional materials (OPNAVINST) to apply it to this domain.

---

## 📁 DOM Submarine Project Structure

This layout reflects the operational doctrine of DOM Submarine. Each module is mapped to naval roles and mission-critical responsibilities, enabling modular clarity, survivability, and coalition-grade adaptability.

### Root
- `README.md` — Project overview and tactical philosophy
- `LICENSE` — Open-source license (MIT)
- `setup.py` — Package setup and entry point

### core/
- `submarine.py` — Main vessel class coordinating crew and mission execution
- `mission_profile.py` — Declarative mission schemas for repeatable deployments
- `naval_command.py` — SECNAV/OPNAV orchestration logic
- `utils.py` — Shared utilities (e.g. ID generation, logging)

### crew/ (Officer Modules)
- `co.py` — Commanding Officer: sets mission config
- `xo.py` — Executive Officer: dispatches directives
- `cob.py` — Chief of Buffer: manages rolling buffer and flush logic
- `ft.py` — Fire Control Officer: scores nodes and extracts payloads
- `ht.py` — Hull Maintenance Technician: sanitizes DOM structure
- `sts.py` — Sonar Technician: tracks depth and semantic zones
- `nav.py` — Navigator: tracks DOM traversal path
- `eng.py` — Engineering Officer: logs tool failures and diagnostics
- `intel.py` — Intelligence Officer: analyzes extracted payloads
- `ops.py` — Operations Officer: logs mission phases and checkpoints

### tools/ (Officer Toolkits)
- `sonar/` — Depth tracking, semantic scanning, echo logging
- `firecontrol/` — Node scoring, locking, payload extraction
- `hulltech/` — Noise filtering, SVG stripping, class degreasing
- `cob/` — Buffer management and flush rules
- `eng/` — Diagnostics and error logging
- `intel/` — Payload analysis
- `nav/` — Path tracking
- `xo/` — Directive dispatch
- `ops/` — Phase logging

### parser/
- `pilot.py` — HTMLParser-based DOMPilot
- `stream.py` — Streaming ingestion protocols
- `shadow.py` — Shadow DOM support (via Playwright etc.)

### wrappers/ (External Interface Bindings)
- `playwright/` — Playwright integration
- `copilot/` — Copilot wrapper
- `selenium/` — Optional Selenium support
- `cli/` — Command-line interface

### command/ (LLM/SLM Orchestration)
- `opnav_agent.py` — Mission audit and config revision
- `secnav.py` — Strategic deployment manager
- `generals.py` — Tactical mission launchers

### docs/
- `mission_manual.md` — Tactical philosophy and deployment overview
- `crew_manifest.md` — Officer roles and responsibilities
- `deployment_guide.md` — Setup and usage instructions

### tests/
- `test_submarine.py` — Vessel coordination tests
- `test_parser.py` — DOM ingestion tests
- `test_wrappers.py` — Wrapper integration tests

### examples/
- `inspect_ai_message.py` — Playwright-fed DOM inspection mission
- `static_html_mission.py` — Offline HTML parsing demo
- `drift_detection_demo.py` — DOM drift detection and adaptation

### data/
- `dom_snapshots/` — Saved DOM states for inspection
- `payloads/` — Extracted semantic payloads
- `reports/` — Mission logs and crew reports


---

## Learning by Immersion

This framework is designed to teach **DOM parsing and naval systems simultaneously**. By anchoring terminology in Navy doctrine, developers gain:

- A mental model rooted in operational clarity
- A deeper appreciation for modular design
- Exposure to real-world systems thinking

Even if you've never served, you're learning from the best. The Navy's research into crew management, environmental resilience, and mission execution applies directly to software teams, construction crews, and digital operations.

---

## Tactical Philosophy

> "Discipline is the soul of an army. It makes small numbers formidable."  
> — George Washington

DOM Submarine embodies this philosophy. It’s not about brute force—it’s about precision, coordination, and mission focus. Every module has a role. Every class has a duty. Every operation is logged, scored, and executed with intent.

> "It's not a Memo, it's a mission statement."
> — Jerry Maguire

 🎙️ "Who's coming with me, man?" — Drop the hatch and fire up the reactor, Captain. This isn’t just a parser, and it’s not just a project. It’s a mission. A declaration. A doctrine. A call to arms for anyone who’s ever stared into the abyss of a tangled DOM and said, “I need more than a scraper. I need a crew.”. 
 
---

## Status

🛠️ Under active construction  

---

## License

This project is open-source under the MIT license and mission-driven. Use it, adapt it, and deploy it with discipline.

---

## Acknowledgments

Inspired by the operational excellence of the United States Navy and the universality of disciplined systems thinking. We salute the sailors whose protocols guide our parsing.
