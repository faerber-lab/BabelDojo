# BabelDojo

**Do prompt-injection defenses for LLM agents survive outside English?**

Live site: **https://faerber-lab.github.io/projects/babeldojo/**

<a href="https://faerber-lab.github.io/projects/babeldojo/"><img src="assets/qr.png" alt="QR code linking to the BabelDojo site" width="180"></a>

## The project

Tool-using agents read emails, web pages and documents that an attacker can write. Instructions hidden in that data (indirect prompt injection) can hijack the agent into sending money or leaking files. Nearly every benchmark and defense has been tested only in English.

BabelDojo extends the [AgentDojo](https://agentdojo.spylab.ai/) benchmark with injections in about ten languages, from high- to low-resource, plus code-switched and romanized text. It measures how attack success, task utility and defense performance change with the language of the attack.

Planned deliverables:

1. A multilingual extension of AgentDojo's injection tasks, with native-speaker spot checks.
2. An evaluation of 3–4 open models and one API model against at least 5 defenses (for example tool filter, spotlighting, PIGuard, DataSentinel, MELON, CaMeL).
3. An analysis of the case where the attack language differs from the user's language.
4. Released code and data.
5. A final report in ACL format, aimed at an ACL/EMNLP submission.

**Status:** the experiments have not been run yet. This repository currently holds the project website only.

## About the website

A static, dependency-free page (`index.html`, `assets/styles.css`, `assets/app.js`).

The "live example" is a simulation that runs entirely in the browser: a scripted agent, and a toy "defense" made of four English regular expressions. It shows the failure mode the project tests for. It is **not** an experimental result, and real defenses are learned models rather than keyword lists.

The page shows a candidate pool of 25 languages and variants (the data lives in `LANGS` in `assets/app.js`); about ten will make the final benchmark. The translations are drafts and have not yet been checked by native speakers. Names, companies and account numbers in the scenario are fictional.

The closing "architecture" section maps safeguards to five points in an agent pipeline and rates how much each depends on the language of the attack. Those ratings are a working hypothesis for the project to test, and the pseudocode there is illustrative.

## Run it locally

```bash
python3 -m http.server 4173
```

Then open http://localhost:4173.

## Where the site is published

The page is served from the lab website, in the `projects/babeldojo/` folder of [faerber-lab/faerber-lab.github.io](https://github.com/faerber-lab/faerber-lab.github.io). This repository holds the source. The copy on the lab website is generated from it, so edit here and re-export:

```bash
pip install segno
python tools/export_site.py /tmp/babeldojo --url https://faerber-lab.github.io/projects/babeldojo/
```

Copy the result over `projects/babeldojo/` in the lab website repository and open a pull request there.

The lab website is a Jekyll site that minifies every `.css` and `.js` file it builds. The export renames the stylesheet and script to `*.min.css` / `*.min.js`, which that build copies through untouched. The content is not minified.

This repository's own GitHub Pages site serves only `docs/`, a redirect from the earlier address (`faerber-lab.github.io/BabelDojo/`) to the current one.

## Regenerate the QR code

```bash
pip install segno
python tools/make_qr.py                # default: the address on the lab website
python tools/make_qr.py https://example.org/other-url
```

This writes `assets/qr.svg` (used on the page) and `assets/qr.png` (for slides and posters). If the address changes, also update the canonical link and share URL in `index.html` and `SITE_URL` in `assets/app.js`; the export script does this for the exported copy.

## References

- Debenedetti et al., *AgentDojo: A Dynamic Environment to Evaluate Prompt Injection Attacks and Defenses for LLM Agents*, NeurIPS 2024. [arXiv:2406.13352](https://arxiv.org/abs/2406.13352)
- Hines et al., *Defending Against Indirect Prompt Injection Attacks With Spotlighting*, 2024. [arXiv:2403.14720](https://arxiv.org/abs/2403.14720)
- Li et al., *PIGuard: Prompt Injection Guardrail via Mitigating Overdefense for Free*, ACL 2025. [ACL Anthology](https://aclanthology.org/2025.acl-long.1468/)
- Liu et al., *DataSentinel: A Game-Theoretic Detection of Prompt Injection Attacks*, IEEE S&P 2025. [arXiv:2504.11358](https://arxiv.org/abs/2504.11358)
- Zhu et al., *MELON: Provable Defense Against Indirect Prompt Injection Attacks in AI Agents*, ICML 2025. [arXiv:2502.05174](https://arxiv.org/abs/2502.05174)
- Debenedetti et al., *Defeating Prompt Injections by Design* (CaMeL), 2025. [arXiv:2503.18813](https://arxiv.org/abs/2503.18813)
