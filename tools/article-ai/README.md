# Article AI Workflow

This workflow processes PDFs from `../articles` and creates reviewed summaries for the Related Work section of the TCC.

## What It Does

On each run, the workflow:

1. Scans `/home/matheusbarros/projects/idp/tcc/articles` for pending PDFs.
2. Uses `claude` in headless mode with:
   - `claude-sonnet-4-6`
   - `--effort high`
   - permission bypass enabled
3. Uses `gemini` to review the Claude draft with:
   - preferred model `gemini-3.1-pro-preview`
   - `--yolo`
   - automatic fallback to the CLI default model if `gemini-3.1-pro-preview` is unavailable in the environment
   - the `node` runtime resolved from the same `mise` installation directory as the selected `gemini` executable
4. Saves outputs under `/home/matheusbarros/projects/idp/tcc/tcc_notes/related_work_summaries`

The prompts are grounded in:

- `/home/matheusbarros/projects/idp/tcc/parallel-aho-corasick/CONTEX.md`
- `/home/matheusbarros/projects/idp/tcc/tcc_notes/Revisão Sistemática.md`
- the target article PDF itself

## Output Layout

- Raw Claude drafts: `/home/matheusbarros/projects/idp/tcc/tcc_notes/related_work_summaries/raw`
- Reviewed summaries: `/home/matheusbarros/projects/idp/tcc/tcc_notes/related_work_summaries/final`
- Completion markers: `/home/matheusbarros/projects/idp/tcc/tcc_notes/related_work_summaries/status`
- Cron logs: `/home/matheusbarros/projects/idp/tcc/tcc_notes/related_work_summaries/logs/article_workflow.log`

## Run Manually

Process the next pending article:

```bash
cd /home/matheusbarros/projects/idp/tcc
bash acceleration-of-pattern-matching-algorithms-using-parallel-programming/tools/article-ai/run_article_workflow.sh --limit 1
```

Process a specific article:

```bash
cd /home/matheusbarros/projects/idp/tcc
bash acceleration-of-pattern-matching-algorithms-using-parallel-programming/tools/article-ai/run_article_workflow.sh --article yara_aho_corasick.pdf --limit 1
```

## Install Cron

Install a cron job that runs every 20 minutes and processes one article per execution:

```bash
cd /home/matheusbarros/projects/idp/tcc
bash acceleration-of-pattern-matching-algorithms-using-parallel-programming/tools/article-ai/install_cron.sh 20 1
```

Accepted intervals are `15`, `20`, and `30` minutes.

## Useful Overrides

You can tune the workflow through environment variables:

- `CLAUDE_MODEL`
- `CLAUDE_EFFORT`
- `CLAUDE_TIMEOUT_SECS`
- `GEMINI_MODEL`
- `GEMINI_TIMEOUT_SECS`
- `GEMINI_REVIEW_MODE`
- `ARTICLES_DIR`
- `OUTPUT_ROOT`

Example:

```bash
cd /home/matheusbarros/projects/idp/tcc
GEMINI_MODEL=gemini-2.5-pro GEMINI_TIMEOUT_SECS=600 bash acceleration-of-pattern-matching-algorithms-using-parallel-programming/tools/article-ai/run_article_workflow.sh --limit 2
```

## Reprocessing an Article

If you want to regenerate one summary from scratch, remove the matching files from:

- `/home/matheusbarros/projects/idp/tcc/tcc_notes/related_work_summaries/raw`
- `/home/matheusbarros/projects/idp/tcc/tcc_notes/related_work_summaries/final`
- `/home/matheusbarros/projects/idp/tcc/tcc_notes/related_work_summaries/status`

Then run the workflow again for that article.