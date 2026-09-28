# Cloud Workshop — starter files

Everything you edit during the **From Zero to Cloud** workshop (NMAMIT, Nitte).
Clone this once, at the start of Day 1, and work inside one folder per level.

```bash
git clone https://github.com/REPLACE-ME/cloud-workshop-starter.git
cd cloud-workshop-starter
ls
```

No git? `sudo apt install git` on Ubuntu, or download the ZIP from the repository
page on GitHub and unzip it.

## What's in here

| Folder | Level | What it is |
|---|---|---|
| `Lab2/` | Level 2 | `index.html` — your profile page. Edit the **ME block** near the top (name, branch, interests, colour), then upload it to S3. |
| `Lab4/` | Level 4 | `lambda_function.py` — the greeting function. `trust.json` — who may take on the Lambda role. `event.json` — a test request. |
| `Lab7/` | Level 7 | `Dockerfile`, `default.conf`, `index.html` — the container that names the machine that served you. |
| `Lab8/` | Level 8 | `eks-trust.json`, `node-trust.json` — trust policies for the cluster and its workers. `readiness.json` — the readiness check that removes the 503s during a rollout. |
| `Capstone/` | Boss level | `registry.py` (the Student Registry function), `index.html` (the page), `trust.json`, `table-access.json` (least-privilege DynamoDB policy), and two sample events. |

## Before you start

Every `aws` command in the workshop goes to LocalStack, not to real AWS:

```bash
export AWS_PROFILE=localstack        # Ubuntu
$env:AWS_PROFILE="localstack"        # Windows PowerShell
```

Forget it and you get `Unable to locate credentials.`

## Working on your own copy

You can edit these files freely — they are yours for the two days. If you want
to keep your work, fork this repository on GitHub first and clone your fork
instead, so you can push your changes back.
