#!/usr/bin/env python3
"""Generate project detail pages for patelkhush.com.

Each entry in PAGES becomes /<slug>/index.html, styled with the site's
style.css. Re-run after editing: python3 build_pages.py
Remember to add new slugs to sitemap.xml and link them from index.html.
"""
import html
import json
import pathlib

SITE = "https://patelkhush.com"
ROOT = pathlib.Path(__file__).parent

PAGES = [
    {
        "slug": "agent-simulation-engine",
        "title": "Agent Simulation Engine",
        "tagline": "A CI/CD-style testing and improvement platform for AI agents, created at Lyzr AI.",
        "image": "khush-patel-lyzr-agent-evals-webinar.jpg",
        "image_alt": "Khush Patel, speaker on the Behind the Scenes of Lyzr Agent Evals live webinar",
        "body": """
<p>The Agent Simulation Engine is a platform I created at Lyzr AI that brings CI/CD discipline to AI agents. Before an agent reaches production, the engine tests it against realistic simulated scenarios, evaluates the results with AI-powered judgment, analyzes failure patterns, and, through its companion Agent Improvement Engine, automatically improves the agent's configuration using reinforcement learning techniques.</p>
<p>Press coverage of Lyzr's fundraising has repeatedly highlighted the engine. Indian Startup News' story on Lyzr's $8M Series A described it as inspired by Yann LeCun's JEPA research, letting enterprises run over 10,000 simulations per agent before real-world rollout. The Next Web's coverage of Lyzr's $100M Series B raise cited the same capability as a core differentiator for regulated industries.</p>
<p>I presented the engine publicly in "Behind the Scenes of Lyzr Agent Evals" and the "Mastering Evals" session of the Lyzr Agent Building Workshop Series, walking through how to run meaningful evals, harden agents, and build reusable eval loops.</p>
""",
        "links": [
            ("Indian Startup News: $8M Series A coverage", "https://indianstartupnews.com/funding/no-pitch-decks-no-investor-calls-ai-agent-sam-raises-8-million-for-lyzr-ai-check-how-10609263"),
            ("The Next Web: $100M Series B coverage", "https://thenextweb.com/news/lyzr-ai-agent-100-million-series-b"),
            ("Watch: Behind the Scenes of Lyzr Agent Evals (YouTube)", "https://youtube.com/live/TUI_Ez-KXNs"),
            ("Mastering Evals webinar (Luma)", "https://luma.com/h7egimbm"),
        ],
    },
    {
        "slug": "control-plane",
        "title": "Agent Control Plane",
        "tagline": "Among the first multi-cloud control planes for AI agents: one manifest, one pipeline, every cloud.",
        "body": """
<p>The Agent Control Plane is a system I designed and built at Lyzr that brings real deployment discipline to AI agents across clouds. It gives an organization one place to register, deploy, govern, and call its agents: an agent registry, managed credentials, and a gateway that lets any application invoke any agent on any cloud with a single token.</p>
<p>Agents are defined by one manifest in their repo and ship through one pipeline, with keyless sign-in to each cloud and no stored cloud keys. The same agent deploys to the native agent runtimes on AWS and Google Cloud today, with Azure as the next leg. Promotion moves a pinned build through dev, staging, and production with enforced approval gates, an audit trail, and a kill switch.</p>
<p>Microsoft independently published the same pattern as a reference architecture for its own cloud ("CI/CD for AI Agents on Microsoft Foundry", May 2026). The control plane implements that architecture across hyperscalers and runs live today; the same agent code answers from AWS and Google Cloud off one push. The system is the subject of my "CI/CD for AI Agents" session in the Lyzr Workshop Series.</p>
""",
        "links": [
            ("Microsoft's reference architecture for the same pattern", "https://techcommunity.microsoft.com/blog/educatordeveloperblog/cicd-for-ai-agents-on-microsoft-foundry/4522218"),
        ],
    },
    {
        "slug": "ethicaleye",
        "title": "EthicalEye",
        "tagline": "An open-source, cross-lingual AI ethics and content moderation model supporting 88 languages.",
        "body": """
<p>EthicalEye is an open-source content moderation model I created, built on XLM-RoBERTa and supporting 88 languages. It classifies harmful and unsafe content across languages with a single model, making moderation practical for products with international audiences.</p>
<p>Released under the Apache 2.0 license, EthicalEye has passed 10,000 downloads on Hugging Face, was featured in the Hugging Face community showcase, and has been adopted by companies for production content moderation, reducing manual review workloads by approximately 70%.</p>
""",
        "links": [],
    },
    {
        "slug": "agentdefender",
        "title": "AgentDefender",
        "tagline": "A benchmark and neural-embedding defense against prompt injection in LLM agents.",
        "body": """
<p>AgentDefender is a defense methodology and benchmark I developed for securing LLM-based agents against prompt injection. It uses a neural embedding approach to detect injected instructions before they reach the agent, and ships with a benchmark for evaluating injection defenses systematically.</p>
<p>The system is deployed on Lyzr's production agent platform, and the methodology is published as "AgentDefender by Lyzr: A Benchmark Evaluation and Neural Embedding Approach for Agent Prompt Injection" (2024).</p>
""",
        "links": [
            ("Paper on ResearchGate", "https://www.researchgate.net/publication/388554578_AgentDefender_by_Lyzr_A_Benchmark_Evaluation_and_Neural_Embedding_Approach_for_Agent_Prompt_Injection"),
        ],
    },
    {
        "slug": "responsible-ai-engine",
        "title": "Responsible AI Engine",
        "tagline": "Lyzr's production Responsible AI module: guardrails, redaction, and pluggable policy engines.",
        "body": """
<p>I built Lyzr's production Responsible AI engine, the guardrail layer that sits between enterprise AI agents and the real world. It provides PII detection and redaction, toxicity metering, NSFW, gibberish, and prompt-injection detection, and topic controls that keep agents inside their intended scope.</p>
<p>Policy enforcement is pluggable: the engine integrates OPA, Cedar, AWS Bedrock guardrails, and Google Vertex guardrails, so enterprises can bring the policy stack they already trust. I also integrated the engine into ComputerAgent's open-source and enterprise editions as a chained guardrail redaction proxy with policy-bound agent runs.</p>
""",
        "links": [
            ("ComputerAgent on GitHub", "https://github.com/open-gitagent/ComputerAgent"),
        ],
    },
    {
        "slug": "regulatory-knowledge-graph",
        "title": "Regulatory Knowledge Graph",
        "tagline": "A financial-compliance knowledge graph spanning FINRA, FRB, OCC, EU AI Act, DORA, DFS, FDIC, and NAIC.",
        "body": """
<p>For financial-services compliance, I built a regulatory knowledge graph that connects requirements across FINRA, the Federal Reserve Board, the OCC, the EU AI Act, DORA, NY DFS, the FDIC, and NAIC regulations into a single queryable structure.</p>
<p>The graph powers a continuous compliance monitoring system: instead of periodically sampling transactions for audit, every relevant event is checked against the applicable regulatory requirements as it happens, replacing sampling-based audits with continuous coverage.</p>
""",
        "links": [],
    },
    {
        "slug": "lyzr-agent-studio",
        "title": "Lyzr Agent Studio",
        "tagline": "The no-code enterprise AI agent platform serving 80,000+ users.",
        "body": """
<p>Lyzr Agent Studio is the no-code platform where teams build and deploy AI agents on the Lyzr Agent Platform. I am a founding engineer of the platform, which serves 80,000+ users, and its Product Hunt launch earned 522 upvotes.</p>
<p>Enterprises use Agent Studio to build and run agents securely within their own cloud or on-premise environments, keeping full ownership of data and IP. Under the hood it integrates the platform capabilities I built: the <a href="/responsible-ai-engine/">Responsible AI engine</a> for guardrails and policy enforcement, and the <a href="/agent-simulation-engine/">Agent Simulation Engine</a> for testing agents before they reach production.</p>
""",
        "links": [],
    },
    {
        "slug": "skott",
        "title": "Skott",
        "tagline": "An autonomous AI marketing agent producing content end to end with no human intervention.",
        "body": """
<p>Skott is an autonomous AI marketing agent built on the Lyzr agent stack. It runs the entire content pipeline itself, from research through writing to publishing, and has produced over 1,000 pieces of content with no human intervention.</p>
<p>Skott's Product Hunt launch earned 424 upvotes, making it one of the community's most-recognized autonomous marketing agents at the time.</p>
""",
        "links": [],
    },
    {
        "slug": "shadowlm",
        "title": "ShadowLM Trainer",
        "tagline": "An open-source fine-tuning SDK for open models: 13 training methods, any hardware.",
        "body": """
<p>ShadowLM Trainer is an open-source fine-tuning SDK I created and maintain at Lyzr Research Labs. It packages 13 training methods behind one batteries-included install, and is designed to run on whatever hardware you have rather than assuming a specific GPU setup.</p>
<p>The goal is to make fine-tuning open models a dependency you add, not a project you staff: pick a method, point it at your data, and train.</p>
""",
        "links": [
            ("ShadowLM on GitHub", "https://github.com/open-gitagent/shadowLM"),
        ],
    },
    {
        "slug": "opengap",
        "title": "OpenGAP (the Git Agent Protocol)",
        "tagline": "A framework-agnostic, git-native open standard for defining AI agents. 2,800+ GitHub stars.",
        "body": """
<p>OpenGAP, the Git Agent Protocol, is an open standard I contribute to that treats an AI agent as a git repository: the agent's identity, rules, skills, and tools are version-controlled files rather than opaque platform state. Any runtime that speaks the standard can bring the same agent to life.</p>
<p>The standard has earned 2,800+ GitHub stars and includes first-class compliance support for FINRA, Federal Reserve, and SEC requirements, making it practical for regulated industries. It anchors an ecosystem that includes <a href="/gitagent/">GitAgent</a> and <a href="/computeragent/">ComputerAgent</a>.</p>
""",
        "links": [
            ("OpenGAP on GitHub", "https://github.com/open-gitagent/opengap"),
            ("The OpenGAP specification", "https://github.com/open-gitagent/opengap/blob/main/spec/SPECIFICATION.md"),
        ],
    },
    {
        "slug": "gitagent",
        "title": "GitAgent",
        "tagline": "A git-native AI agent whose identity, memory, and skills are version-controlled files. 590+ GitHub stars.",
        "body": """
<p>GitAgent is a git-native AI agent built on the <a href="/opengap/">OpenGAP standard</a>, and an open-source project I contribute to. An agent is defined entirely by files in a repo: a manifest (agent.yaml), its identity (SOUL.md), its hard constraints (RULES.md), and a skills directory, so the agent's whole definition is diffable, reviewable, and version-controlled like any other code. The project has earned 590+ GitHub stars.</p>
<p>In 2026, Lyzr AI hosted the GitAgent Hackathon on HackCulture, a global virtual hackathon on the standard with 637 registrations worldwide. I served on its three-member judging panel, evaluating agent quality, skill design, working demos, and creativity.</p>
""",
        "links": [
            ("GitAgent on GitHub", "https://github.com/open-gitagent/gitagent"),
            ("GitAgent Hackathon on HackCulture", "https://hackculture.io/hackathons/gitagent-hackathon"),
        ],
    },
    {
        "slug": "computeragent",
        "title": "ComputerAgent",
        "tagline": "A portable agent runtime and the reference implementation of the Harness Protocol.",
        "body": """
<p>ComputerAgent is a portable AI agent runtime in the open-gitagent ecosystem and the reference implementation of the Harness Protocol. I contribute to the project across its open-source and enterprise editions.</p>
<p>My main contribution is its safety layer: I integrated Lyzr's <a href="/responsible-ai-engine/">Responsible AI engine</a> into both editions as a chained guardrail redaction proxy, so every agent run is policy-bound, with PII redaction, toxicity and prompt-injection detection, and pluggable policy engines enforced at the runtime boundary.</p>
""",
        "links": [
            ("ComputerAgent on GitHub", "https://github.com/open-gitagent/ComputerAgent"),
        ],
    },
]

GTM = """<!-- Google Tag Manager -->
<script>(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':
new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],
j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
})(window,document,'script','dataLayer','GTM-KSL8TTNW');</script>
<!-- End Google Tag Manager -->"""

GTM_NOSCRIPT = """<!-- Google Tag Manager (noscript) -->
<noscript><iframe src="https://www.googletagmanager.com/ns.html?id=GTM-KSL8TTNW"
height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>
<!-- End Google Tag Manager (noscript) -->"""


def render(page):
    title_text = html.unescape(page["title"])
    url = f"{SITE}/{page['slug']}/"
    desc = html.unescape(page["tagline"])
    og_image = f"{SITE}/images/{page.get('image', 'khush-patel-portrait.jpg')}"
    img_html = ""
    if page.get("image"):
        img_html = f"""
    <figure class="ph wide" style="max-width:640px;margin:26px 0">
      <div class="imgbox"><img src="../images/{page['image']}" alt="{page['image_alt']}"></div>
    </figure>"""
    links_html = ""
    if page["links"]:
        items = "\n".join(
            f'      <li><a href="{href}">{label}</a></li>' for label, href in page["links"]
        )
        links_html = f"""
    <h2 class="sec" style="font-size:19px;margin-top:34px">Links</h2>
    <ul class="std">
{items}
    </ul>"""
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  {GTM}
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{page['title']} | Khush Patel</title>
  <meta name="description" content="{html.escape(desc)} By Khush Patel, AI Lead &amp; Founding Engineer at Lyzr AI.">
  <link rel="canonical" href="{url}">
  <meta property="og:type" content="article">
  <meta property="og:title" content="{page['title']} | Khush Patel">
  <meta property="og:description" content="{html.escape(desc)}">
  <meta property="og:url" content="{url}">
  <meta property="og:image" content="{og_image}">
  <meta name="twitter:card" content="summary">
  <link rel="icon" href="/favicon.svg" type="image/svg+xml">
  <link rel="icon" href="/favicon-32.png" sizes="32x32" type="image/png">
  <link rel="apple-touch-icon" href="/apple-touch-icon.png">
  <link rel="stylesheet" href="../style.css">
  <script type="application/ld+json">
  {json.dumps({
      "@context": "https://schema.org",
      "@type": "WebPage",
      "name": title_text,
      "url": url,
      "description": desc,
      "author": {
          "@type": "Person",
          "name": "Khush Patel",
          "url": SITE + "/",
          "jobTitle": "AI Lead & Founding Engineer at Lyzr AI",
      },
  }, indent=2)}
  </script>
</head>
<body>
{GTM_NOSCRIPT}

<header class="hero" style="padding:36px 0 30px">
  <div class="wrap">
    <p class="kicker"><a href="../" style="text-decoration:none;color:inherit">Khush Patel &middot; Portfolio</a></p>
    <h1 style="font-size:32px">{page['title']}</h1>
    <p class="role">{page['tagline']}</p>
  </div>
</header>

<main>
  <section class="doc" style="padding-top:30px">
    <div class="wrap">
{page['body'].strip()}{img_html}{links_html}
      <p style="margin-top:36px"><a href="../">&larr; Back to the full portfolio</a></p>
    </div>
  </section>
</main>

<footer>
  <div class="wrap">
    <p>&copy; 2026 Khush Patel. All rights reserved. &middot; <a href="../">patelkhush.com</a></p>
  </div>
</footer>

</body>
</html>
"""


def main():
    for page in PAGES:
        out = ROOT / page["slug"] / "index.html"
        out.parent.mkdir(exist_ok=True)
        out.write_text(render(page))
        print(f"wrote {out.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
