# Inspecting the hosted mathematics

The read-only pull-request workflow compares every tracked Markdown page at the exact proposed commit with its actual rendering on GitHub. It runs the finite scientific checks first, then captures wide (1440 pixels) and narrow (760 pixels) views in an anonymous browser. Its artifact contains the source inventory, expected and observed MathML, structural comparisons, HTML, screenshots and a bound report.

The scripts compare expression order, symbols, subscripts, fractions and other mathematical structure. They also check source identities, relation counts, missing expressions and suspicious display geometry. A passing automated report still requires a person or reviewing assistant to inspect the screenshots and compare the displayed claims with the source. It does not establish scientific correctness or guarantee every future browser rendering.

## Run the same check locally

Use Node.js 18 or later, Python 3.10 or later, Git, Playwright 1.56.1 and MathJax 3.2.1. Install browser dependencies outside the source checkout:

```bash
npm install --prefix /absolute/temporary/dependencies --ignore-scripts playwright@1.56.1 mathjax-full@3.2.1
/absolute/temporary/dependencies/node_modules/.bin/playwright install chromium
NODE_PATH=/absolute/temporary/dependencies/node_modules node verification/hosted/scripts/capture_hosted_math.cjs \
  --root /absolute/scientific-checkout \
  --repository GoGoKo699/Quantum-Deletion-Capacity \
  --revision FULL_COMMIT_SHA \
  --contract verification/hosted/math-contract.json \
  --output /absolute/new-empty-evidence-directory
```

Replace the illustrative paths and revision with actual values. The revision must identify a public commit containing the checked pages. The collector reads exact Git objects, so uncommitted edits and moving branch names do not define the inspected source.

By default, all tracked Markdown pages are included. Repeated `--page PATH` arguments can select an explicitly limited diagnostic sample; a sample does not cover the rest of the repository. Use a new output directory for each attempt so earlier failures remain available.

The [text contract](../math-contract.json) binds the complete expected mathematical text of headline formulas, the worked example and repaired expressions to their source hashes. A relevant formula edit requires updating its contract together with the source; the full structural comparison still covers every expression on every captured page.

## Interpret the output

A zero exit status means the automated comparisons passed for the recorded source and page scope. Review the actual images at both widths, including the main claims, substantial proofs, learning route and any repaired expressions. Nonzero results retain the concrete failure; missing pages, network failures and unavailable browsers are not mathematical passes.

The workflow has only `contents: read` permission, uses no repository secrets, makes no source edits and does not publish a release. Captures are temporary diagnostic artifacts. Reproduction commands and the scientific limits of the finite tests are described in the [verification guide](../../README.md).
